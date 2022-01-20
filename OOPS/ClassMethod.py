class Bank:
    minbal = 1000

    def __init__(self, acno, name, bal):
        self.name = name
        self.bal = bal
        self.acno = acno

    @classmethod
    def change_minbal(cls, amount):
        cls.minbal = amount

    # classmethods as alternative constructors
    @classmethod
    def from_string(cls, instr):
        acno, name, bal = instr.split('-')
        return cls(acno, name, bal)
    @staticmethod
    def