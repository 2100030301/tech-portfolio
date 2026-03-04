class Movie:
    language = "Telugu"
    def __init__(self,director,hero,tp):
        self.director=director
        self.hero=hero
        self.tp =tp
    def collections(self,tickets):
        return self.tp*tickets
    def dub(self,lang):
        self.language=lang
m1=Movie("Puri","Mahesh",100)
print(m1.language)
m1.dub("Hindi")
print(m1.language)