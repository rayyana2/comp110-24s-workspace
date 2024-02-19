"""Demonstrate basic list syntax."""

# Initialize an empty list
grocery_list: list[str] = list() # <- list constructor
# You can also use this format:
grocery_list: list[str] = [] # <- this is called a literal

print(grocery_list)

# Add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# Create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list:")
print(grocery_list2)

# Indexing
print("Print first element of string")
print(grocery_list[0])

# Modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

# Measuring length
print("Length of list:")
print(len(grocery_list))

# Removing an item
grocery_list.pop(1)
print("After removing almond milk:")
print(grocery_list)

# Function name: display
# Parameter: list[str]
# Return Nothing!
# Print out the list

def display(word: list[str]) -> None:
    print(word)

display(grocery_list)

# Create a list!
# Function name: create
# Parameters: str and str
# Return value: list[str]
# Put both parameters into list

def create(p1: str, p2: str) -> list[str]:
    p_list: list[str] = [p1, p2]
    return p_list

x: list[str] = create("apples", "bananas")
print(x)

print(grocery_list[10])