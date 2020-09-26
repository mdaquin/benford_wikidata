import math
import sys
import json

if len(sys.argv) !=2:
    print("provide filename")
    sys.exit(-1)

es = {
    "1": math.log10(1.+1.),
    "2": math.log10(1.+(1./2.)),
    "3": math.log10(1.+(1./3.)),
    "4": math.log10(1.+(1./4.)),
    "5": math.log10(1.+(1./5.)),
    "6": math.log10(1.+(1./6.)),
    "7": math.log10(1.+(1./7.)),
    "8": math.log10(1.+(1./8.)),
    "9": math.log10(1.+(1./9.))    
    }

print("expected values: "+str(es))

data = {}
with open(sys.argv[1]) as f:
    data=json.load(f) 

for p in data:
    sum = 0
    for n in es:
        if n in data[p]["ns"]:
            sum += data[p]["ns"][n]
    cs = 0.    
    for n in es:
        e = es[n]
        a = 0.
        if n in data[p]["ns"]:
            a = float(data[p]["ns"][n])/float(sum)
        cs += (((a-e)**2)/e) # chi-square test
    data[p]["f"] = cs

with open(sys.argv[1]+".fit.json", "w") as f:
    json.dump(data, f)
