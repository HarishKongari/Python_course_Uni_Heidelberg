#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from typing import Union  # für mehrere mögliche "type hints"-Angaben


"""Vorlage für Übungsblatt 06

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu
den einzelnen Aufgaben des Übungsblatts. Im letzten Abschnitt können
Sie unter der `if __name__ == "__main__"`-Bedingung Beispielaufrufe
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
# BITTE FOLGENDE OBJEKTE NICHT EDITIEREN
########################################################################


SNAKES = [
    ["Python", "Constriction"],
    ["Cobra", "Venom"],
    ["Rattlesnake", "Venom"],
    ["Boa", "Constriction"],
    ["Adder", "Constriction"]
]

CUSTOMER_EUROS = {
    "Charles": [27, 12],
    "Jacques": [31, 38]
}


########################################################################
# ÜBUNGSBLATT 06 AUFGABE 1  (1 Punkt)
########################################################################


def add_snake(snake: str, killing_method: str) -> list:
    SNAKES.append([snake, killing_method])
    return SNAKES





########################################################################
# ÜBUNGSBLATT 06 AUFGABE 2  (1 Punkt)
########################################################################

#
      
   
#def get_snakes_by_killing_method(killing_method: str, snake_list=[]) -> list:
    """
    Die Gefahr bei diesem Funktionskopf ist:
        Anstatt, 
        get_snakes_by_killing_method(killing_method: str, snake_list: list) -> list:
        schreiben wir,
        get_snakes_by_killing_method(killing_method: str, snake_list=[]) -> list:
            
            Die Fehler ist, das wir nennen die Variable Namens(snake_list)
            "Type" nicht, sondern geben wir diese parameter als leere list.
            
            Die Wert von parameter darf man nicht schon frueher schon in Funktionskopf
            eingeben.
    """
    
    


########################################################################
# ÜBUNGSBLATT 06 AUFGABE 3  (2 Punkte)
########################################################################


def get_snakes_by_killing_method(killing_method: str, snake_list: list):  # TODO: Verbessern
    for name in snake_list:
        if killing_method in name:
            print(name)
    


########################################################################
# ÜBUNGSBLATT 06 AUFGABE 4  (2 Punkte)
########################################################################


def factorial(number: Union[float, int]) -> Union[float, int]:
    """
    
def factorial(number: Union[float, int]) -> Union[float, int]:
    
    return number * factorial(number - 1)
    
    Wenn man so einem Code benutzt, bekommt man ein Fehler und kein Ergebnis:
        Es sieht so aus:
            ........
            ..........
            ............
            RecursionError: maximum recursion depth exceeded

In diesem Fall, benutzen wir Rekursion Funktion, d.h Funktion ruft sich selbst,
hier ist ein Stack overflow, weil Python beschraenkt Rekursionstiefe

In [12]: sys.getrecursionlimit()
Out[12]: 3000

hier gab es kein Limit, die Funktion will sich selbst fuer unendlich viele male
rufen.    

In verbesserte Code, solltet man nur Rekursive Funktion benutzen ohne Fehler 
und richtige Ergebnis zu erhalten

Auf diesem Grund, soll rekursion enden, wenn "number" 1 wird.
In diesem Code, nummern zwischen 0 und 2961 kann python factorial finden.  


    """
    
    if (number % 1 ==0) and (number <= 2961):   # checks if number is a whole number and limits recursion for only 2961 times because it calculates factorial in my python till 2961 times of recursion
        # checks if number is greater than or equal to 0 
        if number >=0 and number <= 2961:   
            
            if number == 1 or number == 0: # to limit recursion till number becomes 1 and to give factorial of 0 or 1
                return 1
            else:
                return number * factorial(number - 1) # calculates factorial
        elif number < 0: # to take only numbers greater than or equal to 0
            print("Please input a whole number greater than or equal to 0 and less than 2962 ")
    else:
        print("Please enter only whole numbers between 0 to 2961")


########################################################################
# ÜBUNGSBLATT 06 AUFGABE 5  (2 Punkte)
########################################################################


def euros_to_dollars(customers: dict) -> dict:
    """
    for name in customers:
        for index, euro in enumerate(customers[name]):
            customers[name][index] = euro * 1.5
    return customers
    
    Die Antwort was wir bekommen ist:
        
Rechnung in Währung Euro:
{'Charles': [40.5, 18.0], 'Jacques': [46.5, 57.0]}
Rechnung in Währung Dollar:
{'Charles': [40.5, 18.0], 'Jacques': [46.5, 57.0]}    
    
    Die Parameter in Funktionkopf behaltet Rechnung in Währung Euro, aber
    wenn spaeter uberschreiben wir "customers" mit Rechnung in Währung Dollar, 
    weil wir gleiche Name von Euro Wahrung hier benutzen, deswegen ist Wahrung
    mit Euro uberschrieben und bekommen wir obene Antwort
    
    
    Fuer verbesserung dieser Code sollen wir anderen Variable Name andern lassen, 
    damit wird Wahrung von Euro so gleich bleiben
    """
    for name in customers:
        for index, euro in enumerate(customers[name]):
            customers_dollars[name][index] = euro * 1.5
    return customers_dollars


########################################################################
# ÜBUNGSBLATT 06 AUFGABE 6  (2 Punkte)
########################################################################


def print_random_chess_position():
    
    """
    def print_random_chess_position():
    import random

    horizontal = list("ABCDEFGH")
    vertical = list("12345678")

    random = random.choice(horizontal) # Modulename als string gegeben
    print("Horizontal: {}".format(random))

    random = random.choice(vertical) # Modulname als string gegeben
    print("Vertikal: {}".format(random))
    
    In diesem Code bekommt man ein Fehler: 

    AttributeError: 'str' object has no attribute 'choice'

    dass heisst hier "modulename" (random) haben wir unvorsichtig überschrieben
    random module wurde importiert, allerdings ist es überschrieben, weil wir gleiche 
    Name wieder als "string" benutzt haben, deswegen erhaltet man ein Fehler.

    Immer muss man vorsichtig bei Namensräumen sein


    In verbesserte Code muss man anderen Namen als String geben, damit wir kein 
    Fehler bekommen."""
    
   

    
    import random

    horizontal = list("ABCDEFGH")
    vertical = list("12345678")

    random_horizontal = random.choice(horizontal) # change name of string
    print("Horizontal: {}".format(random_horizontal))

    random_vertical = random.choice(vertical) # change name of string
    print("Vertikal: {}".format(random_vertical))
    


########################################################################
# TESTS
########################################################################

if __name__ == "__main__":
    ####################################################################
    # Hier könnt Ihr Eure oben angepassten Funktionen testen.
    ####################################################################
    print("Aufgabe 1:\n" )
    print(add_snake("Black Mamba", "Venom"))
    # Aufgabe 1:
    #In [3]: add_snake("Black Mamba", "Venom")
    #Out[3]: 
    #[['Python', 'Constriction'],
    # ['Cobra', 'Venom'],
    # ['Rattlesnake', 'Venom'],
    # ['Boa', 'Constriction'],
    # ['Adder', 'Constriction'],
    # ['Black Mamba', 'Venom']]

    pass

   
    
    

    pass

    # Aufgabe 3:
    # ----------
    print("\nAufgabe 3:\n")
    
    get_snakes_by_killing_method("Venom", SNAKES)
    pass

    
    # Aufgabe 4:
    # ----------
    print("\nAufgabe 4:\n\nDocString 4:")
    
    print(factorial.__doc__)
    print("Fakultät von 3 ist:", factorial(3))
    print("Fakultät von 5 ist:", factorial(5))
    print("Fakultät von 10 ist:", factorial(10))
    

    # Aufgabe 5:
    # ----------
    print("\nAufgabe 5:\n\nDocString 5:\n")
    print(euros_to_dollars.__doc__)
    print("\nAntwort 5:\n")
    customers_dollars = euros_to_dollars(CUSTOMER_EUROS)
    print("Rechnung in Währung Euro:")
    print(CUSTOMER_EUROS)
    print("Rechnung in Währung Dollar:")
    print(customers_dollars)

    # Aufgabe 6:
    # ----------
    print("\nAufgabe 6:\n\nDocString 6:")
    
    print(print_random_chess_position.__doc__)
    print("\nAntwort 6:\n")
    print_random_chess_position()
    

