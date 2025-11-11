import unittest
from datetime import date

from extract.export import OsisExport
from extract.books import Book


class TestOsisExport(unittest.TestCase):
    def test_template(self):
        today = date(2025, 11, 10)

        result = OsisExport.template(publication_date=today)

        self.assertTrue('<date>2025-11-10</date>' in result)
    
    def test_export(self):
        books = [
            Book('Genesis, to jest pierwsze', href='tests/c42_Biblia_Wujka__1923__Ksiega_Rodzaju_1.xhtml')
        ]
        export = OsisExport()

        result = export.export(books)

        # placeholder
        self.assertTrue("<div type='book' osisID='Gen'>" in result)
        self.assertTrue("<chapter osisID='Gen.1'>" in result)
        self.assertTrue("<title>O świata stworzeniu, rzeczy stworzonych różności, i ozdobie; o stanie człowieka, któremu Bóg poddał wszystko, co stworzył.</title>"
            in result)
        self.assertTrue("<verse osisID='Gen.1.1'>Na początku stworzył Bóg niebo i ziemię.</verse>" in result)

