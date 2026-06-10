from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from bibtex_to_markdown import build_bibtex_markdown, build_markdown


class BibtexToMarkdownTests(unittest.TestCase):
  def test_build_markdown_links_to_bibtex_page_and_download(self):
    entry = {
      "ENTRYTYPE": "inproceedings",
      "ID": "Sample:2026",
      "author": "Yamada, Taro and Ono, Kenji",
      "title": "Sample Publication",
      "booktitle": "Sample Conference",
      "year": "2026",
      "doi": "10.0000/example",
    }

    markdown = build_markdown(
      entry,
      Path("data/publications/sample.bib"),
      "/publication-bibtex/2026/sample-x3a-2026/",
      "/bibtex/publications/2026/sample-x3a-2026.bib",
    )

    self.assertIn("bibtex_page: '/publication-bibtex/2026/sample-x3a-2026/'", markdown)
    self.assertIn("bibtex_download: '/bibtex/publications/2026/sample-x3a-2026.bib'", markdown)
    self.assertNotIn("bibtex_source: |", markdown)
    self.assertNotIn("@inproceedings{Sample:2026,", markdown)

  def test_build_bibtex_markdown_includes_source_and_download(self):
    entry = {
      "ENTRYTYPE": "inproceedings",
      "ID": "Sample:2026",
      "author": "Yamada, Taro and Ono, Kenji",
      "title": "Sample Publication",
      "booktitle": "Sample Conference",
      "year": "2026",
      "doi": "10.0000/example",
    }

    markdown = build_bibtex_markdown(
      entry,
      Path("data/publications/sample.bib"),
      "/publications/2026/sample-x3a-2026/",
      "/bibtex/publications/2026/sample-x3a-2026.bib",
    )

    self.assertIn("publication_page: '/publications/2026/sample-x3a-2026/'", markdown)
    self.assertIn("bibtex_download: '/bibtex/publications/2026/sample-x3a-2026.bib'", markdown)
    self.assertIn("bibtex_source: |", markdown)
    self.assertIn("@inproceedings{Sample:2026,", markdown)
    self.assertIn("  title = {Sample Publication},", markdown)


if __name__ == "__main__":
  unittest.main()
