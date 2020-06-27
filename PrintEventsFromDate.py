#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
import os
from Class import Events, event
from AdditionalFunc import PressEnter, ClearScreen

def PrintNFromDate():
    numberofevents = []
    def Date_from() -> list:
        new_event_name = str("Any_Date")
        new_event_place = str("Any_Place")
        try:
            event_year = int(input("Wpisz rok twojej daty:"))
            event_month = int(input("Wpisz numer miesiąca twojej daty:"))
            event_day = int(input("Wpisz dzień miesiąca twojej daty"))
        except ValueError:
            print("Wprowadzono niepoprawny numer miesiaca/roku/dnia. Wracam do menu aplikacji")
            time.sleep(1)
            numberofevents.append(-1)
            ClearScreen()
            return None
        print(" ")
        time.sleep(1)
        os.system('cls')
        event.append(Events(new_event_name, new_event_place, datetime.date(event_year, event_month, event_day)))
        k=event[-1]
        print(f'Twoja data to {event[-1].date_event} .')
        templist=[]
        x=0
        for el in event:
            if int(el.CountDays()) < int(k.CountDays()):
                templist.append(el)
                x+=1
        if x>0:
            print(f'Liczba znalezionych wydarzenia od tej daty:   {x}')
        elif x==0:
            print("Nie znaleziono żadnych wydarzeń po podanej dacie")
            x=(-1)
            PressEnter()
        numberofevents.append(int(x))
        return templist
    ListToSort=[]
    ListToSort=Date_from()
    def bubblesort1(x):
        if x is None:
            return None
        m = len(x)
        templist1 = []
        templist1.extend(x)
        for k in range(m - 1):
            for s in range(m - 1):
                f = (s + 1)
                gm = templist1[s + 1].CountDays()
                float(gm)
                y1 = templist1[s].CountDays()
                float(y1)
                if gm > y1:
                    bufor = templist1[s]
                    templist1[s] = templist1[s + 1]
                    templist1[s + 1] = bufor
        return templist1
    ListToPrint=bubblesort1(ListToSort)
    print(" ")
    if numberofevents[0] == (-1):
        del event[-1]
        numberofevents=[]
        x=0
        return None
    if numberofevents[0]>0:
        n = int(input("Wpisz, ile kolejnych wydarzeń chcesz wyświetlic: "))
        os.system('cls')
    if n>numberofevents[0]:
        n=numberofevents[0]
        print(f'znaleziono tylko {numberofevents[0]} wydarzen od tej daty:')
        time.sleep(3)
        os.system('cls')
    if n<0:
        print("Nie nalezy wpisywac ujemnej liczby wydarzen do wyswietlenia. Wracam do manu aplikacji...")
        time.sleep(2)
        os.system('cls')
        return None
    print(" ")
    if n>0:
        if n==1:
            print("Wypisuję 1 wydarzenie po wybranej dacie")
        else:
            print(f'Wypisywanie {n} kolejnych wydarzen od {event[-1].date_event} :')
        for x in range(n):
            print(f' \n Nazwa wydarzenia: {ListToPrint[x].name_event} \n Data wydarzenia: {ListToPrint[x].date_event},'
                  f' \n miejsce wydarzenia: {ListToPrint[x].place_event} \n Licząc od dzisiaj, {ListToPrint[x].CountdownDays()}')
        PressEnter()
        ClearScreen()
    if n==0:
        print('Wybrales wypisanie "0" wydarzeń. Wracam do menu aplikacji...')
        time.sleep(2)
        ClearScreen()
    del event[-1]
    numberofevents=[]
    x=0
    return None