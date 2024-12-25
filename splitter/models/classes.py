import logging
from utils import dbloader

logger = logging.getLogger(__name__)

class Group():
    def __init__(self, group_id:int):
        '''Create a Group class with a group name and group_id, the database is the queried for the group_id.
        If no group with the group_id exists a new group is created.'''
        self.group_data, self.participant_data = dbloader.load_group(group_id)
        self.name = self.group_data[0]
        self.participants = []
        for name, balance in self.participant_data:
            self.participants.append(Participant(name, balance))

    def get_participants(self):
        return [x.name for x in self.participants]

class Participant():
    def __init__(self, name:str, balance):
        self.name = name
        self.balance = None
    def __str__(self):
        return f"Participant class instance of {self.name}"
    def get_balance(self):
        return self.balance

class Transaction():
    def __init__(self, amount:float, payer:Participant,leechers: list ,wights:list):
        '''Provide the amount, payer and leechers of each transaction
        args: amount: float, payer: Participant'''
        pass