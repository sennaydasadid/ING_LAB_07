# -*- coding: utf-8 -*-
ACCION="Backstage passes to a TAFKAL80ETC concert"
NAME="Sulfuras, Hand of Ragnaros"
class GildedRose(object):
  
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != ACCION and  item.quality > 0 and item.name != NAME:
                item.quality -= 1
            if item.quality < 50 and item.name == ACCION:
                item.quality += 1
            if item.name != NAME:
                item.sell_in -= 1
            if item.sell_in < 0 :
                item.quality -= 1
            else:
                item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
