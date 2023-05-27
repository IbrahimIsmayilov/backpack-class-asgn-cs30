# Backpack Class Assignment by Ibrahim Ismayilov

# Linear Search Algorithm
def linearSearch(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i
    return -1

# TASK 1
class Backpack:
    # Constructor: Properties (State)
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    # Methods (Behaviour)

    # Set the object’s open property to true
    def openBag(self):
        self.open = True
        print("The bag was opened.")
    
    # Set the object’s open property to false
    def closeBag(self):
        self.open = False
        print("The bag is closed.")

    # If the backpack is open, add the item argument to the backpacks items array
    def putin(self, item):
        if self.open == True:
            self.items.append(item)
            print(f"The {item} was added to the backpack.")
    
    # If the backpack is open and the item argument is in the backpack, take out the item argument from the backpack

    def takeout(self, item):
        search_result = linearSearch(self.items, item)
        if self.open == True and search_result != -1:
            self.items.pop(search_result)
            print(f"The {item} was removed from your backpack.")

        

# TASK 2
small_blue_backpack = Backpack("blue", "small")
medium_red_backpack = Backpack("red", "medium")
large_green_backpack = Backpack("green", "large")

# TASK 3
small_blue_backpack.openBag()
small_blue_backpack.putin("lunch")
small_blue_backpack.putin("jacket")
small_blue_backpack.closeBag()
small_blue_backpack.openBag()
small_blue_backpack.takeout("jacket")


