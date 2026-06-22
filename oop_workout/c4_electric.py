from c1_vehicle import Vehicle
from c3_type import Car, Truck, Motorcycle

class ElectricCar(Vehicle):
    ''' Initialize the electric car inheriting from parent Vehicle with
      additional attributes battery capacity, range, and charge.'''
    def __init__(self, plate, make, model, year, battery_kwh, range_km):
        super().__init__(plate, make, model, year)
        self.battery_kwh = battery_kwh
        self.range_km = range_km
        self.__charge = 0.0

    def get_charge(self) -> float:
        return self.__charge

    """Add charge to the battery. Raises a ValueError for overcharging and negative values."""
    def charge(self, kwh: float) -> None:
        if kwh + self.__charge > self.battery_kwh:
            raise ValueError
        if kwh < 0:
            raise ValueError
        self.__charge += kwh


    """Calculate and consume battery power. update odometer if successful."""
    
    def drive(self, km: int) -> float:
       
        energy_required = (self.battery_kwh * km) / self.range_km
        
        if km <= 0:
            raise ValueError("Kilometres must be a positive number")
            
        if self.__charge - energy_required < 0:
            raise ValueError("Insufficient battery charge")
            
        self.__charge -= energy_required
        super().drive(km)
        
        return energy_required

    def describe(self) -> str:
        return f"{super().describe()}, electric car"
    

    
