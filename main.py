class FlatIterator:
	def __init__(self, n_list):
		self.f_list = []
		for item in n_list:
			for item_item in item:
				self.f_list.append(item_item)

	def __iter__(self):
		return self

	def __next__(self):
		if not self.f_list:
			raise StopIteration
		return self.f_list.pop(0)


class FlatIterator2:
	def flat(self, n_list):
		for item in n_list:
			if type(item) == list:
				self.flat(item)
			else:
				self.f_list.append(item)

	def __init__(self, n_list):
		self.f_list = []
		self.flat(n_list)

	def __iter__(self):
		return self

	def __next__(self):
		if not self.f_list:
			raise StopIteration
		return self.f_list.pop(0)


def flat_generator(n_list):
	for item in n_list:
		for item_item in item:
			yield item_item


def flat_generator_2(n_list):
	for item in n_list:
		if type(item) == list:
			for item_item in flat_generator_2(item):
				yield item_item
		else:
			yield item


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[], [],
	[1, 2, None]
]

nested_list_2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[[10, 11, 12, [13, 14, [15], 16], 17], [18, 19, [20]]],
	21, [],
	[1, 2, None]
]

for item in FlatIterator(nested_list):
	print(item)
print()

print([item for item in FlatIterator(nested_list)])
print()

for item in flat_generator(nested_list):
	print(item)
print()

print(nested_list)
print([item for item in FlatIterator(nested_list)])
print([item for item in FlatIterator2(nested_list)])
print([item for item in flat_generator_2(nested_list)])
print()
print(nested_list_2)
print([item for item in FlatIterator2(nested_list_2)])
print([item for item in flat_generator_2(nested_list_2)])
print()

for item in flat_generator_2(nested_list_2):
	print(item)
print()
