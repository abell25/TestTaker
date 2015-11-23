from unittest import TestCase
from WikiPageIndex import WikiPageIndex
import lucene

__author__ = 'anthony bell'


class TestWikiPageIndex(TestCase):

  def setUp(self):
    pass

  def test_queryingIndexWorks(self):
    lucene.initVM(vmargs=['-Djava.awt.headless=true', '-Xmx4g'])

    index_path = "/media/tony/ssd/TestTakerData/wikipedia_books_index"
    wikiIndex = WikiPageIndex(index_path)
    results = wikiIndex.searchIndex("cell")

    doc0_text = results[0]["Text"]
    self.assertTrue(len(doc0_text))
