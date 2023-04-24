from p4_starter_code import *
import pytest

def buildBalancedTree():
    """
    Description: This function builds and returns a tree of the following format:
                                        30
                               20              40
                           15      25      35      45
                         13  17  23  27  33  37  43  47

    Returns: (<RedBlackTree>, [<RBNode>, ...])
    """
    BST = RedBlackTree()

    v = "a"
    N0 = RBNode((30, v)) # root of the tree

    N1 = RBNode((20, v)) #first level
    N2 = RBNode((40, v))

    N3 = RBNode((15, v)) #second level
    N4 = RBNode((25, v))
    N5 = RBNode((35, v))
    N6 = RBNode((45, v))

    N7 = RBNode((13, v)) #Third level
    N8 = RBNode((17, v))
    N9 = RBNode((23, v))
    N10 = RBNode((27, v))
    N11 = RBNode((33, v))
    N12 = RBNode((37, v))
    N13 = RBNode((43, v))
    N14 = RBNode((47, v))

    N0.setLChild(N1)
    N0.setRChild(N2)
    N1.setParent(N0)
    N2.setParent(N0)

    N1.setLChild(N3)
    N1.setRChild(N4)
    N3.setParent(N1)
    N4.setParent(N1)

    N2.setLChild(N5)
    N2.setRChild(N6)
    N5.setParent(N2)
    N6.setParent(N2)

    N3.setLChild(N7)
    N3.setRChild(N8)
    N7.setParent(N3)
    N8.setParent(N3)

    N4.setLChild(N9)
    N4.setRChild(N10)
    N9.setParent(N4)
    N10.setParent(N4)

    N5.setLChild(N11)
    N5.setRChild(N12)
    N11.setParent(N5)
    N12.setParent(N5)

    N6.setLChild(N13)
    N6.setRChild(N14)
    N13.setParent(N6)
    N14.setParent(N6)

    N0.setBlack()
    N3.setBlack()
    N4.setBlack()
    N5.setBlack()
    N6.setBlack()


    BST._root = N0
    return (BST, [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14])


class TestMain:

    def test_initValid(self):
        BST = RedBlackTree()
        assert BST._root == None

    def test_insertValidEmpty(self):
        tree = RedBlackTree()
        T1 = (30, "a")

        ret = tree.insert(T1)
        root = tree._root

        assert ret == True
        assert root.getValue() is T1
        assert root.isBlack()

        assert root.getParent() == root.getRChild() == root.getLChild() == None

    def test_insertValidBalanced(self):
        BST = RedBlackTree()
        v = "data"
        balancedTree = [(30, v), (20, v), (40, v), (15, v), (25, v), (35, v), (45, v), (13, v), (17, v), (23, v), (27, v), (33, v), (37, v), (43, v), (47, v)]
        validationBalanced = {
        0:  "(30, black)",
        1:  "(30, black), (20, red)",
        2:  "(30, black), (20, red), (40, red)",
        3:  "(30, black), (20, black), (15, red), (40, black)",
        4:  "(30, black), (20, black), (15, red), (25, red), (40, black)",
        5:  "(30, black), (20, black), (15, red), (25, red), (40, black), (35, red)",
        6:  "(30, black), (20, black), (15, red), (25, red), (40, black), (35, red), (45, red)",
        7:  "(30, black), (20, red), (15, black), (13, red), (25, black), (40, black), (35, red), (45, red)",
        8:  "(30, black), (20, red), (15, black), (13, red), (17, red), (25, black), (40, black), (35, red), (45, red)",
        9:  "(30, black), (20, red), (15, black), (13, red), (17, red), (25, black), (23, red), (40, black), (35, red), (45, red)",
        10: "(30, black), (20, red), (15, black), (13, red), (17, red), (25, black), (23, red), (27, red), (40, black), (35, red), (45, red)",
        11: "(30, black), (20, red), (15, black), (13, red), (17, red), (25, black), (23, red), (27, red), (40, red), (35, black), (33, red), (45, black)",
        12: "(30, black), (20, red), (15, black), (13, red), (17, red), (25, black), (23, red), (27, red), (40, red), (35, black), (33, red), (37, red), (45, black)",
        13: "(30, black), (20, red), (15, black), (13, red), (17, red), (25, black), (23, red), (27, red), (40, red), (35, black), (33, red), (37, red), (45, black), (43, red)",
        14: "(30, black), (20, red), (15, black), (13, red), (17, red), (25, black), (23, red), (27, red), (40, red), (35, black), (33, red), (37, red), (45, black), (43, red), (47, red)",
        }

        #balanced tree insertion test.
        for i in range(len(balancedTree)):
                ret = BST.insert(balancedTree[i])
                assert ret == True
                ret = BST.traverse("pre-order")
                cmp = validationBalanced[i]
                assert ret == cmp, f"FAILED-{i}: {ret} \n {cmp}\n"

    def test_insertValidSkew(self):
        BST = RedBlackTree()
        v = "data"
        skewTree = [(13, v), (15, v), (17, v), (20, v), (23, v), (25, v), (27, v), (30, v), (33, v), (35, v), (37, v), (40, v), (43, v), (45, v), (47, v)]
        validationSkew = {
        0:  "(13, black)",
        1:  "(13, black), (15, red)",
        2:  "(15, black), (13, red), (17, red)",
        3:  "(15, black), (13, black), (17, black), (20, red)",
        4:  "(15, black), (13, black), (20, black), (17, red), (23, red)",
        5:  "(15, black), (13, black), (20, red), (17, black), (23, black), (25, red)",
        6:  "(15, black), (13, black), (20, red), (17, black), (25, black), (23, red), (27, red)",
        7:  "(20, black), (15, red), (13, black), (17, black), (25, red), (23, black), (27, black), (30, red)",
        8:  "(20, black), (15, red), (13, black), (17, black), (25, red), (23, black), (30, black), (27, red), (33, red)",
        9:  "(20, black), (15, black), (13, black), (17, black), (25, black), (23, black), (30, red), (27, black), (33, black), (35, red)",
        10: "(20, black), (15, black), (13, black), (17, black), (25, black), (23, black), (30, red), (27, black), (35, black), (33, red), (37, red)",
        11: "(20, black), (15, black), (13, black), (17, black), (30, black), (25, red), (23, black), (27, black), (35, red), (33, black), (37, black), (40, red)",
        12: "(20, black), (15, black), (13, black), (17, black), (30, black), (25, red), (23, black), (27, black), (35, red), (33, black), (40, black), (37, red), (43, red)",
        13: "(20, black), (15, black), (13, black), (17, black), (30, red), (25, black), (23, black), (27, black), (35, black), (33, black), (40, red), (37, black), (43, black), (45, red)",
        14: "(20, black), (15, black), (13, black), (17, black), (30, red), (25, black), (23, black), (27, black), (35, black), (33, black), (40, red), (37, black), (45, black), (43, red), (47, red)",
        }

        #balanced tree insertion test.
        for i in range(len(skewTree)):
                ret = BST.insert(skewTree[i])
                assert ret == True
                ret = BST.traverse("pre-order")
                cmp = validationSkew[i]
                assert ret == cmp, f"FAILED-{i}: {ret} \n {cmp}\n"

    def test_insertInvalid(self):
        BST = RedBlackTree()

        T1 = ("a", 1)
        T2 = []
        T3 = None
        T4 = (1)

        ret1 = BST.insert(T1)
        ret2 = BST.insert(T2)
        ret3 = BST.insert(T3)
        ret4 = BST.insert(T4)

        assert ret1 == ret2 == ret3 == ret4 == False
        assert BST._root == None