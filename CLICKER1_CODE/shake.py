import random

class Shake:
    def __init__(self, x, y, amount):
        self.x = x
        self.y = y
        self.amount = amount

    def shake_x(self, x):
        shake_x_1 = random.randint(-self.amount, self.amount)
        object_shake_x = x + shake_x_1
        return object_shake_x

    def shake_y(self, y):
        shake_y_1 = random.randint(-self.amount, self.amount)
        object_shake_y = y + shake_y_1
        return object_shake_y

