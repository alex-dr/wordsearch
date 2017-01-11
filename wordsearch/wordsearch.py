#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
from string import rstrip
import sys


def generate_random_board(n=9):
    return [[choice('abcdefghijklmnopqrstuvwxyz')
             for _ in range(n)]
            for _ in range(n)]


def print_board(board):
    print('---' + '--'*len(board[0]))
    print('\n'.join(map(lambda x: '| ' + ' '.join(x) + ' |', board)))
    print('---' + '--'*len(board[0]))


def read_board(content):
    """Read a board that was loaded with file.readlines()."""
    return map(lambda x: x.rstrip().split(' '), content)


def longest_string(board, row, col, drow, dcol, acc):
    """Find the longest string extending in the (drow, dcol) direction.

    Returns list of tuples (char, row, col).
    """
    if row < 0 or col < 0:
        return acc
    try:
        acc.append((board[row][col], row, col))
    except IndexError:
        return acc

    return longest_string(board, row + drow, col + dcol, drow, dcol, acc)


def find_longest_word(valid_words, candidate):
    if not candidate:
        return None

    test_string = ''.join(x[0] for x in candidate)

    if test_string in valid_words:
        return candidate

    else:
        return find_longest_word(valid_words, candidate[:-1])


def add_word_to_board(word, new_board):
    for char, row, col in word:
        new_board[row][col] = char


def update_board(valid_words, board, new_board, row, col):
    """Update the new board with any words found at this position.

    Parameters
    ----------
    valid_words: set
        Set of valid words
    board: list(list(char))
        Reference to the static board data.
    new_board: list(list(char))
        Mutable board to which we add our new words
    row: int
        Row index (first index into boards)
    col: int
        Column index (second index)

    Side Effects
    ------------
    Updates new_board with new words.
    """
    for drow in [-1, 0, 1]:
        for dcol in [-1, 0, 1]:
            if not (drow == 0 and dcol == 0):
                candidate = longest_string(board, row, col, drow, dcol, [])
                word = find_longest_word(valid_words, candidate)
                if word is not None and len(word) >= 4:
                    print('found word: {}'.format(''.join(x[0] for x in word)))
                    add_word_to_board(word, new_board)


def solve_board(valid_words, board):
    width = len(board[0])
    height = len(board)

    new_board = [[' ' for _ in range(width)] for _ in range(height)]

    for row in range(height):
        for col in range(width):
            update_board(valid_words, board, new_board, row, col)

    return new_board


def main(valid_words, *args):
    board = generate_random_board(n=15)
    print_board(board)

    solved_board = solve_board(valid_words, board)

    print_board(solved_board)


if __name__ == '__main__':
    with open('words.txt', 'rb') as words_file:
        valid_words = set(map(rstrip, words_file.readlines()))

    main(valid_words, sys.argv)
