import argparse
from shell import Shell
from tkinter import Tk
from terminal import Terminal
from logger import Logger


def main():
    parser = argparse.ArgumentParser(description="Terminal Emulator")
    parser.add_argument("username", help="Имя пользователя для приглашения")
    parser.add_argument("hostname", help="Имя компьютера для приглашения")
    parser.add_argument("fs_path", help="Путь к архиву виртуальной файловой системы")
    parser.add_argument("log_path", help="Путь к лог-файлу")
    parser.add_argument("startup_script", help="Путь к стартовому скрипту")
    args = parser.parse_args()

    shell = Shell(username=args.username, hostname=args.hostname, fs_path=args.fs_path)
    shell.logger = Logger(log_file=args.log_path)

    root = Tk()
    terminal = Terminal(root, shell)

    try:
        with open(args.startup_script, "r") as script:
            for line in script:
                command = line.strip()
                if command:
                    terminal.execute_on_startup(command)
    except FileNotFoundError:
        print(f"Ошибка: файл стартового скрипта '{args.startup_script}' не найден.")

    root.mainloop()


if __name__ == "__main__":
    main()