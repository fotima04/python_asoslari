#inkapsulyatsiya
class Kompyuter:
    __number=0
    def __init__(self,nomi,xotirasi,protsessori,narxi):
        Kompyuter.__number += 1
        self.__id=Kompyuter.__number
        self.nomi=nomi
        self.xotirasi=xotirasi
        self.protsessori=protsessori
        self.narxi=narxi
    def get_id(self):
        return self.__id
    
    def get_count(cls):
        return cls.__number
     
    def get_info(self):
        return f"{self.nomi} {self.narxi}"

        
obj1=Kompyuter("Victus", "512 Gb", "Intel Core i5", 10890000)        
obj2=Kompyuter("HP", "256 Gb", "Intel Core i3", 5800000) 