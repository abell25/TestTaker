__author__ = 'anthony bell'

class QueryResultsComparer():
    def __init__(self, wikiPageIndex):
        self.wikiPageIndex = wikiPageIndex

    def compare(self, question, answers):
        self.wikiPageIndex.searchIndex(question, field="Text", max_results=20)