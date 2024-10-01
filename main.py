from zipfile import ZipFile


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
            file = file.split('/')

def pwd_command(pwd: str) -> None:
    print(pwd)


def sudo(args: list) -> None:
    pass


def upname(args: list) -> None:
    pass


def uptime(args: list) -> None:
    pass


def exit():
    pass


def main():
    with ZipFile('filesystem.zip', 'a') as filesystem:
        pwd = '/'
        first_symbol = '$'
        while True:
            command = input(f'{first_symbol} ')
            arr = command.split(' ')
            match arr[0]:
                case 'ls':
                    ls(arr[1::])
                case 'cd':
                    cd(arr[1::])
                case "pwd":
                    pwd_command(pwd)
                case "sudo":
                    first_symbol = '#'
                    sudo(arr[1::])
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