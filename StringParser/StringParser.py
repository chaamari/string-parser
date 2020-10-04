import fileinput
import re

# class  : StringParser
# author : Chaamari Senanayake
# purpose: Class for parsing a file and returning count of valid char sequences

# Assumptions
# 1. Pattern is considered valid only if characters are alpha-numeric and in the same case.
# i.e. Valid sequences : rttr, RttR, rTTr, RTTR, 1rr1
#      Invalid sequences : rtTr


class StringParser:
    filename = ""
    valid_count = 0
    text_pattern = r"[a-zA-Z0-9]{4}" #regex for matching a 4 character alpha-numeric string within square brackets
    square_pattern = r"\[{text_pattern}\]".format(text_pattern=text_pattern)  # regex for matching a 4 character alpha-numeric string within square brackets

    def __init__(self, filename, text_pattern=text_pattern):
        self.filename = filename
        self.text_pattern = text_pattern # override default text search pattern if needed

    def get_valid_line_count(self):
        with fileinput.input(files=self.filename) as f:
            # read and process the file line by line
            for line in f:
                self.valid_count += self.is_valid_line(line)
        return self.valid_count

    # is_valid_line: return 1 if the line is valid 0 otherwise
    def is_valid_line(self, line):
        # first check whether there are any 4 character texts within square brackets
        matches = re.findall(self.square_pattern, line)
        for match in matches:
            text = match[1:5] # extracts text within the square brackets
            if self.is_valid_text(text): # return 0 if there is a valid pattern within sq brackets
                return 0
        # proceed to checking valid text patterns
        i = 0
        while i + 3 < len(line):
            # subscript line starting at index i
            sequence = line[i:i+4]
            # search for a 4 character alpha-numeric pattern
            matches = re.findall(self.text_pattern, sequence)
            for match in matches:
                if self.is_valid_text(match):
                    return 1
            i += 1
        return 0

    def is_valid_text(self, s):
        # check whether the 4 character string is equal to it's reverse \
        # and the first and second characters are different
        if len(s) == 4 and s == s[::-1] and s[0] != s[1]:
            return True
        return False
