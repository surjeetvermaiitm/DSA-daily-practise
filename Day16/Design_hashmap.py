#Link: https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.n=20
        self.my_map=[[] for _ in range(self.n)]
        

    def put(self, key: int, value: int) -> None:
        h=key%self.n
        index=-1
        for i in range(len(self.my_map[h])):
            if self.my_map[h][i][0]==key:
                index=i
        if index!=-1:
            self.my_map[h].pop(index)
        self.my_map[h].append([key,value])
        

    def get(self, key: int) -> int:
        h=key%self.n
        
        for k,v in self.my_map[h]:
            if k==key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        h=key%self.n
        index=-1
        for i in range(len(self.my_map[h])):
            if self.my_map[h][i][0]==key:
                index=i
        if index!=-1:
            self.my_map[h].pop(index)
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class MyHashMap:

    def __init__(self):
        self.n=20
        self.my_map=[[] for _ in range(self.n)]
        

    def put(self, key: int, value: int) -> None:
        h=key%self.n
        # index=-1
        for i in range(len(self.my_map[h])):
            if self.my_map[h][i][0]==key:
                self.my_map[h][i][1]=value
                return
                # index=i
        # if index!=-1:
        #     self.my_map[h].pop(index)
        self.my_map[h].append([key,value])
        

    def get(self, key: int) -> int:
        h=key%self.n
        
        for k,v in self.my_map[h]:
            if k==key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        h=key%self.n
        index=-1
        for i in range(len(self.my_map[h])):
            if self.my_map[h][i][0]==key:
                index=i
        if index!=-1:
            self.my_map[h].pop(index)
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)