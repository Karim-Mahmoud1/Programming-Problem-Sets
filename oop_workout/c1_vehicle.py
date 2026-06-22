
class Vehicle:
    fleet_size = 0

    ''' the __init__ method
    defines the attributes of the vehicle class
    '''
    def __init__(self, plate, make, model, year):
        self.plate = plate
        self.make = make
        self.model = model
        self.year = year
        self.kilometres = 0
        Vehicle.fleet_size += 1 

    ''' the drive method increments km to the base kilometres attribute based on how many km a vehicle drives.
    It raises a ValueError if the km is negative.
    '''
    def drive(self, km: int) -> None:
        if km > 0:
            self.kilometres += km
        else:
            raise ValueError("Kilometres must be a positive number")
        
    def describe(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.plate})"
    
    '''
    the service_due method returns True if the vehicle
      has travelled more than 15,000 km to indicate
        that it is due for a service.
    
    '''
    
    def service_due(self) -> bool:
        if self.kilometres > 15000:
            return True
        else:
            return False
        

    

    