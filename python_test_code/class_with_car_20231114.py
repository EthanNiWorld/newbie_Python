class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        #初始化汽车属性
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 23 #追加

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    def read_meter(self):
        print(f"The meter of the {my_new_card.make} from Ethan is {my_new_card.odometer_reading}")
        
    def update_meter(self,mileage):
        """禁止把数值回调"""
        if mileage >= self.odometer_reading:
              self.odometer_reading = mileage
        else:
            print("you cannot roll back an odometer")


    
my_new_card = Car('audi','a4',2024)
print(my_new_card.get_descriptive_name())
my_new_card.read_meter()       #实例化的instance调用read_meter函数。
my_new_card.update_meter(20)      #通过修改属性值去更新属性。
print("After updated, the new meter is ")
my_new_card.read_meter()    



        