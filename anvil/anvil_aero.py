from abc import ABC, abstractmethod

# ===============================
# Product (추상 제품)
# ===============================
class Ship(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def verify(self):
        pass

    @abstractmethod
    def launch(self):
        pass


# ===============================
# ConcreteProducts
# ===============================
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


# ===============================
# Creator (추상 팩토리)
# ===============================
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


# ===============================
# ConcreteCreator
# ===============================
class AnvilAerospace(AnvilStore):

    def create_ship(self, ship_type: str) -> Ship:
        if ship_type == "hornet":
            return Hornet()
        elif ship_type == "carrack":
            return Carrack()
        else:
            raise ValueError(f"지원하지 않는 함선: {ship_type}")
