import logging
from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        logging.info("Hello, World!")
        print("Hello, World!")