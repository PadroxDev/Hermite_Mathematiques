class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "P(" + str(self.x) + ", " + str(self.y) + ")"