import unittest

from src import style_splitter

class StyleSplitterTestCase(unittest.TestCase):
    def setUp(self):
        self.style_splitter = style_splitter.StyleSplitter()

    def tearDown(self):
        self.style_splitter = None

class StyleSplitterPathTest(StyleSplitterTestCase):
    def runTest(self):
        self.assertTrue(os.path.exists(self.style_splitter.path))

if __name__ == '__main__':
    unittest.main()