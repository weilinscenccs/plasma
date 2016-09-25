/**
 *
 * @file
 *
 *  PLASMA is a software package provided by:
 *  University of Tennessee, US,
 *  University of Manchester, UK.
 *
 * @precisions normal z -> s d c
 *
 **/

#include "plasma_async.h"
#include "plasma_context.h"
#include "plasma_descriptor.h"
#include "plasma_internal.h"
#include "plasma_types.h"
#include "plasma_workspace.h"
#include "core_blas.h"

#define A(m, n) (plasma_complex64_t*)plasma_tile_addr(A, m, n)
#define B(m, n) (plasma_complex64_t*)plasma_tile_addr(B, m, n)
#define C(m, n) (plasma_complex64_t*)plasma_tile_addr(C, m, n)

/***************************************************************************//**
 * Parallel tile matrix-matrix multiplication.
 * @see plasma_omp_zgemm
 ******************************************************************************/
void plasma_pzgemm(plasma_enum_t transA, plasma_enum_t transB,
                   plasma_complex64_t alpha, plasma_desc_t A,
                                             plasma_desc_t B,
                   plasma_complex64_t beta,  plasma_desc_t C,
                   plasma_sequence_t *sequence, plasma_request_t *request)
{
    int m, n, k;
    int ldam, ldak, ldbn, ldbk, ldcm;
    int tempmm, tempnn, tempkn, tempkm;

    plasma_complex64_t zbeta;

    int innerK = transA == PlasmaNoTrans ? A.n : A.m;

    // Check sequence status.
    if (sequence->status != PlasmaSuccess) {
        plasma_request_fail(sequence, request, PlasmaErrorSequence);
        return;
    }

    for (m = 0; m < C.mt; m++) {
        tempmm = plasma_tile_mdim(A, m);
        ldcm   = plasma_tile_mdim(C, m);
        for (n = 0; n < C.nt; n++) {
            tempnn = plasma_tile_ndim(A, n);
            //=========================================
            // alpha*A*B does not contribute; scale C
            //=========================================
            if (alpha == 0.0 || innerK == 0) {
                ldam = imax(1, plasma_tile_mdim(A, 0));
                ldbk = imax(1, plasma_tile_mdim(B, 0));
                core_omp_zgemm(
                    transA, transB,
                    tempmm, tempnn, 0,
                    alpha, A(0, 0), ldam,
                           B(0, 0), ldbk,
                    beta,  C(m, n), ldcm);
            }
            else if (transA == PlasmaNoTrans) {
                ldam = plasma_tile_mdim(A, m);
                //================================
                // PlasmaNoTrans / PlasmaNoTrans
                //================================
                if (transB == PlasmaNoTrans) {
                    for (k = 0; k < A.nt; k++) {
                        tempkn = plasma_tile_ndim(A, k);
                        ldbk   = plasma_tile_mdim(B, k);
                        zbeta = k == 0 ? beta : 1.0;
                        core_omp_zgemm(
                            transA, transB,
                            tempmm, tempnn, tempkn,
                            alpha, A(m, k), ldam,
                                   B(k, n), ldbk,
                            zbeta, C(m, n), ldcm);
                    }
                }
                //=====================================
                // PlasmaNoTrans / Plasma[_Conj]Trans
                //=====================================
                else {
                    ldbn = plasma_tile_mdim(B, n);
                    for (k = 0; k < A.nt; k++) {
                        tempkn = plasma_tile_ndim(A, k);
                        zbeta = k == 0 ? beta : 1.0;
                        core_omp_zgemm(
                            transA, transB,
                            tempmm, tempnn, tempkn,
                            alpha, A(m, k), ldam,
                                   B(n, k), ldbn,
                            zbeta, C(m, n), ldcm);
                    }
                }
            }
            else {
                //=====================================
                // Plasma[_Conj]Trans / PlasmaNoTrans
                //=====================================
                if (transB == PlasmaNoTrans) {
                    for (k = 0; k < A.mt; k++) {
                        tempkm = plasma_tile_mdim(A, k);
                        ldak   = plasma_tile_mdim(A, k);
                        ldbk   = plasma_tile_mdim(B, k);
                        zbeta = k == 0 ? beta : 1.0;
                        core_omp_zgemm(
                            transA, transB,
                            tempmm, tempnn, tempkm,
                            alpha, A(k, m), ldak,
                                   B(k, n), ldbk,
                            zbeta, C(m, n), ldcm);
                    }
                }
                //==========================================
                // Plasma[_Conj]Trans / Plasma[_Conj]Trans
                //==========================================
                else {
                    ldbn = plasma_tile_mdim(B, n);
                    for (k = 0; k < A.mt; k++) {
                        tempkm = plasma_tile_mdim(A, k);
                        ldak   = plasma_tile_mdim(A, k);
                        zbeta = k == 0 ? beta : 1.0;
                        core_omp_zgemm(
                            transA, transB,
                            tempmm, tempnn, tempkm,
                            alpha, A(k, m), ldak,
                                   B(n, k), ldbn,
                            zbeta, C(m, n), ldcm);
                    }
                }
            }
        }
    }
}
