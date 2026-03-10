# Publications 運用ワークフロー

## 目的

研究室サイトの Publications ページを継続的に更新・運用するための手順を定義する。

対応する更新方式:

1. 手動更新
2. BibTeX を使った半自動更新
3. GitHub Actions を使った自動更新

---

## 前提

本リポジトリは以下を前提とする。

- 静的サイト生成: Hugo
- コンテンツ管理: Markdown
- 論文データソース: BibTeX (`data/publications.bib`)
- 品質チェック: `scripts/validate_content.py` など

---

## ディレクトリ構成

Hugo ソースルートは `site/`。

```text
site/content/publications/
  2026/
  2025/
```

各論文は1ファイル（Markdown）で管理する。

---

## 方法1: 手動更新

向いているケース:

- 論文数が少ない
- 更新頻度が低い

### Step 1: Markdown ファイルを追加

```text
site/content/publications/2026/wake-modeling.md
```

### Step 2: Front Matter を記述

```yaml
---
title: "Data-driven Wake Modeling using AI"
date: 2026-01-01
authors: "Kenji Ono, John Smith"
journal: "Journal of Wind Engineering"
year: "2026"
pub_type: "journal"
doi: "10.xxxx/xxxxx"
---

論文概要をここに記載。
```

### Step 3: ビルドと検証

```bash
python scripts/validate_content.py
cd site
hugo --destination ../public --cleanDestinationDir
```

---

## 方法2: BibTeX 半自動更新

単一ソースとして `data/publications.bib` を使う。

```text
data/publications.bib
```

BibTeX 例:

```bibtex
@article{ono2026wake,
  title={Data-driven wake modeling using AI},
  author={Ono, Kenji and Smith, John},
  journal={Journal of Wind Engineering},
  year={2026},
  doi={10.xxxx/xxxxx}
}
```

### Step 1: BibTeX を更新

取得元例:

- Google Scholar
- Scopus
- Zotero

保存先:

```text
data/publications.bib
```

### Step 2: 変換スクリプトを実行

```bash
python scripts/bibtex_to_markdown.py data/publications.bib --clean
python scripts/validate_content.py
```

`bibtex_to_markdown.py` は `pub_type` を自動設定する。

判定優先順位:

1. BibTeXの明示値 `pub_type`（最優先）
2. `journal` / `booktitle` / `author` の日本語判定（国内会議）
3. `ENTRYTYPE`・venueキーワードに基づく自動分類

- `@article` -> `journal`
- `@inproceedings` / `@conference` / `@proceedings` -> `international-conference`
  - venue が国内会議キーワードに一致する場合 -> `domestic-conference`
- それ以外 -> `others`
- `journal` / `booktitle` に日本語を含む場合 -> `domestic-conference`
- `author` に日本語を含む場合 -> `domestic-conference`

会議論文 (`international-conference` / `domestic-conference`) には、必要に応じて `peer_reviewed` が付与される。

- `peer_reviewed: true` -> Refereed
- `peer_reviewed: false` -> Non-Refereed
- 未設定 -> Unspecified

判定優先順位:

1. BibTeXの明示値（`peer_reviewed` / `peerreviewed` / `refereed` / `reviewed`）
2. `note`/`keywords` 等のキーワード推定（`non-refereed`, `査読なし` など）
3. 入力Bibファイル名ヒント（`*_non_refereed.bib`, `*_refereed.bib`）

出力先:

```text
site/content/publications/<year>/<slug>.md
```

### Step 3: Hugo ビルド

```bash
cd site
hugo --destination ../public --cleanDestinationDir
```

---

## 方法3: 完全自動更新（CI）

目的:

Google Scholar / BibTeX 更新をサイトへ自動反映する。

パイプライン:

```text
Google Scholar
  ↓
BibTeX 更新
  ↓
Markdown 生成
  ↓
Hugo build
  ↓
CIチェック
  ↓
サイト反映
```

---

## GitHub Actions 連携

主な workflow:

- `.github/workflows/update_publications.yml`
  - weekly 実行（publication 同期）
- `.github/workflows/site_checks.yml`
  - PR / develop / main で軽量チェック
- `.github/workflows/site_audit.yml`
  - 月次フル監査

`update_publications.yml` の標準処理:

1. Scholar/BibTeX 取得
2. BibTeX -> Markdown 変換
3. content validation
4. Hugo build
5. commit/push

---

## 推奨運用

安定性重視では「方法2（半自動）」を基本にする。

```text
Scholar
  ↓
BibTeX
  ↓
script
  ↓
site
```

利点:

- 再現性が高い
- データソースを一本化できる
- 手作業ミスを減らせる
- LaTeX/BibTeX 運用と親和性が高い

---

## 運用上の注意

- `year` と配置ディレクトリ（`publications/<year>/`）を一致させる
- `date` は `<year>-` で始める
- ファイル名は kebab-case を使う
- `pub_type` は `journal` / `international-conference` / `domestic-conference` / `others` のいずれかにする
- `international-conference` / `domestic-conference` で査読有無を表示したい場合は `peer_reviewed` を設定する（`true` / `false`）
- 本番反映前に `site_checks` 相当の検証を通す
