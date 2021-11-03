#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price  # FIXME: zwróć odpowiednią wartość

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania

class AbstractServer:

    n_max_returned_entries: int = 3

    def __init__(self, products: List[Product]):
        pass

    def get_entries(self, lst: List[Product], n_letters: int) -> List[Product]:
        result = []
        for el in lst:
            if condition:  # TODO: UZUPELNIC CONDITION z n_letters
                result.append(el)
        return result # TODO: posortowac wg rosnacej ceny

    def get_all_products(self, lst: List[Product], n_letters: int):
        pass



class ListServer(AbstractServer):
    def __init__(self, products: List[Product]):
        super().__init__(self, products)
        self.products = products

    def get_all_products(self, lst: List[Product], n_letters: int):
        return get_entries(self.products)



class MapServer(AbstractServer):
    def __init__(self, products: List[Product]):
        super().__init__(self, products)
        self.products: Dict[str, Product] = {product.name: product for product in products}

    def get_all_products(self, lst: List[Product], n_letters: int):
        return get_entries(self.products.items(), n_letters)

class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, server: AbstractServer):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()


