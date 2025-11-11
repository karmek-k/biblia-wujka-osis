import unittest
from datetime import date

from extract.export import OsisExport


class TestOsisExport(unittest.TestCase):
    def test_template(self):
        today = date(2025, 11, 10)

        result = OsisExport.template(publication_date=today)

        self.assertTrue('<date>2025-11-10</date>' in result)
