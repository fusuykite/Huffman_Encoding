from linked_list import *
import unittest


#Song Class incorporates number, name, artist, album

class Song:
    def __init__(self, number, name, artist, album):
        self.number = number
        self.name = name
        self.artist = artist
        self.album = album
    def __eq__(self, other):
        return (type(other) == Song and self.number == other.number and self.name == other.name and \
               self.artist == other.artist and self.album == other.album)

    def __repr__(self):
        return 'Song({!r}, {!r}, {!r}, {!r})'.format(str(self.number), self.name, self.artist, self.album)

    def __str__(self):
        return(self.number + "--" + self.name + "--" + self.artist + "--" + self.album)

class Leaf:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
    def __eq__(self, other):
        return (type(other) == Leaf and self.val == other.val and self.freq == other.freq)
    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.val, self.freq)


list1 = Pair(3, Pair("tree", Pair(1.7, None)))
list2 = Pair(Song('3', "Angel, Won't You Call Me?", 'The Decemberists', '5 Songs'), Pair(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Pair(Song('1', 'Shiny', 'The Decemberists', '5 Songs'), None)))
list3 = Pair(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), None)

list4 = Pair(Leaf('52', 1), Pair(Leaf('49', 3), None))

list5 = List([Leaf('1', 1), Leaf('4', 1), Leaf('3', 2)], 3)

def compare_number(one, two):
    if int(one.number) == int(two.number):
        if one.album < two.album:
            return True
        if one.artist < two.artist:
            return True
        if one.name < two.name:
            return True
    return int(one.number) < int(two.number)




class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        #temp_list = add(temp_list, 0, "Hello!")
        #length(temp_list)
        #get(temp_list, 0)
       # temp_list = set(temp_list, 0, "Bye!")
       # remove(temp_list, 0)

    def test_empty_list1(self):
        self.assertEqual(empty_list(), None)

    def test_add5(self):
        self.assertEqual(add(None, 0, 5), Pair(5, None))
    def test_add1(self):
        self.assertEqual(add(list1, 2, "new value"), Pair(3, Pair("tree", Pair("new value", Pair(1.7, None)))))

    def test_add2(self):
        self.assertRaises(IndexError, add, list1, 5, "nothing")

    def test_add3(self):
        self.assertEqual(add(Pair("value", None), 0, 3), Pair(3, Pair("value", None)))

    def test_add4(self):
        self.assertRaises(IndexError, add, list1, -5, "nothing")

    def test_length1(self):
        self.assertEqual(length(list1), 3)

    def test_get1(self):
        self.assertEqual(get(list1, 1), "tree")

    def test_get2(self):
        self.assertRaises(IndexError, get, list1, 4)

    def test_get3(self):
        self.assertRaises(IndexError, get, list1, -4)

    def test_set1(self):
        self.assertEqual(set(list1, 2, "new value"), Pair(3, Pair("tree", Pair("new value", None))))

    def test_set2(self):
        self.assertRaises(IndexError, set, list1, 4, "nothing")

    def test_set3(self):
        self.assertRaises(IndexError, set, list1, -4, "nothing")

    def test_remove1(self):
        self.assertEqual(remove(list1, 1), Pair(3, Pair(1.7, None)))

    def test_remove2(self):
        self.assertRaises(IndexError, remove, list1, 4)

    def test_get_new_list1(self):
        self.assertRaises(IndexError, get_new_list, list1, -4)

    def test_get_new_list2(self):
        self.assertRaises(IndexError, get_new_list, Pair("Tree", None), 4)

    def test_repr1(self):
        self.assertEqual(Pair.__repr__(Pair("first", Pair("rest", "mt"))), "Pair('first', Pair('rest', 'mt'))")

    def test_repr2_song(self):
        self.assertEqual(Song.__repr__(Song('0', 'Oceanside', 'The Decemberists', '5 Songs')), "Song('0', 'Oceanside', 'The Decemberists', '5 Songs')")

    def test_repr4_song(self):
        self.assertEqual(Song.__str__(Song('0', 'Oceanside', 'The Decemberists', '5 Songs')), "0--Oceanside--The Decemberists--5 Songs")


    def test_foreach(self): #should return None but print 3, tree, 1.7
        self.assertEqual(foreach(list1, print), None)

    def test_foreach_1(self):
        self.assertEqual(foreach(None, print), None)

    def test_is_sort(self):
        self.assertEqual(is_sort(list2, compare_number), Pair(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Pair(Song('1', 'Shiny', 'The Decemberists', '5 Songs'),
                                                                 Pair(Song('3', "Angel, Won't You Call Me?", 'The Decemberists', '5 Songs'), None))))

    def test_insert(self):
        self.assertEqual(insert(None, Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), compare_number), Pair(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), None))


    def test_compare_num(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('1', 'Oceanside', 'The Decemberists', '5 Songs')), True)

    def test_compare_num_1(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('0', 'Oceanside', 'The Decemberists', '8 Songs')), True)

    def test_compare_num_2(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('0', 'Sceanside', 'The Decemberists', '5 Songs')), True)

    def test_compare_num_3(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('0', 'Oceanside', 'Vhe Decemberists', '5 Songs')), True)


    def test_insert_sorted(self):
        self.assertEqual(insert_sorted(list4, Leaf('56', 2), comes_before), Pair(Leaf('52', 1), Pair(Leaf('56', 2), Pair(Leaf('49', 3), None))))

if __name__ == '__main__':
    unittest.main()




