"""
Program: Project 4 - Red Black Tree
Author: William Qiu
Date: 3/17/2023
"""


# ============================== Aux Classes ====================================
class TreeIsEmpty(Exception):
    """ An exception raised if the tree is empty. """
    pass


class RBNode():
    """ This class implements a node for the BST. """

    def __init__(self, item):
        """
        Description: The constructor for the RBNode class. Default color is red.
        Usage: node = RBNode(item)
               item == (<int>, <value>)
        """
        self._parent = None
        self._lChild = None
        self._rChild = None
        self.color = True
        self._value = item
        self._key = item[0]

    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        color = "red" if (self.color) else "black"
        returnValue = f"Node: ({self._key}, {color})\n"
        returnValue += f"Parent: {self._parent._key if (self._parent != None) else self._parent}\n"
        returnValue += f"Left Child: {self._lChild._key if (self._lChild != None) else self._lChild}\n"
        returnValue += f"Right Child: {self._rChild._key if (self._rChild != None) else self._rChild}\n"
        return returnValue

    # Accessor Methods
    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        Usage: <node>.getParent()
        """
        return self._parent

    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        Usage: <node>.getRChild()
        """
        return self._rChild

    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        Usage: <node>.getLChild()
        """
        return self._lChild

    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the item.
        Usage: <node>.getValue()
        """
        return self._value

    def getKey(self):
        """
        Description: Accessor method for the Node. Returns the key.
        Usage: <node>.getKey()
        """
        return self._key

    def getColor(self):
        """
        Description: Accessor method for the Node. Returns the color.
        Usage: <node>.getColor()
        """
        return self.color

    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Usage: <node>.setParent(<RBNode>)
        """
        self._parent = node

    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Usage: <node>.setLChild(<RBNode>)
        """
        self._lChild = node

    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Usage: <node>.setRChild(<RBNode>)
        """
        self._rChild = node

    def setValue(self, value):
        """
        Description: Mutator method. Sets the value reference.
        Usage: <node>.setValue(<tuple>)
        """
        self._value = value

    def setKey(self, key):
        """
        Description: Mutator method. Sets the key reference.
        Usage: <node>.setKey(<int>)
        """
        self._key = key

    def setRed(self):
        """
        Description: Sets the color of the node to red.
        Usage: <node>.setRed()
        """
        self.color = True

    def setBlack(self):
        """
        Description: Sets the color of the node to black.
        Usage: <node>.setBlack()
        """
        self.color = False

    # comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                     nodes.
        Usage: node1 > node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key > other._key
        return returnValue

    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                     nodes.
        Usage: node1 < node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key < other._key
        return returnValue

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes.
        Usage: node1 == node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key == other._key
        return returnValue

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes.
        Usage: node1 != node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key != other._key
        if (other == None):
            returnValue = True
        return returnValue

    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                     nodes.
        Usage: node1 <= node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key <= other._key
        return returnValue

    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                     nodes.
        Usage:  node1 >= node2
        Input: Another instance of the node class.
        """
        returnValue = False
        if (other != None):
            returnValue = self._key >= other._key
        return returnValue

    # Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This method returns true if the current node
                     has a left child.
        Usage: <node>.hasLeftChild()
        """
        returnValue = False
        if (type(self._lChild) == RBNode and self._lChild._parent is self):
            returnValue = True
        return returnValue

    def hasRightChild(self):
        """
        Description: This method returns true|false depending on if the current
                     node has a right child or not.
        Usage: <node>.hasRightChild()
        """
        returnValue = False
        if (type(self._rChild) == RBNode and self._rChild._parent is self):
            returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """
        Description: Returns True if the current node has only one child.
        Usage: <node>.hasOnlyOneChild()
        """
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)

    def hasBothChildren(self):
        """
        Description: Returns True if the current node has both children
        Usage: <node>.hasBothChildren()
        """
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """
        Description: Returns true if the current node is a leaf node.
        Usage: <node>.isLeaf()
        """
        returnValue = False
        if (self._rChild == None and self._lChild == None):
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """
        Description: Returns true if the current node is a left child
        Usage: <node>.isLeftChild()
        """
        returnValue = False
        if (self._parent != None):
            if (self._parent._lChild is self):
                if (self._parent._rChild is not self):
                    returnValue = True
        return returnValue

    def isRightChild(self):
        """
        Description: Returns true if the current node is a right child
        Usage: <node>.isRightChild()
        """
        returnValue = False
        if (self._parent != None):
            if (self._parent._rChild is self):
                if (self._parent._lChild is not self):
                    returnValue = True
        return returnValue

    def isRed(self):
        """
        Description: Returns True if this node is red.
        Usage: <node>.isRed()
        """
        return self.color == True

    def isBlack(self):
        """
        Description: Returns True if this node is black.
        Usage: <node>.isBlack()
        """
        return self.color == False


class NilNode(RBNode):
    def __init__(self, parent):
        self._parent = None
        self._lChild = None
        self._rChild = None
        self.color = False
        self._value = None
        self._key = None

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes.
        Usage: node1 == node2
        """
        if (other == None or type(other) == NilNode):
            return True
        else:
            return False

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes.
        Usage: node1 != node2
        """
        if (other != None or type(other) != NilNode):
            return True
        else:
            return False


# ===============================================================================

class RedBlackTree:
    """
    Description: A Red-Black Tree (RBT).

    """

    def __init__(self):
        """ The constructor for our RBT """
        self._root = None
        # Add any other instance variables you need.

    def _isValid(self, item):
        """
        Description: Checks to see if a tuple is valid
        Usage: (outside) <RBT>._isValid(item) (inside) self._isValid(item)
        """
        returnValue = True
        if (type(item) != tuple):
            returnValue = False
        elif (type(item[0]) != int):
            returnValue = False
        elif (len(item) != 2):
            returnValue = False
        return returnValue

    def _isRoot(self, node):
        """
        Description: This function returns true if the given node is the root.
        Usage: self._isRoot(node)
        """
        return node is self._root

    def _isEmpty(self):
        """
        Description: This method returns true if the tree is empty, else False.
        """
        return self._root == None

    def _rbTransplant(self, u, v):
        """
        Description: A pretty straightforward implementation of RB-Transplant from ch. 12 pg. 323 of the book.
        """
        if (u._parent == None):
            self._root = v
        elif (u.isLeftChild()):
            u.getParent().setLChild(v)
        else:
            u.getParent().setRChild(v)
        if (v != None):
            v.setParent(u.getParent())

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                     of the tree according to the specified mode
        """
        self.output = ""
        if (type(mode) == str):
            if (mode == "in-order"):
                self.inorder(self._root)
            elif (mode == "pre-order"):
                self.preorder(self._root)
            elif (mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "ERROR: Unrecognized mode..."
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if (node != None):
            self.inorder(node.getLChild())
            color = "red" if (node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if (node != None):
            color = "red" if (node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if (node != None):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            color = "red" if (node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "

    def _findMinimum(self, node):
        """
        Description: Finds the successor of the current node and returns it.
        Usage: self._findMinimum(<RBNode>)
        """
        min = node
        while (min.hasLeftChild()):
            min = min.getLChild()
        return min

    def _findNode(self, id):
        """
        Description: Finds node in tree with given id,
                     returns corresponding ticket. Returns False if unsuccessful.
        """
        currentNode = None
        if (type(id) == int):
            currentNode = self._root
            while (currentNode != None and currentNode.getKey() != id):
                if (id < currentNode._key):
                    currentNode = currentNode.getLChild()
                else:
                    currentNode = currentNode.getRChild()
        return currentNode if (currentNode != None) else False

    def insert(self, item):
        """
        Description: Inserts given tuple into the tree while
                     preserving binary tree property.
                     Returns True if successful, False otherwise
                     See ch. 12 pg. 315 of the book
        """
        ret = False
        if (self._isValid(item)):
            z = RBNode(item)
            ret = True
            y = None
            x = self._root
            while (x != None):
                y = x
                if (z < x):
                    x = x.getLChild()
                else:
                    x = x.getRChild()
            z.setParent(y)
            if (y == None):
                self._root = z
            elif (z < y):
                y.setLChild(z)
            else:
                y.setRChild(z)
            z.setLChild(None)
            z.setRChild(None)
            z.setRed()
            self._insertFixup(z)
        return ret

    def _addTemp(self, CN, parent, flag):
        if (CN == None):
            CN = NilNode(parent)
            if (flag):
                parent.setRChild(CN)
            else:
                parent.setLChild(CN)
        return CN

    def _remTemp(self, CN):
        parent = CN.getParent()
        if (type(parent) == RBNode):
            if (CN.isRightChild()):
                parent.setRChild(None)
            else:
                parent.setLChild(None)
        CN.setParent(None)

    def find(self, id):
        """
        Description: Finds node in tree with given id,
                     returns corresponding ticket. Returns False if unsuccessful.
        """
        ret = False
        if (self._root == None):
            raise TreeIsEmpty("ERROR: Cannot find any nodes in an empty tree.\n")
        if (type(id) == int):
            result = self._findNode(id)
            if (type(result) == RBNode):
                ret = result.getValue()
        return ret

    def _rightRotate(self, currentNode):
        """ perform a right rotation from a given node"""
        lChild = currentNode.getLChild()
        grChild = lChild.getRChild()
        parent = currentNode.getParent()

        currentNode.setLChild(grChild)
        if (grChild != None):
            grChild.setParent(currentNode)

        lChild.setParent(parent)
        if (parent == None):
            self._root = lChild
        elif (currentNode.isRightChild()):
            parent.setRChild(lChild)
        else:
            parent.setLChild(lChild)

        lChild.setRChild(currentNode)
        currentNode.setParent(lChild)

    # ====================== IMPLEMENT THE METHODS BELOW ============================

    def _leftRotate(self, currentNode):
        """
        Description:  this method performs a left rotation from a given node
        Input: a RBT node.
        """
        rChild = currentNode.getRChild()
        parent = currentNode.getParent()
        left_rChild = rChild.getLChild()


        currentNode.setRChild(left_rChild)
        if (left_rChild != None):
            left_rChild.setParent(currentNode)

        rChild.setParent(parent)
        if (parent == None):
            self._root = rChild
        elif (currentNode.isLeftChild()):
            parent.setLChild(rChild)
        else:
            parent.setRChild(rChild)

        rChild.setLChild(currentNode)
        currentNode.setParent(rChild)


    def _insertFixup(self, z):
        """
        Description: This method fix up the tree to the RBT order after insert.
        Input: A RBT node z in the tree
        """
        p=z.getParent()

        while p!= None and p.isRed():
            gp = p.getParent()

            if gp !=None:
                if p.isLeftChild():
                    y=gp.getRChild()
                    if y!=None and y.isRed():
                        p.setBlack()
                        y.setBlack()
                        gp.setRed()
                        z = gp
                    else:
                        if z.isRightChild():
                            self._leftRotate(p)
                        p.setBlack()
                        gp.setRed()
                        self._rightRotate(gp)
                else:
                    y = gp.getLChild()
                    if y !=None and y.isRed():
                        p.setBlack()
                        y.setBlack()
                        gp.setRed()
                        z=gp
                    else:
                        if z.isLeftChild():
                            self._rightRotate(p)
                        p.setBlack()
                        gp.setRed()
                        self._leftRotate(gp)
            p = z.getParent()
        self._root.setBlack()

