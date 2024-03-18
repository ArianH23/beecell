from src.dexma.device import Device
from src.dexma.location import Locations
from src.dexma.parameter import Parameters
from src.dexma.reading import Readings
from src.dexma.supply import Supplies


class Dexma(object):
    def __init__(self, api_key):
        self.base_url = "https://api.dexma.com/v3/"
        self.headers = {
            "x-dexcell-token": api_key,
            "Content-Type": "application/json",
        }

    def devices(self):
        return Device(self)

    def locations(self):
        return Locations(self)

    def parameters(self):
        return Parameters(self)

    def readings(self):
        return Readings(self)

    def supplies(self):
        return Supplies(self)



