SOURCE=resources/Biblia_Wujka.epub
BIBLE_DIR=bible-text

PYTHON=python3

extract: bible-text
	$(PYTHON) extract.py $(BIBLE_DIR)

bible-text: $(SOURCE)
	unzip $(SOURCE) -d $(BIBLE_DIR)

.PHONY: extract