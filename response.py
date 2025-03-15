from message import IMessage

class Response(IMessage):
    def __init__(self,type,to,froms):
        super().__init__(type,to,froms)

    def display(self):
        print('    - '+self.type.replace('\n','')+ ' From: '+self.froms) 
   