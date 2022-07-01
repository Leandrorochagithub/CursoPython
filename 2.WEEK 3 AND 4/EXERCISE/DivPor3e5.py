x=int(input("Digite um número inteiro: "))
DivPor3= x%3
DivPor5= x%5
if DivPor3== 0 or DivPor5== 0:
    print("FizzBuzz")
else:
    print(x)