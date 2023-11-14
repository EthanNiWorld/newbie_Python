#在python中，首字母大小写的名称指的是class类
class Dog:
    # _init_是特殊的方法，每次根据类创建实例时都会调用_init_
    def __init__(self,name,age):
        #初始化name和age
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")    
    
    def roll_over(self):
         print(f"{self.name} rolled over")   
my_dog = Dog('ethan',5)     #根据类来创建东西叫做实例化instance.
my_dog.sit() 
my_dog.roll_over()   

my_dog.sit() 