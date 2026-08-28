from errs import sem # simple err message


def tof(err_code, err_station, err_station_zone, contex): #transfare of care
    if err_station == "SEM":
        sem.dispatch(err_code, err_station_zone, contex)
