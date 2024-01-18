class Shaxs:
    def __init__(self,ism,familiya,ish_joyi):
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.ish_joyi} "
    
    def __repr__(self):
        return self.ism
    
class Foydalanuvchi(Shaxs):
     def __init__(self,ism,familiya,ish_joyi,tel):   
        super().__init__(ism,familiya,ish_joyi)
        self.tel=tel
        
     def get_info(self):
         full= super().get_info()
         full+=self.tel
         return full
        
obj1=Foydalanuvchi("Fotima", "Nurmetova", "TATU", "+998977920403")

class Admin(Foydalanuvchi):
      def __init__(self,ism,familiya,ish_joyi,tel,manzili):   
         super().__init__(ism,familiya,ish_joyi,tel)
         self.manzili=manzili
         
      def get_info(self):
          full= super().get_info()
          full+=self.tel
          return full
      def ban_user(self):
          return "Foydalanuvchi bloqlandi"