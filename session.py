from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.types import InputChannel, InputUser


class Session:
    def __init__(self, username, api_id, api_hash):
        self.client = TelegramClient(username, api_id, api_hash)
        self.client.start(max_attempts=4)

    def add_users_to_chat(self, channel, users):
        input_channel = InputChannel(channel.id, channel.access_hash)
        input_users = [InputUser(user.id, user.access_hash) for user in users]
        self.client(InviteToChannelRequest(input_channel, input_users))
