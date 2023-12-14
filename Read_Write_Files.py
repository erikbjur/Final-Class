names = ["Fred", "Bob", "Chuck"]
ages = [56, 34, 23]

reader = open('TestFile.txt', "x")
reader.write("Names")
try:
    for value in names:
        reader.write(value + '\n')
finally:
    reader.close()