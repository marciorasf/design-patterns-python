from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    @abstractmethod
    def some_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def some_function_a(self) -> str:
        return "Product A1"


class ConcreteProductA2(AbstractProductA):
    def some_function_a(self) -> str:
        return "Product A2"


class AbstractProductB(ABC):
    @abstractmethod
    def some_function_b(self) -> str:
        pass

    @abstractmethod
    def another_function_b(self, collaborator: AbstractProductA) -> str:
        pass


class ConcreteProductB1(AbstractProductB):
    def some_function_b(self) -> str:
        return "Product B1"

    def another_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.some_function_a()
        return f"The result of the B1 collaborating with the {result}"


class ConcreteProductB2(AbstractProductB):
    def some_function_b(self) -> str:
        return "Product B2"

    def another_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.some_function_a()
        return f"The result of the B2 collaborating with the {result}"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.some_function_b()}")
    print(f"{product_b.another_function_b(product_a)}")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing client code with the second factory type:")
    client_code(ConcreteFactory2())
