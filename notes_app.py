#!/usr/bin/env python

from notes_app_ui import *

class notes_app (QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save)

    def save(self):
        name_of_note = ""
        note_contents = self.plainTextEdit.toPlainText() #or maybe text edit to get the text

        saved_note = open("name_of_note.txt", "w+")

        saved_note.write(note_contents)
        saved_note.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = notes_app()
    window.show()
    app.exec()
