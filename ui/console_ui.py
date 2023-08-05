from ui.organiser_mode import OrganiserMode
from ui.participant_mode import ParticipantMode
class ConsoleUI:

    def __init__(self, organiser_mode: OrganiserMode, participant_mode: ParticipantMode):
        self.__organiser_mode = organiser_mode
        self.__participant_mode = participant_mode

    def __print_menu(self):
        print("\nTIPD EVENTS\n\n"
              "Options:\n"
              "<1>Organiser mode\n"
              "<2>Participant mode\n"
              "<0>Exit\n")

    def run(self):
        while True:
            try:
                self.__print_menu()
                command = int(input("Pick one of the options: "))
                if command == 0:
                    break
                elif command == 1:
                    self.__organiser_mode.run_organiser_mode()
                elif command == 2:
                    self.__participant_mode.run_participant_mode()
            except Exception as error:
                print(error)