class TimeTraveler:
    registry = 0
    lst = []
    def __init__(self, codename, origin_year, destination_year):
        self.codename = codename
        self.origin_year=origin_year
        self.destination_year=destination_year
        TimeTraveler.registry+=1
        TimeTraveler.lst.append(codename)
    @classmethod
    def show_registry(cls):
        print(cls.registry)
        if cls.registry:
            print(cls.lst)
    @staticmethod
    def year_status(origin_year, destintion_year):
        if origin_year<destintion_year:
            return "Future"
        elif origin_year==destintion_year:
            return "Present"
        else:
            return "Past"

t1 = TimeTraveler("Red",2025,2027)
t2 = TimeTraveler("Blue",2024,2021)
t3 = TimeTraveler("Green",2025,2025)

TimeTraveler.show_registry()
print(t1.year_status(t1.origin_year,t1.destination_year))
print(t2.year_status(t2.origin_year,t2.destination_year))
print(t2.year_status(t3.origin_year,t3.destination_year))