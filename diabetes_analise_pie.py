# comparar a média de todas as colunas entre os dois grupos
comparacao_medias = df.groupby('Outcome').mean(numeric_only=True)
comparacao_medias.round(2)
plt.figure(figsize=(10, 6))

# cores baseadas em códigos RGB
plum = (221/255, 160/255, 221/255)
medium_violet_red = (199/255, 21/255, 133/255)
deep_pink = (255/255, 20/255, 147/255)
hot_pink = (255/255, 105/255, 180/255)
MistyRose= (255/255, 228/255, 225/255)

#lista da paleta
paleta_rosa = [plum, medium_violet_red, deep_pink, hot_pink, MistyRose]
plt.figure(figsize=(10, 6))

# Aplicando a paleta
plt.pie(
    comp_idade['Total_Casos_Diabetes'],
    labels=comp_idade.index,
    colors=paleta_rosa,
    autopct='%.1f%%',
    startangle=90
)

plt.title('Total de Casos de Diabetes por Faixa Etária', fontsize=14, color='black')

# remover as bordas do gráfico 
sns.despine()

plt.show()
