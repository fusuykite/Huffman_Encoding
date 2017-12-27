
import array_list
import linked_list
from sys import *
from huffman_bits_io import *
import unittest


# -------- 2.1 Count Occurrences --------

#inFile -> (main_list, line_string)
#takes a file and returns a list(256) and a string of the line in the input text
def count_occurences(inFile):
    inFile = open(inFile, 'r')
    main_list = []
    for i in range(256):
        main_list.append(0)
    for line in inFile:
        for i in line:

            alpha_int = ord(i)
            main_list[alpha_int] += 1
    inFile.close()
    return main_list



# -------- 2.2 Data Definition for Huffman Tree --------
# a Huffman tree is either
# - a Huffman node
# - or a Leaf node

#contains a val and freq
class Leaf:
    def __init__(self, val, freq):
        self.val = val #string val the ascii value
        self.freq = freq #int val for number amount of occurences
    def __eq__(self, other):
        return (type(other) == Leaf and self.val == other.val and self.freq == other.freq)
    def __repr__(self):
        return "Leaf({!r}, {!r})".format(self.val, self.freq)

#contains a val, freq, left, and right
class Node:
    def __init__(self, val, freq, left, right):
        self.val = val  # the ascii value
        self.freq = freq # the number of occurences
        self.left = left # Huffman Tree
        self.right = right # Huffman Tree

    def __eq__(self, other):
        return (type(other) == Node and self.val == other.val and self.freq == other.freq and self.left == other.left
                and self.right == other.right)
    def __repr__(self):
        return "Node({!r}, {!r}, {!r}, {!r})".format(self.val, self.freq, self.left, self.right)

# a pair is (first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first #pair value
        self.rest = rest #pair value

    def __eq__(self, other):
        return (type(other) == Pair and self.first == other.first and self.rest == other.rest)

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

#a List consists of a lst and length
class List:
    def __init__(self, lst, length):
        self.lst = lst  #a list
        self.length = length # a list value

    def __eq__(self, other):
        return (type(other) == List and self.lst == other.lst and self.length == other.length)

    def __repr__(self):
        return "List({!r}, {!r})".format(self.lst, self.length)




#tree -> string
#creates a string out of all the characters in a string in pre_order order
def pre_order_traversal(tree):
    if type(tree) == Leaf:
        return chr(int(tree.val))
    else:
        return pre_order_traversal(tree.left) + pre_order_traversal(tree.right)



#main_list -> list
#takes a main_list [0,1,0,0] and returns a sorted list[leaf('92', 2)], 1]
def sorted_leaf_list(list):
    interval = len(list)
    sorted_list = array_list.empty_list()
    for i in range(interval):
        if list[i] != 0:
            if sorted_list.length == 0:
                array_list.add(sorted_list, 0, Leaf(str(i), list[i]))
            else:
                x = 0
                for d in range(sorted_list.length):
                    if comes_before(Leaf(str(i), list[i]), sorted_list.lst[d]) and x == 0:
                        array_list.add(sorted_list, d, Leaf(str(i), list[i]))
                        x = 1
                if x == 0:
                    length_s = sorted_list.length
                    array_list.add(sorted_list, length_s, Leaf(str(i), list[i]))
    return sorted_list

#array_list -> linked_list
#takes an array list and returns a linked list
def array_to_linked(list1):
    if list1.length > 1:
        value, list1 = array_list.remove(list1, 0)

        return Pair(value, array_to_linked(list1))
    return Pair(list1.lst[0], None)




#Huffman Tree -> int
#takes a huffman tree and returns the number of leaves within the tree itself
def leaf_count(tree, value = 0):
    if type(tree) == Leaf:
        value += 1
        return value
    else:
        return leaf_count(tree.left) + leaf_count(tree.right)

#file -> string
#takes the file and returns the contents within the file
def line_string3(inFile):
    inFile = open(inFile, 'r')
    line_string2 = ''
    for line in inFile:
        line_string2 += line
    inFile.close()
    return line_string2

# -------- 2.3 Build a Huffman Tree --------


#node, node -> boolean
#the comes_before function compares the frequency of nodes the value if frequency is equal
def comes_before(a, b):
    if a.freq < b.freq:
        return True
    elif a.freq > b.freq:
        return False
    else:
        if int(a.val) < int(b.val):
            return True
        return False

#main_list, comes_before -> linked_list(Huffman Tree)
#takes a main_list, sorts the nodes, and then returns a Huffman Tree Linked List
def build_tree(list, func):
    sorted_list1 = sorted_leaf_list(list)
    sorted_list = array_to_linked(sorted_list1)
    while linked_list.length(sorted_list) > 1:
        leaf_node, sorted_list = linked_list.remove(sorted_list, 0)
        leaf_node1, sorted_list = linked_list.remove(sorted_list, 0)

        if int(leaf_node.val) < int(leaf_node1.val):
            x = Node(leaf_node.val, leaf_node.freq + leaf_node1.freq, leaf_node, leaf_node1)
        else:
            x = Node(leaf_node1.val, leaf_node.freq + leaf_node1.freq, leaf_node, leaf_node1)
        sorted_list = linked_list.insert_sorted(sorted_list, x, func)
    ptree = linked_list.get(sorted_list, 0)
    return ptree


# -------- 2.4 Build a List for the Character Codes --------

#tree -> string
#creates a string representing the 0/1 traversal in a tree
def pre_order_binary(tree, value = ''):
    if type(tree) == Leaf: #find == ascii value of the letter to find
        return (value, (tree.val))
    else:
        return pre_order_binary(tree.left, value + '0') + pre_order_binary(tree.right, value + '1')


# -------- 2.5 Huffman Encoding --------


#inFile, outFile -> string
#the encode function encodes the bit version of the tree traversal to the outfile
def huffman_encode(inFile, outFile):
    main_list = count_occurences(inFile)
    hb_writer = HuffmanBitsWriter(outFile)
    if main_list == [0] * len(main_list):
        hb_writer.write_byte(0)
        hb_writer.close()
        return ''

    line_string = line_string3(inFile)
    sorted_tree = build_tree(main_list, comes_before)
    leaf_alpha = pre_order_traversal(sorted_tree)

    key = pre_order_binary(sorted_tree)
    key_1 = []
    for i in key:
        key_1.append(i)

    bin = ""
    for i in line_string:
        alpha_val = ord(i)
        if alpha_val < 257:
            for d in range(len(key)):
                if d % 2 != 0:
                    if int(key_1[d]) == alpha_val:
                        bin += (key_1[d-1])
    bin += "000"
    leaf_num = leaf_count(sorted_tree)
    count = 0
    hb_writer.write_byte(leaf_num)  #prints frequency of leafs for header
    for i in range(len(main_list)):
        if main_list[i] != 0:
            hb_writer.write_byte(i)
            hb_writer.write_int(main_list[i])
            count += 1
    if bin != '000':
        hb_writer.write_code(bin)
    hb_writer.close()
    return leaf_alpha

# -------- 2.6 Huffman Decoding  --------

#inFile, outFile
#huffman decode the bit format of an inFile into the outFile ascii version

def huffman_decode(inFile, outFile):
    outFile_w = open(outFile, 'w')
    hb_reader = HuffmanBitsReader(inFile)
    codes_num = (hb_reader.read_byte())
    if codes_num == 0:
        outFile_w.write('')
        outFile_w.close()
        hb_reader.close()
    else:

        index = 0
        main_list = []
        for i in range(256):
            main_list.append(0)
            # print(main_list)
            index += 1
        # creates a main_list using the file values
        for i in range(codes_num):
            alpha_int = hb_reader.read_byte() #ASCII Value
            val = hb_reader.read_int() #frequency
            main_list[alpha_int] += val

        #creates a sorted huffman tree
        huffman_tree = build_tree(main_list, comes_before)

        #creates a key list ['00', '32', '01', '98', '100', '100', '101', '99']
        key = pre_order_binary(huffman_tree)
        key_1 = []
        for i in key:
            key_1.append(i)

        if len(key_1) == 2 and key_1[0] == '':
            for i in range(huffman_tree.freq):
                val = chr(int(huffman_tree.val))
                outFile_w.write(val)

        else:
            #finds the total number of characters in original string
            cur_sum_freq = 0
            sum_freq = 0
            for i in main_list:
                if i != 0:
                    sum_freq += i

            hi = 0
            current_val = ''
            while cur_sum_freq < sum_freq:

                bit = hb_reader.read_bit()
                hi += 1
                if bit == True:
                    current_val += '1'
                else:
                    current_val += '0'

                for d in range(len(key_1)):
                    if d % 2 == 0:
                        if (key_1[d]) == current_val:
                            outFile_w.write(chr(int((key_1[d + 1]))))
                            cur_sum_freq += 1
                            current_val = ''
        hb_reader.close()
        outFile_w.close()


# -> List

tree1 = Node('32', 3, Leaf('105', 1), Leaf('106', 2))
ctree = Node('34', 7, Node('65', 3, Leaf('90', 1), Leaf('87', 2)), Leaf('89', 4))

list1 = List([0, 1, 0, 2, 1], 5)

list5 = List([Leaf('1', 1), Leaf('4', 1), Leaf('3', 2)], 3)

list6 = [0, 0, 0, 1, 3, 0, 0]
list7 = [0, 0, 0, 0, 0, 0, 0]


list8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
               
list9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 4, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0,
   0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.


    def test_sort(self):
        self.assertEqual(pre_order_traversal(tree1), 'ij')

    def test_pre_order(self):
        self.assertEqual(pre_order_traversal(ctree), "ZWY")

    def test_pre_order_binary(self):
        self.assertEqual(pre_order_binary(ctree), ('00', '90', '01', '87', '1', '89'))

    def test_sorted_leaf_list(self):
        self.assertEqual(str(sorted_leaf_list(list6)), str(List([Leaf('3', 1), Leaf('4', 3)], 2)))

    def test_sorted_leaf_list_2(self):
        self.assertEqual(str(sorted_leaf_list(list7)), 'List([], 0)')
    
    def test_sorted_leaf_list_3(self):
        self.assertEqual(str(sorted_leaf_list(list9)), str(List([Leaf('32', 1), Leaf('100', 1), Leaf('97', 2), Leaf('98', 2), Leaf('99', 2)], 5)))

    def test_array_to_linked(self):
        self.assertEqual(array_to_linked(list5), Pair(Leaf('1', 1), Pair(Leaf('4', 1), Pair(Leaf('3', 2), None))))

    def test_array_to_linked1(self):
        self.assertEqual(array_to_linked(List([Leaf('97', 1), Leaf('98', 1), Leaf('99', 1)], 3)), Pair(Leaf('97', 1), Pair(Leaf('98', 1), Pair(Leaf('99', 1), None))))

    def test_comes_before(self):
        self.assertTrue(comes_before(Leaf('32', 2), Leaf('42', 3)))

    def test_comes_before1(self):
        self.assertTrue(comes_before(Leaf("21", 3), Leaf("45", 3)))

    def test_comes_before2(self):
        self.assertFalse(comes_before(Leaf("45", 3), Leaf("21", 3)))

    def test_leaf_count(self):
        self.assertEqual(leaf_count(ctree), 3)

    def test_count_occurences(self):
        self.assertEqual(str((count_occurences('try.txt'))), str([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


    def test_build_tree(self):
        self.assertEqual(build_tree(list8, comes_before), Node('97', 2, Leaf('97', 1), Leaf('98', 1)))
    
    def test_build_tree1(self):
        self.assertEqual(build_tree(list10, comes_before), Node('32', 25, Node('98', 10, Node('104', 4, Node('104', 2, 
        Leaf('104', 1), Leaf('106', 1)), Leaf('110', 2)), Node('98', 6, Leaf('98', 3), Node('99', 3, Leaf('113', 1), 
        Leaf('99', 2)))), Node('32', 15, Node('32', 7, Leaf('119', 3), Leaf('32', 4)), Node('97', 8, Leaf('97', 4), 
        Leaf('100', 4)))))
    def test_encode5(self):
        open("blank.txt", 'w').close()
        self.assertEqual(huffman_encode('blank.txt', 'blank2.txt'), '')

    def test_encode(self):
        self.assertEqual(huffman_encode('try.txt', 'output.txt'), 'ab')

    def test_encode1(self):
        self.assertEqual(huffman_encode('try2.txt', 'output_2.txt'), 'a')

    #def test_encode2(self):
    #    self.assertEqual(huffman_encode('try3.txt', 'output3.txt'), '')

    def test_decode(self):
        self.assertEqual(huffman_decode('output.txt', 'output2.txt'), None)


    def test_decode3(self):
        self.assertEqual(huffman_decode('output_2.txt', 'output2_2.txt'), None)

    def test_decode2(self):
        self.assertEqual(huffman_decode('blank2.txt', 'blank3.txt'), None)

    def test_line_string(self):
        self.assertEqual(line_string3('try.txt'), 'ab')

    def test_repr1(self):
        self.assertEqual(Pair.__repr__(Pair("first", Pair("rest", "mt"))), "Pair('first', Pair('rest', 'mt'))")

    def test_repr2(self):
        self.assertEqual(List.__repr__(List([1, 3, 6, 14], 4)), "List([1, 3, 6, 14], 4)")

    def test_eq(self):
        list = List(['1', '2', '3', '4'], 4)
        list1 = List(['1', '2', '3', '4'], 4)
        self.assertEqual(list, list1)

    def test_repr(self):
        node1 = Node(87, 3, Leaf(33, 10), Leaf(101, 5))
        self.assertEqual(repr(node1), 'Node(87, 3, Leaf(33, 10), Leaf(101, 5))')




if __name__ == '__main__':
    unittest.main()