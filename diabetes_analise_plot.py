# paleta roxa
indigo = (75/255, 0/255, 130/255)
medium_slate_blue = (123/255, 104/255, 238/255)


# lista da paleta
paleta_roxa = [indigo,medium_slate_blue]

df_plot= df.copy()  # Criar uma cópia do DataFrame para plotagem
df_plot['Outcome'] = df_plot['Outcome'].map({0: 'Sem Diabetes', 1: 'Com Diabetes'})  # Mapear os valores para rótulos mais legíveis

plt.figure(figsize=(10, 6))
# preparar os dados para o gráfico de comparação
comp_melted = comp_glicose_bp.reset_index().melt(id_vars='Outcome', var_name='Metrica', value_name='Valor')
sns.scatterplot(data=df_plot, x='BMI', y='SkinThickness', hue='Outcome', alpha=0.6, palette=paleta_roxa)

plt.title('Comparação: IMC vs Espessura da Pele')
plt.xlabel('IMC')
plt.ylabel('Espessura da Pele (Skin Thickness)')
plt.legend(title='Status')
sns.despine()
plt.show()
