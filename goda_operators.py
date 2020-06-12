# Conditional operators - Python defines the scope of the condition by the indentation. So be careful
age = 15
if age == 15:
    print("its Goda")
elif age < 15:
    print("its tanu")
    print("and she loves chocolate")
else:
    print("Its rama")

# Logical operators
name = "Goda"
if age > 14 and name == "Goda":
    print("Goda rules!")
elif age <= 14 or name == "tanu":
    print("Its Tanu")
elif not age <= 15:
    print("Its rama")

# Terenary operators
age = 15 if name == "Goda" else 14
print(age)
