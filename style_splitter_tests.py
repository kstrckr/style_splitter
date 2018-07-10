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

    def test_style_splitter_name_parsing(self):
        self.style_splitter.parse_names()
        self.assertEquals(self.style_splitter._names, self.expected_names)
    
    def test_style_splitter_target_directory_accurate(self):
        self.assertTrue(os.path.isdir(self.style_splitter._target_dir))

class StyleSplitterDirectoryArgsTestCase(unittest.TestCase):

    def tearDown(self):
        self.style_splitter = None

    def test_trying_to_create_style_splitter_without_filename(self):
        with self.assertRaises(ValueError):
            path = r'G:\current_coding_projects\style_splitter\sample_data'
            self.style_splitter = style_splitter.StyleSplitter(path)

    def test_trying_to_create_style_splitter_without_args(self):
        with self.assertRaises(TypeError):
            self.style_splitter = style_splitter.StyleSplitter()

suite1 = unittest.TestLoader().loadTestsFromTestCase(StyleSplitterTestCase)
suite2 = unittest.TestLoader().loadTestsFromTestCase(StyleSplitterDirectoryArgsTestCase)

print('\n**Testing Naming and Path Validity**')
unittest.TextTestRunner(verbosity=2).run(suite1)
print('\n**Testing StyleSplitter Class Instancing**')
unittest.TextTestRunner(verbosity=2).run(suite2)


