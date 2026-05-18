# Preparando os dados para o gráfico de comparação
comp_melted = comp_glicose_bp.reset_index().melt(id_vars='Outcome', var_name='Metrica', value_name='Valor')

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=comp_melted, x='Outcome', y='Valor', hue='Metrica', palette=paleta_rosa) #ax=eixos
plt.title('Comparação: Média de Glicose vs Pressão Arterial')
plt.xticks([0, 1], ['Sem Diabetes', 'Com Diabetes'])
# Altera os textos e o título da legenda manualmente 
handles, _ = ax.get_legend_handles_labels()
plt.legend(handles=handles, title='Métricas', labels=['Média de Glicose', 'Média de Pressão Arterial'])
sns.despine()
plt.show()
