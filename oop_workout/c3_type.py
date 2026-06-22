from c1_vehicle import Vehicle
from c2_tank import FuelTank

class FuelledVehicle(Vehicle):

    """Initialize a fuelled vehicle by setting up the base attributes, 
a custom FuelTank, and consumption rate."""

    def __init__(self, plate, make, model, year, capacity: float, consumption: float):
        super().__init__(plate, make, model, year)
        self.tank = FuelTank(capacity)
        self.consumption = float(consumption)

    def refuel(self, litres: float) -> None:
        self.tank.fill(litres)

    """Calculate and consume the required fuel before updating 
the odometer for the driven distance."""

    def drive(self, km: int) -> float:

        fuel_required = (km * self.consumption) / 100
        self.tank.consume(fuel_required)
        super().drive(km)
        
        return fuel_required

    def range_remaining(self) -> float:
        return (self.tank.get_level() / self.consumption) * 100


class Car(FuelledVehicle):
    def __init__(self, plate, make, model, year, seats: int = 5):
        super().__init__(plate, make, model, year, capacity=50.0, consumption=6.0)
        self.seats = seats

    def describe(self) -> str:
        return f"{super().describe()}, car, {self.seats} seats"


class Truck(FuelledVehicle):
    def __init__(self, plate, make, model, year, payload_kg: int):
        super().__init__(plate, make, model, year, capacity=200.0, consumption=18.0)
        self.payload_kg = payload_kg

    def describe(self) -> str:
        return f"{super().describe()}, truck, {self.payload_kg} kg payload"


class Motorcycle(FuelledVehicle):
    def __init__(self, plate, make, model, year):
        super().__init__(plate, make, model, year, capacity=15.0, consumption=3.5)

    def describe(self) -> str:
        return f"{super().describe()}, motorcycle"

class Van(FuelledVehicle):
    def __init__(self, plate, make, model, year, volume_m3: float):
        super().__init__(plate, make, model, year, capacity=75.0, consumption=9.0)
        self.volume_m3 = volume_m3

    def describe(self) -> str:
        return f"{super().describe()}, van, {self.volume_m3} m³ volume"
