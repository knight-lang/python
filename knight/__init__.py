from knight.stream import Stream
from knight.error import Error, RunError, ParseError
from knight.value import Value

from knight.literal import Literal
from knight.null import Null
from knight.list import List
from knight.boolean import Boolean
from knight.number import Number
from knight.string import String
from knight.variable import Variable
from knight.function import Function

def run(stream: str) -> Value:
	value = Value.parse(Stream(stream))

	if value is None:
		raise ParseError('Nothing to parse.')

	return value.run()

