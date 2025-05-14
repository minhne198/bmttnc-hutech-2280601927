def dnl(lst):
    return lst[::-1]
input_list = input("Nhập ds các số cách nhau = dấu phẩy: ")
n = list(map(int,input_list.split(',')))
ldn = dnl(n)
print("List sau khi đảo ngược:",ldn)