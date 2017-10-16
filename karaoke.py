#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal(SmallSMILHandler):

    def __init__(self):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        self.list = cHandler.get_tags()
        try:
            parser.parse(open(sys.argv[1]))
        except SyntaxError:
            print("Usage: python3 karaoke.py file.smil")

    def __str__(self):
        list_str = ''
        for labelsD in self.list:
            list_str = list_str + labelsD['name']
            for atributo in labelsD:
                if labelsD[atributo] != "" and atributo != 'name':
                    list_str = list_str + "\t" + atributo + '='
                    list_str = list_str + labelsD[atributo] + '"' + "\n"
        return(list_str)

    def to_json(self, ficheroS, ficheroJ=''):
        if ficheroJ == '':
            ficheroJ = ficheroS.split('.')[0] + '.json'
        with open(ficheroJ, 'w') as outfile:
            json.dump(self.list, outfile)

    def do_local(self):
        for labelsD in self.list:
            for atributo in labelsD:
                if labelsD[atributo][0:7] == "http://":
                    atributolargo = labelsD[atributo]
                    atributocorto = labelsD[atributo].split('/')[-1]
                    urllib.request.urlretrieve(atributolargo, atributocorto)
                    labelsD[atributo] = atributocorto

if __name__ == "__main__":
    objeto = KaraokeLocal()
    print(objeto)
    objeto.to_json(sys.argv[1])
    objeto.do_local()
    objeto.to_json(sys.argv[1], 'local.json')
    print(objeto)
