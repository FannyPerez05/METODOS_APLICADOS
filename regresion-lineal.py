import pandas as pd
import statsmodels.formula.api as smf

# Crear un DataFrame
datos = pd.DataFrame({
    'x': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'y': [60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
})

# Ajustar el modelo lineal usando una fórmula
modelo = smf.ols('y ~ x', data=datos).fit()

# Obtener solo los coeficientes
print('Coeficientes:')
print(modelo.params)

