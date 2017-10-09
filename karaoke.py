#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)

    try:
        parser.parse(open(sys.argv[1]))
    except SyntaxError:
        print("Usage: python3 karaoke.py file.smil") 

    lista = cHandler.get_tags()

    for labelsD in lista:
        print(labelsD['name'], "\t")
        for atributo in labelsD:
            if labelsD[atributo] != "" and atributo != 'name':
                print(atributo, "=", labelsD[atributo])
            else:
                pass
