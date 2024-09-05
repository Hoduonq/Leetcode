class Node(object):
        def __init__(self, val, min):
            self.val = val
            self.min = min

    def __init__(self):
        self.top_node = None
        self.stack = []

    def push(self, val):
        if self.top_node is None or val < self.top_node.min:
            node = self.Node(val=val, min=val)
        else:
            node = self.Node(val=val, min=self.top_node.min)
        self.top_node = node
        self.stack.append(node)
        
    def pop(self):
        self.stack.pop()
        if self.stack:
            self.top_node = self.stack[-1]
        else:
            self.top_node = None
        
    def top(self):
        if self.top_node is None:
            return None
        else:
            return self.top_node.val
        
    def getMin(self):
        if self.top_node is None:
            return None
        else:
            return self.top_node.min