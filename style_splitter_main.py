#!/usr/bin/python

from src import style_splitter
from src import ui

if __name__ == '__main__':

    repeat = True

    while repeat:
        current_ui = ui.UI()
        if current_ui.force_quit == True:
            break

        sp = style_splitter.StyleSplitter(current_ui.target_file_path)
        sp.parse_names()

        current_ui.print_preview(sp.get_names())

        if current_ui.confirm_file_creation() == True:
            sp.create_files()
            sp.confirm_files()

            if current_ui.repeat():
                repeat = True
            else:
                repeat = False
        else:
            pass


