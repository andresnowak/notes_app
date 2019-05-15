#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, sys

class MarkdownToHtml():
    def __init__(self, note):
        #note = open("notes/{note}")
        self.note_name = note
        note = open(("notes/{}").format(note))
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
        self.unordered_list_ul = False

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
        self.note_name = self.note_name.replace(".txt", "")
        saved_note = open(("notes/{}.html").format(self.note_name), "w+")
        self.text_note = "".join(self.text_note)
        saved_note.write(self.text_note)
        saved_note.close()
        exit()

    def note_reader_checker(self, character):
        if character == "#":
                self.header_checker()

        if character == "\n":
            #TODO: change this if so it doesnt add the /n newline apart from the <br>
            if self.header == True:
                self.header_checker()

            self.text_note.append("<br>")

            self.counter_note_reader = 0

        if character == "*" or character == "_":
            self.bold_italic_checker()

        if character in self.list_numbers and self.counter_note_reader == 1:
            self.ordered_list_checker()

        if character not in self.list_numbers and self.counter_note_reader == 1:
            self.ordered_list_checker_finish()

        if character == "-" and self.counter_note_reader == 1 or character == "+" and self.counter_note_reader == 1:
            self.unordered_list_checker()

        if self.counter_note_reader == 1:
            self.unordered_list_checker_finish()
        
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
        #FIXME: fix the case where a strong or em is being added at start, because if we dont add one at the finish html will apply the bold or italic either way
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
                    self.text_note.append("<em>")
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

    def unordered_list_checker(self):
        #TODO: add a checker to see if it has a space next to the syntax for unordered list
        #FIXME: fix a bug were there is being added a <br> inside of a list <li>
        if self.unordered_list_ul == False:
            self.text_note.append("<ul>")

            self.unordered_list_ul = True

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

    def unordered_list_checker_finish(self):
        if self.unordered_list_ul == True:
            self.text_note.append("</ul>")

            self.unordered_list_ul = False

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

        if self.unordered_list_ul == True:
            self.unordered_list_checker_finish()

if __name__ == "__main__":
    note = "hello.txt"
    MarkdownToHtml(note)
