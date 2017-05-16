# -*- coding: utf-8 -*-
"""
Unit tests for the recursion sub-module
"""
from __future__ import division, print_function

from nose.tools import assert_equals
from nose.tools import raises
from python_examples import recursion  # pylint: disable=import-error


def test_recursion_fib_memo():
    """ fib_memo assertion tests"""
    assert_equals(recursion.fib_memo(2), 1)
    assert_equals(recursion.fib_memo(20), 6765)
    assert_equals(recursion.fib_memo(50), 12586269025)


@raises(TypeError, ValueError)
def test_recursion_fib_memo_raises():
    """ fib_memo raises tests"""
    recursion.fib_memo('foo')
    recursion.fib_memo(-1)


def test_recursion_permute():
    """ parmute assertion tests"""
    assert_equals(recursion.permute('abc'),
                  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert_equals(recursion.permute('dog'),
                  ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])
    assert_equals(recursion.permute('a'), ['a'])


@raises(TypeError, ValueError)
def test_recursion_permute_raises():
    """ permut raises tests"""
    recursion.permute(1234)


def test_reverse_string():
    """ reverse_string assertion tests"""
    assert_equals(
        recursion.reverse_string('hello'),
        'olleh')
    assert_equals(
        recursion.reverse_string('hello world'),
        'dlrow olleh')
    assert_equals(
        recursion.reverse_string('123456789'),
        '987654321')


@raises(TypeError)
def test_reverse_string_raises():
    """ test_reverse_string raises tests"""
    recursion.reverse_string(1234)


def test_recursion_word_split():
    """ word_split assertion tests"""
    assert_equals(recursion.word_split('themanran', ['the', 'ran', 'man']),
                  ['the', 'man', 'ran'])
    assert_equals(recursion.word_split('ilovedogsJohn',
                                       ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']),
                  ['i', 'love', 'dogs', 'John'])


def test_rec_fact():
    """ rec_fact assertion tests"""
    assert_equals(recursion.rec_fact(4), 24)


@raises(TypeError)
def test_rec_fact_raises():
    """ rec_fact_raises tests"""
    recursion.rec_fact('foo')


def test_rec_sum():
    """ rec_sum assertion tests"""
    assert_equals(recursion.rec_sum(4), 10)
    assert_equals(recursion.rec_sum(0), 0)


@raises(TypeError, ValueError)
def test_rec_sum_raises():
    """ rec_sum raises tests"""
    recursion.rec_sum(-4)
    recursion.rec_sum('foo')
    recursion.rec_sum('1000')


def test_rec_sum_digits():
    """ rec_sum_digits assertion tests"""
    assert_equals(recursion.rec_sum_digits(4321), 10)


@raises(TypeError)
def test_rec_sum_digits_raises():
    """ rec_sum_digits raises tests"""
    recursion.rec_sum_digits('foo')


if __name__ == '__main__':  # pragma: no cover
    pass
