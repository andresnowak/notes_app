#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class MarkdownToHtml():
    def __init__(self, note):
        #note = open("notes/{note}")
        self.note_name = note
        note = open(("notes/{}").format(note))
        note = note.read()
        # NOTE:you can iterate over characters in contents of a read file and  i think strings to

        new_note = self.note_reader(note)

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
        #new_string = None

        for line in note:
            line = self.header_checker(line) if self.header_checker(line) != None else line

            new_note.append(line)
        
        return "\n".join(new_note)


    def header_checker(self, string):
        header_syntax = [r"^# ", r"^#{2} ", r"^#{3} ", r"^#{4} ", r"^#{5} ", r"^#{6} "]
        
        for index, header in enumerate(header_syntax):
            header_found = re.search(header, string)

            if header_found != None:
                header_location = [header_found.span()[0], header_found.span()[1]]

                string = f"<h{index+1}>" + string[header_location[1]::] + f"</h{index+1}>"

                break
        
        return string

if __name__ == "__main__":
    note = input("Write the name of the file you want to convert: ")
    MarkdownToHtml(note)
