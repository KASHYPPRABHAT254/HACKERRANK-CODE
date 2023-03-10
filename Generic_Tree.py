class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
    def newNode(data):
        temp = Node(data)
        return temp
    def constructor(list,n):
        root  = None
        stack = []
        for i in range(n):
            if(list[i]==-1):
                stack.pop()
            else:
                nodeN = Node(list[i])
                if(len(stack)>0):
                    stack[-1].children.append(nodeN)
                else:
                    root = nodeN
                root = nodeN
        return root
        
