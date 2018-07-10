import os

class UI:
    ask_for_input = '\nPlease drag the file to be style-split into this window\nor enter X to exit:\n'
    preview_header = '\ntarget file will generate the following files'
    creation_confirmation_msg = '\nVerify correct naming and enter [Y/n] to continue '
    process_repeat_msg = '\nContinue with another file? [Y/n]'
    exit_msg = '\nExiting program.'
    invalid_path_msg = 'is not a valid path to an image file, please try again'
    arrow = '--> '
    force_quit = False

    def __init__(self):
        print(self.ask_for_input)
        self.target_file_path = raw_input(self.arrow)
        if self.target_file_path == "X".lower():
            self.force_quit = True

    def print_preview(self, list_of_expected_names):
        print(self.preview_header)
        for name in list_of_expected_names:
            print('--> {}'.format(name))

    def confirm_file_creation(self):
        print(self.creation_confirmation_msg)
        confirmation = raw_input(self.arrow)

        if confirmation == 'Y'.lower() or confirmation == "":
            return True
        else:
            return False

    def exit_message(self):
        print(self.exit_msg)

    def repeat(self):
        print(self.process_repeat_msg)
        confirmation = raw_input(self.arrow)

        if confirmation == "Y".lower() or not confirmation:
            return True
        else:
            return False

    @classmethod
    def clear_screen(self):
        os.system('cls' if os.name=='nt' else 'clear')

    @classmethod
    def path_error_message(self, invalid_path):
        print('"{}" '.format(invalid_path) + self.invalid_path_msg)