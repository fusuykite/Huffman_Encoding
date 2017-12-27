# a listItem is one of:
# - a number
# - a string


# AnyList is one of
# - None or
# Pair(first, rest)_

class List:
    def __init__(self, lst, length):
        self.lst = lst  #a list
        self.length = length # a list value

    def __eq__(self, other):
        return (type(other) == List and self.lst == other.lst and self.length == other.length)

    def __repr__(self):
        return "List({!r}, {!r})".format(self.lst, self.length)


# a Pair is a pair of any and another pair or None
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return (type(other) == Pair and self.first == other.first and self.rest == other.rest)

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)



# nothing -> list
# takes nothing and returns and empty list
def empty_list():
    return None

def comes_before(a, b):
    if a.freq < b.freq:
        return True
    elif a.freq == b.freq and a.val < b.val:
        return True
    return False


def less_than(x, y):
    if x == y:
        return True
    return x < y

#list, int, any -> list
#takes a list and places the any type at the index given by the int and returns the list
def add(lst, index, value):
    if index < 0:
        raise IndexError
    if lst == None:
        if index == 0:
            return Pair(value, None)
        else:
           raise IndexError
    else:
        if index > 0:
            index -= 1
            return Pair(lst.first, add(lst.rest, index, value))
        else:
            return Pair(value, lst)

#list -> int
#takes a list and returns the number of elements in it
def length(lst):
    if lst == None:
        return 0
    else:
        return 1 + length(lst.rest)

#list, int -> any
#takes a list and an int and returns the value at that index
def get(lst, index):
    if index < 0:
        raise IndexError
    if lst == None:
        raise IndexError
    else:
        if index != 0:
            index -= 1
            return get(lst.rest, index)
        else:
            return lst.first

#list, int, value -> list
#takes a list and returns a new list with a new value at the specified index
def set(lst, index, value):
    if index < 0:
        raise IndexError
    if lst == None:
        raise IndexError
    else:
        if index != 0:
            index -= 1
            return Pair(lst.first, set(lst.rest, index, value))
        else:
            return Pair(value, lst.rest)

#list, int -> tuple
#takes a list and takes out the value at the index and returns a tuple with the removed element and the new listn ***changed

def remove(anyList, index, count = 0):
    if index < 0 or anyList == None and index >= count:
        raise IndexError()
    if index == count:
        return (anyList.first, anyList.rest)
    return (remove(anyList.rest, index, count + 1)[0], Pair(anyList.first, remove(anyList.rest, index, count + 1)[1]))


#Signature: AnyList int -> AnyList
#Purpose Statement: To take a list and an index and return a new list with the value at the index removed, (helper function
#for remove function).
#Header: def get_new_list(lst, index):

def get_new_list(lst, index):
    if index < 0:
        raise IndexError
    if lst == None:
        raise IndexError
    else:
        if index != 0:
            index -= 1
            return Pair(lst.first, (get_new_list(lst.rest, index)))
        else:
            if lst.rest != None:
                return Pair(lst.rest.first, lst.rest.rest)
            else:
               return None

#list, function -> None
#foreach function takes a list and a function and applies every element in the list to the function
def foreach(lst, func):
    if lst is not None:
        func(lst.first)
        return foreach(lst.rest, func)
    return None

#List, list, function -> list
# insert(lst, val, func) function compares two different lists given by the func parameter and returns a list
def insert(lst, val, func):
    if lst == None:
        return Pair(val, None)
    if func(val, lst.first):
        return Pair(val, lst)
    else:
        return Pair(lst.first, insert(lst.rest, val, func))

#lst, func -> sorted_list
# is_sort(lst, func) takes a list and a function and returns a new sorted list with the function given
def is_sort(lst, func):
    sorted_list = empty_list()

    while length(lst) > 0:

        sorted_list = insert(sorted_list, lst.first, func)

        lst = remove(lst, 0)

    return sorted_list

"""def comes_before(a, b):
    print("\n\n")
    print("BYEEEEEEEEEEEEEE")
    if a.freq < b.freq:

        print("\n<")
        return True
    elif a.freq > b.freq:
        print("\n>")
        return False
    else:

        if a.val < b.val:
            print("\nSAME")
            return True
        return False
"""
#list, val, function
#inserts the value into a sorted list
def insert_sorted(list, val, function):

    if list == None:
        return Pair(val, None)
    if function(val, list.first):
        #print('HEELLLOO')
        return Pair(val, Pair(list.first, list.rest))
    return Pair(list.first, insert_sorted(list.rest, val, function))




