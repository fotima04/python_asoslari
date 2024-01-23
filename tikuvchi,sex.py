class Tikuvchi:
   def __init__(self,ismi,familiya,staji):
      self.ismi=ismi
      self.familiya=familiya
      self.staji=staji
      
   def get_info(self):
        return f"{self.ismi} {self.familiya} {self.staji}"
  
   def __repr__(self):
      return self.ismi
  
a1=Tikuvchi("Alisher","Qodirov","2 yil")
a2=Tikuvchi("Alibek","Qodirov","3 yil")
a3=Tikuvchi("Fotix","Yusupov","5 yil")  
a4=Tikuvchi("Azamat","Nurmetov","2,5 yil")

class Tikuvchiliksexi:
     def __init__(self,nomi,boshliq,ishchi_soni):
         self.nomi=nomi
         self.boshliq=boshliq
         self.ishchi_soni=ishchi_soni
         self.Tikuvchilar=[]
         
     def get_info(self):
         return f"{self.nomi} {self.firma_raqami} {self.manzili}"
         
     def add_Tikuvchilar(self,tikuvchi):
         self.Tikuvchilar.append(tikuvchi)
         
     def get_Tikuvchilar(self):
         return self.Tikuvchilar
         
obj1= Tikuvchiliksexi("Zamin","Fotima Nurmetova", 1240) 