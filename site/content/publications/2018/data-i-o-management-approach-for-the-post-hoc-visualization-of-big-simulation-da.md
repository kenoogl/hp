---
title: 'Data I/O management approach for the post-hoc visualization of big simulation data results'
date: 2018-01-01
authors: 'Nonaka, Jorji and Inacio, Eduardo C. and Ono, Kenji and Dantas, Mario A. R. and Kawashima, Yasuhiro and Kawanabe, Tomohiro and Shoji, Fumiyoshi'
journal: 'International Journal of Modeling, Simulation, and Scientific Computing'
year: '2018'
pub_type: 'journal'
doi: '10.1142/S1793962318400068'
doi_url: 'https://doi.org/10.1142/S1793962318400068'
abstract: 'Leading-edge supercomputers, such as the K computer, have generated a vast amount of simulation results, and most of these datasets were stored on the file system for the post-hoc analysis such as visualization. In this work, we first investigated the data generation trends of the K computer by analyzing some operational log data files. We verified a tendency of generating large amounts of distributed files as simulation outputs, and in most cases, the number of files has been proportional to the number of utilized computational nodes, that is, each computational node producing one or more files. Considering that the computational cost of visualization tasks is usually much smaller than that required for large-scale numerical simulations, a flexible data input/output (I/O) management mechanism becomes highly useful for the post-hoc visualization and analysis. In this work, we focused on the xDMlib data management library, and its flexible data I/O mechanism in order to enable flexible data loading of big computational climate simulation results. In the proposed approach, a pre-processing is executed on the target distributed files for generating a light-weight metadata necessary for the elaboration of the data assignment mapping used in the subsequent data loading process. We evaluated the proposed approach by using a 32-node visualization cluster, and the K computer. Besides the inevitable performance penalty associated with longer data loading time, when using smaller number of processes, there is a benefit for avoiding any data replication via copy, conversion, or extraction. In addition, users will be able to freely select any number of nodes, without caring about the number of distributed files, for the post-hoc visualization and analysis purposes.'
---

