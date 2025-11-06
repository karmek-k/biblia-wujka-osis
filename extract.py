import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from extract.books import parse_toc


#
# Set working directory to $(BIBLE_DIR)/OPS
#
directory = Path(sys.argv[1]) / 'OPS'
os.chdir(directory)

#
# List books
#
with open('toc.ncx') as f:
    # table of contents
    toc = ET.parse(f)

books = parse_toc(toc)
assert len(books) == 66  # protestant canon length
