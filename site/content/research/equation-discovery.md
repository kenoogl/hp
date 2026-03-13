---
title: "Equation Discovery"
date: 2026-03-12
summary: "Data-driven discovery of mathematical models for physical phenomena."
thumbnail: "/images/GP_overview.png"
top_highlight: true
---

English version: [Equation Discovery (EN)](/research-en/equation-discovery/)

## 遺伝的プログラミングによる方程式発見
コンピュータ、観測、シミュレーション技術などの進歩により、大量のデータが生成される時代になりました。そのため、データに含まれる意味や知識を得ることがますます重要になっています。本研究では、与えられたデータを記号回帰問題として記述し、進化計算により支配方程式を見つけるプロセスを構築しました。提案手法では、遺伝的プログラミング（Genetic Programming, GP）に「偏微分関数」を導入して偏微分方程式を自動生成し、生成された方程式とデータを比較評価することで、誤差の少ない方程式を自動抽出します。数値実験では、流体シミュレーションデータから支配方程式を推定し、提案手法の有効性を評価しました。その結果、元の方程式が高い確率で得られ、提案手法がデータを表す有用なモデルを見つけるための有効なツールとなることを確認しました。

<img src="/images/GP_overview.png" alt="Genetic Programmingによる方程式探索の概要" style="max-width:720px; width:100%; height:auto; display:block; margin:0.5rem auto;">



## 大規模言語モデルを援用した遺伝的プログラミングによる方程式発見

遺伝的プログラミング（Genetic Programming: GP）は、データから数式モデルを発見する有力な方法です。しかし、GP は本質的に発見的探索（heuristic search）であり、探索空間が極めて広大になるため、最適解に到達するまでに多くの計算量を要するという課題があります。

そこで本研究では、従来プログラムのみで実装されていた探索処理の一部を大規模言語モデル（Large Language Model: LLM）に委譲し、プログラムコードと LLM を連携させた **LLM-GP システム**を構築します。LLM は学習済み知識と言語理解能力を活用し、物理的に意味のある構造を持つ数式候補を生成します。このような **知識を利用した知的探索**を導入することで、従来のランダム性に依存する探索と比較して、探索効率の向上が期待できます。

本システムにおいて、LLM の主な役割は以下の二つです。

1. **候補モデル式の生成**
    LLM は事前に学習した物理・数理的知識を利用し、意味のある構造を持つ数式を提案します。これにより、完全なランダム探索から開始する場合に比べて、探索の初期段階から有望なモデル構造を得ることができます。
2. **進化計算フローの制御**
    進化計算の各段階（初期個体生成、突然変異、交叉、淘汰など）を、LLM への自然言語プロンプトによって制御します。これにより、探索戦略の変更や評価条件の調整などを柔軟に行うことが可能になります。

一方、提案されたモデル式とデータとの一致度は、プログラム側で定量的指標（例えば平均二乗誤差など）を計算して評価します。すなわち、本システムでは

- **LLM：探索戦略とモデル生成**
- **プログラム：数値評価と最適化**

という役割分担により、効率的なモデル探索を実現します。

さらに、本システムでは対話的操作や全自動実行を自然言語によって指示できるため、探索戦略の変更やパラメータ調整を柔軟に行うことができます。このような **自然言語による探索制御**は、従来の完全にプログラムベースの手法にはない運用上の大きな利点です。

<img src="/images/LLM-GP_system.png" alt="LLM-GPシステムの処理ダイアグラム" style="max-width:720px; width:100%; height:auto; display:block; margin:0.5rem auto;">

### Key publications

- 小野謙二, 古賀壱成, 遺伝的プログラミングによる支配方程式の推定, Transactions of JSCES, DOI: [10.11421/jsces.2020.20201004](https://doi.org/10.11421/jsces.2020.20201004), 2020.
- Kenji Ono and Kanae Shiragami, *Equation discovery through genetic programming reflecting the importance of generated terms*, 16th world congress on computational mechanics / 4th pan american congress on computational mechanics, 2024.
