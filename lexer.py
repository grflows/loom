from syntax import *
import err_triage

def lex(file_name):
    tokens = []
    line_number = 0
    line_start = True
    with open(file_name) as f:
        source = f.read().split(" ")

    for chunk in source:
        first_char = chunk[0]
        if line_start:
            if first_char == "#":
                pass 
            elif first_char == "\n":
                pass
            else:
                pass
            line_start = False
            continue
        elif first_char == "\n":
            line_start = True
            line_number += 1


    return tokens
