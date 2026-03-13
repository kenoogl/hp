---
title: 'A Scalable Parallel Partition Tridiagonal Solver for Many-Core and Low B/F Processors'
date: 2022-05-01
authors: 'Mitsuda, Tatsuya and Ono, Kenji'
journal: '2022 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)'
year: '2022'
pub_type: 'international-conference'
peer_reviewed: true
doi: '10.1109/IPDPSW55747.2022.00142'
abstract: 'Tridiagonal systems are among the most fundamental computations in science, engineering, and mathematics, and one solver used in such systems is Tree Partitioning Reduction (TPR), which is a divide-and-conquer method that solves large-scale linear equations by dividing them and then computing the parts in parallel within different local memory threads. Herein, we propose an improved TPR algorithm that has a parallel cyclic reduction flavor, with which we reduced the number of algorithm steps by approximately half while simultaneously increasing arithmetic intensity and cache reusability. A performance evaluation conducted on an Intel Skylake-SP microprocessor showed a high hit ratio for the L1 cache and that our solver was as much as 31 times faster on 32 threads for 262144 equations. In the case of a Nvidia Tesla P100 GPU, our method processed 10 MRow/s more than TPR and cuSPARSE.'
---

