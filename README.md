~~~~
 _ \ |      \    __|  \  |   \
 __/ |     _ \ \__ \ |\/ |  _ \
_|  ____|_/  _\____/_|  _|_/  _\
~~~~

**Parallel Linear Algebra Software for Multicore Architectures**

**University of Tennessee (US)**

**University of Manchester (UK)**

About PLASMA
============

PLASMA is a software package for solving problems in dense linear algebra
using multicore processors and Xeon Phi coprocessors.
PLASMA provides implementations of state-of-the-art algorithms
using cutting-edge task scheduling techniques.
PLASMA currently offers a collection of routines
for solving linear systems of equations, least squares problems,
eigenvalue problems, and singular value problems.

PLASMA is in the process of porting form [QUARK](http://icl.cs.utk.edu/quark/)
to [OpenMP](http://openmp.org/wp/).
At the same time, it is moving from its ICL SVN repository
to this Bitbucket Mercurial repository.
The content of this repository reflects the progress of the transition.
Before the transition is complete, the last release of the old PLASMA
is available here: https://bitbucket.org/icl/plasma/downloads/plasma_2.8.0.tar.gz

Documentation
=============

Doxygen-generated PLASMA documentation is available at:
http://icl.bitbucket.org/plasma/doxygen/

Get Assistance
==============

To get assistance with PLASMA, join the *PLASMA User* Google group by going to
https://groups.google.com/a/icl.utk.edu/forum/#!forum/plasma-user and clicking
`Apply to join group`.
Then email your questions and comments to `plasma-user@icl.utk.edu`.

Cite PLASMA
===========

Feel free to use the following publications to reference PLASMA:

* Asim YarKhan, Jakub Kurzak, Piotr Luszczek, Jack Dongarra,
  **Porting the PLASMA Numerical Library to the OpenMP Standard**,
  *International Journal of Parallel Programming*,
  [First Online: 14 June 2016](http://dx.doi.org/10.1007/s10766-016-0441-6).

* Simplice Donfack, Jack Dongarra, Mathieu Faverge, Mark Gates,
  Jakub Kurzak, Piotr Luszczek, Ichitaro Yamazaki,
  **A survey of recent developments in parallel implementations
  of Gaussian elimination**,
  *Concurrency and Computation: Practice and Experience*,
  [Volume 27, Issue 5, April 2015, Pages 1292–1309](http://dx.doi.org/10.1002/cpe.3306).

* Azzam Haidar, Jakub Kurzak, Piotr Luszczek,
  **An improved parallel singular value algorithm and its implementation
  for multicore hardware**,
  *Proceedings of the International Conference on High Performance Computing,
  Networking, Storage and Analysis*
  [Article No. 90](http://dx.doi.org/10.1145/2503210.2503292), ACM, 2013.

* Jakub Kurzak, Hatem Ltaief, Jack Dongarra, Rosa M. Badia,
  **Scheduling dense linear algebra operations on multicore processors**,
  *Concurrency and Computation: Practice and Experience*,
  [Volume 22, Issue 1, January 2010, Pages 15–44](http://dx.doi.org/10.1002/cpe.1467).

* Alfredo Buttari, Julien Langou, Jakub Kurzak, Jack Dongarra,
  **A class of parallel tiled linear algebra algorithms for multicore architectures**,
  *Parallel Computing*,
  [Volume 35, Issue 1, January 2009, Pages 38–53](http://dx.doi.org/10.1016/j.parco.2008.10.002).

PLASMA Funding
==============

Primary funding for PLASMA was provided by NSF grants:

* [CPA-ACR-T: PLASMA:
   Parallel Linear Algebra Software for Multiprocessor Architectures]
  (http://www.nsf.gov/awardsearch/showAward?AWD_ID=0811642),

* [Collaborative CPA-ACR-T: PLASMA:
   Parallel Linear Algebra Software for Multiprocessor Architectures.]
  (http://www.nsf.gov/awardsearch/showAward?AWD_ID=0811520)

Work on PLASMA was also partially funded by NSF grants:

* [SI2-SSI: Collaborative Research:
   Sustained Innovation for Linear Algebra Software (SILAS)]
  (http://www.nsf.gov/awardsearch/showAward?AWD_ID=1339822),

* [SHF: Small:
   Empirical Autotuning of Parallel Computation for Scalable Hybrid Systems]
  (http://nsf.gov/awardsearch/showAward?AWD_ID=1527706).

Additional funding was provided by the following companies:

* Microsoft Corporation,
* Intel Corporation,
* Advanced Micro Devices,
* The MathWorks,
* Fujitsu.

PLASMA People
=============

The following people contributed to the development of PLASMA:

* Maksims Abalenkovs
* Emmanuel Agullo
* Wesley Alvaro
* Dulceneia Becker
* Alfredo Buttari
* Jack Dongarra
* Joseph Dorris
* Mathieu Faverge
* Mark Gates
* Fred Gustavson
* Bilel Hadri
* Azzam Haidar
* Blake Haugen
* Vijay Joshi
* Bo Kågström
* Lars Karlsson
* Jakub Kurzak
* Julien Langou
* Julie Langou
* Hatem Ltaief
* Piotr Luszczek
* Samuel Relton
* Stanimire Tomov
* Pedro Valero Lara
* Ichitaro Yamazaki
* Asim YarKhan
* Mawussi Zounon

PLASMA License
==============

```
  -- Innovative Computing Laboratory
  -- University of Tennessee
  -- (C) Copyright 2008-2016

  Redistribution  and  use  in  source and binary forms, with or without
  modification,  are  permitted  provided  that the following conditions
  are met:

  * Redistributions  of  source  code  must  retain  the above copyright
    notice,  this  list  of  conditions  and  the  following  disclaimer.
  * Redistributions  in  binary  form must reproduce the above copyright
    notice,  this list of conditions and the following disclaimer in the
    documentation  and/or other materials provided with the distribution.
  * Neither  the  name of the University of Tennessee, Knoxville nor the
    names of its contributors may be used to endorse or promote products
    derived from this software without specific prior written permission.

  THIS  SOFTWARE  IS  PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  ``AS IS''  AND  ANY  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
  A  PARTICULAR  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
  HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
  SPECIAL,  EXEMPLARY,  OR  CONSEQUENTIAL  DAMAGES  (INCLUDING,  BUT NOT
  LIMITED  TO,  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
  DATA,  OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
  THEORY  OF  LIABILITY,  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
  OF  THIS  SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
