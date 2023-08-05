from service.organiser_service import OrganiserService
from datetime import datetime


class OrganiserMode:

    def __init__(self, organiser_service: OrganiserService):
        self.__organiser_service = organiser_service

    def __print_organiser_menu(self):
        print("\n\nORGANISER MODE\n\n"
              "Options:\n"
              "<1> Add Event\n"
              "<2> Delete Event\n"
              "<3> Modify event\n"
              "<4> Inspect event list\n"
              "<5> Inspect particular city events\n"
              "<6> Events that include 'participant'\n"
              "<0> Return to main menu\n")

    def __validate_input_number(self, input):
        try:
            int(input)
        except:
            raise Exception("Numerical value expected!")


    def __validate_number_participans_vs_capacity(self, number_participants, capacity):
        if int(number_participants) > int(capacity):
            raise Exception("Number of participants cannot exceed capacity!")

    def __validate_input_date(self, input_date):
        try:
            datetime.strptime(input_date, "%Y-%m-%d")
        except:
            raise Exception("Date format not respected!")

    def __validate_event_dates(self, start_date, end_date):
            if start_date > end_date:
                raise Exception("End Date of the event should be after the Start Date!")

    def run_organiser_mode(self):
        while True:
            try:
                self.__print_organiser_menu()
                command = int(input("Pick one of the options: "))
                if command == 0:
                    break
                elif command == 1:
                    name = input("Name: ")
                    event_id = input("ID: ")

                    city = input("City: ")

                    number_participants = input("Current nr of participants: ")
                    self.__validate_input_number(number_participants)
                    capacity = input("Capacity: ")
                    self.__validate_input_number(capacity)

                    self.__validate_number_participans_vs_capacity(number_participants, capacity)

                    start_date = input("Start date: Year-month-day(use '-' in between)")
                    self.__validate_input_date(start_date)
                    end_date = input("End date: Year-month-day(use '-' in between)")
                    self.__validate_input_date(end_date)
                    self.__validate_event_dates(start_date, end_date)

                    self.__organiser_service.add_event(name, event_id, city, number_participants, capacity, start_date,
                                                       end_date)
                elif command == 2:
                    event_id = input("Type in id: ")
                    self.__organiser_service.delete_event(event_id)

                elif command == 3:
                    event_id = input("Type in id: ")

                    name = input("New name: ")
                    city = input("New City: ")

                    number_participants = input("New nr of participants: ")
                    self.__validate_input_number(number_participants)
                    capacity = input("New capacity: ")
                    self.__validate_input_number(capacity)

                    self.__validate_number_participans_vs_capacity(number_participants, capacity)

                    start_date = input("Start date: Year-month-day(use '-' in between)")
                    self.__validate_input_date(start_date)
                    end_date = input("End date: Year-month-day(use '-' in between)")
                    self.__validate_input_date(end_date)
                    self.__validate_event_dates(start_date, end_date)

                    self.__organiser_service.modify_event(event_id, name, city, number_participants, capacity,
                                                          start_date, end_date)
                elif command == 4:
                    self.__organiser_service.get_all_events()

                elif command == 5:
                    city = input("Type in city: ")
                    self.__organiser_service.get_all_events_city(city)

                elif command == 6:
                    self.__organiser_service.get_events_with_participant()

            except  Exception as error:
                print(error)
