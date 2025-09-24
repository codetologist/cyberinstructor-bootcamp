# Simple Hashing Example in Python
# Step 1: Define a hash function
# We'll use a simple hash function: value modulo table size
def simple_hash(key, table_size):
    return key % table_size
    # 5 %10 = 5
    # 10% 10 = 0
    # 11%10 = 1
    # Step 2: Create a hash table with chaining to handle collisions
def create_hash_table(size):
# Each slot will hold a list to handle collisions
    return [[] for _ in range(size)]
    # Step 3: Insert a value into the hash table
def insert(hash_table, key, value):
    index = simple_hash(key, len(hash_table))
    print(f"Inserting ({key}, {value}) at index {index}")
    # Check if key already exists and update
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
        return
    # If not, append the key-value pair
    hash_table[index].append([key, value])
# Step 4: Search for a value by key
def search(hash_table, key):
    index = simple_hash(key, len(hash_table))
    print(f"Searching for key {key} at index {index}")
    for pair in hash_table[index]:
        if pair[0] == key:
            print(f"Found value: {pair[1]}")
            return pair[1]
    print("Key not found")
    return None

# Step 5: Demonstrate the hash table
hash_table = create_hash_table(10)
# Insert some key-value pairs
insert(hash_table, 1, "Alice")
insert(hash_table, 2, "Bob")
insert(hash_table, 3, "Charlie")
insert(hash_table, 5, "David")
insert(hash_table, 6, "Alice2")
insert(hash_table, 7, "Bob2")
insert(hash_table, 8, "Charlie2")
insert(hash_table, 9, "David2")
print("\nHash Table State:")
for i, bucket in enumerate(hash_table):
    print(f"Index {i}: {bucket}")
print("\nSearch Examples:")
search(hash_table, 2) # Should find Bob
search(hash_table, 5) # Should find David
search(hash_table, 0) # Should report not found