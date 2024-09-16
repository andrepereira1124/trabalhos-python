#Explicação do Código
#Inicialização do Vetor:
#O vetor é inicializado como uma lista vazia. O usuário é solicitado a inserir 10 valores inteiros que são armazenados nesta lista.
#Verificação de Valores Duplicados:
#O código utiliza dois loops aninhados para comparar cada par de elementos no vetor. Se dois elementos são iguais e o valor não está na lista duplicados, ele é adicionado a essa lista.
#Exibição dos Valores Duplicados:
#Após a verificação, o código verifica se a lista duplicados contém algum valor. Se sim, ele imprime cada valor duplicado. Se não, informa que nenhum valor duplicado foi encontrado.
#Esse código vai funcionar bem para verificar e listar valores duplicados em um vetor com 10 elementos fornecidos pelo usuário. Caso queira tratar vetores maiores ou adicionar mais funcionalidades, ajustes adicionais podem ser necessários.


# faça um programa que leia um vetor de 10 possições 
# e verfique se existem valores iguais e escreva-os na tela

vetor = []

#Lendo os valores a serem inseridos
print("Digite 10 valores para o vetor")
for i in range(10):
    valor = int(input(f"valor {i+1}: "))
    vetor.append(valor)

#verificar valores duplicados
duplicados = []
for i in range(len(vetor)):
    for j in range(i+1,len(vetor)):
        if vetor[i] == vetor[j] and vetor[i] not in duplicados:
            duplicados.append(vetor[i])

#exibir os valores duplicados
if duplicados:
    print("Valores duplicados encontrados:")
    for valor in duplicados:
        print(valor)
else:
    print("Nenhum valor duplicado encontrado.")