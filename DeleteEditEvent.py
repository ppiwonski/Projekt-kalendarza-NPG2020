from Class import Events, event
import datetime

def DeleteEvent() -> Events:
    delete_event_name = str(input("Wpisz nazwę wydarzenia do usunięcia:"))
    for el in event:
        if el.name_event == delete_event_name:
            event.remove(el)
            return 0
    print("Nie ma takiego wydarzenia! Podaj nazwę istniejącego wydarzenia!")
    return 0


def EditEvent() -> Events:
    try:
        edit_event_name = str(input("Wpisz nazwę wydarzenia do edytowania:"))
        for el in event:
            if el is not event:
                print("Nie ma takiego wydarzenia! Podaj nazwę istniejącego wydarzenia!")
                return 0
            elif el.name_event == edit_event_name:
                new_edit_event_name = str(input("Wpisz nową nazwę wydarzenia:"))
                new_edit_event_place = str(input("Wpisz nowe miejsce, w którym odbędzię się wydarzenie: "))
                event_edit_year = int(input("Wpisz nowy rok, w którym odbędzie się wydarzenie:"))
                event_edit_month = int(input("Wpisz nowy numer miesiąca, w którym odbędzie się wydarzenie:"))
                event_edit_day = int(input("Wpisz nowy dzień miesiąca w którym odbędzie się wydarzenie:"))
                el.name_event = new_edit_event_name
                el.place_event = new_edit_event_place
                el.date_event = datetime.date(event_edit_year,event_edit_month,event_edit_day)
                return Events(new_edit_event_name, new_edit_event_place, datetime.date(event_edit_year, event_edit_month, event_edit_day))
            else:
                print("Nie ma takiego wydarzenia! Podaj nazwę istniejącego wydarzenia!")
                return 0
    except ValueError:
        print("\n"
              "UWAGA!!!\n"
              "Nie poprawnie wprowadzone dane.\n"
              "Wprowadź dzień miesiąca z zakreu 1-31, a numer miesiąca z zakresu 1-12.\n")