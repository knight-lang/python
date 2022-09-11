from __future__ import annotations
from knight import Value, Stream, RunError
from typing import Union, Dict
import re

_ENV: Dict[str, Value] = {}

class Variable(Value):
	"""
	Represents an Variable within Knight.

	Because all Variables in Knight are global---and don't go out of
	scope---we have a single dict that keeps track of _all_ Variables.
	"""

	REGEX: re.Pattern = re.compile(r'[a-z_][a-z0-9_]*')
	name: str

	@classmethod
	def parse(cls, stream: Stream) -> Union[None, Variable]:
		"""
		Parses an Variable out from the stream.

		This returns `None` if the stream doesn't start with a lowercase
		letter, or an underscore.
		"""
		if match := stream.matches(Variable.REGEX):
			return cls(match)

	def __init__(self, name: str):
		""" Creates a new Variable associated with the given `name`. """
		self.name = name

	def __repr__(self) -> str:
		""" Gets a debugging mode representation of this Variable. """
		return f"Variable({self.name})"

	def run(self) -> Value:
		"""
		Fetches the value associated with this Variable from the list
		of known Variables.

		If the Variable has not been assigned yet (cf `assign`), then a
		`RunError` will be raised.
		"""
		if self.name not in _ENV:
			raise RunError(f"unknown Variable '{self.name}'")
		return _ENV[self.name]

	def assign(self, value: Value):
		"""
		Associated the Value `value` with this Variable.

		Any previously associated value with this Variable is discarded.
		"""
		_ENV[self.name] = value
