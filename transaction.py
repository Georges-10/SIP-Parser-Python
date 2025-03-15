from typing import Dict, List
from message import IMessage
from response import Response

class Transaction:
    def __init__(self,messages:List[IMessage]):
        self.messages=messages

    def _add_message(self,message):
        self.messages.append(message)
    
    def _display_messages(self):
        is_displayed=False
        for message in self.messages:
            if isinstance(message, Response):# just to display "responses" once
                print(f"\n  🔸reponses:") if  is_displayed==False else None
                is_displayed=True
            else: is_displayed=False
            message.display()