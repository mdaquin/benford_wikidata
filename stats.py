import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) != 2:
    print("please provide filename.")
    sys.exit(-1)
    
data = {}
with open(sys.argv[1]) as f:
    data = json.load(f)

print("property,label,description,number,min,max,magnitude range,fit")
for p in data:
    mr = len(str(data[p]["a"]))-len(str(data[p]["i"]))
    fit = "n/a"
    label = ""
    description = ""
    if "l" in data[p]:
        label = data[p]["l"]
    if "d" in data[p]:
        description = data[p]["d"].replace('"',"''")
    if "f" in data[p]:
        fit = str(data[p]["f"])
    print(p+',"'+label+'","'+description+'",'+str(data[p]["c"])+","+str(data[p]["i"])+","+str(data[p]["a"])+","+str(mr)+","+fit)
