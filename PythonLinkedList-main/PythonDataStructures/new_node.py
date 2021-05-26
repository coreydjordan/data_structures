class New_Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = New_Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = New_Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_value(self, searched_val):
        if searched_val < self.data:
            if self.left is None:
                return str(searched_val) + " Not Found"
            return self.left.findval(searched_val)
        elif searched_val > self.data:
            if self.right is None:
                return str(searched_val) + " Not Found"
            return self.right.findval(searched_val)
        else:
            print(str(self.data) + ' is found')