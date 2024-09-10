from random import randint

class Train:
    def book(self,train_no,fro,to):
        print(f"Ticket is booked in {train_no} from {fro} to {to }\n")
        
    def getStatus(self,train_no):
        print(f"Your train with train number: {train_no} is running on Time:\n")
        
    def getFare(self,train_no,fro,to):
        print(f"Ticket fare in train number {train_no} from {fro} to {to} is ₹ {randint(555,999)}\n")
        
a=Train()
a.book(12655,"Ahemdabad","Vijaywada")
a.getStatus(12655)
a.getFare(12655,"Ahemdabad","Vijaywada")