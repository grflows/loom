from syntax import *
import err_triage

lexer_errs = []

def lex(file_name):
    tokens = []
    line_number = 0
    start_of_line = True
    with open(file_name) as f:
        source = f.read().split("\n")
        
    for line in source:
        line = line.strip()
        line_number += 1
        fchar = line[0] if line != "" else "empty"
        print(line_number, "|", line)
        if start_of_line:
            if fchar == "|":
                pass
            elif fchar == "?":
                pass
            elif fchar == "#":
                pass
            elif fchar == "@":
                pass
            elif fchar == "/":
                continue
            elif 'a' <= fchar <= 'z':
                pass
            # invalids
            elif '0' <= fchar <= '9':
                lexer_errs.append(("GRM001", "SEM", 1, [f"line[{line_number}]: Expected line to start with a reserved keyword or symbol", f"{line}"]))
            else :
                lexer_errs.append(("GRM001", "SEM", 1, [f"line[{line_number}]: Expected line to start with a reserved keyword or symbol", f"{line}"]))
                
    if lexer_errs == []:
        return tokens
    else:
        print(f"Exited with {len(lexer_errs)} errors(s)")
        for err in lexer_errs:
            err_triage.tof(err[0], err[1], err[2], err[3])
        exit()
