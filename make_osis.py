import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from extract.books import parse_toc
from extract.export import OsisExport


#
# Set working directory to $(BIBLE_DIR)/OPS
#
directory = Path(sys.argv[1]) / 'OPS'
cwd = Path.cwd()
os.chdir(directory)

#
# List books
#
toc = ET.parse('toc.ncx')
books = parse_toc(toc)

#
# Extract chapters and verses
#
for book in books:
    book.parse()

    # one chapter for now
    for chapter in book.chapters:
        print(f'[PROCESSING] {book.name} - Chapter {chapter.number}')
        chapter.parse()

#
# OSIS export
#
export = OsisExport()
result = export.export(books)

with open(cwd / 'out' / 'bwujka.xml', mode='w', encoding='UTF-8') as f:
    f.write(result)
