from zipfile import ZipFile
import getpass
import hashlib
import os

def ls(args: list) -> None:
    with ZipFile("filesystem.zip", "r") as filesystem:
        for file in filesystem.namelist():
            file = file.split('/')
            print(file[-2])


def cd(args: list) -> None:
    pass


def mkdir(dirname: str) -> None:
    with ZipFile("filesystem.zip", "r") as filesystem:
        for file in filesystem.namelist():
            pass


def rmdir(dirname: str) -> None:
    os.rmdir(dirname)
    pass


def pwd(pwd: str) -> None:
    print(pwd)


def sudo(args: list) -> bool:
    password = getpass.getpass('Password: ')
    print(password)

    command = args[0]
    match command:
        case 'ls':
            ls(args[1::])
        case 'cd':
            cd(args[1::])
        case "pwd":
            pass
            #pwd_command(pwd)
        case "sudo":
            first_symbol = '#'
            sudo(args[1::])
        case "upname":
            upname(args[1::])
        case "uptime":
            uptime(args[1::])
        case "exit":
            exit()
        case _:
            print(f'terminal: command not found: {command}')


def upname(args: list) -> None:
    pass


def uptime(args: list) -> None:
    pass


def exit():
    pass


def main():
    with ZipFile('filesystem.zip', 'a') as filesystem:
        username = 'user'
        desktop_name = 'desktop'
        _pwd = '/'
        first_symbol = '$'
        while True:
            command = input(f'{username}@{desktop_name}:~{first_symbol} ')
            arr = command.split(' ')
            match arr[0]:
                case 'ls':
                    ls(arr[1::])
                case 'cd':
                    cd(arr[1::])
                case "pwd":
                    pwd(_pwd)
                case "sudo":
                    if sudo(arr[1::]):
                        first_symbol = '#'
                case "upname":
                    upname(arr[1::])
                case "uptime":
                    uptime(arr[1::])
                case "exit":
                    exit()
                case _:
                    print(f'terminal: command not found: {arr[0]}')


if __name__ == "__main__":
    main()