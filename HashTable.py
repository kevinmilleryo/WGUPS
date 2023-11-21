# HashTable class
class HashTable:
    #initialize hash table with default capacity of 20
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])


#new item insertion
    def insert(self, key, item):
        #calculate hash of key
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

    #if key is already in bucket, update
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

    #if key is not in bucket, insert at the end of list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

#lookup items in the hash table
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

#remove item from hash table
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        #remove item if key is found
        if key in destination:
            destination.remove(key)
