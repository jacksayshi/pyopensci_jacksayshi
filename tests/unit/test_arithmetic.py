"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from pyospackage_jacksayshi.arithmetic import add_numbers, sub_numbers

def test_add_numbers_1():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_add_numbers_2():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(10, -6)
    expected_out = 4
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_sub_numbers_1():
    """
    Test that sub_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = sub_numbers(6, 3)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_sub_numbers_2():
    """
    Test that sub_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = sub_numbers(6, "")
    expected_out = 6
    assert  out == expected_out, f"Expected {expected_out} but got {out}"