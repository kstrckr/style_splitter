import os

class StyleSplitter:

    def __init__(self, source_path):
        self.path = source_path
        self.names = []

    def parse_names(self):
        file_name = os.path.split(self.path)
        expected_names = file_name[1].split('-')
        for name in expected_names:
            if name[-4:] != ".jpg":
                full_name = name + ".jpg"
            else:
                full_name = name
            self.names.append(full_name)



    def say_hello(self, msg):
        return msg

if __name__ == '__main__':

    example_path = r'G:\current_coding_projects\style_splitter\sample_data\7SWPO00176TOBYSWEATER_2-W2550O137WHTJUSTINE_2-SVB46MSS18SKY_ALT_1.jpg'
    example = StyleSplitter(example_path)
    example.parse_names()
