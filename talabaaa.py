class Talaba:
    __talabalar_soni=0
    def __init__(self,ism,familiya,guruh,shartnoma):
        Talaba.__talabalar_soni +=1
        self.__id=Talaba.__talabalar_soni
        self.ism=ism
        self.familiya=familiya
        self.guruh=guruh
        self.shartnoma=shartnoma
        
    def change_id(self,new):
        self.__id=new
        
    def get_id(self):
        return self.__id
    
    def get_count(cls):
        return cls.__talabalar_soni
     
    def get_info(self):
        return f"{self.ismi} {self.guruh}"

        
obj1=Talaba("Fotima", "Nurmetova", "941-22", "kantrakt")        
obj2=Talaba("Fozil", "Yoldashev", "941-21", "grant") 