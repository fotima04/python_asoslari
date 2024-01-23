class Kompyuter:
    def __init__(self,nomi,xotirasi,protsessori,narxi):
        self.nomi=nomi
        self.xotirasi=xotirasi
        self.protsessori=protsessori
        self.narxi=narxi
        
    def get_info(self):
        return f"{self.nomi} {self.xotirasi} {self.protsessori} {self.narxi}"
        
    def update_narxi(self,n):
        self.narxi= self.narxi+n
        
    def __repr__(self):
        return self.nomi
    
    def __call__(self,narx2):
        self.narxi+=narx2
        
obj1=Kompyuter("Victus", "512 Gb", "Intel Core i5", 10890000)        
obj2=Kompyuter("HP", "256 Gb", "Intel Core i3", 5800000) 
obj3=Kompyuter("Aser", "128 Gb", "Intel Core i3", 5800000) 
obj4=Kompyuter("HP", "256 Gb", "Intel Core i3", 5800000) 

class Kompyuter_dukon:
     def __init__(self,nomi,manzili,telefoni):
         self.nomi=nomi
         self.manzili=manzili
         self.telefoni=telefoni
         self.kompyuterlar =[]
         
     def get_info(self):
         return f"{self.nomi} {self.manzili} {self.telefoni}"
         
     def __call__(self,komp):
         self.kompyuterlar.append(komp)
         
     def __getitem__(self,index):
         return self.kompyuterlar[index]
     
     def __setitem__(self,index,obj):
         self.kompyuterlar[index]=obj
         
         
     def get_kompyuter(self):
         return self.kompyuterlar        
         
dukon = Kompyuter_dukon("IBM","Urganch 5 blok", "+999871234444")   
      
dukon(obj1)         
dukon(obj2)
dukon(obj3)         
dukon(obj4)         
         
         