import xml.etree.ElementTree as ET
import datetime


class Logger:
    def __init__(self, log_file="logs.xml"):
        self.log_file = log_file
        self.root = ET.Element("session")

    def log_action(self, user, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = ET.SubElement(self.root, "action")
        ET.SubElement(entry, "timestamp").text = timestamp
        ET.SubElement(entry, "user").text = user
        ET.SubElement(entry, "command").text = action

    def save(self):
        tree = ET.ElementTree(self.root)
        with open(self.log_file, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)