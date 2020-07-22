#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
# ---- To-do List ---- #

# ---- ---- #

# ------ Begin Hash Table of Elements ------ #
hydrogen = {
    "name" : "H",
    "atoms" : 1,
    "needed" : 1,
    "ve" : 1,
    "halogen" : "false"
}
helium = {
    "name" : "He",
    "atoms" : 2,
    "needed" : 0,
    "ve" : 2,
    "halogen" : "false"
}
lithium = {
    "name" : "Li",
    "atoms" : 3,
    "needed" : 7,
    "ve" : 1,
    "halogen" : "false"
}
beryllium = {
    "name" : "Be",
    "atoms" : 4,
    "needed" : 6,
    "ve" : 2,
    "halogen" : "false"
}
boron = {
    "name" : "B",
    "atoms" : 5,
    "needed" : 5,
    "ve" : 3,
    "halogen" : "false"
}
carbon = {
    "name" : "C",
    "atoms" : 6,
    "needed" : 4,
    "ve" : 4,
    "halogen" : "false"
}
nitrogen = {
    "name" : "N",
    "atoms" : 7,
    "needed" : 3,
    "ve" : 5,
    "halogen" : "false"
}
oxygen = {
    "name" : "O",
    "atoms" : 8,
    "needed" : 2,
    "ve" : 6,
    "halogen" : "false"
}
fluorine = {
    "name" : "F",
    "atoms" : 9,
    "needed" : 1,
    "ve" : 7,
    "halogen" : "true"
}
neon = {
    "name" : "Ne",
    "atoms" : 10,
    "needed" : 0,
    "ve" : 8,
    "halogen" : "false"
}
sodium = {
    "name" : "Na",
    "atoms" : 11,
    "needed" : 7,
    "ve" : 1,
    "halogen" : "false"
}
magnesium = {
    "name" : "Mg",
    "atoms" : 12,
    "needed" : 6,
    "ve" : 2,
    "halogen" : "false"
}
aluminium = {
    "name" : "Al",
    "atoms" : 13,
    "needed" : 5,
    "ve" : 3,
    "halogen" : "false"
}
silicon = {
    "name" : "Si",
    "atoms" : 14,
    "needed" : 4,
    "ve" : 4,
    "halogen" : "false"
}
phosphorus = {
    "name" : "P",
    "atoms" : 15,
    "needed" : 3,
    "ve" : 5,
    "halogen" : "false"
}
sulfur = {
    "name" : "S",
    "atoms" : 16,
    "needed" : 2,
    "ve" : 6,
    "halogen" : "false"
}
chlorine = {
    "name" : "Cl",
    "atoms" : 17,
    "needed" : 1,
    "ve" : 7,
    "halogen" : "true"
}
argon = {
    "name" : "Ar",
    "atoms" : 18,
    "needed" : 0,
    "ve" : 8,
    "halogen" : "false"
}
bromine = {
    "name" : "Br",
    "atoms" : 35,
    "needed" : 1,
    "ve" : 7,
    "halogen" : "true"
}
iodine = {
    "name" : "I",
    "atoms" : 53,
    "needed" : 1,
    "ve" : 7,
    "halogen" : "true"
}
krypton = {
    "name" : "Kr",
    "atoms" : 36,
    "needed" : 0,
    "ve" : 8,
    "halogen" : "false"
}
xenon = {
    "name" : "I",
    "atoms" : 54,
    "needed" : 0,
    "ve" : 8,
    "halogen" : "false"
}
# ------ End Hash Table of Elements ------ #

# ------ Begin General Periodic Table ------ #
# Used to relate Element inputs to Hash Table Values
periodicTable = {
    "H" : hydrogen,
    "He" : helium,
    "Li" : lithium,
    "Be" : beryllium,
    "B" : boron,
    "C" : carbon,
    "N" : nitrogen,
    "O" : oxygen,
    "F" : fluorine,
    "Ne" : neon,
    "Na" : sodium,
    "Mg" : magnesium,
    "Al" : aluminium,
    "Si" : silicon,
    "P" : phosphorus,
    "S" : sulfur,
    "Cl" : chlorine,
    "Ar" : argon,
    "Br" : bromine,
    "I" : iodine,
    "Kr" : krypton,
    "Xe" : xenon
}

# ------ End General Periodic Table ------ #

# ---- Begin Functions ---- #

def checkInteger(case):
# Integer Check Function
    try:
        int(case)
        return True
    except:
        ValueError
        return False

def convertFormula(initialFormula):
# Convert any input into a readable array
# Array is all strings [Charge, Value, Element1, Element1Amount, Element2, Element2Amount, ..., ElementN, ElementNAmount]
    newFormula = []
    x = 0
    if initialFormula.find("^") == -1:
# Check for '^' symbol, when it does not exist then assign 0 to the charge in array
        newFormula.insert(0, 0)
        newFormula.insert(0, "Charge")
    while(x < len(initialFormula)):
        elementSymbol = initialFormula[x]
        if elementSymbol == "^":
# Check for current interated character for '^' symbol, assigns the correct charge to the array
            charge = assignCharge(initialFormula[x+1:])
            newFormula.insert(0, str(charge))
            newFormula.insert(0, "Charge")
            break
        elif elementSymbol.isupper():
# Check for Uppercase character        
            if initialFormula[x] == initialFormula[-1]:
# Check to see if formula ends in an Uppercase character and assigns an amount of 1 to the element
                newFormula.append(elementSymbol)
                newFormula.append("1")
            while(x < len(initialFormula)-1):
                if initialFormula[x+1] == "^":
# Check for '^' after an Uppercase character that ends element symbol
                    newFormula.append(elementSymbol)
                    break
                elif not initialFormula[x+1].isupper() and not initialFormula[x+1].isdigit():
# Check for lowercase letter and end the element symbol
                    elementSymbol += initialFormula[x+1]
                    newFormula.append(elementSymbol)
                    if (x+2 < len(initialFormula)-1):
# Check if last character and assign amount of 1                    
                        if initialFormula[x+2].isupper():
                            newFormula.append("1")
                            break
                    break
                elif initialFormula[x+1].isupper():
# Check if next character is Uppercase and assign amount of 1
                    newFormula.append(elementSymbol)
                    newFormula.append("1")
                    break
                else:
                    newFormula.append(elementSymbol)
                    break
        elif elementSymbol.isdigit():
# Check for a Digit character and ensure all following digits are accounted for
            while(x < len(initialFormula)-1):
                if initialFormula[x+1].isdigit():
                    elementSymbol += initialFormula[x+1]
                    x += 1
                else:
                    break
            newFormula.append(elementSymbol)
        x += 1
    if checkInteger(newFormula[len(newFormula)-1]) == False:
        newFormula.append("1")
    return newFormula

def generateHTMLFormula(formula):
# Used to apply all subscripts and superscripts to the formula to display in HTML
# Takes in formula as an array format
    htmlFormula = ""
    x = 2
    if formula[1] == 0:
        while(x < len(formula)):
            if formula[x].isdigit() and int(formula[x]) != 1:
                htmlFormula += "<sub>"
                htmlFormula += str(formula[x])
                htmlFormula += "</sub>"
                x += 1
            elif formula[x].isdigit() and int(formula[x]) == 1:
                x += 1
            else:
                htmlFormula += formula[x]
                x += 1
    else:
        while(x < len(formula)):
            if formula[x].isdigit() and int(formula[x]) != 1:
                htmlFormula += "<sub>"
                htmlFormula += str(formula[x])
                htmlFormula += "</sub>"
                x += 1
            elif formula[x].isdigit() and int(formula[x]) == 1:
                x += 1
            else:
                htmlFormula += formula[x]
                x += 1
        htmlFormula += "<sup>"
        if int(formula[1]) == -1:
            htmlFormula += "-"
        elif int(formula[1]) < -1:
            htmlFormula += str(int(formula[1]) * -1)
            htmlFormula += "-"
        else:
            htmlFormula += str(formula[1])
        htmlFormula += "</sup>"
    return htmlFormula

def assignCharge(input):
# Checks for the value and returns the charge
# Used for inputs after a '^' symbol
    charge = 0
    if input == "-":
        charge = -1
    if input == "2-":
        charge = -2
    if input == "3-":
        charge = -3
    if input == "4-":
        charge = -4
    if input == "5-":
        charge = -5
    if input == "6-":
        charge = -6
    if input == "7-":
        charge = -7
    if input == "8-":
        charge = -8
    if input == "+":
        charge = 1
    if input == "2+":
        charge = 2
    if input == "3+":
        charge = 3
    if input == "4+":
        charge = 4
    if input == "5+":
        charge = 5
    if input == "6+":
        charge = 6
    if input == "7+":
        charge = 7
    if input == "8+":
        charge = 8
    return charge

def getElementValues(element):
# Test script to return items from the hash table
# Unused
    elementDict = atoms = ve = needed = 0
    elementDict = periodicTable.get(element)
    atoms = elementDict.get("atoms")
    ve = elementDict.get("ve")
    needed = elementDict.get("needed")
    print(atoms)
    print(ve)
    print(needed)
    return True

def valenceElectron(element, amount):
# Return valence electron value from hash table and multiply it by the amount of elements
    elementDict = periodicTable.get(element)
    totalVE = ve = 0
    amount = int(amount)
    ve = elementDict.get("ve")
    totalVE = ve * amount
    return totalVE

def needed(element, amount):
# Return needed electrons for octet value from hash table and multiply it by the amount of elements
    amount = int(amount)
    elementDict = periodicTable.get(element)
    needed = elementDict.get("needed")
    totalNeeded = needed * amount
    return totalNeeded

def atoms(element, amount):
# Return atoms value from hash table and multiply it by the amount of elements
# Unused
    amount = int(amount)
    elementDict = periodicTable.get(element)
    atoms = elementDict.get("atoms")
    totalAtoms = atoms * amount
    return totalAtoms

#####################
#   Choosing Case   #
#####################

def choosingCase(formula, convertedFormula):
# Return case in algorithms pdf
    case = ""
    if len(convertedFormula) > 4:
        if formula.find("C") != -1 and formula.find("O") != -1 and int(convertedFormula[formula.find("C")+3]) >= 2:
# Check for multiple C atoms and an O atoms
            case = "Case3a"
            return case
        elif formula.find("N") != -1 and formula.find("O") != -1 and int(convertedFormula[formula.find("N")+3]) >= 2:
# Check for multiple N atoms and an O atoms
            case = "Case3a"
            return case
        elif formula.find("P") != -1 and formula.find("O") != -1 and int(convertedFormula[formula.find("P")+3]) >= 2:
# Check for multiple P atoms and an O atoms
            case = "Case3a"
            return case
        elif formula.find("S") != -1 and formula.find("O") != -1 and int(convertedFormula[formula.find("S")+3]) >= 2:
# Check for multiple S atoms and an O atoms
            case = "Case3a"
            return case
        elif formula.find("Cl") != -1 and formula.find("O") != -1 and int(convertedFormula[formula.find("Cl")+3]) >= 2:
# Check for multiple Cl atoms and an O atoms
            case = "Case3a"
            return case
        elif formula.find("C") != -1 and (formula.find("H") != -1 or formula.find("F") != -1 or formula.find("Cl") != -1 or formula.find("Br") != -1 or formula.find("I") != -1 or formula.find("At") != -1 or formula.find("Ts") != -1) and int(convertedFormula[formula.find("C")+3]) >= 2:
# Check for multiple C atoms and an Halogen atoms
            case = "Case3b"
            return case
        elif formula.find("N") != -1 and (formula.find("H") != -1 or formula.find("F") != -1 or formula.find("Cl") != -1 or formula.find("Br") != -1 or formula.find("I") != -1 or formula.find("At") != -1 or formula.find("Ts") != -1) and int(convertedFormula[formula.find("N")+3]) >= 2:
# Check for multiple N atoms and an Halogen atoms
            case = "Case3b"
            return case
        elif formula.find("He") != -1 or formula.find("Ne") != -1 or formula.find("Ar") != -1 or formula.find("Kr") != -1 or formula.find("Xe") != -1 or formula.find("Rn") != -1 or formula.find("Og") != -1:
# Check for Noble Gas atoms
            case ="Case2b"
            return case
        elif formula.find("O") != -1 and formula.find("H") == -1:
            if formula.find("C") != -1 or formula.find("N") != -1 or formula.find("S") != -1:
# Check for O and H atoms with C, N, S atoms
                case = "Case2c"
                return case
# Base Case for multiple atoms
        case = "Case2a"
        return case
    elif len(convertedFormula) == 4 and int(convertedFormula[3]) < 4:
# Monoatomic atoms with less than 4 total
        case = "Case1a"
        return case
    elif len(convertedFormula) == 4 and int(convertedFormula[3]) >= 4:
# Monoatomic atoms with more than 4 total
        case = "Case1b"
        return case
    return case

def diatomicCheck(formula):
# Check for diatomic atoms
# Unused
    if len(formula) == 4 and formula[len(formula)-1] == 2:
        return True
    else:
        return False

# ----- Begin Case Formulas ----- #
# See PDF of algorithms for the math

#####################
#      Case 1a      #
#####################

def lonePairCase1a(formula):
    x = charge = ve = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            ve += valenceElectron(element, amount)
            x += 2
    lonePairCase1a = ((ve - charge) % 8)/2
    return lonePairCase1a

def numBondCase1a(formula, db1a):
    x = charge = neededElectron = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            neededElectron += needed(element, amount)
            x += 2
    if db1a < 0:
        nonBondingCase1a = (neededElectron + charge)/2 - db1a
    else:
        nonBondingCase1a = (neededElectron + charge)/2
    return nonBondingCase1a

def doubleBondCase1a(formula):
    x = db1a = charge = halogenAtoms = carbonAtoms = boronAtoms = nitrogenAtoms = hydrogenAtoms = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            elementDict = periodicTable.get(formula[x])
            halogenBoolean = elementDict.get("halogen")
            if halogenBoolean == "true":
                halogenAtoms += int(formula[x+1])
            if formula[x] == "C":
                carbonAtoms += int(formula[x+1])
            if formula[x] == "B":
                boronAtoms += int(formula[x+1])
            if formula[x] == "N":
                nitrogenAtoms += int(formula[x+1])
            if formula[x] == "H":
                hydrogenAtoms += int(formula[x+1])
            x += 2
    db1a = carbonAtoms - ((halogenAtoms + hydrogenAtoms)/2) + ((boronAtoms + nitrogenAtoms)/2) + 1 + charge/2
    return db1a

#####################
#      Case 1b      #
#####################

def lonePairCase1b(formula):
    if formula[len(formula)-2] == "C" or formula[len(formula)-2] == "P":
        lp = int(formula[len(formula)-1])
    else:
        lp = 2*(int((formula[len(formula)-1])))
    return lp

def numBondCase1b(formula):
    x = charge = neededElectron = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            neededElectron += needed(element, amount)
            x += 2
    nb = (neededElectron)/2
    return nb

def ringsCase1b(formula):
    rings = 0
    if formula[2] == "C" or formula[2] =="P":
          rings = int(formula[3])/2 + 2
    if formula[2] == "S":
          rings = 1
    return rings

#####################
#      Case 2a      #
#####################

def lonePairCase2a(formula):
    x = y = charge = ve = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            ve += valenceElectron(element, amount)
            x += 2
    if ve <= 8:
        while(y < len(formula)-1):
            if formula[y] == "H":
                ve += 6 * int(formula[y+1])
                y += 2
            else:
                y += 2
    lonePairCase2a = ((ve - charge) % 8)/2
    return lonePairCase2a

def numBondCase2a(formula, db2a):
    x = charge = neededElectron = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            if element == "Be":
                neededElectron += 2 * int(amount)
                x += 2
            elif element == "B" or element == "Al":
                neededElectron += 3 * int(amount)
                x += 2
            else:
                neededElectron += needed(element, amount)
                x += 2
    if db2a < 0:
        nonBondingCase2a = (neededElectron + charge)/2 - db2a
    else:
        nonBondingCase2a = (neededElectron + charge)/2
    return nonBondingCase2a

def doubleBondCase2a(formula):
    x = db2a = charge = halogenAtoms = carbonAtoms = boronAtoms = nitrogenAtoms = hydrogenAtoms = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            elementDict = periodicTable.get(formula[x])
            halogenBoolean = elementDict.get("halogen")
            if halogenBoolean == "true":
                halogenAtoms += int(formula[x+1])
            if formula[x] == "C":
                carbonAtoms += int(formula[x+1])
            if formula[x] == "B":
                boronAtoms += int(formula[x+1])
            if formula[x] == "N":
                nitrogenAtoms += int(formula[x+1])
            if formula[x] == "H":
                hydrogenAtoms += int(formula[x+1])
            x += 2
    db2a = carbonAtoms - ((halogenAtoms + hydrogenAtoms)/2) + ((boronAtoms + nitrogenAtoms)/2) + 1 + charge/2
    return db2a

#####################
#      Case 2b      #
#####################

def lonePairCase2b(formula):
    x = charge = ve = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            ve += valenceElectron(element, amount)
            x += 2
    lonePairCase2b = ((ve - charge) % 8)/2
    return lonePairCase2b

def numBondCase2b(formula, db2b):
    x = charge = neededElectron = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            neededElectron += needed(element, amount)
            x += 2
    if db2b < 0:
        nonBondingCase2b = (neededElectron + charge)/2 - db2b
    else:
        nonBondingCase2b = (neededElectron + charge)/2
    return nonBondingCase2b

def doubleBondCase2b(formula):
    x = db2b = charge = halogenAtoms = oxygenAtoms = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            elementDict = periodicTable.get(formula[x])
            halogenBoolean = elementDict.get("halogen")
            if halogenBoolean == "true":
                halogenAtoms += int(formula[x+1])
            if formula[x] == "O":
                oxygenAtoms += int(formula[x+1])
            x += 2
    db2b = - halogenAtoms/2 - oxygenAtoms
    return db2b

#####################
#      Case 3a      #
#####################

def lonePairCase3a(formula):
    x = charge = ve = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            ve += valenceElectron(element, amount)
            x += 2
    lonePairCase3a = ((ve - charge) % 8)/2
    return lonePairCase3a

def numBondCase3a(formula, db3a):
    x = charge = neededElectron = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            neededElectron += needed(element, amount)
            x += 2
    if db3a < 0:
        nonBondingCase3a = (neededElectron + charge)/2 - db3a
    else:
        nonBondingCase3a = (neededElectron + charge)/2
    return nonBondingCase3a

def doubleBondCase3a(formula):
    x = db3a = charge = halogenAtoms = hydrogenAtoms = carbonAtoms = boronAtoms = nitrogenAtoms = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            elementDict = periodicTable.get(formula[x])
            halogenBoolean = elementDict.get("halogen")
            if halogenBoolean == "true":
                halogenAtoms += int(formula[x+1])
            if formula[x] == "C":
                carbonAtoms += int(formula[x+1])
            if formula[x] == "B":
                boronAtoms += int(formula[x+1])
            if formula[x] == "N":
                nitrogenAtoms += int(formula[x+1])
            if formula[x] == "H":
                hydrogenAtoms += int(formula[x+1])
            x += 2
    db3a = carbonAtoms - ((halogenAtoms + hydrogenAtoms)/2) + ((boronAtoms + nitrogenAtoms)/2) + 1 + charge/2
    return db3a

#####################
#      Case 3b      #
#####################

def lonePairCase3b(formula):
    x = charge = ve = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        elif formula[x] == "H":
            ve += 7 * int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            ve += valenceElectron(element, amount)
            x += 2
    lonePairCase3b = ((ve - charge) % 8)/2
    return lonePairCase3b

def numBondCase3b(formula, db3b):
    x = charge = neededElectron = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            element = formula[x]
            amount = formula[x+1]
            neededElectron += needed(element, amount)
            x += 2
    if db3b < 0:
        nonBondingCase3b = (neededElectron + charge)/2
    else:
        nonBondingCase3b = (neededElectron + charge)/2
    return nonBondingCase3b

def doubleBondCase3b(formula):
    x = db3b = charge = halogenAtoms = hydrogenAtoms = carbonAtoms = boronAtoms = nitrogenAtoms = 0
    while(x < len(formula)-1):
        if formula[x] == "Charge":
            charge += int(formula[x+1])
            x += 2
        else:
            elementDict = periodicTable.get(formula[x])
            halogenBoolean = elementDict.get("halogen")
            if halogenBoolean == "true":
                halogenAtoms += int(formula[x+1])
            if formula[x] == "C":
                carbonAtoms += int(formula[x+1])
            if formula[x] == "B":
                boronAtoms += int(formula[x+1])
            if formula[x] == "N":
                nitrogenAtoms += int(formula[x+1])
            if formula[x] == "H":
                hydrogenAtoms += int(formula[x+1])
            x += 2
    db3b = carbonAtoms - ((halogenAtoms + hydrogenAtoms)/2) + ((boronAtoms + nitrogenAtoms)/2) + 1
    return db3b
