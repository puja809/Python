import random

class RandomPasswordGenerator:
    def __init__(self, lengthOfReq):
        self.lengthOfReq = lengthOfReq;

    def randomStr(self):
        alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVW"
        alphaLower = alphaUpper.lower()
        digit = "0123456789"
        specialSymbol = "!~#$%*"
        return random.choice(alphaUpper+alphaLower+digit+specialSymbol)

    def sendPass(self):
        llo = ""
        for i in range(lengthOfReq):
            llo = llo + self.randomStr()
        return llo

lengthOfReq = int(input("What is the length of password you need?"))
R1 = RandomPasswordGenerator(lengthOfReq)
print("Your high secure password is: "+ R1.sendPass())