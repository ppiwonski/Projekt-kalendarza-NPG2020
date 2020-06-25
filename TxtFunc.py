#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from Class import Events, event
from AdditionalFunc import ClearScreen

def WriteTxt():
    a = open("CalendarData.txt", "w")
    for el in event:
        s=el.name_event
        a.write(str(s))
        a.write("\n")
        s = el.date_event
        a.write(str(s))
        a.write("\n")
        s = el.place_event
        a.write(str(s))
        a.write("\n")
    a.close()

def ReadTxt():
    d = open("CalendarData.txt", "r")
    if d.closed:
        print("\nNie znaleziono żadnych zapisanych wydarzeń w kalendarzu\n")
    line_list=d.readlines()
    d.close()
    try:
        lenght=len(line_list)
        if lenght<3:
            print("\nNie znaleziono żadnych zapisanych wydarzeń w kalendarzu\n")
            WriteTxt()
            return None
        for x in range(0, lenght):
            line_list[x]=line_list[x][:-1]
        for i in range(0, lenght, 3):
            name = str(line_list[i])
            date = str(line_list[i+1])
            place = str(line_list[i+2])
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[8:10])
            event.append(Events(name, place, datetime.date(year,month,day)))
    except ValueError:
        print("\nUwaga:\n"
              "Plik tekstowy modyfikowany recznie lub uszkodzony!\n"
              "Nie wczytano żadnych zapisanych danych. Plik wyczyszczono\n")
        WriteTxt()

def DoAfterAction():
    WriteTxt()
    ClearScreen()