from tkinter import *
from tkinter.font import Font
from shell import Shell

class Terminal:
    def __init__(self, root, shell):
        self.root = root
        self.shell = shell

        self.root.title("Terminal_emulator")
        self.root.geometry("800x600")

        self.font = Font(family="FiraCodeNFM-Ret", size=18)

        self.editor = Text(root, wrap="word", font=self.font, bg="black", fg="white", insertbackground="white")
        self.editor.pack(fill=BOTH, expand=1)

        self.editor.bind("<Return>", self.on_enter)
        self.editor.bind("<Key>", self.on_key_press)
        self.editor.focus_set()

        self.insert_prompt()

    def insert_prompt(self):
        prompt = f"{self.shell.username}@{self.shell.hostname}:{self.shell.current_dir} $ "
        self.editor.insert("end", prompt)
        self.editor.mark_set("prompt", "end-1c")
        self.editor.see("end")

    def on_key_press(self, event):
        prompt_index = self.editor.index("prompt")
        if self.editor.compare("insert", "<", prompt_index):
            return "break"

    def on_enter(self, event):
        current_line = self.editor.index("insert").split(".")[0]
        user_input = self.editor.get(f"{current_line}.0", "end").strip()

        prompt_length = len(f"{self.shell.username}@{self.shell.hostname}:{self.shell.current_dir} $ ")
        command = user_input[prompt_length:]

        result = self.shell.execute_command(command)

        if result == "exit":
            self.root.quit()
            return "break"

        if result:
            self.editor.insert("end", f"\n{result}")
        self.editor.insert("end", "\n")
        self.insert_prompt()
        return "break"

    def execute_on_startup(self, command):
        self.editor.insert("end", f"{command}\n")
        result = self.shell.execute_command(command)
        if result:
            self.editor.insert("end", f"{result}\n")
        self.insert_prompt()