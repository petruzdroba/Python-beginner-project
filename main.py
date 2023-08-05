from entities.events import Event
from entities.participant import Participant
from ui.console_ui import ConsoleUI
from repository.repository import Repository
from ui.organiser_mode import OrganiserMode
from service.organiser_service import OrganiserService
from ui.participant_mode import ParticipantMode
from service.participant_service import ParticipantService
from repository.file_repository import FileRepository

event_repository = Repository([],[Participant("Zdroba Petru", "yoda.jpg", ["id209"])])

file_repository = FileRepository(event_repository)
event_repository = file_repository.get_file_events()

organiser_service = OrganiserService(event_repository)
organiser_mode = OrganiserMode(organiser_service)

participant_service = ParticipantService(event_repository)
participant_mode = ParticipantMode(participant_service)

ui = ConsoleUI(organiser_mode, participant_mode)

ui.run()

file_repository.update_file_events(event_repository.__str__())

