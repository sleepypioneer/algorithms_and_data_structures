# Associative arrays / maps / dictionaries

"""
- Abstract data types (contains specification only)
- Key value pairs, where each key is unique (appears only once)
- Most of the time we implement them with hashtable but binary search trees can be used as well
- Aim to reach O(1) time complexity for most of the operations
- we can achieve O(1) running time complexity for insertion and retrieval with perfect hash function
Operations:
    - add
    - remove
    - update
    - lookup (search)
    ** Sorting is not supported! (no order is defined) **


Hashtable & dictionaries
    - using an array as a base implementation and the indices as the keys we can do operations very quick O(1)
    - hash functions allow us to map keys to indices
        - distributes the keys UNIFORMLY into buckets
        - n: number of keys
        - m: number of buckets
        - h(x) = n % m
        - we use the modulo operator to check that the index is within the range
        - We have to use prime numbers
        - For string keys we could calculate the ASCII value for each character, add them up
    - Collision (items assigned same index)
        - chaining: store both values at the same bucket using linked lists
            - if there are many collisions O(1) complexity gets worst (could end up with only linked list
            - requires more memory
        - open addressing: generate a new index for the second item
            - linear probing: we check the next slot, then the next, then the next
            - quadratic probing: we try in 1,2,4,8 slots from the original
            - rehashing: we hash the results again

    |           | Average case  | Worst Case    |
    |-----------|---------------|---------------|
    | Space     | O(N)          | O(N)          |
    | Insert    | O(1)          | O(N)          |
    | Delete    | O(1)          | O(N)          |
    | Search    | O(1)          | O(N)          |

    ** we have to make sure the algorithms used for hashing and handling collisions are efficient to avoid worst case **

Load factor: number of entries divided by the number of slots/buckets    n
                                                                         -
If approx 1 the array is nearly full, performance decreases              m
    and operations are slow (many possible collisions)
If the load factor is approx 0 the array is nearly empty (a lot of memory is wasted)
** Sometimes dynamic resizing is needed **

In python when 66% of the array is full we have to resize the underlying array structure. Resizing takes O(N)
We can NOT just copy items across as we have to rehash them because hashing is reliant on the hashtable size

Application:
    - databases
    - counting given word occurrence
    - storing data + lookup tables (password checks etc)
    - substring search (Rabin-karp algorithm)

"""


class HashTable:

    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, data):

        index = self.hash_function(key)

        # not None -> it is a collision !!
        while self.keys[index] is not None:
            if self.keys[index] == key: # we want to update
                self.values[index] = data
                return

            # open addressing to try find another slot with linear probing
            index = (index+1)%self.size

        # insert
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):

        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key: # we want to update
                return self.values[index]

            index = (index+1)%self.size  # perhaps we shifted the index due to a collision

        return None  # key is not present in the associative array

    # returns an integer (index of the array slot)
    # we can take the ASCII value for each character
    # sum them up and use modulo operator (to normalize it)
    def hash_function(self, key):
        sum_of_characters = 0
        for pos in range(len(key)):
            sum_of_characters = sum_of_characters + ord(key[pos])

        return sum_of_characters % self.size


table = HashTable()
table.put("apple", 20)
table.put("orange", 10)
table.put("lemons", 15)
table.put("peanuts", 30)

print(table.get("lemons"))


# Creating dictionaries in python

dictionary = {'Joe': 14, 'Jill': 39, 'Vanessa': 21}

print(dictionary['Joe'])  # O(1) if hash function is efficient

# update
dictionary['Joe'] = 15

print(dictionary['Joe'])  # Hashtable / dictionary: O(1)  arrays: O(N) BST: O(logN)

# remove all entries
# dictionary.clear()

# delete dictionary
# del dictionary

# get all key value pairs
print(dictionary.items())

# get all the keys
print(dictionary.keys())

# get all the values
print(dictionary.values())

# ** order between dict.values() and dict.keys() may be different!!! No order is maintained

