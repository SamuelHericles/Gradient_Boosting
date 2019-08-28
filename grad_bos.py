def prod(x):
  y = x / 2 + (x // 10) % 2 * 20 * x / 5 + np.random.random() * 10
  return y

#Definindo entrada e saída para o testo com o modelo
x = np.arange(0, 60)
y = prod(x)
x = pd.DataFrame({'x': x})

# Criação do modelo de gradient bossting, definindos os parâmetros
params = {
    'n_estimators': 10,
    'max_depth': 5,
    'learning_rate': 1,
    'criterion': 'mse'
}

gradient_boosting_regressor = ensemble.GradientBoostingRegressor(**params)
gradient_boosting_regressor.fit(x, y)
