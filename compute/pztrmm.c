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

/***************************************************************************//**
 *  Parallel tile triangular matrix-matrix multiplication.
 *  @see plasma_omp_ztrmm
 ******************************************************************************/
void plasma_pztrmm(plasma_enum_t side, plasma_enum_t uplo,
                   plasma_enum_t trans, plasma_enum_t diag,
                   plasma_complex64_t alpha, plasma_desc_t A, plasma_desc_t B,
                   plasma_sequence_t *sequence, plasma_request_t *request)
{
    int k, m, n;
    int ldak, ldam, ldan, ldbk, ldbm;
    int tempkm, tempkn, tempmm, tempnn;

    plasma_complex64_t zone = 1.0;

    // Check sequence status.
    if (sequence->status != PlasmaSuccess) {
        plasma_request_fail(sequence, request, PlasmaErrorSequence);
        return;
    }

    if (side == PlasmaLeft) {
        if (uplo == PlasmaUpper) {
            //===========================================
            // PlasmaLeft / PlasmaUpper / PlasmaNoTrans
            //===========================================
            if (trans == PlasmaNoTrans) {
                for (m = 0; m < B.mt; m++) {
                    tempmm = plasma_tile_mdim(B, m);
                    ldbm = plasma_tile_mdim(B, m);
                    ldam = plasma_tile_mdim(A, m);
                    for (n = 0; n < B.nt; n++) {
                        tempnn = plasma_tile_ndim(B, n);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(m, m), ldam,
                                   B(m, n), ldbm);

                        for (k = m+1; k < A.mt; k++) {
                            tempkn = plasma_tile_ndim(A, k);
                            ldbk = plasma_tile_mdim(B, k);
                            core_omp_zgemm(
                                trans, PlasmaNoTrans,
                                tempmm, tempnn, tempkn,
                                alpha, A(m, k), ldam,
                                       B(k, n), ldbk,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
            //================================================
            // PlasmaLeft / PlasmaUpper / Plasma[_Conj]Trans
            //================================================
            else {
                for (m = B.mt-1; m > -1; m--) {
                    tempmm = plasma_tile_mdim(B, m);
                    ldbm = plasma_tile_mdim(B, m);
                    ldam = plasma_tile_mdim(A, m);
                    for (n = 0; n < B.nt; n++) {
                        tempnn = plasma_tile_ndim(B, n);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(m, m), ldam,
                                   B(m, n), ldbm);

                        for (k = 0; k < m; k++) {
                            ldbk = plasma_tile_mdim(B, k);
                            ldak = plasma_tile_mdim(A, k);
                            core_omp_zgemm(
                                trans, PlasmaNoTrans,
                                tempmm, tempnn, B.mb,
                                alpha, A(k, m), ldak,
                                       B(k, n), ldbk,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
        }
        else {
            //===========================================
            // PlasmaLeft / PlasmaLower / PlasmaNoTrans
            //===========================================
            if (trans == PlasmaNoTrans) {
                for (m = B.mt-1; m > -1; m--) {
                    tempmm = plasma_tile_mdim(B, m);
                    ldbm = plasma_tile_mdim(B, m);
                    ldam = plasma_tile_mdim(A, m);
                    for (n = 0; n < B.nt; n++) {
                        tempnn = plasma_tile_ndim(B, n);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(m, m), ldam,
                                   B(m, n), ldbm);

                        for (k = 0; k < m; k++) {
                            ldbk = plasma_tile_mdim(B, k);
                            core_omp_zgemm(
                                trans, PlasmaNoTrans,
                                tempmm, tempnn, B.mb,
                                alpha, A(m, k), ldam,
                                       B(k, n), ldbk,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
            //================================================
            // PlasmaLeft / PlasmaLower / Plasma[_Conj]Trans
            //================================================
            else {
                for (m = 0; m < B.mt; m++) {
                    tempmm = plasma_tile_mdim(B, m);
                    ldbm = plasma_tile_mdim(B, m);
                    ldam = plasma_tile_mdim(A, m);
                    for (n = 0; n < B.nt; n++) {
                        tempnn = plasma_tile_ndim(B, n);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(m, m), ldam,
                                   B(m, n), ldbm);

                        for (k = m+1; k < A.mt; k++) {
                            tempkm = plasma_tile_mdim(A, k);
                            ldak = plasma_tile_mdim(A, k);
                            ldbk = plasma_tile_mdim(B, k);
                            core_omp_zgemm(
                                trans, PlasmaNoTrans,
                                tempmm, tempnn, tempkm,
                                alpha, A(k, m), ldak,
                                       B(k, n), ldbk,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
        }
    }
    else {
        if (uplo == PlasmaUpper) {
            //============================================
            // PlasmaRight / PlasmaUpper / PlasmaNoTrans
            //============================================
            if (trans == PlasmaNoTrans) {
                for (n = B.nt-1; n > -1; n--) {
                    tempnn = plasma_tile_ndim(B, n);
                    ldan = plasma_tile_mdim(A, n);
                    for (m = 0; m < B.mt; m++) {
                        tempmm = plasma_tile_mdim(B, m);
                        ldbm = plasma_tile_mdim(B, m);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(n, n), ldan,
                                   B(m, n), ldbm);

                        for (k = 0; k < n; k++) {
                            ldak = plasma_tile_mdim(A, k);
                            core_omp_zgemm(
                                PlasmaNoTrans, trans,
                                tempmm, tempnn, B.mb,
                                alpha, B(m, k), ldbm,
                                       A(k, n), ldak,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
            //=================================================
            // PlasmaRight / PlasmaUpper / Plasma[_Conj]Trans
            //=================================================
            else {
                for (n = 0; n < B.nt; n++) {
                    tempnn = plasma_tile_ndim(B, n);
                    ldan = plasma_tile_mdim(A, n);
                    for (m = 0; m < B.mt; m++) {
                        tempmm = plasma_tile_mdim(B, m);
                        ldbm = plasma_tile_mdim(B, m);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(n, n), ldan,
                                   B(m, n), ldbm);

                        for (k = n+1; k < A.mt; k++) {
                            tempkn = plasma_tile_ndim(A, k);
                            core_omp_zgemm(
                                PlasmaNoTrans, trans,
                                tempmm, tempnn, tempkn,
                                alpha, B(m, k), ldbm,
                                       A(n, k), ldan,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
        }
        else {
            //============================================
            // PlasmaRight / PlasmaLower / PlasmaNoTrans
            //============================================
            if (trans == PlasmaNoTrans) {
                for (n = 0; n < B.nt; n++) {
                    tempnn = plasma_tile_ndim(B, n);
                    ldan = plasma_tile_mdim(A, n);
                    for (m = 0; m < B.mt; m++) {
                        tempmm = plasma_tile_mdim(B, m);
                        ldbm = plasma_tile_mdim(B, m);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(n, n), ldan,
                                   B(m, n), ldbm);

                        for (k = n+1; k < A.mt; k++) {
                            tempkn = plasma_tile_ndim(A, k);
                            ldak = plasma_tile_mdim(A, k);
                            core_omp_zgemm(
                                PlasmaNoTrans, trans,
                                tempmm, tempnn, tempkn,
                                alpha, B(m, k), ldbm,
                                       A(k, n), ldak,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
            //=================================================
            // PlasmaRight / PlasmaLower / Plasma[_Conj]Trans
            //=================================================
            else {
                for (n = B.nt-1; n > -1; n--) {
                    tempnn = plasma_tile_ndim(B, n);
                    ldan = plasma_tile_mdim(A, n);
                    for (m = 0; m < B.mt; m++) {
                        tempmm = plasma_tile_mdim(B, m);
                        ldbm = plasma_tile_mdim(B, m);
                        core_omp_ztrmm(
                            side, uplo, trans, diag,
                            tempmm, tempnn,
                            alpha, A(n, n), ldan,
                                   B(m, n), ldbm);

                        for (k = 0; k < n; k++) {
                            core_omp_zgemm(
                                PlasmaNoTrans, trans,
                                tempmm, tempnn, B.mb,
                                alpha, B(m, k), ldbm,
                                       A(n, k), ldan,
                                zone,  B(m, n), ldbm);
                        }
                    }
                }
            }
        }
    }
}
