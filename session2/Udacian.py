class Udacian: 
    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    def print_udacain(self):
        print(self.name + " is Living in " + self.city + " and is studying " + self.nanodegree + " and enrolled in " + self.enrollment + ", he/she is " + self.status )
enrollment = ("Mon virtual")
u2 = Udacian("Saud","Riyadh",enrollment,"FSND","On track")
u2.print_udacain()
