class Point:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '({0}, {1})'.format(self.latitude, self.longitude)
