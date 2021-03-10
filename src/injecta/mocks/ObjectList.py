from typing import List
from injecta.mocks.Empty import Empty


class ObjectList:
    def __init__(self, objects: List[Empty], name: str = "my_name"):
        self.__name = name
        self.__objects = objects
