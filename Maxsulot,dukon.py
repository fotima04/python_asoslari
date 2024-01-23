class Maxsulot:
   def __init__(self,nomi,soni,narxi,mamlakat):
      self.nomi=nomi
      self.__soni=soni
      self.narxi=narxi
      self.mamlakat=mamlakat
      
   def get_info(self):
        return f"{self.nomi} {self.soni} {self.narxi}"
  
   def __repr__(self):
      return self.nomi
  
a1=Maxsulot("olma",2000,12000,"uzbekiston")
a2=Maxsulot("anor",3000,25000,"uzbekiston")
a3=Maxsulot("banan",5000,33000,"amerika")  
a4=Maxsulot("ananas",1200,12000,"afrika")

class Dukon:
     def __init__(self,nomi,manzili,turi):
         self.nomi=nomi
         self.manzili=manzili
         self.turi=turi
         self.Maxsulot=[]
         
     def get_info(self):
         return f"{self.nomi} {self.manzili}"
         
     def add_Maxsulot(self,maxsulot):
         self.Maxsulot.append(maxsulot)
         
     def get_Maxsulot(self):
         return self.Maxsulot
         
obj1= Dukon("Zamin","Xonqa tuman ", "oziq-ovqat") 
obj2= Dukon("Tomarisnur","Urganch shaxar","gipermarket")