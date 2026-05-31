class Person:
    def __init__(self, name, job=None, pay=0): # Normal function args, job and pay are now optional
        self.name = name
        self.job = job
        self.pay = pay