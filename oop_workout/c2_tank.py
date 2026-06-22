class FuelTank:
    '''init method defines the attributes of the FuelTank class. raises a value error if the capacity is less than or equal to 0'''
    def __init__(self, capacity: float):
        if capacity <= 0:
            raise ValueError
        
        self.__capacity = capacity
        self.__level = 0.0
        
    def get_level(self) -> float:
        return round(self.__level, 2)
    
    def get_capacity(self) -> float:
        return self.__capacity
    
    ''' the fill method adds litres to the tank. Raises a ValueError 
    if the litres is less than or equal to 0. Raises a ValueError if tfilling more than capacity'''
    def fill(self, litres: float) -> None:
        if litres <=0:
            raise ValueError
        elif litres + self.__level > self.__capacity:
            raise ValueError
        
        self.__level += litres

    ''' the consume method removes litres from the tank. Raises a ValueError 
    if the litres is less than or equal to 0. Raises a ValueError if consuming more than the tank level'''
    def  consume(self,litres: float) -> None:
        if litres <=0:
            raise ValueError
        if self.__level - litres < 0:
            raise ValueError
        
        self.__level -= litres

    ''' the fill_to_full method fills the tank to the full.'''
    def fill_to_full(self) -> float:

        litres_needed = self._capacity - self.__level

        self.__level = self._capacity
        return float(litres_needed)

    ''' the percent_full method returns the percentage of the tank that is full.'''
    def percent_full(self) -> float:

        percentage = (self.__level / self._capacity) * 100
        return round(percentage, 1)

