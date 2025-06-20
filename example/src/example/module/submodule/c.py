from ...a import A
from ..b import B


class BaseC:
    attr_base_c: int

    def __init__(self, a: A, b: B):
        self.a = a
        self.b = b

    def base_b(self, x: int, y: int) -> int:
        return x + y


class C(BaseC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b: float = 0.0

    def b(self, x) -> float:
        return x + self.b
