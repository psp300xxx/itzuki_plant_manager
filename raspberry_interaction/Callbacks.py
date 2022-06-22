from .ChannelInput import ChannelInput
from .MessagingInteractor import MessagingInteractor
import logging

def default_channel_input_handler( input : int )-> str:
    if input:
        return "Mi sento asciutta, prova ad annaffiarmi"
    return "Mi sento annaffiata"

def callback(channel : int, channel_input : ChannelInput, messaging_interactor : MessagingInteractor, bot, telegram_user_id : str, channel_input_handler : callable = default_channel_input_handler) -> str:
    message = channel_input_handler(channel_input.input(channel))
    # Avoid prints in favor of logging module
    print(message)
    messaging_interactor.sendMessage(telegram_user_id, message)
    return message
