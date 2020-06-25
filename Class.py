import datetime,math
class Events:
    def __init__(self, name_event, place_event, date_event):
        self.name_event = name_event
        self.place_event = place_event
        self.date_event = date_event

    def CountdownDays(self):
        today = datetime.date.today()
        difference = (today-self.date_event).days
        if difference > 0:
            return f'Wydarzenie odbyło się {int(difference)} dni temu.'
        elif difference < 0:
            return f'Wydarzenie odbędzie się za {int(math.fabs(difference))} dni.'
        else:
            return f'Wydarzenie odbywa się dzisiaj.'

    def CountDays(self):
        today2=(datetime.date.max)
        difference2 = (today2-self.date_event).days
        return int(math.fabs(difference2))

#lista służąca to przechowywania elementów stworzonych obiektów klasy
event = []

