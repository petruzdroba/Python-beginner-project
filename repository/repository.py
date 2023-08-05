class Repository:

    def __init__(self, event_list, participant):
        self.__event_list = event_list
        self.__participant = participant

    def find_position(self, event):
        for i in range(len(self.__event_list)):
            if self.__event_list[i] == event:
                return i
        return None

    def add(self, event):
        location = self.find_position(event)
        if location is not None:
            raise Exception("Event with ID:{0} already in database!".format(event.get_event_id()))
        self.__event_list.append(event)

    def delete(self, event):
        location = self.find_position(event)
        if location is None:
            raise Exception("Event with this ID does not exist!")
        del self.__event_list[location]

    def modify(self, new_event):

        event_id_found = 0
        for event in self.__event_list:
            if event.get_event_id() == new_event.get_event_id():

                event.set_new_event_in_place(new_event.get_event_name(), new_event.get_event_id(),
                                             new_event.get_event_city(), new_event.get_event_number_participants(),
                                             new_event.get_event_capacity(), new_event.get_event_start_date(),
                                             new_event.get_event_end_date())
                event_id_found =1
        if event_id_found ==0:
            raise Exception("Event with this ID does not exist!")

    def get_all(self):
        if len(self.__event_list) == 0:
            raise Exception("No events to show!")
        return self.__event_list
    def get_participant(self):
        return self.__participant
    def add_event_to_participant(self, event_id):
        for participant in self.__participant:
            participant.set_participants_signed_up_events(event_id)

    def __str__(self):
        new_string_for_update = ""
        for i in range(len(self.__event_list)):
            new_string_for_update += self.__event_list[i].get_all_info()
        return new_string_for_update
