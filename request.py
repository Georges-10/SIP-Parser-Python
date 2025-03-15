from message import IMessage

class Request(IMessage):
    def __init__(self,type,to,froms):
        super().__init__(type,to,froms)
        
    def display(self):

        print('\n  🔹Type: '+self.type+' '+'\n    From: '+self.froms + '\n    To: '+ self.to) 