import os
import time
import zipfile
from logger import Logger


class Shell:
    def __init__(self, username="root", hostname="localhost", fs_path="filesystem.zip"):
        self.username = username
        self.hostname = hostname
        self.logger = Logger()
        self.current_dir = "/"
        self.start_time = time.time()
        self._file_system = {"/": []}
        self.load_file_system(fs_path)

    def load_file_system(self, fs_path):
        with zipfile.ZipFile(fs_path, 'r') as zf:
            for file in zf.namelist():
                path_parts = file.strip("/").split("/")
                if len(path_parts) == 1:
                    self._file_system["/"].append(f"/{path_parts[0]}")
                    self._file_system[f"/{path_parts[0]}"] = []
                else:
                    parent = "/" + "/".join(path_parts[:-1])
                    if parent not in self._file_system:
                        self._file_system[parent] = []
                    self._file_system[parent].append(f"/{'/'.join(path_parts)}")
                    self._file_system[f"/{'/'.join(path_parts)}"] = []

    def execute_command(self, command):
        self.logger.log_action(f"{self.username}@{self.hostname}", command)
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
            return f"Команда {command.split()[0]} не найдена"

    def ls(self):
        contents = self._file_system.get(self.current_dir, [])
        return "\n".join(sorted(os.path.basename(item.strip("/")) for item in contents))

    def cd(self, path):
        if path == "..":
            if self.current_dir == "/":
                return f"Ошибка: вы уже в корневой директории."
            self.current_dir = "/".join(self.current_dir.strip("/").split("/")[:-1]) or "/"
            return f"Текущая директория: {self.current_dir}"

        if path.startswith("/"):
            new_dir = path
        else:
            new_dir = os.path.normpath(os.path.join(self.current_dir, path))

        if new_dir in self._file_system:
            self.current_dir = new_dir
            return f"Текущая директория: {self.current_dir}"
        else:
            return f"Ошибка: директория '{path}' не найдена."

    def exit(self):
        self.logger.save()
        return "exit"

    def uname(self):
        return f"Darwin"

    def uptime(self):
        current_time = time.strftime("%H:%M")
        elapsed = int(time.time() - self.start_time)
        days, rem = divmod(elapsed, 86400)
        hours, seconds = divmod(rem, 3600)
        minutes = seconds // 60
        uptime_str = f"{days} days,  {hours}:{minutes:02d}" if days > 0 else f"{hours}:{minutes:02d}"
        return f"{current_time}  up {uptime_str}, 2 users, load averages: 2,20 2,19 2,15"