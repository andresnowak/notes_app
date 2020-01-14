#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class MarkdownToHtml():
    def __init__(self, note):
        #note = open("notes/{note}")
        self.note_name = note
        note = open(("notes/{}").format(note))
        note = note.read()

        new_note = self.note_reader(note)

        self.bold_syntax = [r"(\*{2}|_{2})", r"\S(\*{2}|_{2})", r"(\*{2}|_{2})\S"]

        self.save_note(new_note)

    def save_note(self, note):
        self.note_name = self.note_name.replace(".md", "")
        saved_note = open(("notes/{}.html").format(self.note_name), "w+")

        saved_note.write(note)
        saved_note.close()
        exit()
    
    def note_reader(self, note):
        note = note.split("\n")
        new_note = []

        bold_syntax = [r"(\*{2}|_{2})", r"\S(\*{2}|_{2})", r"(\*{2}|_{2})\S"]
        italic_syntax = [r"(\*|_)", r"\S(\*|_)", r"(\*|_)\S"]

        for line in note:
            line = self.header_checker(line) if self.header_checker(line) != None else line
            line = self.emphasis_checker(line, bold_syntax, "b")
            line = self.emphasis_checker(line, italic_syntax, "i")

            new_note.append(line)
        
        return "\n".join(new_note)


    def header_checker(self, string):
        header_syntax = [r"^# ", r"^#{2} ", r"^#{3} ", r"^#{4} ", r"^#{5} ", r"^#{6} "]
        
        for index, header in enumerate(header_syntax):
            header_found = re.search(header, string)

            if header_found != None:
                header_location = [header_found.span()[0], header_found.span()[1]]
                string = f"<h{index+1}>{string[header_location[1]::]}</h{index+1}>"

                break
        
        return string

    def emphasis_checker(self, string, syntax, html_format):
        syntax_counter = re.findall(syntax[0], string)
        syntax_found = False

        for index in range(len(syntax_counter)):
            if syntax_found:
                syntax_location = re.search(syntax[1], string).span()
                string = f"{string[0:syntax_location[0]+1]}</{html_format}>{string[syntax_location[1]::]}"

                syntax_found = False
            else:
                if index != len(syntax_counter) - 1:
                    syntax_location = re.search(syntax[2], string).span()
                    string = f"{string[0:syntax_location[0]]}<{html_format}>{string[syntax_location[1]-1::]}"

                    syntax_found = True
                
        return string

if __name__ == "__main__":
    note = input("Write the name of the file you want to convert: ")
    #note = "hello3.md"
    MarkdownToHtml(note)
