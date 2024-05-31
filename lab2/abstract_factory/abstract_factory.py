from abc import ABC, abstractmethod

# Abstract Product Classes
class Laptop(ABC):
    @abstractmethod
    def get_laptop(self):
        pass

class Smartphone(ABC):
    @abstractmethod
    def get_smartphone(self):
        pass

# Concrete Product Classes
class IProneLaptop(Laptop):
    def get_laptop(self):
        return "IProne Laptop"

class IProneSmartphone(Smartphone):
    def get_smartphone(self):
        return "IProne Smartphone"

class KiaomiLaptop(Laptop):
    def get_laptop(self):
        return "Kiaomi Laptop"

class KiaomiSmartphone(Smartphone):
    def get_smartphone(self):
        return "Kiaomi Smartphone"

class BalaxyLaptop(Laptop):
    def get_laptop(self):
        return "Balaxy Laptop"

class BalaxySmartphone(Smartphone):
    def get_smartphone(self):
        return "Balaxy Smartphone"

# Abstract Factory
class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass

    @abstractmethod
    def create_smartphone(self):
        pass

# Concrete Factories
class IProneFactory(DeviceFactory):
    def create_laptop(self):
        return IProneLaptop()

    def create_smartphone(self):
        return IProneSmartphone()

class KiaomiFactory(DeviceFactory):
    def create_laptop(self):
        return KiaomiLaptop()

    def create_smartphone(self):
        return KiaomiSmartphone()

class BalaxyFactory(DeviceFactory):
    def create_laptop(self):
        return BalaxyLaptop()

    def create_smartphone(self):
        return BalaxySmartphone()

# Client Code
def main():
    for factory in (IProneFactory(), KiaomiFactory(), BalaxyFactory()):
        laptop = factory.create_laptop()
        smartphone = factory.create_smartphone()
        print(laptop.get_laptop())
        print(smartphone.get_smartphone())

if __name__ == "__main__":
    main()
