#!/usr/bin/python

class IterableEx(object):
	"""
	 Iterables return the next object in the list
	"""

	def __init__(self, n):
		self.sequence = range(0, n)

	def __iter__(self):
		return iter(self.sequence)

class IteratorEx(object):
	"""
	Iterators implement the next() method
	"""

	def __init__(self, n):
		self.sequence = range(0, n)

	def __iter__(self):
		self.i = 0
		return self

	def next(self):
		if self.i >= len(self.sequence):
			raise StopIteration, "Reached end of sequence"
		else:
			tmp = self.sequence[i]
			self.i += 1
			return tmp

"""
Usage:
	a = IteratorEx(4)
	b = IterableEx(4)

	print iter(a)
	print iter(b)

	print 3 in a
	print filter(lambda x: x < 2, b)
"""

