import pytest
from project import show_products, show_macros, _calculate_bmr, _get_nested_val, main
from project import *


def test_main(monkeypatch):
    # monkeypatch the "input" function, so that it returns "suggest".
    # This simulates the user entering any of the availabl commands in the terminal:
    monkeypatch.setattr("builtins.input", lambda _: "show products")

    # using input() like you normally would:
    i = input("What do you want the program to do? ")
    assert i == "show products"

    monkeypatch.setattr("builtins.input", lambda _: "show macros")

    i = input("What do you want the program to do? ")
    assert i == "show macros"

    monkeypatch.setattr("builtins.input", lambda _: "show specifics")

    i = input("What do you want the program to do? ")
    assert i == "show specifics"

    monkeypatch.setattr("builtins.input", lambda _: "calculate bmr")

    i = input("What do you want the program to do? ")
    assert i == "calculate bmr"

    monkeypatch.setattr("builtins.input", lambda _: "suggest")

    i = input("What do you want the program to do? ")
    assert i == "suggest"

def test_show_products():
    show_products()

def test_show_macros(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "banana")

    i = input("Enter the name of a product: ")
    assert i == "banana"

def test_get_nested_val():
    ...

def test_calculate_bmr():
    ...
