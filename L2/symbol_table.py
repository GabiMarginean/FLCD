# 1b

def h(id):
	return sum(map(ord, id))


class SymbolTable:
	def __init__(self, n = 100):
		self._n = n
		self._data = [[] for i in range(self._n)]

		for i in range(self._n):
			self._data[i] =  []

	def pos(self, identifier):
		hval = h(identifier) // self._n
		bucket = self._data[hval]

		if identifier in bucket:
			return (hval, bucket.index(identifier))
		else:
			bucket.append(identifier)
			return (hval, len(bucket) - 1)

	def get(self, i1, i2):
		return self.get((i1,i2))

	def get(self, idx):
		try:
			return self._data[idx[0]][idx[1]]
		except IndexError:
			return None
		except TypeError:
			print("Index must be touple.")
			return None

	def __str__(self):
		return "".join('{} -> {}\n'.format(i, bucket) for i, bucket in enumerate(self._data) if bucket)
    

