class Building:
    no_of_rooms=50
    build_cnt=0
    def __init__(self, build_name):
        self.build_name=build_name
        Building.build_cnt+=1
        print(build_name)

    def change_rooms(self,nor):
        Building.no_of_rooms=nor

obj1 = Building("Tea labs")
obj2 = Building("Cake Facctory")
print(Building.build_cnt)
print(Building.no_of_rooms)