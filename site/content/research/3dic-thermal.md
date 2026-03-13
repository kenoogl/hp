---
title: "3D-IC Thermal Design"
date: 2026-03-13
summary: "Fast thermal simulation for early-stage 3D-IC design, hotspot prediction, and cooling optimization."
thumbnail: "/images/3DICthermal.png"
top_highlight: true
---

English version: [3D-IC Thermal Design (EN)](/research-en/3dic-thermal/)

## 半導体チップの熱設計
近年、AIや高性能コンピュータの発展により、半導体チップにはより高い性能と低消費電力が同時に求められています。その解決策の一つが、チップを縦方向に積み重ねる3次元集積回路（3D-IC）です。しかし、チップを重ねると内部の発熱密度が高くなり、局所的な高温（ホットスポット）が発生して性能低下や寿命短縮の原因となります。この問題を解決するためには、設計の初期段階からチップ内部の温度分布を予測し、配置や冷却構造を最適化する熱設計が重要になります。しかし従来のシミュレーションは計算コストが高く、設計段階で多数のパターンを試すことが困難でした。また、簡易モデルは複雑な材料構造や局所的な発熱を十分に再現できないという課題があります。

そこで本研究では、**高速かつ高精度に温度分布を計算できる熱解析システム**を開発しました。チップ構造を基本形状（直方体・円柱など）の組み合わせで自動生成し、効率的な数値計算手法を用いることで、熱伝導方程式を高速に解きます。さらに、層構造に合わせて計算格子を最適化することで、計算量を大幅に削減しました。

その結果、従来の均一な計算格子に比べて**最大で約40倍の高速化**を達成し、一般的なノートPCでも**数秒でチップ全体の温度分布を計算**できることを示しました。この手法により、チップ配置、電力分布、冷却条件などの設計パラメータを高速に評価でき、**半導体設計の初期段階での熱設計探索が可能**になります。

本研究は、半導体の高性能化だけでなく、データセンターやAI計算の**エネルギー効率向上**にも貢献する技術です。高速な物理シミュレーションを基盤として、今後は機械学習と組み合わせた次世代の半導体設計支援へと発展させていきます。



<img src="/images/NUgrid.png" alt="モデル断面と層方向の温度分布" style="max-width:1280px; width:100%; height:auto; display:block; margin:0.5rem auto;">

## Key publications
- Kenji Ono, Takanori Iwasaki, Takeshi Ohkawa, *High-Throughput Thermal Simulation for Early-Stage 3D-IC Design Using Automated Meshing and Pseudo-3D Modeling*, 2025 20th International Microsystems, Packaging, Assembly and Circuits Technology Conference (IMPACT), [https://www.impact.org.tw/site/page.aspx?pid=901&sid=1283&lang=en](https://www.impact.org.tw/site/page.aspx?pid=901&sid=1283&lang=en), 2025.
