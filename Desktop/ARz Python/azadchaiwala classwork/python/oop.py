# Object Oriented Programming
# Incapsulation
# Inheritance
# Polymorphism
# Abstraction




# class cat :
#     legs=4
#     tail=1
#     eyes=2
#     ears=2


#     def __init__(self,l,t):
#         self.legs = l
#         self.tail = t


#     def meow(self):
#         print('meow meow')

#     def play(self):
#         print('playing')


# cat1 = cat(4,False)
# cat2 = cat(3,True)
# print(cat1.legs)
# print(cat1.tail)
# print(cat1.eyes)
# print(cat1.ears)




# cat1.play()
# cat2.play()




# class student:
#     name='Abdul Rehman'
#     age=18
#     st_id='307'
#     marks=919
#     subject='cs'




#     def study(self):
#         print('studying')


#     def attend_school(self):
#         print('attending')

#     def intro(self):
#         print('introducing')

#     student = student()




# class circle:
#     def __init__(self,r):
#         self.a= 3.14*r*r
#         print(self.a)

# circle = circle(3)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def intro(self):
#         print(f'My name is {self.name} and my age is {self.age}')
        

# person = Person('Abdul Rehman Zaheer',18)

# person.intro()

# class Student(Person):
#     def __init__(self, name, age,rollno,marks):
#         super().__init__(name, age)

# s = Student('Rafay',17,97,860)
# s.intro()
# print(s.name,s.age)


# Task 1
# class Animal:
    
#     def speak(self):
#         print('Animal speaks')
        
# animal = Animal()
# animal.speak()

# class Dog(Animal):
#     def speak(self):
#         print('Dog Barks')

# dog = Dog()
# dog.speak()




# Task 2
# class Vehicle:
#     def __init__(self,speed) :
#         self.speed = speed


#     def drive(self):
#         print('Driving')


# class Car(Vehicle):
#     def air_condition(self):
#         print('open Ac')


    
# class Bike(Vehicle):
#     def Wheelie(self):
#         print('Wheelie maar')




# Task 3
# class Animal:
#     def eyes(elf):
#         print('animals have eyes')

# class Mammal(Animal):
#     def reproduce(self):
#         print('Mammals can reproduce')

# class Human(Mammal):
#     def talk(self):
#         print('Human can Talk')



# Task 4
# class FlyingCreature:
#     def fly(self):
#         print('fly')


# class SwimmingCreature:
#     def swim(self):
#         print('swim')


# class Duck(FlyingCreature,SwimmingCreature):
#     pass



class Car:
    @staticmethod
    def Checkfeul():
        print('Feul is full')

    @staticmethod
    def CheckEngine():
        print('Engine is good')

    def Start(self):
        self.Checkfeul()
        self.CheckEngine()

# c=Car()
# c.start()
Car.CheckEngine()
Car.Checkfeul()