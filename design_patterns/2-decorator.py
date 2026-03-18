#!/usr/bin/env python3
from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self) -> int: ...

    @abstractmethod
    def description(self) -> str: ...


class Coffee(Beverage):
    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class MilkDecorator(Beverage):
    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    # Inner is the "order stack" which "composes"
    #   the base beverage which client started to ask
    #   as well as any already added "options"
    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    # Since we implement "cost" method the same way as all other decorators
    #   by first calling the "Inner Beverage's method" THEN adding "our own"
    #   cost on top this technically creates a "call stack" kinda similar to
    #   a weird intermediate between a recursive algorithm and a chained list.
    # Let's say "a call stack constituted from parsing a chain of objects".
    def cost(self) -> int:
        return self._inner.cost() + 15

    # Same logic here
    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main() -> None:
    cup1 = MilkDecorator(Coffee())
    print(cup1.description(), cup1.cost())

    cup2 = MilkDecorator(SugarDecorator(Coffee()))
    print(cup2.description(), cup2.cost())

    # That client is a real gourmet so (s)he wants EVERYTHING at once!
    # Technically this is the same as "reusing cup2" like so
    # final_cup = CaramelDecorator(cup2)
    cup3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    # Detailed "call chain" for each method
    # Phase 1 "Construct call stack"
    # Caramel -> Milk -> Sugar -> Coffee... No inner object left!
    # Phase 2: resolve each call in reverse order
    # For cost this would be equal to
    # get coffee price then add each option's cost by request order.
    print(cup3.description(), cup3.cost())


if __name__ == "__main__":
    main()
