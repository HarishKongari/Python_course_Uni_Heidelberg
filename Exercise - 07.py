#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage für Übungsblatt 07

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
# ÜBUNGSBLATT 07 AUFGABE 1 UND 2
########################################################################


def calculate_digit_sum(number):
    """Calculate digit sum for number

    Every single digit of a number is added. The sum is the digit sum
    of that number.

:param number: Positive integer
    :type number: int
:return: Digit sum of number
:rtype: int
"""
    # try-expect block beginning
    try:
        number_as_string = str(number)
        digit_sum = 0
        for digit_as_string in number_as_string:
            digit = int(digit_as_string)
            digit_sum = digit_sum + digit
        return digit_sum
    # except block to avoid ValueError caused by negative number in this case
    except ValueError:
        return None

########################################################################
# ÜBUNGSBLATT 07 AUFGABE 3
########################################################################


def repetitive_digit_sum_iterative(number):
    """Repetitively calculate digit sum

    Repeat the calculation of the digit sum by using the previously
    calculated digit sum as the new number. In the end, only one digit
    is left.

    :param number: Positive integer
    :type number: int
    :return: Final digit of repetitive calculation of digit sum
    :rtype: int
    """
    digit_sum = number
    while digit_sum > 9:
        digit_sum = calculate_digit_sum(digit_sum)
    return digit_sum


def repetitive_digit_sum_recursive(number):
    """Calculates the Quersum of the given number until it is
    a single digit number, the process is done with recursion function which
    calls itself until the output is single digit"""
    if isinstance(number, int):
        if len(str(number)) == 1:
            return number
        elif len(str(number)) > 1 and isinstance(number, int):
            number = calculate_digit_sum(number)
            return repetitive_digit_sum_recursive(number)
        else:
            return None
    else:
        return None

########################################################################
# ÜBUNGSBLATT 07 AUFGABE 4
########################################################################

########################################################################
# TESTS
########################################################################


if __name__ == "__main__":
    # Aufgabe 2:
    print("\nAufgabe 2:\n")
    print("\nAntwort 2:\n")
    print("The Quersum of 5237 is", calculate_digit_sum(5237))
    print("The Quersum of -5237 is", calculate_digit_sum(-5237))
    # Aufgabe 3:
    print("\nAufgabe 3:\n")
    print("\nAntwort 3:\n")
    print("The iterative digit sum is", repetitive_digit_sum_iterative(5237))
    print("The recursive digit sum is", repetitive_digit_sum_recursive(5237))
    # Aufgabe 4:
    print("\nAufgabe 4:\n")
    print("\nAntwort 4:\n")
    #convert_raw_data("raw_data.csv", "digit_sums.csv")
