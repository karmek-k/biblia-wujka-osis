import unittest
import xml.etree.ElementTree as ET

from extract.chapters import parse_chapter_toc


class TestChapters(unittest.TestCase):
    def test_parse_chapter_toc(self):
        href = 'tests/c2_Biblia_Wujka__1923__Ksiega_Rodzaju.xhtml'
        tree = ET.parse(href)

        chapters = parse_chapter_toc(tree)

        self.assertEqual(50, len(chapters))
