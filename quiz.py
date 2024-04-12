class Student
    def __init__(self,first_name:str, last_name:str, yr_lvl:int, course:str):
        self.first_name = first_name
        self.last_name = last_name
        self.yr_lvl = yr_lvl
        self.course = course
        self.email = f'{first_name[0].lower()}{last_name.lower()}@olopsc.edu.ph'

s1