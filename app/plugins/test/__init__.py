import logging
from app.commands import Command

class TestCommand(Command):
    # inheriting from abc command
    def execute(self):
        logging.info("This is a test message!")
        print("This is a test message!")