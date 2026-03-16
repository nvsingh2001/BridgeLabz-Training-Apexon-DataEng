class A:
    def name(self):
        print("A")


class B(A):
    def name(self):
        print("B")


class C(A):
    def name(self):
        print("C")


class D(B, C):
    def name(self):
        super().name()


d = D()
d.name()

print(D.__mro__)

print(type.__mro__)


print(repr(type))
