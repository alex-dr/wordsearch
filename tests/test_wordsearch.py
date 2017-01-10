#!/usr/bin/env python
from wordsearch.wordsearch import (
    find_longest_word,
    longest_string,
    add_word_to_board,
    update_board
)


TEST_BOARD = [
    ['f', 'o', 'o'],
    ['b', 'a', 'r'],
    ['x', 'x', 'b']
]

TEST_WORDS = {
    'foo',
    'fab'
}


def test_find_longest_word():
    valid_words = {'foo'}
    candidate = [('f', 0, 0), ('o', 0, 0), ('o', 0, 0), ('o', 0, 0)]
    assert find_longest_word(valid_words, candidate) == candidate[:-1]


def test_find_longest_word_bad():
    valid_words = {'foo'}
    candidate = [('o', 0, 0), ('o', 0, 0), ('o', 0, 0), ('o', 0, 0)]
    assert find_longest_word(valid_words, candidate) is None


def test_longest_string():
    board = [['a', 'b'],
             ['c', 'd']]
    assert longest_string(board, 0, 0, 0, 1, []) == [('a', 0, 0), ('b', 0, 1)]


def test_add_word_to_board():
    new_board = [[' ' for _ in range(2)] for _ in range(2)]
    word = [('a', 0, 0), ('b', 0, 1)]
    add_word_to_board(word, new_board)
    assert new_board == [['a', 'b'], [' ', ' ']]


def test_update_board():
    new_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    update_board(TEST_WORDS, TEST_BOARD, new_board, 0, 0)
    assert new_board == [['f', 'o', 'o'],
                         [' ', 'a', ' '],
                         [' ', ' ', 'b']]
