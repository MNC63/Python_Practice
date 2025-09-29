"""
Check two dictionaries is or not similar
"""
from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class DictEqual:
    dict1: Dict[Any, Any] = field(default_factory=dict)
    dict2: Dict[Any, Any] = field(default_factory=dict)

    def is_equal(self) -> bool:
        if self.dict1.keys() != self.dict2.keys():
            return False
        for k in self.dict1:
            if self.dict1[k] != self.dict2[k]:
                return False
        return True

    def display(self):
        print(f"Two dictionaries are equal: {self.is_equal()}")


def main():
    d1 = {"a": 1, "b": 3}
    d2 = {"b": 3, "a": 1}
    dict_equal = DictEqual(d1, d2)
    dict_equal.display()


if __name__ == "__main__":
    main()
