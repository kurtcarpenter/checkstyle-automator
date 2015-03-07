import sys
from os import rename, remove

if len(sys.argv) == 1:
    fileName = input("Enter file name: ")
else:
    fileName = sys.argv[1]

output = open("output", "w")
words = {"while", "for", "if"}

with open(fileName, "r+") as file:
    changes = 0
    for str in file:
        listy = list(str)
        changed = False

        #add spaces after things
        for word in words:
            index = str.find(word)
            if index != -1:
                if str[index + len(word)] != " ":
                    changed = True
                    changes += 1
                    for x in range (len(str) - 1, index + len(word), -1):
                        listy[x] = listy[x-1]
                    listy[index + len(word)] = " "
        #go char by char
        for index in range(0, len(listy)):
            #left bracket
            if listy[index] == "{":
                if listy[index - 1] != " ":
                    changes += 1
                    for x in range (len(str) - 1, index - 1, -1):
                        if x == len(str) - 1:
                            listy.append(listy[x])
                        else:
                            listy[x+1] = listy[x]
                    listy[index] = " "
            #not operator
            if listy[index] == "!":
                if listy[index + 1] == " ":
                    changes += 1
                    for x in range (index + 1, len(str) - 1):
                        listy[x] = listy[x+1]
                    listy[len(listy) - 1] = ""
                if listy[index + 1] == "t":
                    if listy[index + 2] == "r":
                        if listy[index + 3] == "u":
                            if listy[index + 4] == "e":
                                changes += 1
                                listy[index] = "f"
                                listy[index + 1] = "a"
                                listy[index + 2] = "l"
                                listy[index + 3] = "s"
                                listy[index + 4] = "e"
                elif listy[index + 1] == "f":
                    if listy[index + 2] == "a":
                        if listy[index + 3] == "l":
                            if listy[index + 4] == "s":
                                if listy[index + 5] == "e":
                                    changes += 1
                                    listy[index] = "t"
                                    listy[index + 1] = "r"
                                    listy[index + 2] = "u"
                                    listy[index + 3] = "e"
                                    for x in range (index + 4, len(str) - 2):
                                        listy[x] = listy[x+2]
                                    listy[len(listy) - 1] = ""
                                    listy[len(listy) - 2] = ""
        #write changes
        output.write("".join(listy))
        if changed:
            output.write('\n')

output.close()
remove(fileName)
rename("output", fileName)

print("Changes:", changes)
