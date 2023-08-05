from repository.repository import Repository
from entities.events import Event


class OrganiserService:

    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_event(self, name, event_id, city, number_participants, capacity, start_date, end_date):
        event = Event(name, event_id, city, number_participants, capacity, start_date, end_date)
        self.__repository.add(event)

    def delete_event(self, event_id):
        event = Event("a", event_id, "a", "a", "a", "2000-01-01", "2000-01-01", )
        self.__repository.delete(event)

    def modify_event(self, event_id, name, city, number_participants, capacity, start_date,
                     end_date):
        event = Event(name, event_id, city, number_participants, capacity, start_date,end_date)
        self.__repository.modify(event)

    def get_all_events(self):
        for event in self.__repository.get_all():
            print(event)

    def get_all_events_city(self, city):
        validate_city = 0
        for event in self.__repository.get_all():
            if event.get_event_city() == city:
                print(event)
                validate_city = 1
        if validate_city == 0:
            raise Exception("No events in {0} city".format(city))

    def get_events_with_participant(self):
        event_ids =[]

        for participant in self.__repository.get_participant():
            event_ids = participant.get_participant_signed_up_events()

        for i in range(len(event_ids)):
            for event in self.__repository.get_all():
                if event_ids[i] == event.get_event_id():
                    print(event)
