import unittest
import xml.etree.ElementTree as ET

from extract.chapters import parse_chapter_toc


class TestChapters(unittest.TestCase):
    def test_parse_chapter_toc(self):
        href = 'tests/c2_Biblia_Wujka__1923__Ksiega_Rodzaju.xhtml'
        tree = ET.parse(href)
        chapter_count = 50

        chapters = parse_chapter_toc(tree)

        self.assertEqual(chapter_count, len(chapters))
        self.assertTrue(chapters[0].href.startswith('c42'))
        self.assertTrue(chapters[chapter_count - 1].href.startswith('c91'))
