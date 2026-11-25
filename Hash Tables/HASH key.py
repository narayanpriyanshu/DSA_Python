#size=7
prime_number=23
class HashTable:
    def __init__(self,size):
        self.data_map=[None]*size

    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash= (my_hash + ord(letter)*prime_number)%len(self.data_map)
        return my_hash

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,':',val)

    def set_item(self,key,value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]         #we create an array to avoid collisions i.e same index for 2 items
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range (len(self.data_map[index])):
                if self.data_map[index][i][0]==key:      #IMAGINE A MATRIX
                    return self.data_map[index][i][1]
        return None

    def get_key(self):
        all_keys=[]
        for i in range (len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
my_hash_table=HashTable(7)
# my_hash_table.print_table()

my_hash_table.set_item('Bolt',15)
my_hash_table.set_item('Washers',99)
my_hash_table.set_item('Nails',100)
# print("*"*10)
my_hash_table.print_table()

# print("*"*10)

print(my_hash_table.get_item('Nails'))
print(my_hash_table.get_item('Pri'))


print(my_hash_table.get_key())
