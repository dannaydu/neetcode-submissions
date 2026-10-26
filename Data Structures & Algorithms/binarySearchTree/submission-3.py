class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None
    


    def insert(self, key: int, val: int) -> None:
        new = TreeNode(key, val)

        if self.root == None:
            self.root = new
            return

        curr = self.root

        while True:
            #key is less than
            if curr.key > key:
                if curr.left == None:
                    curr.left = new
                    return
                curr = curr.left
            # more
            elif curr.key < key:
                if curr.right == None:
                    curr.right = new
                    return
                curr = curr.right
            else:
                curr.value = val
                return



    def get(self, key: int) -> int:
        
        curr = self.root

        while curr:
            #key is less than
            if curr.key == key:
                return curr.value
            elif curr.key > key:
                curr = curr.left
            # more
            elif curr.key < key:
                curr = curr.right
        
        return -1



    def getMin(self) -> int:
        if self.root == None:
            return -1
        
        curr = self.root

        while True:
            if curr.left:
                curr = curr.left
            else:
                return curr.value



    def getMax(self) -> int:
        if self.root == None:
            return -1
        
        curr = self.root

        while curr.right:
            curr = curr.right
        
        return curr.value


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None
        
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.value = minNode.value
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node  


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
    
    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

