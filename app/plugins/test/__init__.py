import logging
from icecream import ic
from app.commands import Command

class TestCommand(Command):
    # inheriting from abc command
    def execute(self):
        logging.info("This is a test message!")

        mydict = {1,2,3,4,5}
        logging.debug(print(ic(mydict)))

        print("This is a test message!")