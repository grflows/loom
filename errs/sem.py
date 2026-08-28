from errs.err_codes import ERRSDICT
from errs.err_ascii import *

def simple_err_message(err_code, context):
    print(f" {TOP_RIGHT_CURVED} error[{err_code}]:", ERRSDICT[err_code])
    print(f" {BOTTOM_RIGHT_CURVED} {context}")

def simple_err_message_2lines(err_code, context):
    print(f" {TOP_RIGHT_CURVED} error[{err_code}]:", ERRSDICT[err_code])
    print(f" {BRANCH_RIGHT} {context[0]}")
    print(f" {BOTTOM_RIGHT_CURVED} {context[1]}")

# ===================================== dispacthers
SEM = [simple_err_message, simple_err_message_2lines]

def dispatch(err_code, err_station_zone, context):
    if err_station_zone < len(SEM):
        func = SEM[err_station_zone](err_code, context)
    else:
        print("UNKNOW ERROR STATION of index: ", err_station_zone)
        exit()

