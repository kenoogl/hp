---
title: "High-Performance Computing (EN)"
date: 2026-03-11
summary: "Scalable iterative solvers for large-scale sparse matrices."
---

日本語版: [High-Performance Computing (JP)](/research/hpc/)

## High-Performance Iterative Solvers for Large Sparse Matrices

### LSOR-PCR Method

In pressure Poisson equations for CFD, the linear system $A\mathbf{x}=\mathbf{b}$ typically has a large sparse matrix $A$. On modern low Byte/Flop (B/F) architectures, naive sparse matrix-vector multiplication often results in high B/F requirements, making it difficult to fully exploit available compute performance.  
To address this, we proposed the **SLOR-PCR** method, a direct-iterative hybrid approach designed to achieve both high computational throughput and scalability.

The method combines:
- SOR as the base iterative method,
- LU decomposition for efficient inversion of tridiagonal systems in the innermost loop,
- Parallel Cyclic Reduction (PCR) to improve arithmetic intensity and scalability.

> B/F denotes the ratio of data movement (Byte) to floating-point operations (Flop), a key metric for algorithm-hardware matching.

<img src="/images/SLOR-PCR-UV300.png" alt="Performance comparison of SLOR-PCR, Jacobi, and SOR on SGI UV300" style="max-width:600px; width:100%; height:auto; display:block; margin:0.5rem auto;">
Figure: Performance comparison of SLOR-PCR, Jacobi, and SOR on SGI UV300.

---

### Parallel Tree Partitioning Reduction Method

Large sparse linear systems in fluid simulations require repeated matrix-vector operations. Existing algorithms often demand high B/F, which limits performance on modern many-core architectures optimized for low B/F workloads.  
Our work targets thread-scalable sparse solvers suitable for many-core systems such as Fugaku.

The core idea is to transform equations into many mutually independent groups so that a large number of cores can be utilized efficiently. We combine:
- Tree Partitioning Reduction (TPR),
- Parallel Cyclic Reduction (PCR),

to form **PTPR**, which improves data reuse in L1 cache and increases practical performance on low B/F architectures.

<img src="/images/PTPR-1.png" alt="Performance comparison of PTPR, PCR, and TPR" style="max-width:760px; width:100%; height:auto; display:block; margin:0.5rem auto;">
Figure: Performance comparison of PTPR, PCR, and TPR.

## Key Publications

- K. Ono, T. Kato, S. Ohshima, and T. Nanri, *Scalable Direct-Iterative Hybrid Solver for Sparse Matrices on Multi-Core and Vector Architectures*, Proceedings of the International Conference on High Performance Computing in Asia-Pacific Region, pp.11-21, doi:[10.1145/3368474.3368484](https://doi.org/10.1145/3368474.3368484) (2020).
- T. Mitsuda and K. Ono, *A Scalable Parallel Partition Tridiagonal Solver for Many-Core and Low B/F Processors*, 2022 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW), doi:[10.1109/IPDPSW55747.2022.00142](https://ieeexplore.ieee.org/document/9835226) (2022).
