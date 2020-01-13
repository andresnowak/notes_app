#!/usr/bin/env python

from notes_app_ui import *
from PyQt5.QtWidgets import *

class notes_app (QtWidgets.QMainWindow, Ui_Form):
    key_pressed = QtCore.pyqtSignal(QtCore.QEvent)
    click = QtCore.pyqtSignal(QtCore.QEvent)
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setupUiSave(self)
        self.save.hide()
        self.save_as.hide()
        self.save_as_text.hide()
        self.pushButton.clicked.connect(self.Options)
        self.save.clicked.connect(self.Save)
        self.save_as.clicked.connect(self.ShowSaveAsText)
        self.key_pressed.connect(self.SaveAs)
        self.click.connect(self.close_options)

    def Options(self):
        self.save.show()
        self.save_as.show()
    
    def keyPressEvent(self, event):
        super(notes_app, self).keyPressEvent(event)
        self.key_pressed.emit(event) 
    
    def mousePressEvent(self, event):
        super(notes_app, self).mousePressEvent(event)
        self.click.emit(event) 
    
    def close_options(self, event):
        # TODO: make the mousevent with leftbutton and detect where the press is being made so it is only made outside of the options ui the close_options function
        if event.button() == QtCore.Qt.RightButton:
            self.save.hide()
            self.save_as.hide()
            self.save_as_text.hide()

    def Save(self):
        note_contents = self.plainTextEdit.toPlainText() #or maybe text edit to get the text
        saved_note = open("notes/{}.md".format(self.name_of_note), "w+")
        saved_note.write(note_contents)
        saved_note.close()
        self.save.hide()
        self.save_as.hide()
        self.save_as_text.hide()
    
    def SaveAs(self, event):
        name_of_note = ""
        note_contents = self.plainTextEdit.toPlainText()
        if event.key() == QtCore.Qt.Key_Return and self.save_as_text.isVisible(): 
            self.name_of_note = self.save_as_text.text()
            saved_note = open("notes/{}.txt".format(self.name_of_note), "w+")
            saved_note.write(note_contents)
            saved_note.close()
            self.save.hide()
            self.save_as.hide()
            self.save_as_text.hide()


    def ShowSaveAsText(self):
        self.save_as_text.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = notes_app()
    window.show()
    app.exec()
