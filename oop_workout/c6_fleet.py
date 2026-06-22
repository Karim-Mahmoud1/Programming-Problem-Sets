from c1_vehicle import Vehicle
from c3_type import Car, Truck, Motorcycle
from c4_electric import ElectricCar
import c5_dunders  

class Fleet:
    """initialize the fleet with base attributes"""
    def __init__(self, name: str):
        self.name = name
        self._vehicles: dict[str, Vehicle] = {}


    """Add a vehicle to the fleet. Raises ValueError if plate is already registered."""
    def add(self, vehicle: Vehicle) -> None:
        if vehicle.plate in self._vehicles:
            raise ValueError(f"Vehicle with plate {vehicle.plate} is already in the fleet.")
        self._vehicles[vehicle.plate] = vehicle
    
    """Remove a vehicle by its plate. Raises KeyError if not found."""
    def remove(self, plate: str) -> None:
        if plate not in self._vehicles:
            raise KeyError(f"Plate {plate} not found in fleet.")
        del self._vehicles[plate]

    def find(self, plate: str) -> Vehicle | None:
        return self._vehicles.get(plate, None)

    def total_kilometres(self) -> int:
        return sum(v.kilometres for v in self._vehicles.values())

    """Attempt to drive every vehicle. 
        
    Returns a tuple of successful plates and failures.
    """
    def drive_all(self, km: int) -> tuple[list[str], list[tuple[str, str]]]:

        successes = []
        failures = []
        
        for plate, vehicle in self._vehicles.items():
            try:
                vehicle.drive(km)
                successes.append(plate)
            except Exception as e:
                failures.append((plate, str(e)))
                
        return successes, failures

    def __len__(self) -> int:
        return len(self._vehicles)

    def __iter__(self):
        return iter(self._vehicles.values())

    def __contains__(self, plate: str) -> bool:
        return plate in self._vehicles

    def __str__(self) -> str:
        return f"Fleet '{self.name}': {len(self)} vehicle(s)"


"""Print a summary report of the entire fleet """
def print_summary(fleet: Fleet) -> None:

    print("=== FLEET REPORT ===")
    print(str(fleet))
    print(f"Total kilometres: {fleet.total_kilometres()}")
    print("--------------------")
    for vehicle in fleet:
        print(str(vehicle))
    print("====================")



    
 