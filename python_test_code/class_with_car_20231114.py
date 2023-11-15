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
        print(f"The meter of the {self.make} from Ethan is {self.odometer_reading}")
        
    def update_meter(self,mileage):
        """禁止把数值回调"""
        if mileage >= self.odometer_reading:
              self.odometer_reading = mileage
        else:
            print("you cannot roll back an odometer")


""" 
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_meter()       #实例化的instance调用read_meter函数。
my_new_car.update_meter(25)      #通过修改属性值去更新属性。
print("After updated, the new meter is ")
my_new_car.read_meter()    
""" 
class Electricalcar(Car):
    """电动汽车继承super class父类也称为超类 Car"""
    def __init__(self, make, model, year):
        #先初始化父类的属性
        super().__init__(make, model, year)
        #再初始化电动车特有,superclass没有的属性
        self.battery_side = 40
    def describe_battery(self):
        print(f"This car has a {self.battery_side}-kWh bettery.")
    def update_battery(self):
        if self.battery_side != 65:
            self.battery_side = 65
""" 
my_electricalcar = Electricalcar('BYD','Song','2023')
print(my_electricalcar.get_descriptive_name())
my_electricalcar.describe_battery()
my_electricalcar.update_battery()
my_electricalcar.describe_battery()

""" 