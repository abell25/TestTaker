__author__ = 'anthony bell'

import lucene
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.util import Version

from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.search import IndexSearcher

from java.io import File

import os
import threading
import re
from time import time

import logging
log = logging.getLogger(__name__)

class WikiPageIndex():
    def __init__(self, index_dir):
        #lucene.initVM(vmargs=['-Djava.awt.headless=true', '-Xmx4g'])

        self.index_dir = index_dir
        self.directory = SimpleFSDirectory(File(self.index_dir))
        self.analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
        self.config = IndexWriterConfig(Version.LUCENE_CURRENT, self.analyzer)
        self.config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)

        self.searcher = IndexSearcher(DirectoryReader.open(self.directory))

    def createIndex(self):
        self.writer = IndexWriter(self.directory, self.config)

        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)

    def addDocumentToIndex(self, title, text):
        doc = Document()

        doc.add(Field("Title", title, Field.Store.YES, Field.Index.ANALYZED))
        doc.add(Field("Text", text, Field.Store.YES, Field.Index.ANALYZED))

        self.writer.addDocument(doc)

    def closeIndex(self):
        self.writer.commit()
        self.writer.close()


    def searchIndex(self, queryString, field="Text", max_results=100):
        query = QueryParser(Version.LUCENE_CURRENT, field, self.analyzer).parse(queryString)
        scoreDocs = self.searcher.search(query, max_results).scoreDocs
        log.debug("Found {0} documents for query [{1}]".format(len(scoreDocs), queryString))

        docs = []
        for scoreDoc in scoreDocs:
            doc = self.searcher.doc(scoreDoc.doc)
            log.debug(WikiPageIndex.cleanWikiText(doc.get("Text")))

            #print("title: {0}\ncontents: {1}".format(doc.get("Title"), doc.get("Text")[:70]))
            docs.append(doc)

        return docs

    @staticmethod
    def cleanWikiText(text):
        text = text.encode('ascii', 'ignore')
        text = re.sub('(\[\[.*?\]\]|\{\{.*?\}\}|\{\|.*?\|\})', '', text)
        text = re.sub('[^\na-zA-Z0-9\n_-]+', ' ', text)
        text = re.sub('([ \t]*[\n]+[ \t]*)+', '\n', text)
        return text.strip()

