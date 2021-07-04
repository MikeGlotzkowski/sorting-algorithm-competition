from logging import Logger
from typing import List


class Solver(object):

    def __init__(self, logger, riddle):
        self._logger: Logger = logger
        self._riddle = riddle

    def solve(self):
        array: List[int] = (
            self._riddle
            .decode('utf-8')
            .split(',')
        )
        array = [int(numeric_string) for numeric_string in array]
        array.sort()
        return array
