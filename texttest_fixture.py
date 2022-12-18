# -*- coding: utf-8 -*-
from __future__ import print_function
from typing import ItemsView

from gilded_rose import GildedRose, Item
import gilded_rose 
ACCION="Backstage passes to a TAFKAL80ETC concert"

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             ItemsView(name="+5 Dexterity Vest", sell_in=10, quality=20),
             ItemsView(name="Aged Brie", sell_in=2, quality=0),
             ItemsView(name="Elixir of the Mongoose", sell_in=5, quality=7),
             ItemsView(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             ItemsView(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             ItemsView(name=ACCION, sell_in=15, quality=20),
             ItemsView(name=ACCION, sell_in=10, quality=49),
             ItemsView(name=ACCION, sell_in=5, quality=49),
             ItemsView(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRoseTest(items).update_quality() 
