from transaction import Transaction
from messageBuilder import MessageBuilder
from request import Request
from response import Response
import sys

class SipParser:
    def __init__(self,file_path):
        self.file_path = file_path
        self.transactions:  dict[str,Transaction] = {}
        self.request_type = ['INVITE', 'ACK', 'BYE', 'CANCEL', 'REGISTER', 'OPTIONS', 'INFO', 'PRACK', 'SUBSCRIBE', 'NOTIFY', 'PUBLISH', 'MESSAGE', 'REFER', 'UPDATE']
        self.user_info = ['From', 'To', 'Call-ID']

    # principal and only public method to parse the file
    def parse(self):
        current_id = ''
        current_message= MessageBuilder()
        current_transaction = Transaction([])
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue
                    list_line = line.split()
                    token = list_line[0].rstrip(":")

                    if token.isdigit():
                        current_message.setMessageClass(Response)
                        current_message.setType(line)

                    elif token in self.request_type:
                        current_message.setMessageClass(Request)
                        current_message.setType(token)

                    elif token == 'Call-ID':
                        if current_id!='' and list_line[1] not in self.transactions:
                            current_transaction = Transaction([])
                        
                        current_transaction._add_message(current_message.build())
                        current_message= MessageBuilder()
                        current_id = list_line[1]
                        
                        if current_id not in self.transactions:
                            self.transactions[current_id]=current_transaction
                        continue
                    self._add_info(list_line, token, current_message)
                
        except Exception as e:
            print("Error:", e)
    
    
    # add the users information to the current message
    def _add_info(self, list_line, token,current_message):
        if token in self.user_info:
            match token:
                case 'From':
                    current_message.setFrom("".join(list_line[1:]))
                case 'To':
                    current_message.setTo("".join(list_line[1:]))
                case _:
                    pass

    def display_transactions(self):
        for call_id, transaction in self.transactions.items():
            print(f"\n📞 Call-ID: {call_id}")
            transaction._display_messages()
            print("-" * 50)
        print(" Réalisé par: Georges Neil Mboungani\n ")

def main():
    if len(sys.argv) == 1:
        parser = SipParser('sip_multi_log.txt')
        parser.parse()
        parser.display_transactions()
    else:
        for i in range(1, len(sys.argv)):
            print(f" --------------------FILE {i}------------------  : {sys.argv[i]}")  
            parser = SipParser(sys.argv[i])
            parser.parse()
            parser.display_transactions()


if __name__ == "__main__":
    main()