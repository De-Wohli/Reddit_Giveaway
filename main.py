import requests
import random

COUNT_ITEMS = 11 #Anzahl der zu vergebenden elemente.
NUMBER_ARRAY = set()
COMMENT_ARRAY = [] #Liste aller authoren.
EXCLUDED_NAMES = ["Fuyune","CitrusTheFruitDude","Youju","Cpt_Rakuma","ChromeRavenCyclone","shikari3333"] #Namen die ausgeschlossen werden sollen, hier die mods des subs.
WINNERS = [] #Liste der gewinner

def json_extract(jsonData, key):
    arr = []
    def extract(jsonData, arr, key):
        if isinstance(jsonData, dict):
            for k, v in jsonData.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(jsonData, list):
            for item in jsonData:
                extract(item, arr, key)
        return arr

    values = extract(jsonData, arr, key)
    return values

# Das Script sucht in einem beitrag alle Authoren, speichert diese in einer liste (datentyp set: sorgt dafür das keine doppelten einträge in der liste stehen),
# Die URL ist die reguläre Reddit URL mit einem .json am ende, das sollte mit allen Reddit beiträgen funktionieren.
# Es wird zusätzlich eine liste NUMBER_ARRAY erstellt, die den index der gewinner enthält, doppelte zahlen werden hier wieder nicht zugelassen, so das jeder nur einmal gewinnen kann in einem beitrag.
def main():
    rawJson = requests.get("https://www.reddit.com/r/Augenbleiche/comments/qnxcdj/habt_ihr_namensvorschl%C3%A4ge_f%C3%BCr_diesen_sch%C3%BCchternen.json",headers = {'User-agent': 'Gandalf Der Googler Bot 0.1'})
    jsonData = rawJson.json()
    COMMENT_ARRAY = json_extract(jsonData,"author")
    COMMENT_ARRAY = set([x for x in COMMENT_ARRAY if x not in EXCLUDED_NAMES])

    while(len(NUMBER_ARRAY) < COUNT_ITEMS):
        NUMBER_ARRAY.add(random.randint(0,len(COMMENT_ARRAY)-1))
# Wenn der Index eines nutzers in der gewinner liste ist, so wird dieser in WINNERS gespeichert.
    for x in range(len(COMMENT_ARRAY)):
        if x in NUMBER_ARRAY:
            WINNERS.append(list(COMMENT_ARRAY)[x])
    
    print(WINNERS)

if __name__ == "__main__":
    main()