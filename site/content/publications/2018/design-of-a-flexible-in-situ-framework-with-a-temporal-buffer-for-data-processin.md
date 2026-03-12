---
title: 'Design of a Flexible In Situ Framework with a Temporal Buffer for Data Processing and Visualization of Time-Varying Datasets'
date: 2018-01-01
authors: 'Ono, Kenji and Nonaka, Jorji and Yoshikawa, Hiroyuki and Nanri, Takeshi and Morie, Yoshiyuki and Kawanabe, Tomohiro and Shoji, Fumiyoshi'
journal: 'High Performance Computing'
year: '2018'
pub_type: 'journal'
abstract: 'This paper presents an in situ framework focused on time-varying simulations, and uses a novel temporal buffer for storing simulation results sampled at user-defined intervals. This framework has been designed to provide flexible data processing and visualization capabilities in modern HPC operational environments composed of powerful front-end systems, for pre-and post-processing purposes, along with traditional back-end HPC systems. The temporal buffer is implemented using the functionalities provided by Open Address Space (OpAS) library, which enables asynchronous one-sided communication from outside processes to any exposed memory region on the simulator side. This buffer can store time-varying simulation results, and can be processed via in situ approaches with different proximities. We present a prototype of our framework, and code integration process with a target simulation code. The proposed in situ framework utilizes separate files to describe the initialization and execution codes, which are in the form of Python scripts. This framework also enables the runtime modification of these Python-based files, thus providing greater flexibility to the users, not only for data processing, such as visualization and analysis, but also for the simulation steering.'
---

