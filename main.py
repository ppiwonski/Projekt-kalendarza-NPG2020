import Class
from AddEvent import AddNewEvent
from DeleteEditEvent import DeleteEvent, EditEvent
import datetime

while True:
    print("KALENDARZ\n"
          "Instrukcja obsługi (wprowadź konkretną cyfrę w celu wywołania funkcji):\n"
          "1 - dodaj wydarzenie,\n"
          "2 - usuń wydarzenie,\n"
          "3 - edytuj wydarzenie,\n"
          "4 - odliczaj czas do wydarzenie,\n"
          "5 - zamknij kalendarz.\n")
    x = int(input("Wybierz instrukcję, którą chcesz wykonać:"))

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
        CountdownDays()
        continue
    elif x == 5:
        break
    else:
        print("Błąd!\n"
              "Wprowadź cyfrę z zakresu 1-5\n")
        continue

#for e in Class.event:
#    print(e.date_event)



# Do dokończenia