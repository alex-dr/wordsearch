#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from random import choice
from string import rstrip
import sys


LONGEST_WORD_LENGTH = 22


def generate_random_board(n=9):
    return [[choice('abcdefghijklmnopqrstuvwxyz')
             for _ in range(n)]
            for _ in range(n)]


def print_board(board):
    print('---' + '--'*len(board[0]))
    print('\n'.join(map(lambda x: '| ' + ' '.join(x) + ' |', board)))
    print('---' + '--'*len(board[0]))


def print_words(words):
    def print_word(word):
        print(''.join(zip(*word)[0]))
    for word in words:
        print_word(word)


def read_board(content):
    """Read a board that was loaded with file.readlines()."""
    return map(lambda x: x.rstrip().split(' '), content)


def longest_string(board, row, col, drow, dcol, acc):
    """Find the longest string extending in the (drow, dcol) direction.

    Returns list of tuples (char, row, col).
    """
    if row < 0 or col < 0:
        return acc

    if len(acc) > LONGEST_WORD_LENGTH:
        return acc

    try:
        acc.append((board[row][col], row, col))
    except IndexError:
        return acc

    return longest_string(board, row + drow, col + dcol, drow, dcol, acc)


def find_longest_word(valid_words, candidate, min_word_length):
    if len(candidate) < min_word_length:
        return None

    test_string = ''.join(x[0] for x in candidate)

    if test_string in valid_words:
        return candidate

    else:
        return find_longest_word(valid_words, candidate[:-1], min_word_length)


def add_word_to_board(word, new_board):
    for char, row, col in word:
        new_board[row][col] = char


def update_board(valid_words, board, new_board, row, col, min_word_length):
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
    min_word_length: int
        Smallest word to find

    Side Effects
    ------------
    Updates new_board with new words.
    """
    words = []
    for drow in [-1, 0, 1]:
        for dcol in [-1, 0, 1]:
            if not (drow == 0 and dcol == 0):
                candidate = longest_string(board, row, col, drow, dcol, [])
                word = find_longest_word(valid_words, candidate, min_word_length)
                if word is not None and len(word) >= min_word_length:
                    words.append(word)
                    add_word_to_board(word, new_board)
    return words


def solve_board(valid_words, board, min_word_length):
    width = len(board[0])
    height = len(board)

    new_board = [[' ' for _ in range(width)] for _ in range(height)]

    words = []
    for row in range(height):
        for col in range(width):
            words += update_board(valid_words, board, new_board, row, col, min_word_length)

    return new_board, words


def main(valid_words, args):
    parser = argparse.ArgumentParser(
        description='Generate a random wordsearch and solve it')

    parser.add_argument('--board-size', type=int, default=15,
                        help='Number of rows and columns')
    parser.add_argument('--min-word-length', type=int, default=4,
                        help='Smallest words to find')
    parser.add_argument('--just-show-words', action='store_true',
                        help='Only return found words')

    args = parser.parse_args()

    board = generate_random_board(n=args.board_size)

    if not args.just_show_words:
        print_board(board)

    solved_board, words = solve_board(valid_words, board, args.min_word_length)

    if args.just_show_words:
        print_words(words)
    else:
        print_board(solved_board)
        print_words(words)


if __name__ == '__main__':
    with open('words.txt', 'rb') as words_file:
        valid_words = set(map(rstrip, words_file.readlines()))

    main(valid_words, sys.argv)
