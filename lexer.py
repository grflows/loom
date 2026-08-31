from syntax import *
import err_triage

def lex(file_name):
    with open(file_name) as f:
        source = f.read()
    return source
