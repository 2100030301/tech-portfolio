"""
Q6. Design a class Vehicle that:
•	Keeps a record of service charge rate common to all vehicles.
•	Each vehicle has a model, kilometers_run, and service history.
•	Has a function to calculate service charge based on km and rate.
•	Provides a method to update the service rate for all vehicles.
•	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
Demonstrate:
1.	Creating vehicles with different km and models.
2.	Updating the service rate.
3.	Showing charges and eligibility checks.
"""

class Vehicle:
    service_rate = 2
    def __init__(self, model, kilometers, year):
        self.model=model
        self.kilometers=kilometers
        self.year=year
    def service_charge(self):
        service_charge = self.kilometers * Vehicle.service_rate
        return service_charge
    @classmethod
    def update_service_rate(cls,new_rate):
        cls.service_rate=new_rate
    @staticmethod
    def check_vehicle(year):
        curren_year=2026
        return curren_year-year > 15

v1 = Vehicle("Honda City", 50000, 2015)
v2 = Vehicle("Toyota Innova", 80000, 2008)
print(v1.service_charge())
print(v2.service_charge())
v1.update_service_rate(3)
print(v1.service_charge())
print(v2.check_vehicle(v2.year))