# HashTable class
class HashTable():

    # Constructors
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    # Returns a hash value for key
    def _get_hash(self, key):
        return int(key) % self.size - 1

    # Adds a key-value pair to the hash table
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Gets a key-value pair from the hash table
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Deletes a key-value pair from the hash table
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # Prints HashTable
    def print(self):
        print('--- Packages ---')
        for item in self.map:
            if item is not None:
                print(f"Key: {item[0][0]}, Value: {str(item[0][1])}")