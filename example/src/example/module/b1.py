from .b import BaseB


class B1(BaseB):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b: float = 0.0

    def b1(self, x) -> float:
        return x + self.b


def b1():
    pass
