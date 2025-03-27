class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"


class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars_owned = []

    def purchase_car(self, car):
        self.cars_owned.append(car)
        print(f"{self.name} just purchased a {car.get_car_info()}.")

    def show_owned_cars(self):
        print(f"{self.name} owns the following cars:")
        for index, car in enumerate(self.cars_owned, start=1):
            print(f"{index}. {car.get_car_info()}")


def main():
    car1 = Car("Toyota", "Camry", 2010)
    car2 = Car("Tesla", "Model 3", 2022)
    car3 = Car("Ford", "Mustang", 1967)
    car4 = Car("Honda", "Civic", 2019)

    owner1 = Owner("Alice", 30)
    owner2 = Owner("Bob", 45)

    owner1.purchase_car(car1)
