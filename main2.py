from threading import *
import threading


firstName = "Evan "
lastName = "Rothenbacher"
grade = 10
age = 15
garfield = "Garfield is amazing"


def printName():
    print(firstName + lastName)


def addGradeAge():
    print(grade + age)

def printGarfield():
    while True:
        print(garfield)


addGradeAge()
printName()

garfieldThread = Thread(target=printGarfield)

garfieldThread.start()

print("End of code")