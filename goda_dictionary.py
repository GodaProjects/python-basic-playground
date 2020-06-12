
# Dictionary or key value pairs
friends = {
    "Goda": "Chellam",
    "Tanu": "Kutty"
}
print(friends)
friends1 = dict([
    ("Goda", "Chellam"),
    ("Tanu", "Kutty")
])
print(friends1)
print(friends1["Goda"])
print(friends1.items())

del friends1["Tanu"]
print(friends1.items())
friends1.pop("Goda")
print(friends1.items())

# Key and value printing
for k in friends:
    print(k)
for v in friends.values():
    print(v)

print("%(Goda)s is %(Tanu)s's friend" % friends)
