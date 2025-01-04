from __future__ import annotations
from knight import Value, Stream, Literal
from typing import Optional
import re

class Boolean(Literal[bool]):
	""" Used to represent boolean types within Knight. """

	REGEX: re.Pattern = re.compile(r'([TF])[A-Z]*')

	@classmethod
	def parse(cls, stream: Stream) -> Optional[Boolean]:
		""" Parses a `Boolean` if the stream starts with `T` or `F`. """
		if match := stream.matches(Boolean.REGEX, 1):
			return cls(match == 'T')
		return None

	def __str__(self) -> str:
		""" Returns `"true"` when true and `"false"` when false. """
		return 'true' if self else 'false'

	def __iter__(self):
		""" Returns `"true"` when true and `"false"` when false. """
		if self:
			yield self

	def __lt__(self, rhs: Value) -> bool:
		""" Checks to see if `self` is falsey and `rhs` is truthy. """
		return bool(not self and rhs)

	def __gt__(self, rhs: Value) -> bool:
		""" Checks to see if `self` is truthy and `rhs` is falsey. """
		return bool(self and not rhs)
