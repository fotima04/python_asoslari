class ustoz:
   def __init__(self,ismi,yoshi,maktab,sinf):
      self.ismi=ismi
      self.yoshi=yoshi
      self.maktab=maktab
      self.sinf=sinf
      
   def get_info(self):
        return f"{self.ismi} {self.yoshi} {self.sinf}"
  
   def __repr__(self):
      return self.ismi
  
a1=ustoz("Alisher",32,"24-maktab", 10 )
a2=ustoz("Alibek",38, "17-maktab",11)

class maktab:
     def __init__(self,nomi,raqami,manzili,urni):
         self.nomi=nomi
         self.raqami=raqami
         self.manzili=manzili
         self.urni=urni
         self.ustozlar=[]
         
     def get_info(self):
         return f"{self.nomi} {self.raqami} "
         
     def add_ustozlar(self,ustoz):
         self.ustozlar.append(ustoz)
         
     def get_ustozlar(self):
         return self.ustozlar
         
obj1= maktab("Al-xorazmiy",24,"xonqa tuman ", 6) 