import unittest
from collections import Counter
import string
from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):
    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))

    # 2. Czy przekroczenie maksymalnej liczby znalezionych produktów powoduje rzucenie wyjątku?
    def test_get_entries_return_error_too_many_products(self):
        products = [Product('PP12', 1), Product('PP234', 2), Product('PP235', 1), Product('PP123', 1)]
        for server_type in server_types:
            server = server_type(products)
            with self.assertRaises(TooManyProductsFoundError, msg=' ') as cm:
                entries = server.get_entries(2)
            self.assertEqual(' ', cm.exception.msg)


class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))

    # 3a. Czy funkcja obliczająca łączną cenę produktów zwraca poprawny wynik w przypadku rzucenia wyjątku?
    def test_total_price_throw_error(self):
        products = [Product('PP12', 1), Product('PP234', 2), Product('PP235', 1), Product('PP123', 1)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))

    # 3b. Czy funkcja obliczająca łączną cenę produktów zwraca poprawny wynik w przypadku braku produktów pasujących
    # do kryterium wyszukiwania?
    def test_total_price_no_suitable_products(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(1))


class ListServerTest(unittest.TestCase):
    # 1. Czy wyniki zwrócone przez serwer przechowujący dane w liście są poprawnie posortowane?
    def test_get_entries_properly_sorted(self):
        products = [Product('PP234', 4), Product('PP235', 3)]
        list_server = ListServer(products)
        entries = list_server.get_entries(2)
        self.assertEqual([products[1], products[0]], entries)


if __name__ == '__main__':
    unittest.main()
