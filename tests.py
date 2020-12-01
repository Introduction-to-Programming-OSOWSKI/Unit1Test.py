#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2020
month = 12
day = 22

def test_code1():
    assert main.name("Dwight") == "Dwight", "name('Dwight') failed"
    assert main.name("tony") == "tony", "name('tony') failed"

def test_code2():
    assert main.favorites("red", 42) == "Your favorite color is red and your favorite number is 42.", "favorites('red', 42) failed. Check your spelling, capital letters, and make sure you have a period at the end of the sentance. See the reamde for exact formatting."
    assert main.favorites("green", 11) == "Your favorite color is green and your favorite number is 11.", "favorites('green', 11) failed. Check your spelling, capital letters, and make sure you have a period at the end of the sentance. See the reamde for exact formatting."

def test_code3():
    assert main.bigAdd(1,1,1,1,1) == 5, "bigAdd(1, 1, 1, 1, 1) == 5 failed"
    assert main.bigAdd(2,5,1,9,5) == 22, "bigAdd(2, 5, 1, 9, 5) == 22 failed"

def test_code4():
    assert main.fourOperations(2,5,1,9,5) == 5.2, "fourOperations failed"
    assert main.fourOperations(5,10,15,20,25) == 3.0, "fourOperations failed"
    

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
