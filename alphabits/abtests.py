# Name:         Jack Walton
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   AlphaBits
# Term:         Winter 2021

import unittest

import alphabits
from alphabits import HuffmanNode as H  # only allowed use of from ... import

class TestCreateLists(unittest.TestCase):
    def test_create_lists_1(self):
        chars = "DEADBEEFCAFE"
        self.assertEqual(alphabits.create_lists(chars), (['D', 'E', 'A', 'B', \
                         'F', 'C'], [2, 4, 2, 1, 2, 1]))

    def test_create_lists_2(self):
        chars = "DEADBEEF"
        self.assertEqual(alphabits.create_lists(chars), (['D', 'E', 'A', 'B', \
                         'F'], [2, 3, 1, 1, 1]))

    def test_create_lists_3(self):
        chars = "DEAD"
        self.assertEqual(alphabits.create_lists(chars), (['D', 'E', 'A'], \
                         [2, 1, 1]))

    def test_create_lists_4(self):
        chars = "DDDDAA"
        self.assertEqual(alphabits.create_lists(chars), (['D', 'A'], \
                         [4, 2]))
    def test_create_lists_5(self):
        chars = "AADDDD"
        self.assertEqual(alphabits.create_lists(chars), (["A", "D"], \
                         [2, 4]))

    def test_create_lists_6(self):
        chars = ""
        self.assertEqual(alphabits.create_lists(chars), ([], \
                         []))



class TestCreateAllNodes(unittest.TestCase):
    def test_create_all_nodes_1(self):
        chars = ['D', 'E', 'A', 'B', 'F', 'C']
        freq = [2, 4, 2, 1, 2, 1]
        nodes = [H("D", 2, None, None), H("E", 4, None, None), H("A", 2, \
                         None, None), H("B", 1, None, None), H("F", 2, None, \
                              None), H("C", 1, None, None)]
        self.assertEqual(alphabits.create_all_nodes(chars, freq), nodes)

    def test_create_all_nodes_2(self):
        chars = ['D', 'E', 'A', 'B', 'F']
        freq = [2, 3, 1, 1, 1]
        nodes = [H("D", 2, None, None), H("E", 3, None, None), H("A", 1, \
                         None, None), H("B", 1, None, None), H("F", 1, None, \
                              None)]
        self.assertEqual(alphabits.create_all_nodes(chars, freq), nodes)

    def test_create_all_nodes_3(self):
        chars = ['D', 'E', 'A']
        freq = [2, 1, 1]
        nodes = [H("D", 2, None, None), H("E", 1, None, None), H("A", 1, \
                         None, None)]
        self.assertEqual(alphabits.create_all_nodes(chars, freq), nodes)

    def test_create_all_nodes_4(self):
        chars = ['D', 'A']
        freq = [4, 2]
        nodes = [H("D", 4, None, None), H("A", 2, None, None)]
        self.assertEqual(alphabits.create_all_nodes(chars, freq), nodes)

    def test_create_all_nodes_5(self):
        chars = []
        freq = []
        nodes = []
        self.assertEqual(alphabits.create_all_nodes(chars, freq), nodes)



class TestFindMinNode(unittest.TestCase):
    def test_find_min_node_1(self):
        nodes = [H("D", 2, None, None), H("E", 4, None, None), H("A", 2, \
                         None, None), H("B", 1, None, None), H("F", 2, None, \
                              None), H("C", 1, None, None)]
        self.assertEqual(alphabits.find_min_node(nodes), H("B", 1, None, None))

    def test_find_min_node_2(self):
        nodes = [H("D", 2, None, None), H("E", 3, None, None), H("A", 2, \
                         None, None), H("C", 1, None, None), H("F", 1, None, \
                              None)]
        self.assertEqual(alphabits.find_min_node(nodes), H("C", 1, None, None))

    def test_find_min_node_3(self):
        nodes = [H("D", 2, None, None), H("E", 3, None, None), H("A", 2, \
                         None, None), H("C", 2, None, None), H("F", 2, None, \
                              None)]
        self.assertEqual(alphabits.find_min_node(nodes), H("A", 2, None, None))

    def test_find_min_node_4(self):
        nodes = [H("D", 2, None, None), H("E", 3, None, None), H("A", 4, \
                         None, None), H("C", 2, None, None), H("F", 2, None, \
                              None)]
        self.assertEqual(alphabits.find_min_node(nodes), H("C", 2, None, None))

    def test_find_min_node_5(self):
        nodes = [H("F", 1, None, None), H("E", 1, None, None), H("A", 2, \
                         None, None), H("C", 2, None, None), H("D", 1, None, \
                              None)]
        self.assertEqual(alphabits.find_min_node(nodes), H("D", 1, None, None))



class TestFind2MinNodes(unittest.TestCase):
    def test_find_2min_nodes_1(self):
        nodes = [H("F", 1, None, None), H("E", 1, None, None), H("A", 2, \
                         None, None), H("C", 2, None, None), H("D", 1, None, \
                              None)]
        self.assertEqual(alphabits.find_2min_nodes(nodes), (H("D", 1, None, \
                         None), H("E", 1, None, None)))


    def test_find_2min_nodes_2(self):
        nodes = [H("D", 2, None, None), H("E", 3, None, None), H("A", 2, \
                         None, None), H("C", 1, None, None), H("F", 1, None, \
                              None)]
        self.assertEqual(alphabits.find_2min_nodes(nodes), (H("C", 1, None, \
                         None), H("F", 1, None, None)))

    def test_find_2min_nodes_3(self):
        nodes = [H("D", 2, None, None), H("E", 3, None, None), H("A", 2, \
                         None, None), H("C", 2, None, None), H("F", 2, None, \
                              None)]
        self.assertEqual(alphabits.find_2min_nodes(nodes), (H("A", 2, None, \
                         None), H("C", 2, None, None)))

    def test_find_2min_nodes_4(self):
        nodes = [H("D", 2, None, None), H("E", 3, None, None), H("A", 4, \
                         None, None), H("C", 2, None, None), H("F", 2, None, \
                              None)]
        self.assertEqual(alphabits.find_2min_nodes(nodes), (H("C", 2, None, \
                         None), H("D", 2, None, None)))


    def test_find_2min_nodes_5(self):
        nodes = [H("F", 1, None, None), H("E", 1, None, None), H("A", 2, \
                         None, None), H("C", 2, None, None), H("D", 1, None, \
                              None)]
        self.assertEqual(alphabits.find_2min_nodes(nodes), (H("D", 1, None, \
                         None), H("E", 1, None, None)))

    def test_find_2min_nodes_6(self):
        nodes = [H("F", 1, None, None), H("E", 1, None, None), H("A", 2, \
                         None, None), H("C", 2, None, None), H("D", 4, None, \
                              None)]
        self.assertEqual(alphabits.find_2min_nodes(nodes), (H("E", 1, None, \
                         None), H("F", 1, None, None)))



class TestFindMinASCII(unittest.TestCase):

    def test_find_min_ascii_1(self):
        min1 = H("A", 8, None, None)
        min2 = H("E", 4, None, None)
        self.assertEqual(alphabits.find_min_ascii(min1, min2), "A")

    def test_find_min_ascii_2(self):
        min1 = H("A", 2, None, None)
        min2 = H("A", 4, None, None)
        self.assertEqual(alphabits.find_min_ascii(min1, min2), "A")

    def test_find_min_ascii_3(self):
        min1 = H("B", 8, None, None)
        min2 = H("A", 60, None, None)
        self.assertEqual(alphabits.find_min_ascii(min1, min2), "A")

    def test_find_min_ascii_4(self):
        min1 = H("D", 8, None, None)
        min2 = H("C", 10, None, None)
        self.assertEqual(alphabits.find_min_ascii(min1, min2), "C")

    def test_find_min_ascii_5(self):
        min1 = H("E", 4, None, None)
        min2 = H("E", 4, None, None)
        self.assertEqual(alphabits.find_min_ascii(min1, min2), "E")



class TestCreateRefNodes(unittest.TestCase):

    def test_create_ref_nodes_1(self):
        min1 = H("A", 8, None, None)
        min2 = H("E", 4, None, None)
        lref, rref = alphabits.create_ref_nodes(min1, min2)
        self.assertEqual((lref, rref), (min2, min1))

    def test_create_ref_nodes_2(self):
        min1 = H("A", 12, H("E", 4, None, None), None)
        min2 = H("C", 4, None, None)
        lref, rref = alphabits.create_ref_nodes(min1, min2)
        self.assertEqual((lref, rref), (min2, min1))

    def test_create_ref_nodes_3(self):
        min1 = H("B", 12, H("E", 4, None, None), None)
        min2 = H("E", 13, None, None)
        lref, rref = alphabits.create_ref_nodes(min1, min2)
        self.assertEqual((lref, rref), (min1, min2))   

    def test_create_ref_nodes_4(self):
        min1 = H("A", 12, H("E", 4, None, None), None)
        min2 = H("A", 11, None, H("A", 2, None, None))
        lref, rref = alphabits.create_ref_nodes(min1, min2)
        self.assertEqual((lref, rref), (min2, min1))

    def test_create_ref_nodes_5(self):
        min1 = H("A", 11, None, H("A", 2, None, None))
        min2 = H("E", 12, H("E", 4, None, None), None)
        lref, rref = alphabits.create_ref_nodes(min1, min2)
        self.assertEqual((lref, rref), (min1, min2))



class TestCreateParentNode(unittest.TestCase):

    def test_create_parent_node_1(self):
        lref = H("E", 4, None, None)
        rref = H("A", 8, None, None)
        parent = H("A", 12, H("E", 4, None, None), H("A", 8, None, None))
        self.assertEqual(alphabits.create_parent_node(lref, rref), parent)

    def test_create_parent_node_2(self):
        lref = H("A", 4, None, None)
        rref = H("E", 8, None, None)
        parent = H("A", 12, H("A", 4, None, None), H("E", 8, None, None))
        self.assertEqual(alphabits.create_parent_node(lref, rref), parent)

    def test_create_parent_node_3(self):
        lref = H("E", 7, None, None)
        rref = H("A", 8, None, None)
        parent = H("A", 15, H("E", 7, None, None), H("A", 8, None, None))
        self.assertEqual(alphabits.create_parent_node(lref, rref), parent)

    def test_create_parent_node_4(self):
        lref = H("B", 11, None, None)
        rref = H("E", 12, None, None)
        parent = H("B", 23, H("B", 11, None, None), H("E", 12, None, None))
        self.assertEqual(alphabits.create_parent_node(lref, rref), parent)

    def test_create_parent_node_5(self):
        lref = H("A", 12, H("E", 6, None, None), ("F", 6, None, None))
        rref = H("B", 12, None, None)

        parent = H("A", 24, H("A", 12, H("E", 6, None, None), ("F", 6, None, \
                         None)), H("B", 12, None, None))
        self.assertEqual(alphabits.create_parent_node(lref, rref), parent)



class TestCreateTree(unittest.TestCase):

    def test_create_tree_1(self):
        root = H("A", 12, H("E", 4, None, None),
                         H("A", 8, H("A", 4, H("A", 2, None, None),
                                             H("B", 2, H("B", 1, None, None),
                                                     H("C", 1, None, None))),
                                     H("D", 4, H("D", 2, None, None),
                                             H("F", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEFCAFE"), root)

    def test_create_tree_2(self):
        root = H("A", 8, H("E", 3, None, None),
                         H("A", 5, H("D", 2, None, None), H("A", 3, H("F", \
                             1, None, None), H("A", 2, H("A", 1, None, \
                                 None), H("B", 1, None, None)))))
        self.assertEqual(alphabits.create_tree("DEADBEEF"), root)

    def test_create_tree_3(self):
        root = H("A", 8, H("A", 4, H("A", 2, None, None), \
                         H("C", 2, H("C", 1, None, None), H("F", 1, None, \
                              None))), H("D", 4, H("D", 2, None, None), \
                                  H("E", 2, None, None)))
        self.assertEqual(alphabits.create_tree("DEADCAFE"), root)

    def test_create_tree_4(self):
        root = H("A", 7, H("E", 3, None, None), H("A", 4, H("A", 2, \
                         H("A", 1, None, None), H("B", 1, None, None)), \
                             H("D", 2, None, None)))
        self.assertEqual(alphabits.create_tree("DEADBEE"), root)

    def test_create_tree_5(self):
        root1 = alphabits.create_tree("CAFEDEADBEEF")
        root2 = alphabits.create_tree("CAFEDEADBEEF")
        self.assertEqual(root1, root2)



class TestIsParent(unittest.TestCase):

    def test_is_parent_1(self):
        node = H("A", 7, H("E", 3, None, None), H("A", 4, None, None))
        self.assertTrue(alphabits.is_parent(node))

    def test_is_parent_2(self):
        node = H("A", 7, None, H("A", 4, None, None))
        self.assertTrue(alphabits.is_parent(node))

    def test_is_parent_3(self):
        node = H("A", 7, H("E", 3, None, None), None)
        self.assertTrue(alphabits.is_parent(node))

    def test_is_parent_4(self):
        node = H("A", 7, None, None)
        self.assertFalse(alphabits.is_parent(node))

    def test_is_parent_5(self):
        node = None
        self.assertFalse(alphabits.is_parent(node))



class TestFindCodeChar(unittest.TestCase):

    def test_find_code_char_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                     H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.find_code_char("B", root, ""), "1010")

    def test_find_code_char_2(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.find_code_char("D", root, ""), "110")

    def test_find_code_char_3(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.find_code_char("E", root, ""), "0")

    def test_find_code_char_4(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.find_code_char("F", root, ""), "111")

    def test_find_code_char_5(self):
        root = H("A", 7, H("E", 3, None, None), H("A", 4, H("A", 2, \
                         H("A", 1, None, None), H("B", 1, None, None)), \
                             H("D", 2, None, None)))
        self.assertEqual(alphabits.find_code_char("D", root, ""), "11")



class TestEncode(unittest.TestCase):

    def test_encode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                     H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BE", root), "10100")

    def test_encode_2(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                     H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BEEF", root), "101000111")

    def test_encode_3(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                     H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("DADDA", root), "110100110110100")

    def test_encode_4(self):
        root = H("A", 7, H("E", 3, None, None), H("A", 4, H("A", 2, \
                         H("A", 1, None, None), H("B", 1, None, None)), \
                             H("D", 2, None, None)))
        self.assertEqual(alphabits.encode("DED", root), "11011")

    def test_encode_5(self):
        root = H("A", 7, H("E", 3, None, None), H("A", 4, H("A", 2, \
                         H("A", 1, None, None), H("B", 1, None, None)), \
                             H("D", 2, None, None)))
        self.assertEqual(alphabits.encode("BEAD", root), "101010011")



class TestDecode(unittest.TestCase):

    def test_decode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("10100", root), "BE")

    def test_decode_2(self):
        root = alphabits.create_tree("DEADBEE")
        self.assertEqual(alphabits.decode("101010011", root), "BEAD")

    def test_decode_3(self):
        root = alphabits.create_tree("DEADCAFE")
        self.assertEqual(alphabits.decode("011111110", root), "FEED")

    def test_decode_4(self):
        root = alphabits.create_tree("DEADCAFE")
        self.assertEqual(alphabits.decode("0010100111110", root), "ADDFED")

    def test_decode_5(self):
        root = alphabits.create_tree("DEADBEEFCAFE")
        self.assertEqual(alphabits.decode("11110010111001100", root), "FACADE")


if __name__ == "__main__":
    unittest.main()
