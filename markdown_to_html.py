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
            if character == "#":
                index = self.contents.index(character)
                self.contents = self.contents[index:]
                self.header_counter()
            elif character == "\n":
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

    def header_counter(self):
        header_number = 0
        index = 0
        for character in self.contents:
            if character == "#":
                header_number += 1
            else:
                index = self.contents.index(character)
                self.contents = self.contents[index:]
                self.header(self.contents, header_number)

    def header(self, text, header_number):
        header_text = []
        index = 0
        for letter in self.contents:
            if letter == "\n":
                header_text = "".join(map(str, header_text))
                result = "<h{}>{}</h{}>".format(header_number, header_text, header_number)
                self.text_note.append(result)
                index = self.contents.index(letter)
                self.contents = self.contents[index:]
                self.note_reader()

                #print (result)
            else:
                header_text.append(letter)

        header_text = "".join(map(str, header_text))
        result = "<h{}>{}</h{}>".format(header_number, header_text, header_number)
        self.contents = ""
        self.text_note.append(result)
        self.note_reader()

    def bold_italic_checker(self):
        counter = 0
        index = 0
        for letter in self.contents:
            if letter == "*":
                counter += 1
            else:
                index = self.contents.index(letter)
                if counter == 2:
                    self.contents = self.contents[index:]
                    self.bold()
                elif counter == 1:
                    self.contents = self.contents[index:]
                    self.italic()
                else:
                    result = self.contents[index - counter:index]
                    self.text_note.append(result)
                    self.contents = self.contents[index:]
    
    def bold(self):
        #TODO: change how header and bold work
        bold_text = []
        index = 0
        counter = 0
        for letter in self.contents:
            if letter == "*":
                counter += 1
            elif counter == 2:
                bold_text = "".join(map(str, bold_text))
                result = "<strong>{}</strong>".format(bold_text)
                self.text_note.append(result)
                index = self.contents.index(letter)
                self.contents = self.contents[index:]
                self.note_reader()
            elif counter > 2:
                pass
                #TODO: add a checker so it doesnt apply the bold if its not equal to two
            else:
                bold_text.append(letter)
        
        #TODO: add an if here so it checks if the counter is 2 so it doesnt apply the bold if its not equal to 2
        bold_text = "".join(map(str, bold_text))
        result = "<strong>{}</strong>".format(bold_text)
        self.contents = ""
        self.text_note.append(result)
        self.note_reader()

    def italic(self):
        italic_text = []
        index = 0
        counter = 0
        for letter in self.contents:
            if letter == "*":
                counter += 1
            elif counter == 1:
                italic_text = "".join(map(str, italic_text))
                result = "<em>{}</em>".format(italic_text)
                self.text_note.append(result)
                index = self.contents.index(letter)
                self.contents = self.contents[index:]
                self.note_reader()
            elif counter > 1:
                #TODO: add a checker so it doesnt apply the bold if its not equal to two
                pass
            else:
                italic_text.append(letter)

        #TODO: add an if here so it checks if the counter is 2 so it doesnt apply the italic if its not equal to 2
        italic_text = "".join(map(str, italic_text))
        result = "<em>{}</em>".format(italic_text)
        self.contents = ""
        self.text_note.append(result)
        self.note_reader()

    def paragraph(self, text):
        return "<p>{text}</p>".format(text=text)

    def create_html(self):
        pass

if __name__ == "__main__":
    note = open("notes/hello.txt")
    MarkdownToHtml(note)
