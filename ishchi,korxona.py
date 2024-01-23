class Ishchi:
   def __init__(self,ismi,guruh_raqami,staji):
      self.ismi=ismi
      self.guruh_raqami=guruh_raqami
      self.staji=staji
      
   def get_info(self):
        return f"{self.ismi} {self.guruh_raqami} {self.staji}"
  
   def __repr__(self):
      return self.ismi
  
a1=Ishchi("Alisher",2,"2 yil")
a2=Ishchi("Alibek",2,"3 yil")
a3=Ishchi("Fotix",3,"5 yil")  
a4=Ishchi("Azamat",3,"2,5 yil")

class Korxona:
     def __init__(self,nomi,firma_raqami,manzili):
         self.nomi=nomi
         self.firma_raqami=firma_raqami
         self.manzili=manzili
         self.Ishchilar=[]
         
     def get_info(self):
         return f"{self.nomi} {self.firma_raqami} {self.manzili}"
         
     def add_Ishchilar(self,ishchi):
         self.Ishchilar.append(ishchi)
         
     def get_Ishchilar(self):
         return self.Ishchilar
         
obj1= Korxona("Zamin", 12,"Xonqa tuman ") 
obj2= Korxona("IMB servis",10,"Urganch shaxar")