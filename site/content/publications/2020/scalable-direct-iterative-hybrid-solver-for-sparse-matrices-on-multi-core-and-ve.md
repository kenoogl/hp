---
title: 'Scalable Direct-Iterative Hybrid Solver for Sparse Matrices on Multi-Core and Vector Architectures'
date: 2020-01-01
authors: 'Ono, Kenji and Kato, Toshihiro and Ohshima, Satoshi and Nanri, Takeshi'
journal: 'Proceedings of the International Conference on High Performance Computing in Asia-Pacific Region'
year: '2020'
pub_type: 'international-conference'
peer_reviewed: true
doi: '10.1145/3368474.3368484'
doi_url: 'https://doi.org/10.1145/3368474.3368484'
abstract: 'In the present paper, we propose an efficient direct-iterative hybrid solver for sparse matrices that can derive the scalability of the latest multi-core, many-core, and vector architectures and examine the execution performance of the proposed SLOR-PCR method. We also present an efficient implementation of the PCR algorithm for SIMD and vector architectures so that it is easy to output instructions optimized by the compiler. The proposed hybrid method has high cache reusability, which is favorable for modern low B/F architecture because efficient use of the cache can mitigate the memory bandwidth limitation. The measured performance revealed that the SLOR-PCR solver showed excellent scalability up to 352 cores on the cc-NUMA environment, and the achieved performance was higher than that of the conventional Jacobi and Red-Black ordering method by a factor of 3.6 to 8.3 on the SIMD architecture. In addition, the maximum speedup in computation time was observed to be a factor of 6.3 on the cc-NUMA architecture with 352 cores.'
---

