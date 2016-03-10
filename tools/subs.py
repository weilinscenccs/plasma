# Substitutions used in codegen.py
#
# Substitutions are applied in the order listed. This is important in cases
# where multiple substitutions could match, or when one substitution matches
# the result of a previous substitution. For example, these rules are correct
# in this order:
#
#    ('real',   'double precision',  'real',   'double precision' ),  # before double
#    ('float',  'double',            'float',  'double'           ),
#
# but if switched would translate 'double precision' -> 'float precision',
# which is wrong.
#
# @author Mark Gates


# ===========================================================================
# utilitiy functions

# ----------------------------------------
def upper( table ):
    '''
    Maps double-nested list of strings to upper case.
    [ ['Foo', 'bar'], ['baz', 'ZAB'] ]
    becomes
    [ ['FOO', 'BAR'], ['BAZ', 'ZAB'] ]
    '''
    ucase = [ [ x.upper() for x in row ] for row in table ]
    return ucase
# end


# ----------------------------------------
def lower( table ):
    '''
    Maps double-nested list of strings to lower case.
    [ ['Foo', 'BAR'], ['BAZ', 'zab'] ]
    becomes
    [ ['foo', 'bar'], ['baz', 'zab'] ]
    '''
    lcase = [ [ x.lower() for x in row ] for row in table ]
    return lcase
# end


# ----------------------------------------
def title( table ):
    '''
    Maps double-nested list of strings to Title case. Useful for cuBLAS.
    [ ['FOO', 'bar'], ['Baz', 'Zab'] ]
    becomes
    [ ['Foo', 'Bar'], ['Baz', 'Zab'] ]
    '''
    tcase = [ [ x.title() for x in row ] for row in table ]
    return tcase
# end


# ===========================================================================
# BLAS and LAPACK routines need both lower and uppercase, for example:
# in filenames:              zgetrf.cpp
# in magma_zlapack.h:        FORTRAN_NAME( zaxpy, ZAXAPY )
# in doxygen documentation:  ZGETRF computes ...
# BLAS also needs Titlecase: cublasZaxpy
# The easiest way to maintain this is to separate these lists here,
# and use them later with the above lower, upper, and title routines.

# ----------------------------------------
blas_mixed = [
    # BLAS and LAPACK, lowercase, alphabetic order
    # for mixed precision
    # double/single,         double-complex/single-complex
    #'12345678901234567890', '12345678901234567890')
    ('daxpy',                'zaxpy'               ),
    ('ddot',                 'zdotc'               ),
    ('dgemm',                'zgemm'               ),
    ('dgeqrf',               'zgeqrf'              ),
    ('dgeqrs',               'zgeqrs'              ),
    ('dgesv',                'zgesv'               ),
    ('dgetrf',               'zgetrf'              ),
    ('dgetrs',               'zgetrs'              ),
    ('dlacpy',               'zlacpy'              ),
    ('dlag2s',               'zlag2c'              ),
    ('dlagsy',               'zlaghe'              ),
    ('dlange',               'zlange'              ),
    ('dlansy',               'zlanhe'              ),
    ('dlansy',               'zlansy'              ),
    ('dlarnv',               'zlarnv'              ),
    ('dlat2s',               'zlat2c'              ),
    ('dnrm2',                'dznrm2'              ),
    ('dormqr',               'zunmqr'              ),
    ('dpotrf',               'zpotrf'              ),
    ('dpotrs',               'zpotrs'              ),
    ('dsymm',                'zhemm'               ),
    ('dsymv',                'zhemv'               ),
    ('dsyrk',                'zherk'               ),
    ('dtrmm',                'ztrmm'               ),
    ('dtrsm',                'ztrsm'               ),
    ('dtrsv',                'ztrsv'               ),
    ('idamax',               'izamax'              ),
    ('slag2d',               'clag2z'              ),
    ('slansy',               'clanhe'              ),
    ('slat2d',               'clat2z'              ),
    ('spotrf',               'cpotrf'              ),
    ('strmm',                'ctrmm'               ),
    ('strsm',                'ctrsm'               ),
    ('strsv',                'ctrsv'               ),
]


# ----------------------------------------
blas = [
    # BLAS, lowercase, alphabetic order
    # single                  double                  single-complex          double-complex
    #'12345678901234567890', '12345678901234567890', '12345678901234567890', '12345678901234567890')
    ('isamax',               'idamax',               'icamax',               'izamax'              ),
    ('isamax',               'idamax',               'isamax',               'idamax'              ),
    ('isamin',               'idamin',               'icamin',               'izamin'              ),
    ('sasum',                'dasum',                'scasum',               'dzasum'              ),
    ('saxpy',                'daxpy',                'caxpy',                'zaxpy'               ),
    ('scopy',                'dcopy',                'ccopy',                'zcopy'               ),
    ('scopy',                'dcopy',                'scopy',                'dcopy'               ),
    ('sdot',                 'ddot',                 'cdotc',                'zdotc'               ),
    ('sdot',                 'ddot',                 'cdotu',                'zdotu'               ),
    ('sgemm',                'dgemm',                'cgemm',                'zgemm'               ),
    ('sgemv',                'dgemv',                'cgemv',                'zgemv'               ),
    ('sger',                 'dger',                 'cgerc',                'zgerc'               ),
    ('sger',                 'dger',                 'cgeru',                'zgeru'               ),
    ('snrm2',                'dnrm2',                'scnrm2',               'dznrm2'              ),
    ('srot',                 'drot',                 'crot',                 'zrot'                ),
    ('srot',                 'drot',                 'csrot',                'zdrot'               ),
    ('srot',                 'drot',                 'srot',                 'drot'                ),
    ('sscal',                'dscal',                'cscal',                'zscal'               ),
    ('sscal',                'dscal',                'csscal',               'zdscal'              ),
    ('sscal',                'dscal',                'sscal',                'dscal'               ),
    ('sswap',                'dswap',                'cswap',                'zswap'               ),
    ('ssymm',                'dsymm',                'chemm',                'zhemm'               ),
    ('ssymm',                'dsymm',                'csymm',                'zsymm'               ),
    ('ssymv',                'dsymv',                'chemv',                'zhemv'               ),
    ('ssymv',                'dsymv',                'csymv',                'zsymv'               ),
    ('ssyr',                 'dsyr',                 'cher',                 'zher'                ),  # also does zher2, zher2k, zherk
    ('ssyr',                 'dsyr',                 'csyr',                 'zsyr'                ),  # also does zsyrk, zsyr2k
    ('strmm',                'dtrmm',                'ctrmm',                'ztrmm'               ),
    ('strmv',                'dtrmv',                'ctrmv',                'ztrmv'               ),
    ('strsm',                'dtrsm',                'ctrsm',                'ztrsm'               ),
    ('strsv',                'dtrsv',                'ctrsv',                'ztrsv'               ),
]


# ----------------------------------------
lapack = [
    # LAPACK, lowercase, alphabetic order
    # single                  double                  single-complex          double-complex
    #'12345678901234567890', '12345678901234567890', '12345678901234567890', '12345678901234567890')
    ('sbdsdc',               'dbdsdc',               'sbdsdc',               'dbdsdc'              ),
    ('sbdsqr',               'dbdsqr',               'cbdsqr',               'zbdsqr'              ),
    ('sbdt01',               'dbdt01',               'cbdt01',               'zbdt01'              ),
    ('sgbbrd',               'dgbbrd',               'cgbbrd',               'zgbbrd'              ),
    ('sgebak',               'dgebak',               'cgebak',               'zgebak'              ),
    ('sgebal',               'dgebal',               'cgebal',               'zgebal'              ),
    ('sgebd2',               'dgebd2',               'cgebd2',               'zgebd2'              ),
    ('sgebrd',               'dgebrd',               'cgebrd',               'zgebrd'              ),
    ('sgeev',                'dgeev',                'cgeev',                'zgeev'               ),
    ('sgegqr',               'dgegqr',               'cgegqr',               'zgegqr'              ),
    ('sgehd2',               'dgehd2',               'cgehd2',               'zgehd2'              ),
    ('sgehrd',               'dgehrd',               'cgehrd',               'zgehrd'              ),
    ('sgelq2',               'dgelq2',               'cgelq2',               'zgelq2'              ),
    ('sgelqf',               'dgelqf',               'cgelqf',               'zgelqf'              ),
    ('sgelqs',               'dgelqs',               'cgelqs',               'zgelqs'              ),
    ('sgels',                'dgels',                'cgels',                'zgels'               ),
    ('sgeqlf',               'dgeqlf',               'cgeqlf',               'zgeqlf'              ),
    ('sgeqp3',               'dgeqp3',               'cgeqp3',               'zgeqp3'              ),
    ('sgeqr2',               'dgeqr2',               'cgeqr2',               'zgeqr2'              ),
    ('sgeqrf',               'dgeqrf',               'cgeqrf',               'zgeqrf'              ),
    ('sgeqrs',               'dgeqrs',               'cgeqrs',               'zgeqrs'              ),
    ('sgeqrt',               'dgeqrt',               'cgeqrt',               'zgeqrt'              ),
    ('sgerfs',               'dgerfs',               'cgerfs',               'zgerfs'              ),
    ('sgesdd',               'dgesdd',               'cgesdd',               'zgesdd'              ),
    ('sgessm',               'dgessm',               'cgessm',               'zgessm'              ),
    ('sgesv',                'dgesv',                'cgesv',                'zgesv'               ),  # also does zgesvd
    ('sget22',               'dget22',               'cget22',               'zget22'              ),
    ('sgetf2',               'dgetf2',               'cgetf2',               'zgetf2'              ),
    ('sgetmi',               'dgetmi',               'cgetmi',               'zgetmi'              ),
    ('sgetmo',               'dgetmo',               'cgetmo',               'zgetmo'              ),
    ('sgetrf',               'dgetrf',               'cgetrf',               'zgetrf'              ),
    ('sgetri',               'dgetri',               'cgetri',               'zgetri'              ),
    ('sgetrs',               'dgetrs',               'cgetrs',               'zgetrs'              ),
    ('shseqr',               'dhseqr',               'chseqr',               'zhseqr'              ),
    ('shst01',               'dhst01',               'chst01',               'zhst01'              ),
    ('slabad',               'dlabad',               'slabad',               'dlabad'              ),
    ('slabrd',               'dlabrd',               'clabrd',               'zlabrd'              ),
    ('slacgv',               'dlacgv',               'clacgv',               'zlacgv'              ),
    ('slacp2',               'dlacp2',               'clacp2',               'zlacp2'              ),
    ('slacpy',               'dlacpy',               'clacpy',               'zlacpy'              ),
    ('slacrm',               'dlacrm',               'clacrm',               'zlacrm'              ),
    ('sladiv',               'dladiv',               'cladiv',               'zladiv'              ),
    ('slaed',                'dlaed',                'slaed',                'dlaed'               ),
    ('slaex',                'dlaex',                'slaex',                'dlaex'               ),
    ('slag2d',               'dlag2s',               'clag2z',               'zlag2c'              ),
    ('slagsy',               'dlagsy',               'claghe',               'zlaghe'              ),
    ('slagsy',               'dlagsy',               'clagsy',               'zlagsy'              ),
    ('slahr',                'dlahr',                'clahr',                'zlahr'               ),
    ('slaln2',               'dlaln2',               'slaln2',               'dlaln2'              ),
    ('slamc3',               'dlamc3',               'slamc3',               'dlamc3'              ),
    ('slamch',               'dlamch',               'slamch',               'dlamch'              ),
    ('slamrg',               'dlamrg',               'slamrg',               'dlamrg'              ),
    ('slange',               'dlange',               'clange',               'zlange'              ),
    ('slanst',               'dlanst',               'clanht',               'zlanht'              ),
    ('slansy',               'dlansy',               'clanhe',               'zlanhe'              ),
    ('slansy',               'dlansy',               'clansy',               'zlansy'              ),
    ('slantr',               'dlantr',               'clantr',               'zlantr'              ),
    ('slapy3',               'dlapy3',               'slapy3',               'dlapy3'              ),
    ('slaqp2',               'dlaqp2',               'claqp2',               'zlaqp2'              ),
    ('slaqps',               'dlaqps',               'claqps',               'zlaqps'              ),
    ('slaqtrs',              'dlaqtrs',              'claqtrs',              'zlaqtrs'             ),
    ('slarcm',               'dlarcm',               'clarcm',               'zlarcm'              ),
    ('slarf',                'dlarf',                'clarf',                'zlarf'               ),  # also does zlarfb, zlarfg, etc.
    ('slarnv',               'dlarnv',               'clarnv',               'zlarnv'              ),
    ('slarnv',               'dlarnv',               'slarnv',               'dlarnv'              ),
    ('slartg',               'dlartg',               'clartg',               'zlartg'              ),
    ('slascl',               'dlascl',               'clascl',               'zlascl'              ),
    ('slaset',               'dlaset',               'claset',               'zlaset'              ),
    ('slasrt',               'dlasrt',               'slasrt',               'dlasrt'              ),
    ('slaswp',               'dlaswp',               'claswp',               'zlaswp'              ),
    ('slasyf',               'dlasyf',               'clahef',               'zlahef'              ),
    ('slatms',               'dlatms',               'clatms',               'zlatms'              ),
    ('slatrd',               'dlatrd',               'clatrd',               'zlatrd'              ),
    ('slatrs',               'dlatrs',               'clatrs',               'zlatrs'              ),
    ('slauum',               'dlauum',               'clauum',               'zlauum'              ),
    ('slavsy',               'dlavsy',               'clavhe',               'zlavhe'              ),
    ('sorg2r',               'dorg2r',               'cung2r',               'zung2r'              ),
    ('sorgbr',               'dorgbr',               'cungbr',               'zungbr'              ),
    ('sorghr',               'dorghr',               'cunghr',               'zunghr'              ),
    ('sorglq',               'dorglq',               'cunglq',               'zunglq'              ),
    ('sorgql',               'dorgql',               'cungql',               'zungql'              ),
    ('sorgqr',               'dorgqr',               'cungqr',               'zungqr'              ),
    ('sorgtr',               'dorgtr',               'cungtr',               'zungtr'              ),
    ('sorm2r',               'dorm2r',               'cunm2r',               'zunm2r'              ),
    ('sormbr',               'dormbr',               'cunmbr',               'zunmbr'              ),
    ('sormlq',               'dormlq',               'cunmlq',               'zunmlq'              ),
    ('sormql',               'dormql',               'cunmql',               'zunmql'              ),
    ('sormqr',               'dormqr',               'cunmqr',               'zunmqr'              ),
    ('sormr2',               'dormr2',               'cunmr2',               'zunmr2'              ),
    ('sormtr',               'dormtr',               'cunmtr',               'zunmtr'              ),
    ('sort01',               'dort01',               'cunt01',               'zunt01'              ),
    ('spack',                'dpack',                'cpack',                'zpack'               ),
    ('splgsy',               'dplgsy',               'cplghe',               'zplghe'              ),
    ('splgsy',               'dplgsy',               'cplgsy',               'zplgsy'              ),
    ('splrnt',               'dplrnt',               'cplrnt',               'zplrnt'              ),
    ('sposv',                'dposv',                'cposv',                'zposv'               ),
    ('spotf2',               'dpotf2',               'cpotf2',               'zpotf2'              ),
    ('spotrf',               'dpotrf',               'cpotrf',               'zpotrf'              ),
    ('spotri',               'dpotri',               'cpotri',               'zpotri'              ),
    ('spotrs',               'dpotrs',               'cpotrs',               'zpotrs'              ),
    ('sqpt01',               'dqpt01',               'cqpt01',               'zqpt01'              ),
    ('sqrt02',               'dqrt02',               'cqrt02',               'zqrt02'              ),
    ('ssbtrd',               'dsbtrd',               'chbtrd',               'zhbtrd'              ),
    ('sshift',               'dshift',               'cshift',               'zshift'              ),
    ('sssssm',               'dssssm',               'cssssm',               'zssssm'              ),
    ('sstebz',               'dstebz',               'sstebz',               'dstebz'              ),
    ('sstedc',               'dstedc',               'cstedc',               'zstedc'              ),
    ('sstedx',               'dstedx',               'cstedx',               'zstedx'              ),
    ('sstedx',               'dstedx',               'sstedx',               'dstedx'              ),
    ('sstegr',               'dstegr',               'cstegr',               'zstegr'              ),
    ('sstein',               'dstein',               'cstein',               'zstein'              ),
    ('sstemr',               'dstemr',               'cstemr',               'zstemr'              ),
    ('ssteqr',               'dsteqr',               'csteqr',               'zsteqr'              ),
    ('ssterf',               'dsterf',               'ssterf',               'dsterf'              ),
    ('ssterm',               'dsterm',               'csterm',               'zsterm'              ),
    ('sstt21',               'dstt21',               'cstt21',               'zstt21'              ),
    ('ssyev',                'dsyev',                'cheev',                'zheev'               ),
    ('ssyevd',               'dsyevd',               'cheevd',               'zheevd'              ),
    ('ssygs2',               'dsygs2',               'chegs2',               'zhegs2'              ),
    ('ssygst',               'dsygst',               'chegst',               'zhegst'              ),
    ('ssygvd',               'dsygvd',               'chegvd',               'zhegvd'              ),
    ('ssygvr',               'dsygvr',               'chegvr',               'zhegvr'              ),
    ('ssygvx',               'dsygvx',               'chegvx',               'zhegvx'              ),
    ('ssysv',                'dsysv',                'chesv',                'zhesv'               ),
    ('ssysv',                'dsysv',                'csysv',                'zsysv'               ),
    ('ssyt21',               'dsyt21',               'chet21',               'zhet21'              ),
    ('ssytd2',               'dsytd2',               'chetd2',               'zhetd2'              ),
    ('ssytf2',               'dsytf2',               'chetf2',               'zhetf2'              ),
    ('ssytf2',               'dsytf2',               'csytf2',               'zsytf2'              ),
    ('ssytrd',               'dsytrd',               'chetrd',               'zhetrd'              ),
    ('ssytrf',               'dsytrf',               'chetrf',               'zhetrf'              ),
    ('ssytrf',               'dsytrf',               'csytrf',               'zsytrf'              ),
    ('ssytrs',               'dsytrs',               'chetrs',               'zhetrs'              ),
    ('ssytrs',               'dsytrs',               'csytrs',               'zsytrs'              ),
    ('strevc',               'dtrevc',               'ctrevc',               'ztrevc'              ),
    ('strsmpl',              'dtrsmpl',              'ctrsmpl',              'ztrsmpl'             ),
    ('strtri',               'dtrtri',               'ctrtri',               'ztrtri'              ),
    ('stsmqr',               'dtsmqr',               'ctsmqr',               'ztsmqr'              ),
    ('stsqrt',               'dtsqrt',               'ctsqrt',               'ztsqrt'              ),
    ('ststrf',               'dtstrf',               'ctstrf',               'ztstrf'              ),
]


# ===========================================================================
# Dictionary is keyed on substitution type (mixed, normal, etc.)
subs = {
  # ------------------------------------------------------------
  # replacements applied to mixed precision files.
  'mixed': [
    # ----- header
    # double/single,         double/single-complex
    #'12345678901234567890', '12345678901234567890')
    ('ds',                   'zc'                  ),

    # ----- preprocessor
    ('#define REAL',         '#define COMPLEX'     ),
    ('#undef REAL',          '#undef COMPLEX'      ),

    # ----- Text
    ('symmetric',            'hermitian'           ),
    ('symmetric',            'Hermitian'           ),
    ('orthogonal',           'unitary'             ),

    # ----- CBLAS
    ('',                     'CBLAS_SADDR'         ),

    # ----- Complex numbers
    # See note in "normal" section below about regexps
    (r'',                   r'\bconj\b'            ),

    # ----- Constants
    # See note in "normal" section below about ConjTrans
    ('MagmaTrans',           'Magma_ConjTrans'     ),

    # ----- BLAS & LAPACK
    ]
    + title( blas_mixed )  # e.g., Dgemm, as in cuBLAS, before lowercase (e.g., for Zdrot)
    + lower( blas_mixed )  # e.g., dgemm
    + upper( blas_mixed )  # e.g., DGEMM
    + [

    # ----- PLASMA / MAGMA data types
    ('double',               'magmaDoubleComplex'  ),
    ('float',                'magmaFloatComplex'   ),
    ('double',               'PLASMA_Complex64_t'  ),
    ('float',                'PLASMA_Complex32_t'  ),

    # ----- PLASMA / MAGMA functions, alphabetic order

    # ----- Prefixes
    # See note in "normal" section below
    ('LAPACKE_d',            'LAPACKE_z'           ),
    ('LAPACKE_s',            'LAPACKE_c',          ),
    ('PLASMA_d',             'PLASMA_z'            ),
    ('PLASMA_s',             'PLASMA_c'            ),
    ('plasma_d',             'plasma_z'            ),
    ('plasma_s',             'plasma_c'            ),

  ],  # end mixed

  # ------------------------------------------------------------
  # replacements applied to most files.
  'normal': [
    # ----- header
    # single                  double                  single-complex          double-complex
    #'12345678901234567890', '12345678901234567890', '12345678901234567890', '12345678901234567890')
    ('s',                    'd',                    'c',                    'z'                   ),

    # ----- preprocessor
    ('#define PRECISION_s',  '#define PRECISION_d',  '#define PRECISION_c',  '#define PRECISION_z' ),
    ('#undef PRECISION_s',   '#undef PRECISION_d',   '#undef PRECISION_c',   '#undef PRECISION_z'  ),
    ('#define REAL',         '#define REAL',         '#define COMPLEX',      '#define COMPLEX'     ),
    ('#undef REAL',          '#undef REAL',          '#undef COMPLEX',       '#undef COMPLEX'      ),
    ('#define SINGLE',       '#define DOUBLE',       '#define SINGLE',       '#define DOUBLE'      ),
    ('#undef SINGLE',        '#undef DOUBLE',        '#undef SINGLE',        '#undef DOUBLE'       ),

    # ----- Text
    ('symmetric',            'symmetric',            'hermitian',            'hermitian'           ),
    ('symmetric',            'symmetric',            'Hermitian',            'Hermitian'           ),
    ('orthogonal',           'orthogonal',           'unitary',              'unitary'             ),
    ('%f',                   '%lf',                  '%f',                   '%lf'                 ),  # for scanf

    # ----- CBLAS
    ('',                     '',                     'CBLAS_SADDR',          'CBLAS_SADDR'         ),

    # ----- Complex numbers
    # \b regexp here avoids conjugate -> conjfugate, and fabs -> fabsf -> fabsff.
    # Note r for raw string literals, otherwise \b is a bell character.
    # The \b is deleted from replacement strings.
    # conj() and fabs() are overloaded in MAGMA, so don't need substitution.
    (r'',                   r'',                    r'\bconjf\b',           r'\bconj\b'            ),
    (r'\bfabsf\b',          r'\bfabs\b',            r'\bfabsf\b',           r'\bfabs\b'            ),
    (r'\bfabsf\b',          r'\bfabs\b',            r'\bcabsf\b',           r'\bcabs\b'            ),

    # ----- Constants
    # Do not convert ConjTrans to Trans, since in most cases ConjTrans
    # must be a valid option to real-precision functions.
    # E.g., dgemm( ConjTrans, ConjTrans, ... ) should be valid; if ConjTrans is
    # converted, then dgemm will have 2 Trans cases and no ConjTrans case.
    # Only for zlarfb and zunm*, convert it using special Magma_ConjTrans alias.
    ('MagmaTrans',           'MagmaTrans',           'Magma_ConjTrans',      'Magma_ConjTrans'     ),

    # ----- BLAS & LAPACK
    ]
    + title( blas )    # e.g., Dgemm, as in cuBLAS, before lowercase (e.g., for Zdrot)
    + lower( blas )    # e.g., dgemm
    + upper( blas )    # e.g., DGEMM
    + lower( lapack )  # e.g., dgetrf
    + upper( lapack )  # e.g., DGETRF
    + [

    # ----- PLASMA / MAGMA constants
    ('PlasmaRealFloat',      'PlasmaRealDouble',     'PlasmaComplexFloat',   'PlasmaComplexDouble' ),

    # ----- PLASMA / MAGMA data types
    ('float',                'double',               'magmaFloatComplex',    'magmaDoubleComplex'  ),
    ('float',                'double',               'PLASMA_Complex32_t',   'PLASMA_Complex64_t'  ),
    ('float',                'double',               'float',                'double'              ),

    # ----- PLASMA / MAGMA functions, alphabetic order
    ('sy2sb',                'sy2sb',                'he2hb',                'he2hb'               ),
    ('stile',                'dtile',                'ctile',                'ztile'               ),

    # ----- Prefixes
    # Most routines have already been renamed by above BLAS/LAPACK rules.
    # Functions where real == complex name can be handled here;
    # if real != complex name, it must be handled above.
    ('LAPACKE_s',            'LAPACKE_d',            'LAPACKE_c',            'LAPACKE_z'           ),
    ('PLASMA_S',             'PLASMA_D',             'PLASMA_C',             'PLASMA_Z'            ),
    ('PLASMA_s',             'PLASMA_d',             'PLASMA_c',             'PLASMA_z'            ),
    ('plasma_s',             'plasma_d',             'plasma_c',             'plasma_z'            ),
    ('TEST_S',               'TEST_D',               'TEST_C',               'TEST_Z'              ),
    ('test_s',               'test_d',               'test_c',               'test_z'              ),

  ],  # end normal
} # end subs
