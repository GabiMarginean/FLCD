# Symbol Table

> Uses a list of lists to create a HashTable. 
Each list has assigned to it a empty list (bucket) which will contain 
all the elements whose hash value (h(x)) is equal to the index of the corresponding list

### Interface: 
-	#### `constructor: ST(n : int)`
	 where n is the initial capacity of the HashTable

-	#### `pos(identifier : string) -> touple (x, y)`
	Returns the position of an identifier in the HashTable if it exists, otherwise it inserts it and returns the position

-	#### `get(id : touple) -> string`
	Returns the value associated to a position or `None` if no value exists at the corresponding position

### Hash function:
-	#### `h(identifier : str) -> int`
	The hash function returns the sum of the ASCII codes corresponding to all the characters in the identifier