from .c import BaseC


class C1(BaseC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b: float = 0.0

    def c1(self, x) -> float:
        return x + self.b


def c1():
    pass
