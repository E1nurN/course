class Person:
    name: str
    surname: str
    patronymic: str

    def toString(self):
        return f'Name: {self.name} Surname: {self.surname} Patronymic: {self.patronymic}'


class Driver(Person):
    drivingExperience: int

    def __init__(self, name: str, surname: str, patronymic: str, drivingExperience: int):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.drivingExperience = drivingExperience

    def toString(self):
        return f'Driver:\n\t{super().toString()} Driving experience: {self.drivingExperience}'


class Engine:
    power: int
    manufacturer: str
    
    def __init__(self, power: int, manufacturer: str):
        self.power = power
        self.manufacturer = manufacturer

    def toString(self):
        return f'Power: {self.power}, Manufacturer: {self.manufacturer}'


class Car:
    brand: str
    carClass: str
    weight: int
    driver: Driver
    engine: Engine

    def start(self) -> None:
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turnRigth(self):
        print("Поворот направо")

    def turnLeft(self):
        print("Поворот налево")

    def toString(self):
        return f'Car:\n\tBrand: {self.brand}\n\tCar class: {self.carClass}\n\tWeight: {self.weight}\n\tEngine: {self.engine.toString()}'

    def __init__(self, brand: str, carClass: str, weight: int, driver: Driver, engine: Engine):
        self.brand = brand
        self.carClass = carClass
        self.weight = weight
        self.driver = driver
        self.engine = engine


driver = Driver('f', 'i', 'o', 10)

print(driver.toString() + '\n')

e1 = Engine(400, 'a')

Lorry = Car("brand", "carClass", 1000, driver, e1)
print(Lorry.toString() + '\n')

e2 = Engine(1000, 'a')
SportCar = Car("brand", "caClass", 5000, driver, e2)
print(SportCar.toString() + '\n')