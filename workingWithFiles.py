def findShorthand(): 
    shorthand = input("What acronym would you like to know about?\n")
    found = False
    try:
        with open('sample.txt') as file:
            for i in file:
                if shorthand in i:
                    print(i)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
    
    if not found:
        print("Sorry I don;t know what", shorthand, "means.")

def addShorthand():
    newShorthand = input("What acronym would you like to add?\n")
    newDef = input(f"What is the meaning of {newShorthand}?\n")
    try:
        with open("sample.txt", 'a') as file:
            file.write(f"\n{newShorthand} - {newDef}")
            print(file)
    except FileNotFoundError as e:
        print("File not found")
        return

def main():
    selection = input("Would you like to (s)earch for an acronym or (d)efine one?\n")
    if selection == "s" or selection == "S":
        findShorthand()
    if selection == "d" or selection =="D":
        addShorthand()

main()