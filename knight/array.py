from __future__ import annotations
from knight import Value, Stream, Literal, RunError, String
from typing import Optional
import re
import math

class Array(Literal[list]):
	"""
	The number class in Knight.

	As per the Knight specs, the only number type within Knight is
	integral numbers. As such, we use Python's builtin `int` class.
	"""
	REGEX: re.Pattern = re.compile(r'^@')

	@classmethod
	def parse(cls, stream: Stream) -> Optional[Array]:
		"""
		Parses a List out from the stream.

		This returns `None` if the stream doesn't start with a digit.
		"""
		if match := stream.matches(Array.REGEX):
			return cls([])
		return None

	def __str__(self) -> str:
		return self.join('\n')

	def __iter__(self):
		return iter(self.data)

	def __repr__(self) -> str:
		return repr(self.data)

	def __add__(self, rhs: Value) -> Array:
		# """ Converts `rhs` to an `int` and adds it to `self.` """
		return Array(list(self) + list(rhs))

	def __mul__(self, rhs: Value) -> Array:
		# """ Converts `rhs` to an `int` and multiples it by it `self.` """
		return Array(list(self) * int(rhs))

	def __pow__(self, rhs: Value) -> Array:
		# """
		# Converts `rhs` to an `int` and exponentiates `self` by it, with
		# the power ofoperation conforming to the Knight specs.
		# """
		return String(self.join(str(rhs)))

	def join(self, sep: str) -> str:
		return sep.join(map(str, self.data))

	def __lt__(self, rhs: Value) -> bool:
		""" Checks to see if `self` is numerically less than `rhs`. """
		return list(self) < list(rhs)

	def __gt__(self, rhs: Value) -> bool:
		""" Checks to see if `self` is numerically greater than `rhs`. """
		return list(self) > list(rhs)
