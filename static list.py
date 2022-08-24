class static_list:
    def __init__(self, index: int) -> None:
        self.x = [None for _ in range(index)]
    def add(self,idx, value):
        try:
            self.x.insert(idx, value )
            self.x.pop(value)
            return self.x
        except:
            raise ValueError ("add faild. index out of reserved places")
    def delete(self, value):
        try:
            self.x.pop(value)
            return self.x
        except:
            raise ValueError ("delete failde, maybe value does not exsist")