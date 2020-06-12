with open("goda_text_file.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("My name is Goda and my best friend is Tanu")

with open("goda_text_file.txt", mode="r", encoding="UTF-8") as my_file:
    print(my_file.read())

my_file.closed
