"""
Program goals:
3. Pull othe values stored at specific indexes
4. Convert input to INTs
5. Put all action into a while loop
6. Write a exit option

"""
myList = []

def mainProgram():
    #Build a while loop
    while True:
        print("Hello , there! Let's work with lists!")
        print("PLease choose from the following options. Type the number of your choice")
        choice = input("""1. Add to a list,
2. Return a value at a list ,
3. Random Search
4 to quit   """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
                break
def addToList():
    print("Adding to a listt! Great Choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def randomSearch():
    print("bruh, how you doing bruv, im a random search engine")
    print(myList[random.randint(0, len(myList)-1)])

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here!   ")
    print(myList[int(indexPos)])
    



if __name__ == "__main__":
    mainProgram()

