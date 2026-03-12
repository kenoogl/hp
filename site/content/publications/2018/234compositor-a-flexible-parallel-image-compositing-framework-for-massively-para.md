---
title: '234Compositor: A flexible parallel image compositing framework for massively parallel visualization environments'
date: 2018-01-01
authors: 'Jorji Nonaka and Kenji Ono and Masahiro Fujita'
journal: 'Future Generation Computer Systems'
year: '2018'
pub_type: 'journal'
doi: 'https://doi.org/10.1016/j.future.2017.02.011'
doi_url: 'http://www.sciencedirect.com/science/article/pii/S0167739X17302030'
abstract: 'Leading-edge HPC systems have already been generating a vast amount of time-varying complex data sets, and future-generation HPC systems are expected to produce much higher amounts of such data, thus making their visualization and analysis a much more challenging task. In such scenario, the In-situ visualization approach, where the same HPC system is used for both numerical simulation and visualization, is expected to become more a necessity than an option. On massively parallel environments, the Sort-last approach, which requires final image compositing, has become the de facto standard for parallel rendering. In this work, we present the 234Compositor, a scalable and flexible parallel image compositor framework for massively parallel rendering applications. It is composed of a single-stage power-of-two conversion mechanism based on 234 Scheduling of 3-2 and 2-1 Eliminations, and a final image gathering mechanism based on Data Padding and MPI Rank Reordering for enabling the use of MPI_Gather collective operation. In addition, the hybrid MPI/OpenMP parallelism can also be applied to take advantage of current multi-node, multi-core architecture of modern HPC systems. We confirmed the scalability of the proposed approach by evaluating a Binary-Swap implementation of 234Compositor on the K computer, a Japanese leading-edge supercomputer installed at RIKEN AICS. We also evaluated an integration with HIVE (Heterogeneously Integrated Visual-analytic Environment) in order to verify a real-world usage. From the encouraging scalability results, we expect that this approach can also be useful even on the next-generation HPC systems which may demand higher level of parallelism.'
---

