import Class
from AddEvent import AddNewEvent
from DeleteEditEvent import DeleteEvent, EditEvent
import datetime
from AdditionalFunc import PressEnter, ClearScreen
from PrintEventsFromDate import PrintNFromDate
from TxtFunc import DoAfterAction, ReadTxt
import time
import os

while True:
    DoAfterAction()
    print("KALENDARZ\n"
          "Instrukcja obsługi (wprowadź konkretną cyfrę w celu wywołania funkcji):\n"
          "1 - dodaj wydarzenie,\n"
          "2 - usuń wydarzenie,\n"
          "3 - edytuj wydarzenie,\n"
          "4 - wypisz określoną ilość wydarzeń od daty"
          " (wypisuje czas od / do wydarzenia),\n"
          "5 - zamknij kalendarz.\n")
    x = int(input("Wybierz instrukcję, którą chcesz wykonać:"))
    ClearScreen()

    if x == 1:
        AddNewEvent()
        continue
    elif x == 2:
        DeleteEvent()
        continue
    elif x == 3:
        EditEvent()
        continue
    elif x == 4:
        PrintNFromDate()
        PressEnter()
        continue
    elif x == 5:
        DoAfterAction()
        break
    else:
        print("Błąd!\n"
              "Wprowadź cyfrę z zakresu 1-5\n")
        PressAnyKey()
        continue