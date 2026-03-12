---
title: "Equation Discovery (EN)"
date: 2026-03-12
summary: "A data-driven approach to discover governing equations from simulation and observation data."
---

日本語版: [Equation Discovery (JP)](/research/equation-discovery/)

## Equation Discovery via Genetic Programming

With advances in computing, observation, and simulation technologies, large volumes of data are now generated routinely. Extracting meaningful knowledge from such data is increasingly important.  
In this work, the target data are formulated as a symbolic regression problem, and a process is established to discover governing equations through evolutionary computation.

The proposed method introduces partial-derivative operators into genetic programming to automatically construct candidate partial differential equations. These generated equations are evaluated against data, and equations with lower error are selected automatically.

Through numerical experiments on fluid simulation data, the method was used to estimate governing equations and its effectiveness was evaluated. The results showed that the original equations can be recovered with high probability, indicating that the proposed approach is an effective tool for discovering useful models from data.

<img src="/images/GP_overview.png" alt="Overview of equation discovery by genetic programming" style="max-width:600px; width:100%; height:auto; display:block; margin:0.5rem auto;">

### Key Publications

- Kenji Ono and Issei Koga, *Estimation of Governing Equations by Genetic Programming*, Transactions of JSCES, DOI: [10.11421/jsces.2020.20201004](https://doi.org/10.11421/jsces.2020.20201004), 2020.
- Kenji Ono and Kanae Shiragami, *Equation discovery through genetic programming reflecting the importance of generated terms*, 16th World Congress on Computational Mechanics / 4th Pan American Congress on Computational Mechanics, 2024.
