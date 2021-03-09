"""
Program goals:
1. Add items to alist (ints)
2. Offer the user a choice of actions
3. Pull othe values stored at specific indexes
4. Convert input to INTs

"""

def mainProgram():
    myList = []
    print("Hello , there! Let's work with lists!")
    print("PLease choose from the following options. Type the number of your choice")
    choice = input("1. Add to a list, 2. Return a value at a list    ")
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()
def addToList():
    print("Adding to a listt! Great Choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def indexValues():



if __name__ == "__main__":
    mainProgram()

