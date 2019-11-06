#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage für Übungsblatt 09

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu
den einzelnen Aufgaben des Übungsblatts. Im letzten Abschnitt können
Sie unter dem `if __name__ == "__main__"` statement Beispielaufrufe
Ihrer Funktionen einfügen und so ausprobieren, ob Ihre Implementation
funktioniert und die erwarteten Ergebnisse liefert. Es sind bereits
einige (noch auskommentierte) Tests angegeben. Bitte fügen Sie Ihre
Testaufrufe nur dort hinzu und nicht in die Blöcke der Aufgaben - dort
sollen nur die Funktionen stehen.

Falls Sie uns diese Datei per E-Mail zukommen lassen, stellen Sie
bitte sicher, dass die Datei vorher entsprechend der geforderten
Abgabeformalia umbenannt wurde.
"""

########################################################################
# VORGEGEBENER CODE (HIER NICHTS VERÄNDERN)
########################################################################

EXAMPLE_GRID_1 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

EXAMPLE_GRID_2 = [
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [2, 0, 2, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 2],
    [1, 2, 2, 1, 0, 2, 1]
]

EXAMPLE_GRID_3 = [
    [2, 2, 1, 1, 2, 2, 2],
    [2, 1, 2, 2, 1, 1, 1],
    [1, 2, 1, 2, 1, 2, 2],
    [2, 1, 2, 1, 1, 1, 2],
    [1, 2, 2, 1, 2, 1, 2],
    [1, 1, 2, 2, 1, 1, 1]
]

EXAMPLE_GRID_4 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [1, 2, 2, 2, 2, 1, 2],
    [1, 1, 2, 1, 1, 2, 2],
    [2, 1, 2, 2, 1, 2, 1]
]

EXAMPLE_GRID_5 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 2, 0],
    [0, 0, 1, 0, 0, 2, 2],
    [0, 1, 1, 1, 0, 2, 1],
    [1, 2, 1, 2, 2, 1, 2]
]

EXAMPLE_GRID_6 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0],
    [2, 0, 1, 2, 2, 0, 0],
    [2, 1, 2, 1, 1, 0, 2],
    [1, 2, 1, 1, 2, 1, 1]
]

EXAMPLE_GRID_7 = [
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [1, 2, 2, 2, 0, 2, 0],
    [1, 2, 2, 2, 0, 2, 2],
    [2, 1, 2, 2, 1, 1, 1],
    [1, 2, 1, 1, 2, 1, 2]
]


def clear_screen():
    """Clear screen

    Depending on the user's terminal window configuration, there might
    still be output from previous operations visible on the screen. To
    clear the screen, 100 newline characters will be printed.
    """
    print("\n" * 100)


def player_has_won(grid):
    """Find out if the grid contains a winning combination

    To win, four adjacent spaces have to be occupied by the same
    player. They count as adjacent if they are aligned diagonally,
    horizontally or vertically.
    """
    row_count = len(grid)
    column_count = len(grid[0])
    for row_number in range(row_count):
        for column_number in range(column_count):
            if grid[row_number][column_number] == 0:
                continue
            four_in_a_row = map(all_elements_equal, [
                get_four_horizontal(row_number, column_number, grid),
                get_four_vertical(row_number, column_number, grid),
                get_four_diagonal_up(row_number, column_number, grid),
                get_four_diagonal_down(row_number, column_number, grid)
            ])
            if any(four_in_a_row):
                return True
    return False


def game_loop():
    """Run the game loop

    As long as the loop runs, players can select columns to occupy
    spaces. The loop will exit once the grid is full or a player wins
    the game.
    """
    grid = empty_grid()
    player = None
    while True:
        clear_screen()
        print_grid(grid)
        if grid_is_full(grid):
            print("It's a draw!")
            break
        if player_has_won(grid):
            print("Player {} has won!".format(player))
            break
        player = next_player(player)
        player_choice(player, grid)

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 1
########################################################################


def empty_grid():
    """
    Here when one calls the function empty_grid() we have to get an output of
    list with 6 rows and 7 columns which looks like
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
    so we call it from the given list from above
    """
    return EXAMPLE_GRID_1

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 2
########################################################################


def print_grid(grid):
    """
    In the function print_grid(grid) we have to display the 7 columns of the
    list, when the value is "0" then an empty space must be shown, when value
    is 1 it means player 1, must be shown by "X" symbol and when value is 2, it
    means player 2 and must be shown as "O" symbol and also indicate each row.
    """
    for row in grid:
        print("| ", end="")
        for space in row:
            if space == 1:
                print("X ", end="")
            elif space == 2:
                print("O ", end="")
            else:
                print("  ", end="")
        print("| ", end="")
        print("\n")
    print("+---------------+\n")
    print("  1 2 3 4 5 6 7  ")

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 3
########################################################################


def get_column(column_number, grid):
    """
    In the function get_column(column_number, grid), one should extract the
    column which is called and return the column elements as the answer.
    """
    column_elements = []
    for row in grid:
        column_elements.append(row[column_number])
    return column_elements

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 4
########################################################################


def free_space(column_number, grid):
    """
    In the function free_space(column_number, grid), one should check if the
    column in the particular list is not empty, that is with a value of "O",
    if no value in that particular column is "0" then the output is "None",
    else the output must the index of the first occured "0" from bottom.
    """
    try:
        column = get_column(column_number, grid)
        column.reverse()
        index_list = column.index(0)
        return 5 - index_list
    except ValueError:
        return None

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 5
########################################################################


def grid_is_full(grid):
    """
    In the function grid_is_full(grid), one checks if there is any empty space
    in the total list given, that is if there is any "0" present then we have
    to return the value as "False" else the value returned must be "True"
    """
    grid_value = []
    column_count = len(grid[0])
    for column_number in range(column_count):
        grid_value.append(free_space(column_number, grid))
    count_none = grid_value.count(None)
    if count_none == 7:
        return True
    else:
        return False

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 6
########################################################################


def drop_disc(column_number, player, grid):
    """
    In the function drop_disc(column_number, player, grid), we call function
    free_space, in free_space if we get "None", then it means no value is
    empty, when it is so then the returned value must be "False", if there
    is empty space then the return value must be "True".
    """
    row_number = free_space(column_number, grid)
    if row_number is None:
        return False
    else:
        return True

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 7
########################################################################


def get_four_diagonal_up(row_number, column_number, grid):
    # For function `get_four_diagonal_up` we might produce negative
    # list indices which are not allowed but don't raise `IndexError`.
    # Hint: This is not necessary for `get_four_diagonal_down`,
    # `get_four_horizontal` or `get_four_vertical` because all
    # indices will be equal or greater than `row_number`.
    if row_number - 3 < 0:
        return None
    try:
        return [
            # We want four spaces diagonally adjacent to the given
            # coordinates in `row_number` and `column_number`. For
            # each additional space we have to walk up a row (subtract
            # 1 for each row) and walk one column to the right (add
            # 1 for each column).
            grid[row_number][column_number],
            grid[row_number - 1][column_number + 1],
            grid[row_number - 2][column_number + 2],
            grid[row_number - 3][column_number + 3]
        ]
    except IndexError:
        return None


def get_four_diagonal_down(row_number, column_number, grid):
    if row_number - 3 >= 0:
        return None
    try:
        return [
            # TODO
            grid[row_number][column_number],
            grid[row_number + 1][column_number + 1],
            grid[row_number + 2][column_number + 2],
            grid[row_number + 3][column_number + 3]
        ]
    except IndexError:
        return None


def get_four_horizontal(row_number, column_number, grid):
    if (row_number < 0 or row_number >= 6) or (column_number > 3):
        return None
    try:
        return [
            # TODO
            grid[row_number][column_number],
            grid[row_number][column_number + 1],
            grid[row_number][column_number + 2],
            grid[row_number][column_number + 3]
        ]
    except IndexError:
        return None


def get_four_vertical(row_number, column_number, grid):
    if (row_number > 2) or (column_number < 0 or column_number > 6):
        return None
    try:
        return [
            # TODO
            grid[row_number][column_number],
            grid[row_number + 1][column_number],
            grid[row_number + 2][column_number],
            grid[row_number + 3][column_number]
        ]
    except IndexError:
        return None

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 8
########################################################################


def all_elements_equal(sequence):
    """
    In the function all_elements_equal(sequence), one should check if all
    the elements in sequence as similar, if they are similar then "True" must
    be returned else a "False" must be returned.
    """
    try:
        check_sequence = []
        count_sequence = len(sequence)
        for count in range(count_sequence):
            if sequence[0] == sequence[count]:
                check_sequence.append(sequence[0])
        if sequence == check_sequence:
            return True
        else:
            return False
    except TypeError:
        return False

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 9
########################################################################


def next_player(player):
    """
    In the function next_player(player), if the value of player is 1, then
    the returned value is 2 else the returned value is 1.
    """
    if player is 1:
        return 2
    else:
        return 1

########################################################################
# ÜBUNGSBLATT 09 AUFGABE 10
########################################################################


def player_choice(player, grid):
    try:
        print("Next disc: Player {}".format(player))
        while True:
            player_input_str = input("Which column? ")
            # Convert input to integer
            player_input_int = int(player_input_str)
            # List index starts at 0, so we have to subtract 1
            column_number = player_input_int - 1
            # Drop disc into selected column
            if not drop_disc(column_number, player, grid):
                print("Can not drop disc there")
                continue
            # No errors occurred, so we can break the loop
            break
    except IndexError:
        return None

########################################################################
# TESTS
########################################################################

            
if __name__ == "__main__":
    
    print("\nAufgabe 1:\n\nDocString 1:")
    print(empty_grid.__doc__)
    print(empty_grid())

    print("\nAufgabe 2:\n\nDocString 2:")
    print(print_grid.__doc__)
    print_grid(EXAMPLE_GRID_1)
    print_grid(EXAMPLE_GRID_2)
    print_grid(EXAMPLE_GRID_3)

    print("\nAufgabe 3:\n\nDocString 3:")
    print(get_column.__doc__)
    print(get_column(0, EXAMPLE_GRID_3))

    print("\nAufgabe 4:\n\nDocString 4:")
    print(free_space.__doc__)
    print(free_space(1, EXAMPLE_GRID_2))
    print(free_space(2, EXAMPLE_GRID_2))

    print("\nAufgabe 5:\n\nDocString 5:")
    print(grid_is_full.__doc__)
    print(grid_is_full(EXAMPLE_GRID_1))
    print(grid_is_full(EXAMPLE_GRID_2))
    print(grid_is_full(EXAMPLE_GRID_3))

    print("\nAufgabe 6:\n\nDocString 6:")
    print(drop_disc.__doc__)
    print(drop_disc(2, 1, EXAMPLE_GRID_2))
    print("\nEXAMPLE_GRID_2 vorher:\n")
    print_grid(EXAMPLE_GRID_2)
    print(drop_disc(1, 1, EXAMPLE_GRID_2))
    print("\nEXAMPLE_GRID_2 hinterher:\n")
    print_grid(EXAMPLE_GRID_2)

    print("\nAufgabe 7:\n")
    print(player_has_won(EXAMPLE_GRID_1))
    print(player_has_won(EXAMPLE_GRID_2))
    print(player_has_won(EXAMPLE_GRID_3))
    print(player_has_won(EXAMPLE_GRID_4))
    print(player_has_won(EXAMPLE_GRID_5))
    print(player_has_won(EXAMPLE_GRID_6))
    print(player_has_won(EXAMPLE_GRID_7))

    print("\nAufgabe 8:\n\nDocString 8:")
    print(all_elements_equal.__doc__)
    print(all_elements_equal([1, 2, 3]))
    print(all_elements_equal(None))
    print(all_elements_equal([1, 1, 1]))
    print(all_elements_equal([True, True, True]))
    print(all_elements_equal([False, False, False]))

    print("\nAufgabe 9:\n\nDocString 9:")
    print(next_player.__doc__)
    print(next_player(None))
    print(next_player(1))
    print(next_player(2))

    print("\nTest Aufgabe 10:\n")
    game_loop()
