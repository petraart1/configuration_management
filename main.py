from zipfile import ZipFile


def ls(args: list):
    print(args)
    pass

def cd(args: list):
    pass

def pwd_command(pwd: str):
    print(pwd)

def sudo(args: list):
    pass

def upname(args: list):
    pass

def uptime(args: list):
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