from session import Session
import constants
from utils import clear, read_users_template


def add_users():
    channel = client.get_entity(input("Enter channel link or ID: "))
    users = [client.get_entity(user) for user in read_users_template()]
    session.add_users_to_chat(channel, users)


def get_options():
    clear()

    print("[1] == Invite users ==\n")

    user_option = input("Enter option's number: ")

    if user_option == "1":
        add_users()
    else:
        get_options()


def main():
    global client, session

    # Setting configuration values
    api_id = constants.API_ID
    api_hash = str(constants.HASH_ID)
    username = input("Your user tag: @")

    # Create session via user
    session = Session(username, api_id, api_hash)
    client = session.client

    get_options()


if __name__ == "__main__":
    clear()
    main()
    client.run_until_disconnected()
