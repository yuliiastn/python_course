class Car:
    def __init__(
            self,
            model: str,
            year: int,
            speed: int
            ):
        self.model = model
        self.year = year
        self.speed = speed
        if speed < 0:
            raise ValueError('Speed cannot be a negative number')

    def accelerate(self):
        self.speed = self.speed + 5
        return self.speed

    def brake(self):
        self.speed = max(self.speed - 5, 0)
        return self.speed
        
    def display_speed(self):
        return f'The speed is {self.speed}'


Audi = Car('A1', 2020, 5)

print(Audi.accelerate())
