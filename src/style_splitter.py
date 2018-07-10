import os
import shutil

class StyleSplitter:

    def __init__(self, source_path):
        self._path = source_path.strip()
        self._names = []

        if not os.path.isfile(source_path):
            raise ValueError("Path Supplied is not a file, please try again")

        self._target_dir = os.path.split(self._path)[0]


    def parse_names(self):

        file_name = os.path.split(self._path)
        expected_names = file_name[1].split('-')
        for name in expected_names:
            if name[-4:] != ".jpg":
                full_name = name + ".jpg"
            else:
                full_name = name
            self._names.append(full_name.strip())

    def create_files(self):
        
        for file in self._names:
            output_path = os.path.join(self._target_dir, file)
            shutil.copy(self._path, output_path)

    def get_names(self):
        return self._names

    def confirm_files(self):
        
        print('')

        for file in self._names:
            validation_path = os.path.join(self._target_dir, file)
            validated = os.path.isfile(validation_path)
            
            if validated:
                print('{} - Created'.format(file))
            else:
                print('Potential issue with {}'.format(file))

if __name__ == '__main__':

    example_path = r'G:\current_coding_projects\style_splitter\sample_data\7SWPO00176TOBYSWEATER_2-W2550O137WHTJUSTINE_2-SVB46MSS18SKY_ALT_1.jpg'
    example = StyleSplitter(example_path)
    example.parse_names()
    example.create_files()
