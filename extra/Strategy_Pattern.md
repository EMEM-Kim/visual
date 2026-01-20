# 전략 패턴 (Strategy Pattern)

## 1. 전략 패턴이란?

**전략 패턴(Strategy Pattern)** 은  
**알고리즘(행동)을 캡슐화하여 서로 교체 가능하게 만드는 디자인 패턴**이다.

즉,
- 동일한 목적을 가진 여러 알고리즘을
- 각각 클래스로 분리하고
- 실행 시점에 알고리즘을 선택할 수 있도록 한다

➡️ **조건문(if/else, switch)을 제거하고 유연한 구조를 만든다**

---

## 2. 왜 전략 패턴을 사용하는가?

### ❌ 전략 패턴이 없는 경우
```python
if payment_type == "card":
    pay_with_card()
elif payment_type == "cash":
    pay_with_cash()
elif payment_type == "kakao":
    pay_with_kakao()
