import unittest

from search import search


class SearchTests(unittest.TestCase):
    def test_search_ignores_case(self):
        self.assertEqual(search(['Яблоко', 'Груша'], 'ЯБЛ'), ['Яблоко'])

    def test_search_returns_empty_list_without_matches(self):
        self.assertEqual(search(['Яблоко'], 'Груша'), [])
