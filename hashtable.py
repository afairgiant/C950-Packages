# Hashtable class with Chaining
"""
Create and search a hash table of packages. The hash table is sized at start by passed variable
"""
# Set debug mode for print statements
Debug = False


class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.

    def __init__(self, initial_capacity):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        self.table = [[] for _ in range(initial_capacity)]

    # Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if Debug:
            print(f"    DEBUG: Inserting item with key {key} into bucket {bucket}")

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        if Debug:
            print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    def print_table(self):
        # Debug Printing after inserting into buckets
        for index, bucket in enumerate(self.table):
            if bucket:  # If the bucket is not empty
                print(f"Bucket {index}: {bucket}")
            else:
                print(f"Bucket {index}: Empty")
