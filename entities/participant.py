class Participant:
    def __init__(self, name, link_picture, signed_up_events: list):
        self.__name = name
        self.__link_picture = link_picture
        self.__signed_up_events = signed_up_events

    def get_participant_name(self):
        return self.__name

    def get_participant_signed_up_events(self):
        return self.__signed_up_events

    def set_participants_signed_up_events(self, new_event):
        self.__signed_up_events.append(new_event)