from entities.events import Event
from repository.repository import Repository

class FileRepository:

    def __init__(self, event_list: Repository):
        self.__event_list = event_list

    def read_file_event(self):
        event_file = open("repository/file_events.txt", "r")

        file_list = []
        for line in event_file:
            file_list.append(line.rstrip('\n'))

        for i in range(0, len(file_list), 7):
            event = Event(file_list[i], file_list[i + 1], file_list[i + 2], file_list[i + 3], file_list[i + 4],
                          file_list[i + 5], file_list[i + 6])
            self.__event_list.add(event)

    def get_file_events(self):
        self.read_file_event()
        return self.__event_list

    def set_file_event(self,new_event_list):
        event_file = open("repository/file_events.txt", "w")
        event_file.write(new_event_list)
    def update_file_events(self, new_event_list):
        self.set_file_event(new_event_list)
