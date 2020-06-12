import re

if(re.search("ape", "The ape at the apex")):
    print("there is an ape")

godas = re.findall(
    "goda", "Goda is a great linguist and goda is a little girl.", re.IGNORECASE)

print(len(godas))

godas2 = "Goda and her little godas"
for i in re.finditer("goda.", godas2, re.IGNORECASE):
    location = i.span()
    print(location)
    print(godas2[location[0]:location[1]])
