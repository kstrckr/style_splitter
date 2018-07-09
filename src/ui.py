class UI:
    ask_for_input = '\nPlease drag the file to be style-split into this window\nor enter X to exit:\n'
    arrow = '--> '
    force_quit = False

    def __init__(self):
        print(self.ask_for_input)
        self.target_file_path = raw_input(self.arrow)
        if self.target_file_path == "X".lower():
            self.force_quit = True

    def print_preview(self, list_of_expected_names):
        print('\ntarget file will generate the following files')
        for name in list_of_expected_names:
            print('--> {}'.format(name))

    def confirm_file_creation(self):
        print('\nVerify correct naming and enter [Y/n] to continue ')
        confirmation = raw_input(self.arrow)

        if confirmation == 'Y'.lower() or confirmation == "":
            return True
        else:
            return False

    def repeat(self):
        print('\nContinue with another file? [Y/n]')
        confirmation = raw_input(self.arrow)

        if confirmation == "Y".lower() or not confirmation:
            return True
        else:
            return False
