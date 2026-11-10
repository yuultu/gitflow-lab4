import csv
import io
import unittest

from export import export_csv


class ExportTests(unittest.TestCase):
    def test_export_quotes_items_with_commas(self):
        stream = io.StringIO()
        export_csv(["яблоко, груша", "слива"], stream)
        stream.seek(0)
        self.assertEqual(list(csv.reader(stream)), [["item"], ["яблоко, груша"], ["слива"]])
