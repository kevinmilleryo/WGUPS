#Hash Map
class HashTable:
    # Initialize buckets in the hash table
    def __init__(self, initial_length=10):
        self.map = []
        for i in range(initial_length):
            self.map.append([])

    # Hash function
    def create_hash(self, key):
        hash_value = hash(key) % len(self.map)
        return hash_value

    # Add or update an entry in hash table
    def insert(self, key, value):
        # Find the bucket using the hash value of the key
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        # Search to see if the key exists
        for i in range(len(bucket_list)):
            # If the key exists, update the associated value
            if bucket_list[i][0] == key:
                bucket_list[i][1] = value
                return
        # insert the key-value pair if key doesn't exist
        bucket_list.append([key, value])

    # Search for key within hash table
    def search(self, key):
        # Find bucket using key
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        # Search for key and return value
        for i in range(len(bucket_list)):
            if bucket_list[i][0] == key:
                value = bucket_list[i][1]
                return value
        return None