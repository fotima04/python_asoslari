class futbolchi:
   def __init__(self,ismi,yoshi,kim_bolib_oynaydi,gollar_soni):
      self.ismi=ismi
      self.yoshi=yoshi
      self.kim_bolib_oynaydi=kim_bolib_oynaydi
      self.gollar_soni=gollar_soni
      
   def get_info(self):
        return f"{self.ismi} {self.yoshi} "
  
   def __repr__(self):
      return self.ismi
  
a1=futbolchi("Alisher",22,"xujumchi",12)
a2=futbolchi("Alibek",24,"ximoyachi",10)

class jamoa:
     def __init__(self,nomi,galabalar_soni,maglubiyatlar_soni):
         self.nomi=nomi
         self.galabalar_soni=galabalar_soni
         self.maglubiyatlar_soni=maglubiyatlar_soni
         self.futbolchilar=[]
         
     def get_info(self):
         return f"{self.nomi} {self.galabalar_soni} {self.maglubiyatlar_soni}"
         
     def add_futbolchilar(self,futbolchi):
         self.futbolchilar.append(futbolchi)
         
     def get_futbolchilar(self):
         return self.futbolchilar
         
obj1= jamoa("Paxtakor",200,12) 