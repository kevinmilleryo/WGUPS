#Hash Map
class HashMap:
    # Initialize the buckets in the hash table
    def __init__(self, initial_length=10):
        self.map = []
        for i in range(initial_length):
            self.map.append([])

    # Hash function
    def create_hash(self, key):
        hash_value = hash(key) % len(self.map)
        return hash_value

    # Add or update an entry into the hash table
    def insert(self, key, value):
        # Find the bucket using the hash value of the key
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        # Search through hash to see if key exists
        for i in range(len(bucket_list)):
            # If the key exists, update the associated value
            if bucket_list[i][0] == key:
                bucket_list[i][1] = value
                return
        # insert the key-value pair
        bucket_list.append([key, value])

    # Search for key in hash table
    def search(self, key):
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        for i in range(len(bucket_list)):
            if bucket_list[i][0] == key:
                value = bucket_list[i][1]
                return value
        return None