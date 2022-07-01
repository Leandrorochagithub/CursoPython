# Potência de um número
print(2**1)
print(2**2)
print(2**3)
print(2**4)
print(2**5)
print(2**6)
print(2**7)
print(2**8)
print(2**9)
print(2**10)
print(2**11)
print(2**12)
#It's a bad code. It's use while conditional
#
i=0 #It's needed to give a initial value to i
while i <=10: #while conditional print()
    print(2 ** i)
    i=i+1 #To add +1 to the power until it reaches(alcançar) 10

i=0
while i <=20:
    print(2**i)
    i=i+1
#-------------------------------------------
# soma de vários números digitados pelo usuário
print("Digite uma soma de valores terminadas por zero.")
soma=0 #needed to give a initial value to soma
valor=1 #because valor!=0 is a conditional
while valor!=0
    valor= int(input("Digite um valor a ser somado: "))
    soma= soma + valor
print('A soma dos valores digitados é: ', soma)

produto= 1
valor= 1
while valor !=0:
    valor= int(input("Digite um valor a ser multiplicado: "))
    produto= produto * valor
print("A multiplicação dos valores digitados é: ", produto)
#-------------------------------------------
tamanho= int(input("Digite o tamanho da sequência de números: "))
produto= 1 #Needed different from 0 because it's a multiplication
i= 0
while i < tamanho:
    valor= int(input("Digite um valor a ser multiplicado: "))
    produto= produto * valor
    i= i+1
print("O produto dos valores digitados é: ", produto)