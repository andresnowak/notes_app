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

        self.note_reader()

    def note_reader(self):
        text = []
        index = 0
        for character in self.contents:
            if character == "*":
                index = self.contents.index(character)
                self.contents = self.contents[index:]
                self.header_counter(self.contents)
            else:
                pass

        saved_note = open("notes/hello.html", "w+")
        self.text_note = "".join(self.text_note)
        saved_note.write(self.text_note)
        saved_note.close()
        exit()

    def header_counter(self, text):
        header_number = 0
        index = 0
        for character in self.contents:
            if character == "*":
                header_number += 1
            else:
                index = self.contents.index(character)
                self.contents = self.contents[index:]
                self.header(self.contents, header_number)

    def header(self, text, header_number):
        header_text = []
        index = 0
        for letter in self.contents:
            if letter == "*":
                header_text = "".join(map(str, header_text))
                result = "<h{}>{}</h{}>".format(header_number, header_text, header_number)
                index = self.contents.index(letter)
                self.contents = self.contents[index:]

                self.header_counter_finish(result)
                #print (result)
            else:
                header_text.append(letter)

    def header_counter_finish(self, text_header):
        index = 0
        for letter in self.contents[index:]:
            if letter != "*":
                self.text_note.append(text_header)
                index = self.contents.index(letter)
                self.contents = self.contents[index:]
                self.note_reader()

        self.contents = ""
        self.text_note.append(text_header)
        self.note_reader()   

    def paragraph(self, text):
        return "<p>{text}</p>".format(text=text)

    def create_html(self):
        pass

if __name__ == "__main__":
    note = open("notes/hello.txt")
    MarkdownToHtml(note)
