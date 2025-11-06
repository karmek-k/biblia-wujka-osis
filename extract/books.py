from xml.etree.ElementTree import ElementTree


class Book:
    def __init__(self, name, *, href):
        self.name = name
        self.href = href

def parse_toc(tree: ElementTree):
    """
    Extracts all books in the table of contents.
    """
    root = tree.getroot()
    # <navPoint id="c10_Biblia_Wujka__1923__Pierwsza_Ksiega_Samuela" playOrder="12">
    # 						<navLabel><text>Królewskie pierwsze (Samuelowe I)</text></navLabel>
    # 						<content src="c10_Biblia_Wujka__1923__Pierwsza_Ksiega_Samuela.xhtml" />
    # 				</navPoint>
    
    return []