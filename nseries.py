import time
import json
import re

data = {}

st = time.time()
with open("numbers.nt") as f:
    line = f.readline()
    count = 0
    while line:
        p = line.split()[1]
        val = int(re.findall("\d+", line.split()[2])[0])
        val1 = str(val)[0]
        if p not in data:
            data[p] = {"i": val, "a": val, "c": 0, "ns": {}}
        if val < data[p]["i"]: data[p]["i"] = val
        if val > data[p]["a"]: data[p]["a"] = val         
        if val1 not in data[p]["ns"]: data[p]["ns"][val1] = 0
        data[p]["ns"][val1] += 1
        data[p]["c"] += 1
        count += 1
        line = f.readline()
        if count % 1000000 == 0:
            print(str(count/1000000)+" "+str(len(data.keys()))+" "+str(time.time()-st))
            st = time.time()
        if count % 10000000 == 0:
            with open("numbers.json", "w") as f2:
                json.dump(data, f2)
    with open("numbers.json", "w") as f2:
        json.dump(data, f2)
        


