---
title: 'Error-bounded Scalable Parallel Tensor Train Decomposition'
date: 2023-05-01
authors: 'Xie, Shiyao and Miura, Akinori and Ono, Kenji'
journal: '2023 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)'
year: '2023'
pub_type: 'international-conference'
peer_reviewed: true
doi: '10.1109/IPDPSW59300.2023.00064'
abstract: 'Tensor train (TT) decomposition is a method for approximating and analysing tensors. TT-SVD, the most commonly used TT decomposition algorithm, computes the TT-format of a tensor in a sequential manner by alternately reshaping and compressing the tensor. For large tensors, this requires a large amount of computation time and memory. In this paper, we propose a distributed parallel algorithm, PTTD, to perform TT decomposition, which distributes parts of the tensor to all processes, decomposes it in parallel using TT-SVD, and merges the results to obtain the TT-format of the original tensor. Rounding is applied to reduce the size of the merged TT-formats. The algorithm is deterministic, which means that approximation error is controllable and there is no need to know the TT-ranks of the tensor in advance. Experimental results show that PTTD achieves an average speedup of $5384 \times$ using 8192 cores, and that the approximation error decreases as the number of cores increases, at the cost of slowly growing TT-ranks.'
---

