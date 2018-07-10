#!/usr/bin/python

from src import style_splitter
from src import ui

if __name__ == '__main__':

    repeating = True
    retry = False
    incorrect_path = None

    while repeating:
        ui.UI.clear_screen()

        if retry:
            ui.UI.path_error_message(incorrect_path)

        current_ui = ui.UI()
        if current_ui.force_quit == True:
            current_ui.exit_message()
            break

        try:
            retry = False
            incorrect_path = None
            sp = style_splitter.StyleSplitter(current_ui.target_file_path)
            sp.parse_names()

            
            ui.UI.clear_screen()
            current_ui.print_preview(sp.get_names())

            if current_ui.confirm_file_creation() == True:
                sp.create_files()
                ui.UI.clear_screen()
                sp.confirm_files()

                if current_ui.repeat():
                    repeating = True
                else:
                    repeating = False
                    current_ui.exit_message()
            else:
                pass

        except ValueError:
            incorrect_path = current_ui.target_file_path
            retry = True

