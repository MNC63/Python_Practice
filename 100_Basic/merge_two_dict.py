"""
Merge two dictionary into a new dictionary
"""
from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class DictMerger:
    d1: Dict[Any, Any] = field(default_factory=dict)
    d2: Dict[Any, Any] = field(default_factory=dict)

    def merge(self) -> Dict[Any, Any]:
        """Return a new dict with d1 and d2 merged"""
        return {**self.d1, **self.d2}

    def display(self):
        print(f"Merged dict: {self.merge()}")


def main():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}

    merger = DictMerger(d1, d2)
    merger.display()


if __name__ == "__main__":
    main()
