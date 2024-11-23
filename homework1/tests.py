import unittest
from io import StringIO
from unittest.mock import patch
import os
from shell import Shell
import time


class TestCommands(unittest.TestCase):
    def test_ls1(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        self.assertEqual(shell.ls().split()[0], "bin")

    def test_ls2(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        shell.cd("cd boot")
        self.assertEqual(shell.ls(), "grub")

    def test_ls3(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        shell.cd("cd data")
        self.assertEqual(shell.ls().split()[0], "backups")
        self.assertEqual(shell.ls().split()[1], "database")
        self.assertEqual(shell.ls().split()[2], "logs")
        self.assertEqual(shell.ls().split()[3], "temp")

    def test_cd1(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        self.assertEqual(shell.cd("cd bin"), "Текущая директория: /bin")

    def test_cd2(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        self.assertEqual(shell.cd("cd data"), "Текущая директория: /data")

    def test_cd3(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        self.assertEqual(shell.cd("cd"), "Текущая директория: /")

    def test_uname(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        self.assertEqual(shell.uname(), "Darwin")

    def test_uptime(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        self.assertEqual(shell.uptime().split()[0], str(time.strftime("%H:%M")))

    def test_exit(self):
        shell = Shell("root", "localhost", "filesystem.zip")
        self.assertEqual(shell.exit(), "exit")




if __name__ == '__main__':
    unittest.main()