# 팩토리 메서드 패턴 (Factory Method Pattern)

## 1. 팩토리 메서드 패턴이란?

팩토리 메서드 패턴은 객체 생성을 공장 클래스로 캡슐화하여 대신 생성하게 하는 **생성(Creational) 디자인 패턴**이다.  
클라이언트에서는 `new` 연산자를 통해 직접 객체를 생성하지 않고, 객체 생성을 담당하는 공장 클래스에 위임함으로써 **생성 로직과 사용 로직을 분리**한다.

공장 클래스는 객체 생성을 위한 메서드(팩토리 메서드)를 정의만 하고,  
실제 어떤 제품 객체를 생성할지는 이를 상속받는 **서브 공장 클래스**에서 결정한다.

이를 통해 객체 생성 책임을 서브클래스에 위임하고,  
새로운 제품이 추가되더라도 기존 코드를 수정하지 않고 확장할 수 있는 구조를 제공한다.

또한 객체 생성에 필요한 공통 흐름을 **템플릿 메서드 형태**로 미리 정의하고,  
전처리나 후처리 과정을 포함시켜 객체 생성 과정을 일관되게 관리할 수 있다는 특징이 있다.

---

## 2. 언제 사용하는가?

다음과 같은 상황에서 팩토리 메서드 패턴을 사용하면 효과적이다.

- 생성해야 할 객체의 **구체 클래스가 미리 정해지지 않았을 때**
- 객체의 종류가 **자주 추가되거나 변경될 가능성**이 있을 때
- 객체 생성 로직을 클라이언트 코드에서 **분리하고 싶을 때**
- 객체 생성 과정에 **공통된 흐름이나 규칙**이 존재할 때
- **OCP(Open-Closed Principle)** 를 만족하는 구조를 만들고 싶을 때

특히  
**“종류가 계속 늘어나는 객체”** 와 **“공통 생성 절차”** 가 함께 존재하는 경우에 적합하다.

---

## 3. 구조

- **Product**
  - 생성될 객체의 공통 인터페이스 또는 추상 클래스
- **ConcreteProduct**
  - 실제로 생성되는 구체 제품 클래스
- **Creator**
  - 팩토리 메서드를 선언하는 추상 클래스
- **ConcreteCreator**
  - 팩토리 메서드를 구현하여 실제 제품 객체를 생성하는 클래스

---

## 4. 장점

- **객체 생성 책임 분리**
  - 클라이언트는 객체 생성 방법을 알 필요가 없음
- **확장에 유리**
  - 새로운 제품 추가 시 기존 코드 수정 최소화 (OCP 만족)
- **결합도 감소**
  - 구체 클래스가 아닌 추상 타입에 의존
- **공통 생성 흐름 재사용**
  - 템플릿 메서드와 결합하여 일관된 생성 절차 유지
- **유지보수성 향상**
  - 생성 로직이 한 곳에 모여 관리가 쉬움

---

## 5. 단점

- **클래스 수 증가**
  - 제품이 늘어날수록 팩토리 클래스도 함께 증가
- **구조 복잡성 증가**
  - 소규모 프로젝트에서는 과설계가 될 수 있음
- **코드 추적 난이도 상승**
  - 실제 생성되는 객체를 한눈에 파악하기 어려움
- **단순한 경우엔 비효율**
  - 확장 가능성이 없다면 Simple Factory가 더 적합할 수 있음



















```mermaid
sequenceDiagram
    participant Client
    participant AnvilAerospace as ConcreteCreator
    participant Hornet as ConcreteProductA
    participant Carrack as ConcreteProductB

    Client ->> AnvilAerospace: order_ship("hornet")
    AnvilAerospace ->> AnvilAerospace: create_ship("hornet")
    AnvilAerospace ->> Hornet: new Hornet()
    Hornet -->> AnvilAerospace: Ship instance
    AnvilAerospace ->> Hornet: prepare()
    AnvilAerospace ->> Hornet: verify()
    AnvilAerospace ->> Hornet: launch()
    AnvilAerospace -->> Client: return Hornet

    Client ->> AnvilAerospace: order_ship("carrack")
    AnvilAerospace ->> AnvilAerospace: create_ship("carrack")
    AnvilAerospace ->> Carrack: new Carrack()
    Carrack -->> AnvilAerospace: Ship instance
    AnvilAerospace ->> Carrack: prepare()
    AnvilAerospace ->> Carrack: verify()
    AnvilAerospace ->> Carrack: launch()
    AnvilAerospace -->> Client: return Carrack







