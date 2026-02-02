# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
price: int
machine_name: str


class VendingMachine(ABC):

    def serve(self, amount: int):
        self.insert_money(amount)
        self.verify(amount)
        self.prepare()
        self.dispense()
        self.return_change(amount)

    def insert_money(self, amount: int):
        print(f"[{self.machine_name}] 돈 투입: {amount}원")

    def verify(self, amount: int):
        if amount < self.price:
            raise ValueError(f"[{self.machine_name}] 금액 부족")
        print(f"[{self.machine_name}] 금액 검증 완료 (필요: {self.price}원)")

    @abstractmethod
    def prepare(self):
        pass

    def dispense(self):
        print(f"[{self.machine_name}] 제품 배출 완료")

    def return_change(self, amount: int):
        change = amount - self.price
        if change > 0:
            print(f"[{self.machine_name}] 거스름돈 {change}원 반환")


class CoffeeVendingMachine(VendingMachine):
    machine_name = "커피 자판기"
    price = 1200

    def prepare(self):
        print("[커피 자판기] 원두 분쇄 중...")
        print("[커피 자판기] 추출 중...")
        print("[커피 자판기] 컵에 담는 중...")


class ColaVendingMachine(VendingMachine):
    machine_name = "콜라 자판기"
    price = 800

    def prepare(self):
        print("[콜라 자판기] 냉장 상태 확인 중...")
        print("[콜라 자판기] 배출구로 이동 중...")


class RamenVendingMachine(VendingMachine):
    machine_name = "라면 자판기"
    price = 1500

    def prepare(self):
        print("[라면 자판기] 컵면 배출")
        print("[라면 자판기] 뜨거운 물 주입 중...")
        print("[라면 자판기] 뚜껑 열기 힌트 출력")

CoffeeVendingMachine().serve(1500)
print()
ColaVendingMachine().serve(1000)
print()
RamenVendingMachine().serve(5000)
print()