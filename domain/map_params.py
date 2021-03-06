import math


class MapParams:
    LAT_STEP = 0.008
    LON_STEP = 0.02
    MAX_ZOOM = 24
    MIN_ZOOM = 1
    SOURCE_LONGITUDE = 37.530887
    SOURCE_LATITUDE = 55.703118

    def __init__(self):
        self.longitude = self.SOURCE_LONGITUDE
        self.latitude = self.SOURCE_LATITUDE
        self.start_longitude = self.SOURCE_LONGITUDE
        self.start_latitude = self.SOURCE_LATITUDE
        self.zoom = 15
        self.type_map = 'map'
        self.scale_x = float
        self.scale_y = float
        self.find_scale(self.latitude)

    def zoom_up(self):
        self.zoom += 1 if self.zoom < self.MAX_ZOOM else 0

    def zoom_down(self):
        self.zoom -= 1if self.zoom > self.MIN_ZOOM else 0

    def left(self):
        self.longitude -= self.LON_STEP * math.pow(2, 15 - self.zoom)

    def right(self):
        self.longitude += self.LON_STEP * math.pow(2, 15 - self.zoom)

    def up(self):
        self.latitude += self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def down(self):
        self.latitude -= self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def set_longitude(self, longitude):
        self.longitude = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_start_longitude(self, longitude):
        self.start_longitude = longitude

    def set_start_latitude(self, latitude):
        self.start_latitude = latitude

    def into_source_coords(self):
        self.longitude = self.SOURCE_LONGITUDE
        self.latitude = self.SOURCE_LATITUDE

    def change_type_map(self):
        self.type_map = 'map'

    def change_type_sat(self):
        self.type_map = 'sat'

    def change_type_sat_skl(self):
        self.type_map = 'sat,skl'

    def get_scale_x(self):
        return self.scale_x

    def get_scale_y(self):
        return self.scale_y

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_zoom(self):
        return self.zoom

    def get_type_map(self):
        return self.type_map

    def get_start_longitude(self):
        return self.start_longitude

    def get_start_latitude(self):
        return self.start_latitude

    def find_scale(self, latitude):
        self.scale_x = 360 / math.pow(2, self.zoom + 8)
        self.scale_y = math.cos(latitude * math.pi / 180) * 360 / math.pow(2, self.zoom + 8)
