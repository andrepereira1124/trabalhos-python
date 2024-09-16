import pandas as pd  #Criar graficos
import matplotlib.pyplot as plt

# Para carregar os dados de um arquivo cvs (externo)
##df = pd.read_csv ('dados.cvs')
# Ou criando um dataFrame manual
dados = {'ano':[2018, 2019, 2020, 2021, 2022],
         'vendas':[200,250,300,280,320]
         }
df = pd.DataFrame(dados)
# Grafico de linha
df.plot (x='ano',y='vendas',kind='line')
plt.title('Vendas ao longo dos anos')
plt.xlabel('ano')
plt.ylabel('vendas')
plt.grid(True)
plt.show()
#grafico barras
df.plot(x='ano',y='vendas',kind='bar',color='orange')
plt.title('Vendas ao longo dos anos')
plt.xlabel('ano')
plt.ylabel('vendas')
plt.grid(axis='y')
plt.show()
#grafico pizza
df.set_index('ano')['vendas'].plot(kind='pie',autopct='%1.1f%%',startangle=90)
plt.ylabel('')#remove a label padrão do eixo y
plt.show()