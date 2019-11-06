
"""Vorlage für Übungsblatt 08

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
# ÜBUNGSBLATT 08 AUFGABE 1
########################################################################


def contains_letter(text: str, letter: str) -> bool:
    """
    The function checks contains_letter(text: str, letter: str), if the letter
    is present in the text given. For this to be done "re" module was used,
    re module helps in working with regular expressions, before using
    re.search() function we use re.compile() function which helps to do
    various operations such as searching for pattern matches or performing
    string substitutions. And then re.search() function is used to check
    search for letter in text. If the output is search is None then it
    results Boolean False, if the letter is found in text then it gives
    boolean True as output.
    """
    import re
    pattern = re.compile(letter)
    result = pattern.search(text)
    if result is None:
        return False
    else:
        return True

########################################################################
# ÜBUNGSBLATT 08 AUFGABE 2
########################################################################


def read_file(filename: str) -> list:
    """
    The function "read_file(filename: str) -> list:", in this case outputs the
    give text file into list according to line wise, even the line breaks are
    removed and each list element contains exactly one line. To do this task,
    firstly the text file must be opened as a readable file and each line is
    added into the list with "lines.append()" function. To remove the line
    breaks "each_line.rstrip()" function is used and the list is returned
    as output of the function.
    """
    lines = []
    with open(filename, "r") as text:
        for each_line in text:
            lines.append(each_line.rstrip())
        return lines

########################################################################
# ÜBUNGSBLATT 08 AUFGABE 3
########################################################################


def remove_punctuation(sentence_list: list) -> list:
    """
    The function "remove_punctuation(sentence_list: list) -> list:", in this
    case gives a list which was created in the
    "read_file(filename: str) -> list:" function and removes the
    punctuations from the list of multiple items and gives output of cleaned
    list after removing punctuations. For doing this two modules "re" and
    "string" are imported and an empty list new_sentence is created.
    sentence_new_list uses re.compile(), re.escape() and string.punctuation
    which helps in removal of punctuations.
    With the help of "for" loop we remove punctuations from each list item
    and save it in the empty list "new_sentence" and use .append() for adding
    all the list items without punctuations.
    """
    import re
    import string
    new_sentence = []
    sentence_new_list = re.compile("[" + re.escape(string.punctuation) + "]")
    for line_by_line in sentence_list:
        new_sentence.append(sentence_new_list.sub("", line_by_line))
    return new_sentence

########################################################################
# ÜBUNGSBLATT 08 AUFGABE 4
########################################################################


def count_speech(sentence_list: list) -> dict:
    """
    The function "count_speech(sentence_list: list) -> dict:" helps in
    counting the number of occurances of the keys in the dictionary "result".
    From the list which was created in "read_file(filename: str) -> list:"
    occurances must be counted and the dict "result" must be returned as
    output.
    In order to calculate this "re" library was imported and with the help
    of "for" loops, the dict "result" and list of "sentence_list" were
    accessed and then with re.findall() function the matching was done
    and then was counted with a count "variable" and occurances were given to
    respective dict "result" to count them.
    """
    import re
    result = {
        "Arthur": 0,
        "Soldier #1": 0,
        "Soldier #2": 0
    }
    for name in result:
        count = 0
        for line_by_line in sentence_list:
            new_name = name.upper()
            if re.findall(new_name, line_by_line):
                count = count + 1
        result[name] = count
    return result

########################################################################
# ÜBUNGSBLATT 08 AUFGABE 5
########################################################################

def logging_examples():
    """
    this function logging_examples() helps to show the use of logging module,
    instead of using print() function to display everything this with
    level. With this one can get information what one needs with Level and
    Value of level.
    """
    import logging
    logging.basicConfig(filename='Beispiel.log', level=logging.DEBUG,
                        format='%(message)s')
    logging.info("Es geht los mit Loglevel 20")
    logging.debug("Vielleicht ein Problem mit Loglevel 10")
    logging.error("Leider ein Fehler mit Loglevel 40")

########################################################################
# TESTS
########################################################################


if __name__ == "__main__":
    print("\nAufgabe 1:\n\nDocString 1:")
    print(contains_letter.__doc__)
    print("\nAntwort 1:\n")
    print(contains_letter("Monty Python", "y"))
    print(contains_letter("Monty Python", "x"))
    print("\nAufgabe 2:\n\nDocString 2:")
    print(read_file.__doc__)
    print("\nAntwort 2:\n")
    holy_grail_lines = read_file("holy_grail.txt")
    print(holy_grail_lines)
    print("\nAufgabe 3:\n\nDocString 3:")
    print(remove_punctuation.__doc__)
    print("\nAntwort 3:\n")
    print(remove_punctuation(holy_grail_lines))
    print("\nAufgabe 4:\n\nDocString 3:")
    print(count_speech.__doc__)
    print("\nAntwort 4:\n")
    print(count_speech(holy_grail_lines))
    print("\nAufgabe 5:\n\nDocString 3:")
    print(logging_examples.__doc__)
    logging_examples()
