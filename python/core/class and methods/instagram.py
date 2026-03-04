class Profile:
    def __init__(self , username):
        self.followers=0
        self.username=username
    def follow(self):
        print("Someone Started following you")
        self.followers+=1
    def update_profile(self,un):
        self.username=un

p1 = Profile("Rishi_laghuvarapu")
print(p1.username)
print(p1.followers)
p1.follow()
p1.update_profile("Rishita_laghuvarapu")
print(p1.username)
print(p1.followers)