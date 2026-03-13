---
title: "Equation Discovery"
date: 2026-03-12
summary: "A data-driven approach for discovering mathematical models from simulation and observation data."
---

日本語版: [Equation Discovery (JP)](/research/equation-discovery/)

## Equation Discovery via Genetic Programming

With advances in computing, observation, and simulation technologies, large volumes of data are now generated routinely. Extracting meaningful knowledge from such data is increasingly important.  
In this work, the target data are formulated as a symbolic regression problem, and a process is established to discover governing equations through evolutionary computation.

The proposed method introduces partial-derivative operators into genetic programming to automatically construct candidate partial differential equations. These generated equations are evaluated against data, and equations with lower error are selected automatically.

Through numerical experiments on fluid simulation data, the method was used to estimate governing equations and its effectiveness was evaluated. The results showed that the original equations can be recovered with high probability, indicating that the proposed approach is an effective tool for discovering useful models from data.

<img src="/images/GP_overview.png" alt="Overview of equation discovery by genetic programming" style="max-width:720px; width:100%; height:auto; display:block; margin:0.5rem auto;">

## Equation Discovery via Genetic Programming Assisted by a Large Language Model

Genetic Programming (GP) is a powerful approach for discovering mathematical models directly from data. However, GP is fundamentally a heuristic search method, and the search space is extremely large. As a result, substantial computation is often required before a high-quality model is found.

To address this issue, we are developing an **LLM-GP system** that combines conventional program-based search with a Large Language Model (LLM). In this framework, part of the search process, which was previously implemented only in code, is delegated to the LLM. By leveraging pretrained knowledge and language understanding, the LLM can generate mathematically and physically meaningful candidate expressions.

The LLM plays two main roles in this system:

1. **Generating candidate model equations**  
   The LLM proposes expressions with meaningful structural patterns, allowing the search to start from more promising candidates than purely random initialization.
2. **Controlling the evolutionary computation workflow**  
   Each stage of the evolutionary process, such as initialization, mutation, crossover, and selection, can be guided through natural-language prompts. This makes it possible to modify the search strategy and evaluation policy more flexibly.

The quantitative consistency between a proposed model and the data is still evaluated on the program side using numerical criteria such as mean squared error. In other words, the system separates responsibilities as follows:

- **LLM**: search strategy and model generation
- **Program**: numerical evaluation and optimization

This division enables more efficient exploration of candidate equations. In addition, because both interactive operation and fully automated execution can be instructed in natural language, the system provides a level of flexibility that is difficult to achieve with a purely programmatic pipeline.

<img src="/images/LLM-GP_system.png" alt="Processing diagram of the LLM-GP system" style="max-width:720px; width:100%; height:auto; display:block; margin:0.5rem auto;">

### Key Publications

- Kenji Ono and Issei Koga, *Estimation of Governing Equations by Genetic Programming*, Transactions of JSCES, DOI: [10.11421/jsces.2020.20201004](https://doi.org/10.11421/jsces.2020.20201004), 2020.
- Kenji Ono and Kanae Shiragami, *Equation discovery through genetic programming reflecting the importance of generated terms*, 16th World Congress on Computational Mechanics / 4th Pan American Congress on Computational Mechanics, 2024.
