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
        self.italic = False
        self.bold = False
        self.ordered_list_ol = False
        self.ordered_list_li = False

        self.header_number = 0
        self.list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.counter_note_reader = 0

        self.note_reader()

    def note_reader(self):
        index = 0

        for character in self.contents:
            index = self.contents.index(character)
            self.contents = self.contents[index:]

            self.note_reader_checker(character)

            self.counter_note_reader += 1

        self.finish_checker()

        self.save_note()

    def save_note(self):
        saved_note = open("notes/hello.html", "w+")
        self.text_note = "".join(self.text_note)
        saved_note.write(self.text_note)
        saved_note.close()
        exit()

    def note_reader_checker(self, character):
        #FIXME: fix a bug where an <ol> is being added. Because of <strong> and <br> maybe?
        if character == "#":
                self.header_checker()
        elif character == "\n":
            if self.header == True:
                self.header_checker()

            self.text_note.append("<br>")
        elif character == "*" or character == "_":
            index = self.contents.index(character)
            self.contents = self.contents[index:]
            self.bold_italic_checker()
        else:
            self.text_note.append(character)

    def header_checker(self):
        index = 0

        if self.header == True:
            self.text_note.append("</h{}>".format(self.header_number))
            self.header_number = 0
            self.header = False
        else:
            for character in self.contents:
                if character == "#":
                    self.header_number += 1
                else:
                    self.text_note.append("<h{}>".format(self.header_number))
                    index = self.contents.index(character)
                    self.contents = self.contents[index:]
                    self.header = True
                    self.note_reader()

    def bold_italic_checker(self):
        counter = 0

        for character in self.contents:
            if counter == 2:
                if self.bold == True:
                    self.text_note.append("</strong>")
                    index = self.contents.index(character)
                    self.contents = self.contents[2:]
                    self.bold = False
                    self.note_reader()
                else:
                    self.text_note.append("<strong>")
                    index = self.contents.index(character)
                    self.contents = self.contents[2:]
                    self.bold = True
                    self.note_reader()       
            elif character == "*" or character == "_":
                counter += 1
            elif counter == 1:
                if self.italic == True:
                    self.text_note.append("</em>")
                    index = self.contents.index(character)
                    self.contents = self.contents[index:]
                    self.italic = False
                    self.note_reader()
                else:
                    self.text_note.append("<ol>")
                    index = self.contents.index(character)
                    self.contents = self.contents[index:]
                    self.italic = True
                    self.note_reader()

        self.finish_checker(counter)

    def ordered_list_checker(self):
        #TODO: add a checker to see if it has a dot next to the number
        #FIXME: fix a bug were there is being added a <br> inside of a list <li>
        if self.ordered_list_ol == False:
            self.text_note.append("<ol>")

            self.ordered_list_ol = True

        if self.ordered_list_li == True:
            self.text_note.append("</li>")

            self.ordered_list_li = False
            self.note_reader()
        else:
            self.text_note.append("<li>")

            self.contents = self.contents[2:]
            self.ordered_list_li = True

            self.counter_note_reader += 2

            self.note_reader()

    def ordered_list_checker_finish(self):
        if self.ordered_list_ol == True:
            self.text_note.append("</ol>")

            self.ordered_list_ol = False

    def finish_checker(self, counter = 0):
        if self.header == True:
            self.header_checker()

        if self.bold == True:
            if counter == 2:
                self.text_note.append("</strong>")
                self.contents = ""
                self.bold == False
                self.note_reader()

        if self.italic == True:
            if counter == 1:
                self.text_note.append("</em>")
                self.contents = ""
                self.italic == False
                self.note_reader()

        if self.ordered_list_li == True:
            self.text_note.append("</li>")

            self.ordered_list_li = False

        if self.ordered_list_ol == True:
            self.ordered_list_checker_finish()

if __name__ == "__main__":
    note = open("notes/hello.txt")
    MarkdownToHtml(note)
