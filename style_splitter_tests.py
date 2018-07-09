import os
import unittest

from src import style_splitter

class StyleSplitterTestCase(unittest.TestCase):
    def setUp(self):
        self.expected_names = ['7SWPO00176TOBYSWEATER_2.jpg', 'W2550O137WHTJUSTINE_2.jpg', 'SVB46MSS18SKY_ALT_1.jpg']
        self.style_splitter = style_splitter.StyleSplitter(r'G:\current_coding_projects\style_splitter\sample_data\7SWPO00176TOBYSWEATER_2-W2550O137WHTJUSTINE_2-SVB46MSS18SKY_ALT_1.jpg')

    def tearDown(self):
        self.expected_names = None
        self.style_splitter = None

    def test_style_splitter_path_exists(self):
        self.assertTrue(os.path.isfile(self.style_splitter.path))

    def test_style_splitter_incorrect_path_handling(self):
        pass

    def test_style_splitter_name_parsing(self):
        self.style_splitter.parse_names()
        self.assertEquals(self.style_splitter.names, self.expected_names)

suite = unittest.TestLoader().loadTestsFromTestCase(StyleSplitterTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)


