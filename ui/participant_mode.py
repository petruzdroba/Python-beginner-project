from service.participant_service import ParticipantService
class ParticipantMode:

    def __init__(self, participant_service: ParticipantService):
        self.__participant_service = participant_service

    def __print_menu(self):
        print("\n\nPARTICIPANT MODE\n\n"
              "Options:\n"
              "<1> Event list\n"
              "<2> Events starting next week\n"
              "<3> Events starting in a particular month\n"
              "<4> Inscrie-te la un eveniment\n"
              "<0> Return to main menu\n")

    def __validate_month(self, month):
        if month < 1 or month > 12:
            raise Exception("Month input impossible!")

    def run_participant_mode(self):
        while True:
            try:
                self.__print_menu()
                command = int(input("Pick one of the options: "))
                if command == 0:
                    break
                elif command ==1:
                    self.__participant_service.get_all_events()
                elif command == 2:
                    self.__participant_service.get_all_events_next_week()
                elif command == 3:
                    input_month = int(input("Input a month (numerical value): "))
                    self.__validate_month(input_month)

                    self.__participant_service.get_all_events_in_month(input_month)
                elif command == 4:
                    event_id = input("Type the id of the event: ")
                    self.__participant_service.sign_up_for_event(event_id)
            except Exception as error:
                print(error)