# Name:         Jack Walton
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   AlphaBits
# Term:         Winter 2021

from typing import Optional, Tuple, List


class HuffmanNode:
    
    def __init__(self, char: str, count: int, l_ref: Optional["HuffmanNode"],
                 r_ref: Optional["HuffmanNode"]) -> None:
        self.char = char
        self.count = count
        self.l_ref = l_ref
        self.r_ref = r_ref

    def __eq__(self, other: Optional["HuffmanNode"]) -> bool:
        if other is None:
            return False
        return (self.char == other.char and self.count == other.count
                and self.l_ref == other.l_ref and self.r_ref == other.r_ref)

    def __repr__(self) -> str:
        s = f"{self.char}:{self.count}"
        if self.l_ref is not None:
            s += " " + str(self.l_ref)
        if self.r_ref is not None:
            s += " " + str(self.r_ref)
        return s



def create_lists(chars: str) -> Tuple[List[str], List[int]]:
    all_chars = []
    list_chars = []
    list_freq = []
    all_chars = [char for char in chars]
  
    # loop till string values present in list of str chars
    for char in all_chars:              
        # checking for the duplicacy 
        if char not in list_chars: 
            # insert value in list_chars 
            list_chars.append(char) 

    for i in range(0, len(list_chars)): 
        # count the frequency of each letter (present  
        # in list_chars) in all_chars 
        list_freq.append(all_chars.count(list_chars[i]))

    return list_chars, list_freq

# print(create_lists("DEADBEEFCAFE"))



def create_all_nodes(chars: Optional[List[str]], freq: Optional[List[int]]) \
                     -> Optional[List[HuffmanNode]]:
    nodes = []
    for i in range(len(chars)):
        node = HuffmanNode(chars[i], freq[i], None, None)
        nodes.append(node)
    return nodes



def find_min_node(nodes: List[HuffmanNode]) -> HuffmanNode:
    """ a huffman node is min if lowest freq, if 2 or more nodes have the 
    same freq, then take the ones with the highest ascii values """
    min_freq = None
    min_ord = None
    for node in nodes:
        if min_freq is None or node.count == min_freq and ord(node.char) \
                     < min_ord or node.count < min_freq:
            min_node = node
            min_freq = node.count
            min_ord = ord(node.char)

    return min_node
            
def find_2min_nodes(nodes: List[HuffmanNode]) -> Tuple[HuffmanNode, \
                          HuffmanNode]:
    min1 = find_min_node(nodes)
    nodes.remove(min1)
    min2 = find_min_node(nodes)
    nodes.remove(min2)

    return min1, min2

# nodes = [HuffmanNode("D", 2, None, None), HuffmanNode("E", 
#                   3, None, None), HuffmanNode("A", 1, \
#                          None, None), HuffmanNode("C",
#                               2, None, None), HuffmanNode("F", 1, None, \
#                               None)]
# print(find_2min_nodes(nodes))
# print(nodes)
# print(find_min_node(nodes))



def find_min_ascii(min1: HuffmanNode, min2: HuffmanNode) -> str:
    if ord(min1.char) > ord(min2.char):
        return min2.char
    else:
        return min1.char

# min1 = HuffmanNode("A", 8, None, None)
# min2 = HuffmanNode("E", 4, None, None)
# print(find_min_ascii(min1, min2))



def create_ref_nodes(min1: HuffmanNode, min2: HuffmanNode) -> \
                         Tuple[HuffmanNode, HuffmanNode]:
    if min1.count > min2.count:
        lref = min2
        rref = min1
    elif min1.count < min2.count:
        lref = min1
        rref = min2
    else:
        if find_min_ascii(min1, min2) == min1.char:
            lref = min1
            rref = min2
        else:
            lref = min2
            rref = min1

    return lref, rref

# min1 = HuffmanNode("A", 8, None, None)
# min2 = HuffmanNode("E", 4, None, None)
# lref, rref = create_ref_nodes(min1, min2)
# print(lref, rref)



def create_parent_node(lref: HuffmanNode, rref: HuffmanNode) -> HuffmanNode:
    new_count = lref.count + rref.count
    min_ascii = find_min_ascii(lref, rref)
    parent = HuffmanNode(min_ascii, new_count, lref, rref)
    return parent

# print(create_parent_node(lref, rref))



def create_tree(chars: str) -> HuffmanNode:
    """
    Build a Huffman tree by analyzing the frequency of each character in the
    given string and return the root node of the tree.
    """
    # making list of letters and list of frequencies
    parent = None

    chars_list, freq = create_lists(chars)

    # making list of HuffmanNodes with lref and rref of None
    nodes = create_all_nodes(chars_list, freq)

    # declaring tree and sub tree as None    
    
    while len(nodes) > 1:
        # finding 2 smallest nodes, and removes nodes from list "nodes"
        min_node1, min_node2 = find_2min_nodes(nodes)

        # left ref is lowest freq, if freq is tied, left reft is lowest ascii
        lref, rref = create_ref_nodes(min_node1, min_node2)

        # building the parent node
        parent = create_parent_node(lref, rref)

        # inserting parent node back into nodes ( with its refs )
        nodes.append(parent)


    return parent

# chars = "CAFEDEADBEEF"
# print(create_tree(chars))


def is_parent(root: Optional[HuffmanNode]) -> bool:
    if root is None:
        return False
    elif root.l_ref is None and root.r_ref is None:
        return False
    else:
        return True

# print(is_parent(None))

def find_code_char(char: str, root: Optional[HuffmanNode], code: str) -> str:

    # when we are at the character's leaf -> return code (base case)
    if root.char == char and not is_parent(root):
        return code

    # return acc to recursive call, backtrack
    if root.char != char and not is_parent(root):
        return None

    else:
        # add "0" to string because we're traversing left
        code_l = find_code_char(char, root.l_ref, code + "0")

        # if left ref is not the char leaf we're looking for traverse right
        # if not is_parent(root.l_ref) and root.l_ref.char != char:
        if code_l is None:
            # add "1" to string because we're traversing right
            code_r = find_code_char(char, root.r_ref, code + "1")

        else:
            return code_l

        if code_r is None:
            return None

        else:
            return code_r

# root = create_tree("DEADBEEFCAFE")
# print(find_code_char("F", root, ""))



def encode(chars: str, root: Optional[HuffmanNode]) -> str:
    """
    Return the Huffman code (bit string) of the given characters, using the
    provided Huffman tree.
    """
    chars_list = list(chars)
    code = ""
    for char in chars_list:
        code_bit = find_code_char(char, root, "")
        code += code_bit

    return code

# root = create_tree("DEADBEEFCAFE")
# chars = "DADDA"
# print(encode(chars, root)) 



def decode(bits: str, root: Optional[HuffmanNode]) -> str:
    """
    Return the original encoded string from the given string of bits, using the
    provided Huffman tree.
    """
    tree = root
    if tree is None:
        return None

    word = ""
    bits_list = list(bits)
    while len(bits_list) > 0:
        
        if not is_parent(tree):
            word += tree.char
            tree = root

        bit = bits_list[0]

        if bit == "0":
            bits_list.pop(0)
            tree = tree.l_ref 
        
        else:
            bits_list.pop(0)
            tree = tree.r_ref 

    if not is_parent(tree):
        word += tree.char
        tree = root

    return word

# root = create_tree("DEADBEEF")
# bits = "101010011"
# print(decode(bits, root))



# do not modify code below this line
def main() -> None:
    chars = input("Treeify: ")  # initial chars used to create Huffman tree
    root = create_tree(chars)
    while True:
        try:
            chars = input(">>> ")  # chars to encode
            code = encode(chars, root)
            assert decode(code, root) == chars
            print(code)
        except AssertionError:
            print("Encode/Decode Failure")
        except EOFError:  # loop breaks with CTRL+d
            break
    print()


# if __name__ == "__main__":
#     main()
