import sys
import time
import xml.etree.ElementTree as ET
import scryfall_search as scry

def main(deckfile, dbfile):
    tree = ET.parse(deckfile)
    root = tree.getroot()
    cards = root.findall("./Cards")
    output = str()
    bulk = scry.CardBulk(dbfile)
    for card in cards:
        mtgo_id = card.get('CatID')
        qty = card.get('Quantity')
        name = card.get('Name')
        temp = bulk.search_mtgoid(mtgo_id) 
        if temp is not None:
            set = temp['set']
            collector_number = temp['collector_number']
            line_csv = '\"' + qty + '\",\"' + name + '\",\"' + collector_number + '\"'
            print(line_csv)
            output += line_csv + '\n'     
    print(output)
 
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])


