class Shaxs:
    __odamlar_soni=0
    def __init__(self,ism,familiya,ish_joyi,JSHSHIR):
        Shaxs.__odamlar_soni +=1
        self.__JSHSHIR=JSHSHIR
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        
    def change_JSHSHIR(self,new):
        self.__JSHSHIR=new
        
    def get_JSHSHIR(self):
        return self.__JSHSHIR
    
    def get_count(cls):
        return cls.__odamlar_soni
     
    def get_info(self):
        return f"{self.ismi} {self.ish_joyi}"

        
obj1=Shaxs("Fotima", "Nurmetova", "Tatu filial",12343246736624)        
obj2=Shaxs("Fozil", "Yoldashev","Fayz hotel",76584932159473) 