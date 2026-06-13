"""
make_osis.py - converts the Wujek Bible from Wikisource EPUB to OSIS
Copyright (C) 2025-2026 Bartosz Gleń

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from extract.chapters import parse_chapter_toc, Chapter
from extract.parse import XmlTree, parse


class Book:
    def __init__(self, name: str, *, href: str):
        self.name = name
        self.href = href
        self.chapters = []

    def parse(self):
        self.chapters = parse_chapter_toc(parse(self.href))

        if len(self.chapters) == 0:
            # single-chapter book without a TOC
            chapter = Chapter(1, href=self.href)
            chapter.parse()
            self.chapters = [chapter]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<Book name="{self.name}" href="{self.href}">'


def is_valid_title(text: str) -> bool:
    """
    Checks if it is a valid bible book title.
    """

    text = text.lower()

    for s in ("biblia", "strona", "starego", "nowego", "publikacji"):
        if s in text:
            return False

    return True


def parse_toc(tree: XmlTree) -> list[Book]:
    """
    Extracts all books in the table of contents.
    """

    root = tree.getroot()
    namespace = {"ncx": "http://www.daisy.org/z3986/2005/ncx/"}

    nav_points = root.findall(".//ncx:navPoint", namespace)

    result = []

    for chapter in nav_points:
        title = chapter.find("ncx:navLabel/ncx:text", namespace)
        content = chapter.find("ncx:content", namespace)

        # ignore invalid chapters
        if (
            title is None
            or title.text is None
            or content is None
            or title.text.isnumeric()
            or not is_valid_title(title.text)
        ):
            continue

        href = content.attrib["src"]

        # prevent duplicates
        if href not in map(lambda b: b.href, result):
            result.append(Book(title.text, href=href))

    return result
