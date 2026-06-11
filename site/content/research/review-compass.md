---
title: "Review Compass"
date: 2026-06-11
summary: "LLM-assisted specification-driven development platform"
thumbnail: "/images/review-compass-jp.jpg"
top_highlight: true
---

English version: [Review Compass (EN)](/research-en/review-compass/)

## ReviewCompass
ReviewCompass は、LLM（大規模言語モデル）を活用した仕様駆動開発において、開発者が本来集中すべき設計や実装から逸れてしまう「管理的な判断負荷」を軽減するためのレビュー基盤です。

近年、LLMによるコード生成は急速に進歩し、自然言語から短時間で実装を作成できるようになりました。しかし、品質の高いソフトウェアを継続的に開発するためには、「何を作るべきか」「どのように設計するべきか」「どの仕様を正本とするか」といった判断が依然として必要です。実際には、コードを書く時間よりも、仕様の整合性確認やレビュー結果の整理、承認判断に多くの時間が費やされることがあります。

ReviewCompass は、このような負荷を「裁定負荷（Arbitration Load）」として捉えます。裁定負荷とは、レビューで発見された問題や変更提案を、どの仕様書に反映するべきか、どの機能に影響するのか、人間の承認が必要か、といった判断に伴う負荷です。

ReviewCompass では、開発プロセスを

**Intent → Feature Division → Requirements → Design → Tasks → Implementation**

という段階に整理し、各段階をレビュー対象として管理します。さらに、主役（問題発見）、敵対役（反証・別視点）、判定役（分類）の三役レビューを用いて、多角的なレビューを実現します。

単に問題を発見するだけではなく、その問題を

- 同じ段階で修正する
- 上位仕様へ戻す
- 他機能へ波及させる
- 人間へエスカレーションする

といった判断まで支援することが特徴です。

また、複数のLLMを活用し、モデル間の意見の分岐や別案生成、質問返しなどを重要な判断材料として扱います。これにより、単一モデルへの過度な依存を避け、人間が最終的な判断に集中できる環境を提供します。

ReviewCompass の目的は、人間を置き換えることではありません。むしろ、人間が本当に重要な意思決定に集中できるように、レビューや仕様管理に伴う判断作業を整理し、透明性の高い形で支援することです。

仕様、レビュー、状態管理、承認履歴、判断根拠を一貫して記録することで、プロジェクトの説明責任と再現性を高めるとともに、組織の知識資産として蓄積・再利用できる開発基盤を目指しています。

<img src="/images/review-compass-jp.jpg" alt="Review Compass" style="max-width:720px; width:100%; height:auto; display:block; margin:0.5rem auto;">
