import unittest
import xml.etree.ElementTree as ET

from extract.chapters import parse_chapter_toc, Chapter


class TestChapters(unittest.TestCase):
    def test_parse_chapter_toc(self):
        href = 'tests/c2_Biblia_Wujka__1923__Ksiega_Rodzaju.xhtml'
        tree = ET.parse(href)
        chapter_count = 50

        chapters = parse_chapter_toc(tree)

        self.assertEqual(chapter_count, len(chapters))
        self.assertTrue(chapters[0].href.startswith('c42'))
        self.assertTrue(chapters[chapter_count - 1].href.startswith('c91'))
    
    def test_chapter_parse(self):
        chapter = Chapter(1, href='tests/c42_Biblia_Wujka__1923__Ksiega_Rodzaju_1.xhtml')

        chapter.parse()

        self.assertTrue('O świata stworzeniu' in chapter.title)
        self.assertTrue('ROZDZIAŁ I.' in chapter.title)
        self.assertEqual(31, len(chapter.verses))
