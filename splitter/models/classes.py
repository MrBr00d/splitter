import logging
from utils import dbloader

logger = logging.getLogger(__name__)

class Group():
    def __init__(self, group_id:int):
        '''Create a Group class with a group name and group_id, the database is the queried for the group_id.
        If no group with the group_id exists a new group is created.'''
        # self.name = name
        # self.participants_loader = dbloader.load_participants(group_id)
        # self.participants = []
        # for user in self.participants_loader[0]:
        #     self.participants.append(Participant(user))

    def get_participants(self):
        return self.participants

class Participant():
    def __init__(self, name:str):
        self.name = name
        self.balance = None

class Transaction():
    def __init__(self, amount:float, payer:Participant,leechers: list ,wights:list):
        '''Provide the amount, payer and leechers of each transaction
        args: amount: float, payer: Participant'''
        pass