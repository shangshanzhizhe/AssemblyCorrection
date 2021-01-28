import sys

def add2dict(indict, key1, key2, value):
    if key1 in indict:
        indict[key1].update({key2:value})
    else:
        indict[key1] = {{key2:value}}
