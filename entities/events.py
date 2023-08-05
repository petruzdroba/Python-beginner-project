from datetime import datetime


class Event:

    def __init__(self, name, event_id, city, number_participants, capacity, start_date, end_date):
        self.__name = name
        self.__event_id = event_id
        self.__city = city
        self.__number_participants = number_participants
        self.__capacity = capacity
        self.__start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.__end_date = datetime.strptime(end_date, "%Y-%m-%d")

    def get_event_name(self):
        return self.__name

    def get_event_id(self):
        return self.__event_id

    def get_event_city(self):
        return self.__city

    def get_event_number_participants(self):
        return self.__number_participants

    def get_event_capacity(self):
        return self.__capacity

    def get_event_start_date(self):
        return self.__start_date.date()

    def get_event_end_date(self):
        return self.__end_date.date()

    def __str__(self):
        return (" Event: {0}\n ID: {1}\n City: {2} \n Nr Participants: {3}\n"
                " Capacity: {4}\n Starting in: {5}\n Ending on: {6}\n".format(self.__name, self.__event_id, self.__city,
                                                                              self.__number_participants,
                                                                              self.__capacity, self.__start_date,
                                                                              self.__end_date))

    def get_all_info(self):
        string_start_date = datetime.strftime(self.__start_date, "%Y-%m-%d")
        string_end_date = datetime.strftime(self.__end_date, "%Y-%m-%d")
        return ("{0}\n"
                "{1}\n"
                "{2}\n"
                "{3}\n"
                "{4}\n"
                "{5}\n"
                "{6}\n".format(self.__name, self.__event_id, self.__city, self.__number_participants,
                               self.__capacity, string_start_date, string_end_date))

    def __eq__(self, other):
        return self.get_event_id() == other.get_event_id()

    def set_new_event_in_place(self, name, event_id, city, number_participants, capacity, start_date,
                               end_date):
        self.__name = name
        self.__event_id = event_id
        self.__city = city
        self.__number_participants = number_participants
        self.__capacity = capacity
        self.__start_date = start_date
        self.__end_date = end_date
