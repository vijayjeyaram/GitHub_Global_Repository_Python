from Python_Learning_Project.PY_Code.Py_Class import *

# If you want to access class variable and methods you need to create object
# Syntax:
# objectName = class name

#Object - 1
car_01 = Cars()
car_01.brandName = "Toyota"
car_01.modelName = "Innova"
car_01.price = 100000

#Object - 1
car_02 = Cars()
car_02.brandName = "Tata"
car_02.modelName = "Hexa"
car_02.price = 150000

#Object - 1
car_03 = Cars()
car_03.brandName = "Tesla"
car_03.modelName = "Model3"
car_03.price = 350000

print("Tesla Car Price", car_03.price)
