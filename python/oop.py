class Person:
    def __init__(self,name,age,adddress):
        self.name=name
        self.age=age
        self.address=adddress

    
    def sleep(self):
        print(f'{self.name} is sleeping' )
        
    def talk(self):
        print(f'{self.name} is taking')
    def dancing (self):
        print(f'{self.name} is dancing ')
        
Unish=Person("Unish phyal",20,"kathmandu ")
print(Unish.name)
print(Unish.age)
print(Unish.address)
Unish.sleep()
Unish.talk()
Unish.dancing()
Aayush = Person("Aayush gc",43,"pokhara")
Aayush.talk()
