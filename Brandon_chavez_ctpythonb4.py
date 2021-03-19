"""
Program goals:
3. Pull othe values stored at specific indexes
4. Convert input to INTs
5. Put all action into a while loop
6. Write a exit option

"""
import random
myList = []

def mainProgram():
    #Build a while loop
    while True:
        print("Hello , there! Let's work with lists!")
        print("PLease choose from the following options. Type the number of your choice")
        choice = input("""1. Add to a list,
2. Return a value at a list
3. Add a bunch of numbers!
4. Random Search
5. Linear search
6. print list
7. to quit   """)
        if choice == "1":
            addToList()
        elif choice == "2": 
            indexValues()
        elif choice == "3":
            addabunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            print(myList)
        else:
            break
        
def addToList():
    print("Adding to a listt! Great Choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def addabunch():
    print("we're going to add a bunch of numbers to your list")
    numToAdd = input("How many new integers do you want to add   ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is complete")

def randomSearch():
    print("bruh, how you doing bruv, im a random search engine")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("Where going to go through this list one item at a time")
    SeachValue = input("What are you looking for?  ")
    for x in range(len(myList)):
        if myList (x) == int(searchValue):
            print("Your item is at index position {}".format (8))

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here!   ")
    print(myList[int(indexPos)])
    



if __name__ == "__main__":
    mainProgram()

