from message import IMessage
from typing import Type
from request import Request
class MessageBuilder:
    def __init__(self, message_class: Type[IMessage] = Request):
        self._type = None
        self._to = None
        self._froms=None
        self.message_type = message_class

    def setType(self,type):
        self._type=type
        return self

    def setTo(self, to):
        self._to = to
        return self
    
    def setFrom(self,froms):
        self._froms=froms
        return self
    
    def setMessageClass(self, message_class: Type[IMessage]):
        self.message_type = message_class
        return self

    def build(self):
        return self.message_type(self._type, self._to,self._froms)    