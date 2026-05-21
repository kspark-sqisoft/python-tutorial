"""
raise 로 예외를 직접 발생시키고, 사용자 정의 예외 클래스를 만드는 방법.
Exception 을 상속하면 대부분의 경우 충분하며, 추가 속성도 자유롭게 넣을 수 있다.
"""

# ──── 1. raise 기본 ────

def check_age(age):
    # 조건에 맞지 않으면 표준 예외를 직접 발생
    if not isinstance(age, int):
        raise TypeError(f"나이는 정수여야 합니다. 받은 값: {type(age).__name__}")
    if age < 0:
        raise ValueError(f"나이는 0 이상이어야 합니다. 받은 값: {age}")
    return age

# ──── 2. 사용자 정의 예외 클래스 ────

class NegativeBalanceError(Exception):
    """잔액이 음수가 될 때 발생하는 사용자 정의 예외."""

    def __init__(self, balance):
        # 메시지와 함께 balance 속성도 저장
        super().__init__(f"잔액이 음수입니다: {balance}원")
        self.balance = balance  # 호출자가 잔액을 꺼낼 수 있도록

class InsufficientFundsError(Exception):
    """출금 금액이 잔액을 초과할 때 발생."""

    def __init__(self, amount, balance):
        super().__init__(f"출금 불가: 요청 {amount}원, 잔액 {balance}원")
        self.amount = amount
        self.balance = balance

# ──── 3. 사용자 예외를 쓰는 Account 함수 ────

def deposit(account, amount):
    # 입금
    if amount <= 0:
        raise ValueError(f"입금액은 양수여야 합니다: {amount}")
    account["balance"] += amount
    return account["balance"]

def withdraw(account, amount):
    # 출금 — 잔액 부족 시 사용자 예외 발생
    if amount <= 0:
        raise ValueError(f"출금액은 양수여야 합니다: {amount}")
    new_balance = account["balance"] - amount
    if new_balance < 0:
        raise InsufficientFundsError(amount, account["balance"])
    account["balance"] = new_balance
    return new_balance

# ──── 4. raise ... from (연쇄 예외) ────

def load_config(path):
    # 원래 예외를 원인으로 연결해 컨텍스트를 보존
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as original:
        raise RuntimeError(f"설정 파일 로드 실패: {path}") from original


if __name__ == "__main__":
    print("=== 1. raise 표준 예외 ===")
    try:
        check_age("스물")
    except TypeError as e:
        print(f"TypeError: {e}")

    try:
        check_age(-5)
    except ValueError as e:
        print(f"ValueError: {e}")

    print(f"정상: {check_age(25)}")

    print("\n=== 2. 사용자 정의 예외 ===")
    account = {"balance": 1000}

    try:
        deposit(account, 500)
        print(f"입금 후 잔액: {account['balance']}원")
        withdraw(account, 2000)   # 잔액 부족
    except InsufficientFundsError as e:
        print(f"InsufficientFundsError: {e}")
        print(f"  요청액: {e.amount}, 현재 잔액: {e.balance}")

    print("\n=== 3. NegativeBalanceError 직접 발생 ===")
    try:
        raise NegativeBalanceError(-300)
    except NegativeBalanceError as e:
        print(f"NegativeBalanceError: {e}")
        print(f"  .balance 속성: {e.balance}")

    print("\n=== 4. raise ... from (연쇄 예외) ===")
    try:
        load_config("/없는/경로/config.txt")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
        print(f"  원인(.__cause__): {e.__cause__}")
