import os
import unittest

from src import style_splitter

class StyleSplitterTestCase(unittest.TestCase):
    def setUp(self):
        self.expected_names = ['7SWPO00176TOBYSWEATER_2.jpg', 'W2550O137WHTJUSTINE_2.jpg', 'SVB46MSS18SKY_ALT_1.jpg']
        self.style_splitter = style_splitter.StyleSplitter(r'G:\current_coding_projects\style_splitter\sample_data\7SWPO00176TOBYSWEATER_2-W2550O137WHTJUSTINE_2-SVB46MSS18SKY_ALT_1.jpg')

    def tearDown(self):
        self.style_splitter = None

class StyleSplitterPathTest(StyleSplitterTestCase):
    def runTest(self):
        self.assertTrue(os.path.isfile(self.style_splitter.path))

class StyleSplitterNameParsingTest(StyleSplitterTestCase):
    def runTest(self):
        self.style_splitter.parse_names()
        self.assertEquals(self.style_splitter.names, self.expected_names)

if __name__ == '__main__':
    unittest.main()