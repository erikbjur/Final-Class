# here is a list of names
names = ["Fred", "Bob", "Chuck"]

# here we open the file as write only
file = open('TestFile.txt', 'w')

# here we try to open the file, and it it works
# we write all the data to the file
try:
    # loop through the list of names
    for value in names:
        # write each name to the file with a new line character
        file.write(value + '\n')
finally:
    file.close()

# lets make a class to hold the person data in
class Person:
    def __init__(self, nameOfPerson) -> None:
        self.Name = nameOfPerson
    
    def PrintName(self) -> None:
        print(f"{self.Name} is my name!")

# now lets create a list of people from the list
listOfPeople = []

# here we open the file as read only
file = open('TestFile.txt', "r")

try:
    for line in file:
        # create a person with this name
        newPerson = Person(line.rstrip())
        # add them to the list of people
        listOfPeople.append(newPerson)
finally:
    # here's how we close the file
    file.close()

# now print off the names of the people in the list
for person in listOfPeople:
    person.PrintName()