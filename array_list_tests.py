import unittest
from array_list import *



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


list1 = List([Song('1', 'Oceanside', 'The Decemberists', '5 Songs'), Song('0', 'Shiny', 'The Decemberists', '5 Songs')], 2)

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
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_empty_list(self):
        self.assertEqual(empty_list(), List([], 0))

    def test_add1(self):
        self.assertEqual(add(List([1, 3, 6, 14], 4), 2, 10), List([1, 3, 10, 6, 14], 5))

    def test_add2(self):
        self.assertRaises(IndexError, add, List([1, 3, 6, 14], 4), 5, 0)

    def test_length1(self):
        self.assertEqual(length(List([1, 3, 6, 14], 4)), 4)

    def test_length2(self):
        self.assertEqual(length(List([], 0)), 0)

    def test_get1(self):
        self.assertEqual(get(List([1, 3, 6, 14], 4), 2), 6)

    def test_get2(self):
        self.assertRaises(IndexError, get, List([1, 3, 6, 14], 4), -4)

    def test_set1(self):
        self.assertEqual(set(List([1, 3, 6, 14], 4), 1, 2), List([1, 2, 6, 14], 4))

    def test_set2(self):
        self.assertRaises(IndexError, set, List([1, 3, 6, 14], 4), 4, 7)

    def test_remove1(self):
        self.assertEqual(remove(List([1, 3, 6, 14], 4), 2), (6 ,List([1, 3, 14], 3)))

    def test_remove2(self):
        self.assertRaises(IndexError, remove, List([1, 3, 6, 14], 4), 5)

    def test_repr1(self):
        self.assertEqual(List.__repr__(List([1, 3, 6, 14], 4)), "List([1, 3, 6, 14], 4)")

    def test_compare_num_22(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('1', 'Oceanside', 'The Decemberists', '5 Songs')), True)

    def test_compare_num_0(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('0', 'Oceanside', 'The Decemberists', '8 Songs')), True)

    def test_compare_num_22(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('0', 'Sceanside', 'The Decemberists', '5 Songs')), True)

    def test_compare_num_33(self):
        self.assertEqual(compare_number(Song('0', 'Oceanside', 'The Decemberists', '5 Songs'), Song('0', 'Oceanside', 'Vhe Decemberists', '5 Songs')), True)

    def test_foreac3h(self):
        self.assertEqual(foreach(list1, print), None)

    def test_is_sort(self):
        self.assertEqual(is_sort(list1, compare_number), List([Song('0', 'Shiny', 'The Decemberists', '5 Songs'), Song('1', 'Oceanside', 'The Decemberists', '5 Songs'), ], 2))



if __name__ == '__main__':
    unittest.main()
