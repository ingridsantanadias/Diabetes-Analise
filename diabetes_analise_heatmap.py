plt.figure(figsize=(12, 4))
# Transpor (.T) ler as variáveis
sns.heatmap(comparacao_medias.T, annot=True, cmap='PuRd', fmt='.2f')

plt.title('Diferença das Médias: Sem Diabetes (0) vs Com Diabetes (1)')
plt.show()
