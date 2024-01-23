from openpyxl import Workbook

obj=Workbook()

# jadval=obj.active 

# jadval["B2"]="salom"
# jadval["C5"]="24"
# jadval["A2"]="xayr"

# jadval.append([1,2,3,4,5,6,7])

# print(jadval["A2"].value)

obj.save("hujjat.xlsx")