def ktsnt(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
nb = int(input("Nhập số cần kiểm tra: "))
if ktsnt(nb):
    print(nb, "Là số NT")
else:
    print(nb, "Ko phải là SNT")