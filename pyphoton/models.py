class Location:

    @property
    def latitude(self):
        return self._point.latitude

    @property
    def longitude(self):
        return self._point.longitude

    def __str__(self):
        rep = '{0}\n{1}'.format(
            str(self.name),
            str(self._point)
        )
        for k, v in self.__dict__.items():
            if k in ['state', 'city', 'street', 'postcode']:
                rep += '\n{0}: {1}'.format(k, v)
        for k, v in self.__dict__.items():
            if k.startswith('osm_'):
                rep += '\n{0}: {1}'.format(k, v)
        return rep


class Point:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '({0}, {1})'.format(self.latitude, self.longitude)
