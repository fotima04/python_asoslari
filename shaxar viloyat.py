class Shaxar:
   def __init__(self,tuman_nomi,xolati):
      self.tuman_nomi=tuman_nomi
      self.xolati=xolati
      
   def get_info(self):
        return f"{self.tuman_nomi} {self.xolati} "
  
   def __repr__(self):
      return self.tuman_nomi
  
a1=Shaxar("xonqa","yaxshi")
a2=Shaxar("xiva","yaxshi")


class viloyat:
     def __init__(self,nomi,yer_maydoni,aholi_soni,respublikasi):
         self.nomi=nomi
         self.yer_maydoni=yer_maydoni
         self.aholi_soni=aholi_soni
         self.respublikasi=respublikasi
         self.shaxarlari=[]
         
     def get_info(self):
         return f"{self.nomi} {self.yer_maydoni} "
         
     def add_shaxarlari(self,shaxar):
         self.shaxarlari.append(shaxar)
         
     def get_shaxarlari(self):
         return self.shaxarlari
         
obj1= viloyat("Xorazim","144 km.kv", 3245890,"Uzbekiston") 