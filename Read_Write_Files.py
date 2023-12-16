# here is a list of names
names = ["Fred", "Bob", "Chuck","Jim","Tom"]

# here we open the file as write only
file = open('TestFile.rad', 'w') # the 'w' means write

# here we try to open the file, and if it works
# we write all the data to the file
try:
    # loop through the list of names
    for value in names:
        # write each name to the file with a new line character
        file.write(value + '\n') # note that the '\n' is the end line character
finally:
    # if the file was opened and the data written,
    # then close the file
    file.close()

# now lets do something with the data we wrote to the file
# lets make a class to hold the person data in
class Person:
    # here's the constructor for the person class
    def __init__(self, nameOfPerson) -> None:
        # create one field for the name of the person
        self.Name = nameOfPerson
    
    # here's a method to print the name of the person
    def PrintName(self) -> None:
        print(f"{self.Name} is my name!")

# now lets create a list of people
# we create from the data in the file
listOfPeople = []

# here we open the file as read only
file = open('TestFile.rad', 'r') # the 'r' means read only

try:
    # loop through each line in the file
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
#lucas pull request test