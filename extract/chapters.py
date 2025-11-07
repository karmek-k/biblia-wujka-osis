from xml.etree.ElementTree import ElementTree


class Chapter:
    def __init__(self, number: int, *, href: str):
        self.number = number
        self.href = href

    def __str__(self) -> str:
        return f'Chapter {self.number}'
    
    def __repr__(self) -> str:
        return f'<Chapter number="{self.number}" href="{self.href}">'


def parse_chapter_toc(tree: ElementTree) -> list[Chapter]:
    root = tree.getroot()
    namespace = {'xhtml': 'http://www.w3.org/1999/xhtml'}
    
    anchors = root.findall('.//xhtml:a', namespace)
    
    result = []

    return result