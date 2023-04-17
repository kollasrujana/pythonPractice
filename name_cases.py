# studentName = "Rams"
# print(f"hello {studentName}, would you like to learn some Python today?")

# scientistName = "Albert Einstein"
# scientistQuote = "A person who never made a mistake never tried anything new."

# print(f"{scientistName} once said \"{scientistQuote}\"")

scientistName = "\tAlbert Einstein\t\t\n"
scientistQuote = "\tA person who never made a mistake never tried anything new.\n\n"
print(f"{scientistName.strip()} once said \"{scientistQuote.lstrip().rstrip()}\"")

filename = "python_notes.txt"
print(f"remove suffix method applied on {filename.removesuffix('.txt')}")

x,y,z = 1,2,3
print(x,y,z)
