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
    template = "users.temp.txt"
    data = rf"{curr_dir}/{template}"
    users = []
    try:
        with open(data) as f:
            for line in f:
                users.append(line.strip())
    except FileNotFoundError:
        print(f"Cann't find {template}")
    return users
