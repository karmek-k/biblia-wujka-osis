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
toc = ET.parse('toc.ncx')
books = parse_toc(toc)
