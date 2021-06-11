class atm:       
    def __init__(self,cashWithdrawl,userAtm,cardNumber,pinNumber):
        self.cashWithdrawl = cashWithdrawl
        self.userAtm = userAtm
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber   
    def getCashWithdrawl(self):
        return f"Account {self.userAtm} has withdrawl {self.cashWithdrawl} but need to upgrade kyc"           
    def getBalanceEnquiry(self):
        return f"Call 1800-230-200 to upgrade your kyc in account {self.userAtm} here is your pin Number {self.pinNumber} and card number {self.cardNumber}"

#creating the object
Atm = atm(10000,"whitehatjr","4331-0000",491441)
print(Atm.getCashWithdrawl())
print(Atm.getBalanceEnquiry())
