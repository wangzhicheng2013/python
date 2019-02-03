import sys
if __name__ == '__main__':
    n1 = int(raw_input("n1 = "))
    n2 = int(raw_input("n2 = "))
    n3 = int(raw_input("n3 = "))
    L = []
    L.append(n1)
    L.append(n2)
    L.append(n3)
    L.sort(reverse = True)
    print L
