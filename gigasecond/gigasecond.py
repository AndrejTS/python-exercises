from datetime import timedelta


def add(moment):
    tdelta = timedelta(seconds=1000000000)
    return moment + tdelta
