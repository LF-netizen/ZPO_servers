#!/usr/bin/python
# -*- coding: utf-8 -*-

import operator

from typing import Optional, List, Dict


class Product:
    @staticmethod
    def if_name_correct(name: str) -> None:
        name_letters = ''.join(el for el in name if 'a' <= el.lower() <= 'z')
        name_numbers = ''.join(el for el in name if '0' <= el <= '9')

        if name_numbers == '' or name_letters == '' or not name_letters + name_numbers == name:
            raise ValueError('Wrong name for object in class Product')

    def __init__(self, name: str, price: float) -> None:
        Product.if_name_correct(name)
        self.name = name
        self.price = price

    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str)
    #  i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu
    #  float)

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.price == other.price  # FIXME: zwróć odpowiednią wartość

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError(Exception):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    def __init__(self, msg=None) -> None:
        if msg is None:
            self.msg = ' '
        super().__init__()


# FIXME: Każda z poniższych klas serwerów powinna posiadać:
# (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z
# typem reprezentacji produktów na danym serwerze,
# (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną
# dopuszczalną liczbę wyników wyszukiwania,
# (3) możliwość odwołania się do metody `get_entries(self, n_letters) zwracającą listę produktów spełniających
# kryterium wyszukiwania

class AbstractServer:
    n_max_returned_entries: int = 3

    def __init__(self):
        pass

    @staticmethod
    def get_all_products(lst: List[Product], n_letters: int) -> List[Product]:
        result = []
        for el in lst:
            if (
                len(el.name) > n_letters + 1
                and 'a' <= el.name[n_letters - 1].lower() <= 'z'
                and '0' <= el.name[n_letters] <= '9'
                and 2 <= len(el.name) - n_letters <= 3
            ):
                result.append(el)

        if AbstractServer.n_max_returned_entries < len(result):
            raise TooManyProductsFoundError()
        return sorted(result, key=operator.attrgetter("price"))  # TODO: posortowac wg rosnacej ceny

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        pass


class ListServer(AbstractServer):
    def __init__(self, products: List[Product]) -> None:
        super().__init__()
        self.products = products

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        return self.get_all_products(self.products, n_letters)


class MapServer(AbstractServer):
    def __init__(self, products: List[Product]) -> None:
        super().__init__()
        self.products: Dict[str, Product] = {product.name: product for product in products}

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        return self.get_all_products([el[1] for el in self.products.items()], n_letters)


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, server: AbstractServer) -> None:
        self.server = server

    def get_total_price(self, n_letters: Optional[int] = 1) -> Optional[float]:
        try:
            lst_of_products = self.server.get_entries(n_letters)
        except TooManyProductsFoundError:
            return None
        if not lst_of_products:
            return None
        return sum([el.price for el in lst_of_products])
