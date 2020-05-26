from Class import Events , event
import datetime

def AddNewEvent() -> Events:
    try:
        new_event_name = str(input("Wpisz nazwę nowego wydarzenia:"))
        new_event_place = str(input("Wpisz miejsce, w którym odbędzię się wydarzenie: "))
        event_year = int(input("Wpisz rok, w którym odbędzie się wydarzenie:"))
        event_mouth = int(input("Wpisz numer miesiąca, w którym odbędzie się wydarzenie:"))
        event_day = int(input("Wpisz dzień miesiąca w którym odbędzie się wydarzenie:"))
        event.append(Events(new_event_name,new_event_place,datetime.date(event_year,event_mouth,event_day)))
        return Events(new_event_name,new_event_place,datetime.date(event_year,event_mouth,event_day))
    except ValueError:
        print("\n"
              "UWAGA!!!\n"
              "Nie poprawnie wprowadzone dane.\n"
              "Wprowadź dzień miesiąca z zakreu 1-31, a numer miesiąca z zakresu 1-12.\n")