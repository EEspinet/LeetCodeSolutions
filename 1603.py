class ParkingSystem:
    bigNum = 0
    mediumNum = 0
    smallNum = 0

    def __init__(self, big: int, medium: int, small: int):
        self.bigNum = big
        self.mediumNum = medium
        self.smallNum = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigNum > 0:
                self.bigNum -= 1
                return True
            return False
        elif carType == 2:
            if self.mediumNum > 0:
                self.mediumNum -= 1
                return True
            return False
        elif carType == 3:
            if self.smallNum > 0:
                self.smallNum -= 1
                return True
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
