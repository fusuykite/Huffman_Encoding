#A List is an arrray list and its length
class List:
    def __init__(self, lst, length):
        self.lst = lst
        self.length = length

    def __eq__(self, other):
        return (type(other) == List and self.lst == other.lst and self.length == other.length)

    def __repr__(self):
        return "List({!r}, {!r})".format(self.lst, self.length)

# -> List
# Takes nothing and return an empty List object
def empty_list():
    return List([], 0)


# List, int, any -> List
# Takes a List object and returns a new List object with the specified value at the specified index included
def add(x, index, value):
    if index < 0 or index > x.length:
        raise IndexError
    new_list = []
    for val in range(index):
        new_list += [x.lst[val]]
    new_list += [value]
    for val in range(index, x.length):
        new_list += [x.lst[val]]
    x.lst = new_list
    x.length += 1
    return x


#List -> int
#Takes a List object and returns the number of elements in the List
def length(x):
    return x.length


#List, int -> any
#Takes a List object and an integer index and returns the value in the list at that index
def get(x, index):
    if index < 0 or index > x.length:
        raise IndexError
    else:
        return x.lst[index]




#List, int, any -> List
#Takes a List object and replaces the value at the passed index with the passed value, and returns the resulting list.
def set(x, index, value):
    if index < 0 or index >= x.length:
        raise IndexError
    else:
        x.lst[index] = value
        return x


#List, int -> tuple
#Removes a value from a List at the given index and returns a tuple of the removed value and resulting list.
def remove(x, index):
    if index < 0 or index >= x.length:
        raise IndexError
    else:
        new_list = []
        count = 0
        for val in x.lst:
            if count != index:
                new_list += [val]
            else:
                removed_val = x.lst[index]
            count += 1
        x.lst = new_list
        x.length -= 1
        return (removed_val, x)

#list, function -> None
#foreach function takes a list and a function and applies every element in the list to the function
def foreach(list, function):
    for i in range(list.length):
        function(list.lst[i])
    return None


#lst, func -> sorted_list
# is_sort(list, func) takes a list and a function and returns a new sorted list with the function given
def is_sort(lst, func):
    y = lst
    for i in range(1, y.length):

        b = i
        while b > 0 and func(y.lst[b], y.lst[b - 1]):

            y.lst[b], y.lst[b-1] = y.lst[b-1], y.lst[b]

            b = b - 1
    return y
