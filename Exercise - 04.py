#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BITTE EN_DE UND TEXT NICHT VERÃ„NDERN
EN_DE = {
    "King": "König",
    "Knight": "Ritter",
    "Dragon": "Drache",
    "Aaaarrggh": "Aaaarrggh"
}

TEXT = "Der König ist da! Der Drache Aaaarrggh ist beim König. " \
       "Ritter Bedevere scheint auch da zu sein. Er hilft Arthur " \
       "dabei, das Monster zu besiegen."

##############################################################################
# LÃ–SUNG AUFGABE 1
##############################################################################

def translate(input_string: str, translations: dict) -> str:
    if input_string in translations:
        print(EN_DE[input_string])
    else:
        print(input_string)
        
#Aufgabe 1: Antwort:
#In [7]: translate("King", EN_DE)
#König      
        
#In [8]: translate("Monster", EN_DE)
#Monster

##############################################################################
# LÃ–SUNG AUFGABE 2
##############################################################################

def inverse_dict(input_dict: dict) -> dict:
    global newDict
    newDict = {val:key for (key, val) in input_dict.items()}
    
     
    print(newDict)
    
#Aufgabe 2: Antwort: 
#In [4]: inverse_dict(EN_DE)
#{'König': 'King', 'Ritter': 'Knight', 'Drache': 'Dragon', 'Aaaarrggh': 'Aaaarrggh'}
   
##############################################################################    
#LOESUNG AUFGABE 3: ##########################################################
##############################################################################

#Parametername in Funktion und Parametername in function body muss gleich sein,
#weil es wichtig ist, falls wir mehrere Dictionaries in diesem Fall haben. Wenn 
#wir in newDict die Funktion nur fuer EN_DE schreiben wuerden, koennten wir 
#keine andere Dictionaries oeffnen. Es wuerde immer, unabhaengig davon,welche 
#Name von Dictionary wir in "print" eingeben, den Inhalt von Dictionary EN_DE
#anzeigen
    

##############################################################################
# LÃ–SUNG AUFGABE 4
##############################################################################

punctuation_marks = ["?", "!", ".", ":", ",", ";", "…"]

    
punctuation_marks = ["?", "!", ".", ":", ",", ";", "…"]

    
def tokenize_text(text: str) -> list:
    for i in punctuation_marks:
        text = text.replace(i,"")
    global splitted_text   
    splitted_text = text.split()
    print(splitted_text)
    
#Aufgabe 4: Antwort:
#In [3]: tokenize_text(TEXT)
#['Der', 'König', 'ist', 'da', 'Der', 'Drache', 'Aaaarrggh', 'ist', 'beim', 
# 'König', 'Ritter', 'Bedevere', 'scheint', 'auch', 'da', 'zu', 'sein', 'Er', 
#'hilft', 'Arthur', 'dabei', 'das', 'Monster', 'zu', 'besiegen']
 

##############################################################################
# LÃ–SUNG AUFGABE 5
##############################################################################

def get_translated_mentions(text: str, input_dict: dict) -> list:
    new_list = []
    for a in splitted_text:
        if a in newDict :
            new_list.append(newDict[a])
            
            
            
            
    print(new_list)

#Aufgabe 5: Antwort:

#In [97]: get_translated_mentions(TEXT, EN_DE)
#['King', 'Dragon', 'Aaaarrggh', 'King', 'Knight']
##############################################################################
# LÃ–SUNG AUFGABE 6
##############################################################################
def perfect_number(a):
    sum = 0
    if a==0:
        sum = 1
    
    else:
        for x in range(1, a):
            if (a% x == 0) and (a>0):
                sum += x
            
        
            
    print(sum ==a)

#Aufgabe 6: Antwort:
#In [4]: perfect_number(28)
#True

#In [5]: perfect_number(3)
#False
