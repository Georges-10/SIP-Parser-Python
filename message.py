from abc import ABC, abstractmethod
class IMessage(ABC):
    
    def __init__(self,type,to,froms):
        super().__init__()
        self.type=type
        self.to=to
        self.froms=froms
    @abstractmethod
    def display(self):
        print('\n  🔹Type: '+self.type+' '+'\n    From: '+self.froms + '\n    To: '+ self.to)
