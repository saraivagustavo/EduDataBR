# Modelos Preditivos — EduDataBR

Este diretório contém os artefatos serializados dos modelos de Machine Learning desenvolvidos no projeto (Sprint 5).

> [!NOTE]
> Os arquivos binários de modelos (`*.joblib`, `*.pkl`) são ignorados pelo Git via `.gitignore` devido ao tamanho dos pesos serializados. Os modelos são gerados e persistidos localmente durante a execução do notebook `notebooks/04_machine_learning.ipynb`.

## Artefatos Gerados

1. **`regressor_enem2023.joblib`**:
   - **Objetivo:** Estimação da nota média geral (`nu_nota_media_geral`) a partir do perfil contextual e socioeconômico.
   - **Algoritmo:** `HistGradientBoostingRegressor` encapsulado em `Pipeline` com `ColumnTransformer`.
   - **Métricas de Validação:** $R^2 \approx 0{,}35$, RMSE $\approx 64$ pontos, MAE $\approx 51$ pontos.

2. **`classificador_enem2023.joblib`**:
   - **Objetivo:** Previsão binária de alto desempenho (`fl_alto_desempenho` — percentil 80, $\ge 618$ pontos).
   - **Algoritmo:** `HistGradientBoostingClassifier` encapsulado em `Pipeline` com `ColumnTransformer`.
   - **Métricas de Validação:** ROC-AUC $\approx 0{,}79$, PR-AUC $\approx 0{,}52$, Balanced Accuracy $\approx 0{,}72$.
