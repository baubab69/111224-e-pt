# Проблема алмаза с передачей параметров в конструкторы.

class A:
    def __init__(self, a):
        self.value = 2
        print(f"Initializing A with {a}")

    def get_value(self):
        return self.value

class B(A):
    def __init__(self, b, **kwargs):
        super(B, self).__init__(**kwargs)
        self.extra = b
        print(f"Initializing B with {b}")

    def get_value(self):
        return self.value * 2

class C(A):
    def __init__(self, c, **kwargs):
        super(C, self).__init__(**kwargs)
        self.val = c
        print(f"Initializing C with {c}")

    def get_value(self):
        return self.value * 3


class D(B, C):
    def __init__(self, a, b, c, d, **kwargs):
        super(D, self).__init__(a=kwargs.get('a'), b=b, c=c)
        self.d = d
        print(f"Initializing D with parameters {a, b, c, d}")


    def get_value(self):
        return super(C, self).get_value()


def main():
    # Тестирование
    d = D(10, 20, 30, 40)

    # Порядок MRO
    print(D.mro())

    print(d.get_value())


if __name__ == "__main__":
    main()
