---
title: "Scalable Iterative Solvers"
date: 2026-03-11
summary: "Scalable iterative solvers for large-scale sparse matrices."
thumbnail: "/images/SLOR-PCR-UV300.png"
slug: "iterative-solver"
top_highlight: true
---

English version: [Scalable Iterative Solvers (EN)](/research-en/iterative-solver/)

## 大規模疎行列の高性能反復計算法

### LSOR-PCR法

流体計算の圧力ポアソン方程式から導出される連立一次方程式 $A\mathbf{x}=\mathbf{b}$ の係数行列 $A$ は大規模疎行列となります。近年の高い演算性能をもつ低Byte/Flop(B/F)アーキテクチャにおいては、行列ベクトル積のナイーブな実装はB/F値${}^{※}$が高くなるため、低B/F計算機の性能を引き出すことが難しくなっています。そこで、連立一次方程式の解法として高い演算性能とスケーラビリティを達成できる直接法と反復法のハイブリッド解法SLOR-PCR法を提案しました。
提案方法は、シンプルなSOR法を基本反復法とし、多重ループの最内側の三重対角行列の反転に効率的なLU分解を組み合わせています。このとき、LU分解だけではB/F値が高くなるため、Parallel Cyclic Reduction (PCR)法を併用し、演算密度とスケーラビリティを向上させています。

> ※) メモリから演算ユニットまでのデータの移動量 (Byte) と演算ユニットでの浮動小数点演算数の比。計算アルゴリズムやハードウェアの特性を表す指標の一つ。

<img src="/images/SLOR-PCR-UV300.png" alt="SLOR-PCR法とJacobi, SOR法との性能比較" style="max-width:600px; width:100%; height:auto; display:block; margin:0.5rem auto;">
図　SGI UV300でのSLOR-PCR法とJacobi, SOR法との実行性能比較。スケーラブルな性能向上が確認できる。

---

### Parallel Tree Partitioning Reduction法

流体シミュレーションなどに現れる大規模な疎行列を係数にもつ連立一次方程式の求解は、行列・ベクトル積の計算が必要ですが、既存の解法アルゴリズムの要求B/F（演算に対するデータ移動の比率）が大きく、近年の高性能ではあるけれども低B/FのCPUアーキテクチャの性能を引き出せない問題点があります。この研究では、「富岳」でも採用されているメニーコアの計算機において、その性能を引き出せるスレッド・スケーラブルな疎行列解法アルゴリズム開発をめざしています。そのアイデアは、方程式を互いに依存関係の無い多数のグループに分け、多数のコアを十分な演算量で動作できるように式変形を行うところにあります。この方法は、Tree Partitioning Reduction(TPR)法とParallel Cyclic Reduction(PCR)法を組み合わせ（PTPR法）、低B/Fアーキテクチャのコアで重要なL1キャッシュ上にあるデータの再利用性を高めたものになります。左図はスレッド数に対する性能、右図は方程式の数に対する性能を示しています。既存手法のPCR, TPRに比べると、PTPRはスレッド数、方程式の数（連立一次方程式の大きさ）ともに大きくなるとその性能が向上する特性をもっていることがわかり、メニーコアの性能を引き出せることがわかります。

<img src="/images/PTPR-1.png" alt="提案するPTPR法とPCR, TPR法の性能比較" style="max-width:760px; width:100%; height:auto; display:block; margin:0.5rem auto;">
図　提案するPTPR法とPCR, TPR法の性能比較

## Key publications
- K. Ono, T. Kato, S. Ohshima, and T. Nanri, *Scalable Direct-Iterative Hybrid Solver for Sparse Matrices on Multi-Core and Vector Architectures*, Proceedings of the International Conference on High Performance Computing in Asia-Pacific Region, pp.11––21, doi:[10.1145/3368474.3368484](https://doi.org/10.1145/3368474.3368484) (2020).
- T. Mitsuda, and K. Ono, *A Scalable Parallel Partition Tridiagonal Solver for Many-Core and Low B/F Processors*, 2022 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW), doi: [10.1109/IPDPSW55747.2022.00142](https://ieeexplore.ieee.org/document/9835226) (2022).
