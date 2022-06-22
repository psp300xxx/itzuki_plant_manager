
# this class will act as base class to the interactions with raspberry and mock for the unit/integration
# tests
class MessagingInteractor():
    def sendMessage(self, user_id : str, message: str) -> None:
        pass