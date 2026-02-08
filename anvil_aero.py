from abc import ABC, abstractmethod




class Ship(ABC):
    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def verify(self): pass

    @abstractmethod
    def launch(self): pass




class Hornet(Ship):
    def prepare(self):
        print("Hornet 호출중")

    def verify(self):
        print("Hornet 함선 시스템 점검")

    def launch(self):
        print("Hornet 전투하러 출발")


class Carrack(Ship):
    def prepare(self):
        print("Carrack 호출중")

    def verify(self):
        print("Carrack 함선 시스템 점검")

    def launch(self):
        print("Carrack 탐사하러 출발")



class AnvilStore(ABC):

    def order_ship(self, ship_type: str) -> Ship:
        ship = self.create_ship(ship_type)
        ship.prepare()
        ship.verify()
        ship.launch()
        return ship

    @abstractmethod
    def create_ship(self, ship_type: str) -> Ship:
        pass



class AnvilAerospace(AnvilStore):

    _ship_map = {
        "hornet": Hornet,
        "carrack": Carrack,
    }

    def create_ship(self, ship_type: str) -> Ship:
        try:
            return self._ship_map[ship_type]()
        except KeyError:
            raise ValueError(f"지원하지 않는 함선: {ship_type}")

