class Point:
    def __init__(self, x: float = 0, y: float = 0, slope: float = 0):
        self.x = x
        self.y = y
        self.slope = slope

    def __str__(self):
        return "P(%d, %d, %d)" % (self.x, self.y, self.slope)