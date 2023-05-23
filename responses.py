#import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return "`I put people in the jail channel, they cannot leave for 15 seconds. try !jail @user`"

    if p_message.startswith('!jail'):
        return "To move a user to jail, use the command `!jail @user`."

