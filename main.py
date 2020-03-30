from typing import List

import font
import random

def main():
    print("enter string (only latters)")
    str = input()
    for i in str:
        if is_number(i):
            print("you enter numeric")
            return
    print("enter file name")
    inp = input()
    file = open("./out/" + inp + ".txt", "w")
    string_builder(str, inp)
def string_builder(string, name):
    str = string
    str = list(str)
    leters = []
    mass = [["","","","","",""]]
    i = 0
    for inc in str:
        leters.append(font.call_letter(inc))
    for inc in range(len(leters)):
        for incr in range(6):
            if incr < 6:
                mass[0][incr] = mass[0][incr] + leters[inc][incr]
            else:pass
    for innn in range(6):
        if innn < 6:
            mass[0][innn] = mass[0][innn] + "\n"
            print(mass[0][innn], end="")
            writeInFile(name, mass[0][innn])
        else:pass

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def writeInFile(file, data):
    with open("./out/" + file +  ".txt", "a") as fi:
        fi.write(data)

if __name__ == '__main__':
    main()

