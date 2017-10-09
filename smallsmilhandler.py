#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler (ContentHandler):

    def __init__ (self):
        
        self.root_layout = ""
        self.region = ""
        self.img = ""
        self.audio = ""
        self.textstream = ""
        self.lista = []

    def get_tags(self, name, attrs):

        if name == "root_layout":
            self.width = attrs.get('width')
            print(self.root_layout)

            self.height = attrs.get('height', "")
            print(self.root_layout)

            self.background_color = attrs.get('background_color', "")
            print(self.background_color)

        elif name == "region":
            self.id = attrs.get('id', "")
            print(self.region)

            self.top = attrs.get('top', "")
            print(self.region)

            self.left = attrs.get('left', "")
            print(self.region)

            self.right = attrs.get('right', "")
            print(self.right)

        elif name == "img":
            self.src = attrs.get('src', "")
            print(self.src)

            self.region = attrs.get('region', "")
            print(self.region)

            self.begin = attrs.get('begin', "")
            print(self.begin)

            self.dur = attrs.get('dur', "")
            print(self.dur)

        elif name == "audio":
            self.src = attrs.get('src', "")
            print(self.src)

            self.begin = attrs.get('begin', "")
            print(self.begin)

            self.dur = attrs.get('dur', "")
            print(self.dur)

        elif name == "textstream":
            self.src = attrs.get('src', "")
            print(self.src)

            self.region = attrs.get('region', "")
            print(self.region)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.root_layout)
