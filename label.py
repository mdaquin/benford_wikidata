import json
import requests
data={}
with open("numbers.json") as f:
    data=json.load(f)

for p in data:
    np = p[p.rfind('/')+1:].replace('>','')
    print(np)
    url = 'https://www.wikidata.org/wiki/Special:EntityData/'+np+'.json'
    r = requests.get(url)
    try:
        d = json.loads(r.text)
        if "entities" in d and np in d["entities"] and "labels" in d["entities"][np] and "en" in d["entities"][np]["labels"] and "value" in d["entities"][np]["labels"]["en"]:    
            label = d["entities"][np]["labels"]["en"]["value"]
            print("Label:"+label)
            data[p]["l"] = label
            if "entities" in d and np in d["entities"] and "descriptions" in d["entities"][np] and "en" in d["entities"][np]["descriptions"] and "value" in d["entities"][np]["descriptions"]["en"]:    
                desc = d["entities"][np]["descriptions"]["en"]["value"]
                print("Description: "+ desc)
                data[p]["d"] = desc
    except json.decoder.JSONDecodeError:
        print("nop "+r.text)

with open("numbers-l.json", "w") as f:
    json.dump(data, f)
