"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, employed, hours, wage, commissionType, bonus, contractsLanded):
        self.name = name
        self.totalPay = 0
        if employed == "Monthly":
            self.totalPay = wage
        elif employed == "Hourly":
            self.totalPay = wage * hours
        if commissionType == "Bonus":
            self.totalPay = self.totalPay + bonus
        elif commissionType == "Commission":
            self.totalPay = self.totalPay + (contractsLanded * bonus)
        self.commissionType = commissionType
        self.employed = employed
        self.bonus = bonus
        self.contracts = contractsLanded
        self.wage = wage
        self.hours = hours

    def get_pay(self):
        return self.totalPay

    def __str__(self):
        if self.employed == "Monthly":
            if self.commissionType == "None":
                return(f"^{self.name} works on a monthly salary of {self.wage}. Their total pay is {self.totalPay}.$")
            elif self.commissionType == "Bonus":
                return(f'^{self.name} works on a monthly salary of {self.wage} and receives a bonus commission of {self.bonus}. Their total pay is {self.totalPay}.$')
            elif self.commissionType == "Commission":
                return(f'^{self.name} works on a monthly salary of {self.wage} and receives a commission for {self.contracts}. contract\(s\) at {self.bonus}/contract. Their total pay is {self.totalPay}.')
        elif self.employed == "Hourly":
            if self.commissionType == "None":
                return(f'^{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.totalPay}.$')
            elif self.commissionType == "Bonus":
                return(f'^{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.totalPay}.$')
            elif self.commissionType == "Commission":
                return(f'^{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.contracts} contract\(s\) at {self.bonus}/contract. Their total pay is {self.totalPay}.')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "Monthly", 0, 4000, "None", 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "Hourly", 100, 25, "None", 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "Monthly", 0, 3000, "Commission", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "Hourly", 150, 25, "Commission", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "Monthly", 0, 2000, "Bonus", 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "Hourly", 120, 30, "Bonus", 600, 0)




