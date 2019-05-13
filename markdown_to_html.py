#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, sys

class MarkdownToHtml():
    def __init__(self, note):
        #note = open("notes/{note}")
        note = note.read() 
        # NOTE:you can iterate over characters in contents of a read file and  i think strings to
        self.contents = []
        for character in note:
            self.contents.append(character)

        #print(self.contents)
        #self.header_number = 0
        self.text_note = []
        self.header = False
        self.header_number = 0

        self.note_reader()

    def note_reader(self):
        text = []
        index = 0
        for character in self.contents:
            if character == "#":
                index = self.contents.index(character)
                self.contents = self.contents[index:]
                self.header_checker()
            elif character == "\n":
                if self.header == True:
                    index = self.contents.index(character)
                    self.contents = self.contents[index:]
                    self.header_checker()

                self.text_note.append("<br>")
            elif character == "*":
                index = self.contents.index(character)
                self.contents = self.contents[index:]
                self.bold_italic_checker()
            else:
                self.text_note.append(character)

        saved_note = open("notes/hello.html", "w+")
        self.text_note = "".join(self.text_note)
        saved_note.write(self.text_note)
        saved_note.close()
        exit()

    def header_checker(self):
        index = 0

        if self.header == True:
            self.text_note.append("</h{}".format(self.header_number))
            self.header_number = 0
            self.header = False
        else:
            for character in self.contents:
                if character == "#":
                    self.header_number += 1
                else:
                    self.text_note.append("<h{}".format(self.header_number))
                    index = self.contents.index(character)
                    self.contents = self.contents[index:]
                    self.header = True
                    break
        
        #TODO: add a header creator here for the special case when the text finishes here

    def bold_italic_checker(self):
        pass

if __name__ == "__main__":
    note = open("notes/hello.txt")
    MarkdownToHtml(note)
