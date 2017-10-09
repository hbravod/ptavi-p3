#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.list = []
        self.labels = {'root-layout': ['width', 'height', 'backgroundcolor'],
                       'region': ['id', 'top', 'bottom'],
                       'img': ['src', 'region', 'begin', 'dur'],
                       'audio': ['src', 'begin', 'dur'],
                       'textstream': ['src', 'region']
                       }

    def startElement(self, name, attrs):

        diccionario = {}

        if name in self.labels:
            diccionario['name'] = name
            for atribute in self.labels[name]:
                diccionario[atribute] = attrs.get(atribute, "")
            self.list.append(diccionario)

    def get_tags(self):
        return(self.list)

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.list)
