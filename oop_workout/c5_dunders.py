from c1_vehicle import Vehicle
from c3_type import Car, Truck
from c4_electric import ElectricCar

def vehicle_str(self) -> str:
    return self.describe()

"""Return a specific string representation of the vehicle."""

def vehicle_repr(self) -> str:
    class_name = type(self).__name__
    return f"{class_name}('{self.plate}', '{self.make}', '{self.model}', {self.year})"

"""Check if two vehicles are identical by comparing plates."""

def vehicle_eq(self, other) -> bool:
    if not isinstance(other, Vehicle):
        return False
    return self.plate == other.plate

def vehicle_hash(self) -> int:
    return hash(self.plate)

Vehicle.__str__ = vehicle_str
Vehicle.__repr__ = vehicle_repr
Vehicle.__eq__ = vehicle_eq
Vehicle.__hash__ = vehicle_hash
