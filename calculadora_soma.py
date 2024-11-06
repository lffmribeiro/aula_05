'''
Esse código ten como finalidade criar uma cálculadora simples para o curso
'''


print('**************** bem vindo à sua calculadora simples de soam ************')
print()
print()
try:
    primeiro_numero: float = float(input("Digite o primeiro número: "))
    segundo_numero: float = float(input("Digite o primeiro número: "))
    soma: float = primeiro_numero + segundo_numero
except:
    print('Digite apenas números e o separador decimal precisa ser um ponto (".")')
print()
print(f'Sua soma é = {soma}')