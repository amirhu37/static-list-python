# Make Static List
import numpy as np
from types import Any
from _collections_abc import dict_items, dict_keys, dict_values
from collections.abc import Iterator


class static_list(list):

    def __init__(self, volume: int) -> None:
        self.volume = volume
        self.x = list()
        pass
    def __str__(self) -> str:
        return f"{self.x}"
    def __repr__(self) -> str:
        return f"static_list({self.x})"
    def __iter__(self) -> Iterator:
        return self.x.__iter__()
    
    def __len__(self) -> int:
        return len(self.x)
    
    def append(self, value : Any , sorted : bool = False):
        if len(self.x) == self.volume:
            self.x.append(  value )
            self.x.pop(0)
            self.x.sort(reverse = True) if sorted else None
        else :
            self.x.append(  value )
            self.x.sort(reverse = True) if sorted else None
        self.__repr__()
        pass
      
    def to_list(self) -> list:
        return self.x
    def to_numpy(self) -> np.ndarray :
        return np.array(self.x)


class static_dict(dict):

    def __init__(self, volume: int) -> None:
        self.volume = volume
        self.solution = dict()
        pass
    def __str__(self) -> str:
        return f"{self.solution}"
    def __repr__(self) -> str:
        return f"static_dict({self.solution})"
    def keys(self) -> dict_keys:
        return list(self.solution.keys())
    def values(self) -> dict_values:
        return list(self.solution.values())
    def items(self) -> dict_items:
        return list(self.solution.items())
    def __iter__(self) -> Iterator:
        return self.solution.__iter__()
    
    def add(self, value : tuple):
        if len(self.solution) == self.volume:
            self.solution[value[0]] =  value[1]
            self.solution.pop( list(self.solution.keys()) [0])
        else :
            self.solution[value[0]] =  value[1]

        self.__repr__()
        pass