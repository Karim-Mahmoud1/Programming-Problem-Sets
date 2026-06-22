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

if __name__ == "__main__":
    # Initialize instances for verification
    c = Car("B-CD-5678", "Toyota", "Yaris", 2023, seats=5)
    tr = Truck("B-CD-5678", "MAN", "Other", 2000, payload_kg=1)
    tr2 = Truck("B-EF-9012", "MAN", "TGX", 2021, payload_kg=18000)
    e = ElectricCar("B-EV-0001", "Tesla", "Model 3", 2024, battery_kwh=60.0, range_km=400)

    print("--- 1. TESTING STR AND REPR ---")
    print(f"str(c)  # {repr(str(c))}")
    print(f"repr(c) # {repr(repr(c))}")
    print(f"repr(tr2) # {repr(repr(tr2))}")
    print(f"repr(e)   # {repr(repr(e))}")

    print("\n--- 2. TESTING EQUALITY (PLATES AS IDENTITY) ---")
    same_plate_diff_car = Car("B-CD-5678", "Toyota", "Corolla", 2020)
    print(f"c == same_plate_diff_car # {c == same_plate_diff_car}")

    diff_plate_same_car = Car("B-XX-0000", "Toyota", "Yaris", 2023)
    print(f"c == diff_plate_same_car # {c == diff_plate_same_car}")

    print(f"c == tr # {c == tr}")
    
    print("\n--- 3. TESTING DICTIONARY/SET HASHABILITY ---")
    vehicle_set = {c, tr2, e}
    print(f"Successfully added vehicles to a set. Set size: {len(vehicle_set)}")