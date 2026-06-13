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

import re

from extract.parse import XmlTree, parse


NS = {"xhtml": "http://www.w3.org/1999/xhtml"}


class Chapter:
    def __init__(self, number: int, *, href: str):
        self.number = number
        self.href = href
        self.title = ""
        self.verses = {}

    def __str__(self) -> str:
        return f"Chapter {self.number}"

    def __repr__(self) -> str:
        return f'<Chapter number="{self.number}" href="{self.href}">'

    def parse(self) -> None:
        tree = parse(self.href)

        self.title = self._parse_title(tree)
        self.verses = self._parse_verses(tree)

    def _parse_title(self, tree) -> str:
        root = tree.getroot()

        roman_numeral_node = root.find(".//xhtml:div[@class='center']/xhtml:b", NS)
        roman_numeral = (
            "".join(roman_numeral_node.itertext())
            if roman_numeral_node is not None
            else None
        )

        title_node = root.find(
            ".//xhtml:div[@style='font-size:85%;line-height:normal']", NS
        )
        title = "".join(title_node.itertext()).strip() if title_node is not None else ""

        # only chapter markers (e.g. "ROZDZIAŁ I.") belong in the title;
        # single-chapter books have a book superscription here instead
        if roman_numeral is None or not roman_numeral.startswith("ROZDZIAŁ"):
            return title

        return roman_numeral + " " + title

    def _parse_verses(self, tree) -> dict[str, str]:
        root = tree.getroot()

        result = {}

        verses = root.findall(".//xhtml:p", NS)
        for verse in verses:
            text = "".join(verse.itertext()).strip()

            if not re.search(r"[A-z]", text):
                # no letters found
                continue

            number_regex = r"^([0-9]+)\u00a0"

            number_match = re.search(number_regex, text)
            number = number_match.group(1) if number_match is not None else "1"

            text = re.sub(number_regex, "", text)

            # remove newlines
            text = re.sub(r"\n", " ", text)

            # remove commentary tags
            # TODO: bring it back!!
            text = re.sub(r"\s\[\d+\]", "", text)

            result[number] = text

        return result


def parse_chapter_toc(tree: XmlTree) -> list[Chapter]:
    root = tree.getroot()

    anchors = root.findall(".//xhtml:a", NS)

    result = []

    for anchor in anchors:
        # only numeric anchor contents have meaningful hrefs
        if anchor.text is None or not anchor.text.isnumeric():
            continue

        result.append(Chapter(int(anchor.text), href=anchor.attrib["href"]))

    return result
