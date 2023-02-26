from os import system, name, path, getcwd


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def read_users_template():
    curr_dir = path.abspath(getcwd())
    template = rf"{curr_dir}\users.txt"
    users = []
    with open(template) as f:
        for line in f:
            users.append(line.strip())
    return users
