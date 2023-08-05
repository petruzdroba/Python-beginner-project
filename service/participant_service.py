from repository.repository import Repository
import datetime as DateTime
from datetime import datetime
from entities.events import Event


class ParticipantService:

    def __init__(self, repository: Repository):
        self.__repository = repository

    def get_all_events(self):
        for event in self.__repository.get_all():
            print(event)

    def __get_event_duration(self, start_date, end_date):
        return end_date - start_date

    def __find_position(self, event, event_list: list):
        for i in range(len(event_list)):
            if event_list[i] == event:
                return i
        return None

    def __sort_list_duration_event(self, new_event_list):
        for event in new_event_list:
            for copy_event in new_event_list:
                if self.__get_event_duration(event.get_event_start_date(),
                                             event.get_event_end_date()) > self.__get_event_duration(
                    copy_event.get_event_start_date(), copy_event.get_event_end_date()):
                    aux = new_event_list[self.__find_position(event, new_event_list)]
                    new_event_list[self.__find_position(event, new_event_list)] = new_event_list[
                        self.__find_position(copy_event, new_event_list)]
                    new_event_list[self.__find_position(copy_event, new_event_list)] = aux

    def get_all_events_in_month(self, month):

        month_check = 0
        new_event_list = []
        for event in self.__repository.get_all():

            if int(event.get_event_start_date().month) == month:
                month_check = 1
                new_event_list.append(event)

        if month_check == 1:
            self.__sort_list_duration_event(new_event_list)
        else:
            raise Exception("No events in the {0} month!".format(month))

        for i in range(len(new_event_list)):
            print(new_event_list[i])

    def __sort_number_participants(self, new_event_list):
        for event in new_event_list:
            for copy_event in new_event_list:
                if int(event.get_event_number_participants()) < int(copy_event.get_event_number_participants()):
                    aux = new_event_list[self.__find_position(event, new_event_list)]
                    new_event_list[self.__find_position(event, new_event_list)] = new_event_list[
                        self.__find_position(copy_event, new_event_list)]
                    new_event_list[self.__find_position(copy_event, new_event_list)] = aux

    def get_all_events_next_week(self):
        current_date = DateTime.date.today()
        next_week_date = current_date + DateTime.timedelta(days=7)

        new_event_list = []

        for event in self.__repository.get_all():
            if current_date <= event.get_event_start_date() <= next_week_date:
                new_event_list.append(event)

        self.__sort_number_participants(new_event_list)

        for i in range(len(new_event_list)):
            print(new_event_list[i])

    def sign_up_for_event(self, event_id):

        for event in self.__repository.get_all():
            if event.get_event_id() == event_id:
                new_event_number_participants = int(event.get_event_number_participants()) + 1
                if new_event_number_participants + 1 <= int(event.get_event_capacity()):
                    start_date = datetime.strftime(event.get_event_start_date(), "%Y-%m-%d")
                    end_date = datetime.strftime(event.get_event_end_date(), "%Y-%m-%d")
                    placeholder_event = Event(event.get_event_name(), event_id,
                                          event.get_event_city(), str(new_event_number_participants),
                                          event.get_event_capacity(), start_date,
                                          end_date)
                    self.__repository.modify(placeholder_event)
                    self.__repository.add_event_to_participant(event_id)
                else: raise Exception("Event is sold out!")
