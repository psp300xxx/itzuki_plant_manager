
# this class will act as base class to the interactions with raspberry and mock for the unit/integration
# tests
# In general avoid leveraging directly on classes, use something as bridge in the middle, this will allow you to
# change clients much easier and to write better tests
class ChannelInput():
    def input(self, channel : int):
        pass