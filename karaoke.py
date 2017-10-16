#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal():

    def Inicializador(SmallSMILHandler):
        lista = cHandler.get_tags()

    def __str__(self):
        for labelsD in lista:
            print(labelsD['name'], "\t",)
        for atributo in labelsD:
            if labelsD[atributo] != "" and atributo != 'name':
                print(atributo, "=", '"', labelsD[atributo], '"')

    def to_json(self):
        with open('karaoke.json', 'w') as outfile:
            json.dump(lista, outfile)

    def do_local(self):
        for labelsD in lista:
            print(labelsD['name'], "\t",)
        for atributo in labelsD:
            if labelsD[atributo][0:7] == "http://":
                atributolargo = labelsD[atributo]
                atributocorto = labelsD[atributo].split('/')[-1]
                urllib.request.urlretrieve(atributolargo, atributocorto)
                labelsD[atributo] = atributocorto
            if labelsD[atributo] != "" and atributo != 'name':
                print(atributo, "=", '"', labelsD[atributo], '"')

if __name__ == "__main__":

    parser = make_parser()
    cHandler = KaraokeLocal()
    parser.setContentHandler(cHandler)

    try:
        parser.parse(open(sys.argv[1]))
    except SyntaxError:
        print("Usage: python3 karaoke.py file.smil")
