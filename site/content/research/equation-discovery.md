---
title: "Equation Discovery"
date: 2026-03-12
summary: "Data-driven approach for discovering mathematical model to describe phenomena."
---

English version: [Equation Discovery (EN)](/research-en/equation-discovery/)

## 遺伝的プログラミングによる方程式発見
コンピュータ、観測、シミュレーション技術などの進歩により大量のデータが生成される時代になり、データに含まれる意味や知識をえることがますます重要になっている。 この論文では、与えられたデータを記号回帰問題として記述し，進化計算により支配方程式を見つけるプロセスを構築した。 提案手法では、遺伝的プログラミングに「偏微分関数」を導入して偏微分方程式を自動生成し、生成された方程式とデータを比較評価して誤差の少ない方程式を自動抽出する。 数値実験を行い、流体シミュレーションデータから支配方程式を推定し、提案手法の有効性を評価した。 その結果、元の方程式が高い確率で得られ、提案された方法がデータを表すための有用なモデルを見つけるための有効なツールになることがわかった。

<img src="/images/GP_overview.png" alt="Genetic Programmingによる方程式探索の概要" style="max-width:600px; width:100%; height:auto; display:block; margin:0.5rem auto;">

### Key publications
- 小野謙二, 古賀壱成, 遺伝的プログラミングによる支配方程式の推定, Transactions of JSCES, DOI: [10.11421/jsces.2020.20201004](https://doi.org/10.11421/jsces.2020.20201004), 2020.
- Kenji Ono and Kanae Shiragami, *Equation discovery through genetic programming reflecting the importance of generated terms*, 16th world congress on computational mechanics / 4th pan american congress on computational mechanics, 2024.
