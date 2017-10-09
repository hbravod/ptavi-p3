#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler (ContentHandler):

    def __init__ (self):
        
        self.dic_root_layout = {'width':"", 'height':"", 'background_color':""}
        self.dic_region = {'id':"", 'top':"", 'bottom':"", 'left':"", 'right':""}
        self.dic_img = {'src':"", 'region':"", 'begin':"", 'dur':""}
        self.dic_audio = {'src':"", 'begin':"", 'dur':""}
        self.dic_textstream = {'src':"", 'region':""}
        self.list = []

    def startElement(self, name, attrs):

        if name == "root_layout":
            self.dicc_root_layout['width'] = attrs.get('width', "")
            self.dicc_root_layout['height'] = attrs.get('height', "")
            self.dicc_root_layout['background_color'] = attrs.get('background_color', "")
            self.list.append(self.dic_root_layout)

        elif name == "region":
            self.dic_region['id'] = attrs.get('id', "")
            self.dic_region['top'] = attrs.get('top', "")
            self.dic_region['bottom'] = attrs.get('bottom', "")
            self.list.append(self.dic_region)

        elif name == "img":
            self.dic_img['src'] = attrs.get('src', "")
            self.dic_img['region'] = attrs.get('region', "")
            self.dic_img['begin'] = attrs.get('begin', "")
            self.dic_img['dur'] = attrs.get('dur', "")
            self.list.append(self.dic_img)

        elif name == "audio":
            self.dic_audio['src'] = attrs.get('src', "")
            self.dic_audio['begin'] = attrs.get('begin', "")
            self.dic_audio['dur'] = attrs.get('dur', "")
            self.list.append(self.dic_audio)

        elif name == "textstream":
            self.dic_textstream['src'] = attrs.get('src', "")
            self.dic_textstream['region'] = attrs.get('region', "")
            self.list.append(self.dic_textstream)

    def get_tags(self):
        return(self.list)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.list)
