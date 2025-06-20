from ..a import A


class BaseB:
    attr_base_b: int

    def __init__(self, a: A):
        self._a = a

    def base_b(self, x: int, y: int) -> int:
        return x + y

    @property
    def a(self) -> A:
        return self._a


class B(BaseB):
    attr_b: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b: float = 0.0

    def b(self, x) -> float:
        return x + self.b
