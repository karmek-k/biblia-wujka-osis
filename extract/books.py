import xml.etree.ElementTree as ET

from extract.chapters import parse_chapter_toc


class Book:
    def __init__(self, name: str, *, href: str):
        self.name = name
        self.href = href
        self.chapters = []
    
    def parse(self):
        self.chapters = parse_chapter_toc(ET.parse(self.href))
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'<Book name="{self.name}" href="{self.href}">'

def is_valid_title(text: str) -> bool:
    """
    Checks if it is a valid bible book title.
    """

    text = text.lower()

    for s in ('biblia', 'strona', 'starego', 'nowego', 'publikacji'):
        if s in text:
            return False
    
    return True

def parse_toc(tree: ET.ElementTree) -> list[Book]:
    """
    Extracts all books in the table of contents.
    """

    root = tree.getroot()
    namespace = {'ncx': 'http://www.daisy.org/z3986/2005/ncx/'}
    
    nav_points = root.findall('.//ncx:navPoint', namespace)
    
    result = []
    
    for chapter in nav_points:
        title = chapter.find('ncx:navLabel/ncx:text', namespace)
        content = chapter.find('ncx:content', namespace)

        # ignore invalid chapters
        if title.text.isnumeric() or content is None or not is_valid_title(title.text):
            continue
        
        href = content.attrib['src']

        # prevent duplicates
        if href not in map(lambda b: b.href, result):
            result.append(Book(title.text, href=href))
    
    return result