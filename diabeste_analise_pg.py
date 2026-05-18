#Criar uma pg em branco com espaço p 4 gráficos (2 linhas e 2 colunas)
fig, axes = plt.subplots(2, 2, figsize=(18, 12))

# Título principal da página
fig.suptitle('Dashboard de Análise - Dataset Diabetes', fontsize=22, color=medium_violet_red)


# POSIÇÃO [0, 0]: Gráfico de Casos por Idade
axes[0, 0].pie(
    comp_idade['Total_Casos_Diabetes'],
    labels=comp_idade.index,
    colors=paleta_rosa,
    autopct='%.1f%%',
    startangle=90
)
axes[0, 0].set_title('Distribuição de Casos de Diabetes por Faixa Etária', fontsize=14)


# POSIÇÃO [0, 1]: Gráfico Glicose vs Pressão
comp_melted = comp_glicose_bp.reset_index().melt(id_vars='Outcome', var_name='Metrica', value_name='Valor')
comp_melted['Metrica'] = comp_melted['Metrica'].replace({'Média_Glicose': 'Média de Glicose', 'Média_BloodPressure': 'Média de Pressão'})
#  "ax=axes[0, 1]" para  ir pra o canto superior direito:
sns.barplot(data=comp_melted, x='Outcome', y='Valor', hue='Metrica', palette=[plum, deep_pink], ax=axes[0, 1])
axes[0, 1].set_title('Comparação: Média de Glicose vs Pressão Arterial', fontsize=14)
axes[0, 1].set_xticklabels(['Sem Diabetes', 'Com Diabetes'])
axes[0, 1].set_xlabel('Diagnóstico')
axes[0, 1].set_ylabel('Valores Médios')
axes[0, 1].legend(title='Métricas')

# POSIÇÃO [1, 0]: Gráfico de Dispersão (Pele vs IMC)
# "ax=axes[1, 0]" para ir para o canto inferior esquerdo:
sns.scatterplot(data=df, x='BMI', y='SkinThickness', hue='Outcome', palette=paleta_roxa, alpha=0.7, ax=axes[1, 0])
axes[1, 0].set_title('Relação entre IMC e Espessura da Pele', fontsize=14)
axes[1, 0].set_xlabel('IMC (BMI)')
axes[1, 0].set_ylabel('Espessura da Pele')
handles, labels = axes[1, 0].get_legend_handles_labels()
axes[1, 0].legend(handles=handles, labels=['Sem Diabetes', 'Com Diabetes'], title='Diagnóstico')

# POSIÇÃO [1, 1]: O seu Mapa de Calor (Heatmap) 
# "ax=axes[1, 1]" para ir para o último quadrado:
sns.heatmap(comparacao_medias.T, annot=True, cmap='PuRd', fmt='.2f', robust=True, ax=axes[1, 1])
axes[1, 1].set_title('Mapa de Calor: Diferença das Médias Gerais', fontsize=14)
sns.despine() 
plt.tight_layout() 
plt.savefig('dashboard_diabetes_final.png', dpi=300, bbox_inches='tight')
plt.show()
