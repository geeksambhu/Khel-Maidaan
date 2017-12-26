##
# Method resolution according to DLR algorithm Depth first, Left , then right
# #
class A:
    def whereiam(self):
        print("I am in A")


class B(A):
    def whereiam(self):
        print("I am in B")


class C(A):
    def whereiam(self):
        print("I am in C")


class D(B, C):
    pass

if __name__=="__main__":
    d=D()
    d.whereiam() #prints I am in B