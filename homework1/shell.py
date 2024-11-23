import os
import time


class Shell:
    def __init__(self, username="root", hostname="localhost", vfs_path=None):
        self.username = username
        self.hostname = hostname
        self.current_dir = "/"
        self.vfs_path = vfs_path
        self.start_time = time.time()

        # Если задан путь к виртуальной файловой системе, разархивируем её
        if vfs_path:
            self.mount_vfs()

    def mount_vfs(self):
        # Заглушка: позже здесь будет логика для работы с zip-архивом
        print(f"Монтирую виртуальную файловую систему из {self.vfs_path}")

    def process_command(self, command):
        if command == "ls":
            return self.ls()
        elif command.startswith("cd "):
            return self.cd(command.split(" ", 1)[1])
        elif command == "exit":
            return self.exit()
        elif command == "uname":
            return self.uname()
        elif command == "uptime":
            return self.uptime()
        else:
            return f"Команда '{command}' не найдена"

    def ls(self):
        # Заглушка для команды ls
        return f"Содержимое директории {self.current_dir}: ..."

    def cd(self, path):
        # Заглушка для команды cd
        if path == "/":
            self.current_dir = "/"
        else:
            self.current_dir = os.path.normpath(os.path.join(self.current_dir, path))
        return f"Текущая директория: {self.current_dir}"

    def exit(self):
        return "Завершение работы эмулятора."

    def uname(self):
        return f"Эмуляция Unix shell на {self.hostname}"

    def uptime(self):
        elapsed = time.time() - self.start_time
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        return f"Время работы эмулятора: {int(hours)}ч {int(minutes)}м {int(seconds)}с"
