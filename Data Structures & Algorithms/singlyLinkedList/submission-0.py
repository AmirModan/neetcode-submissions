class LinkedList:
    
    def __init__(self):
        self.ll = []
    
    def get(self, index: int) -> int:
        if len(self.ll) > index:
            return self.ll[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        self.ll.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.ll.append(val)

    def remove(self, index: int) -> bool:
        if len(self.ll) > index:
            self.ll.pop(index)
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        return self.ll
