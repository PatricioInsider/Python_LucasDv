# Evaluar el modelo con las predicciones
y_pred = model.predict(X_test)

# Calcular las métricas de evaluación
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n" + "="*70)
print("EVALUACIÓN DEL MODELO - MÉTRICAS DE REGRESIÓN")
print("="*70)

# 1. MAE - Error Absoluto Medio
print("\n1️⃣  MAE (Error Absoluto Medio): ${:,.2f}".format(mae))
print("    📌 Calcula el promedio de las diferencias absolutas entre")
print("       los valores reales y predichos.")
print("    💡 Interpretación: En promedio, el modelo se equivoca por ${:,.2f}".format(mae))

# 2. MSE - Error Cuadrático Medio
print("\n2️⃣  MSE (Error Cuadrático Medio): ${:,.2f}".format(mse))
print("    📌 Calcula el promedio de los cuadrados de los errores.")
print("    💡 Penaliza más los errores grandes.")

# 3. RMSE - Raíz del Error Cuadrático Medio
print("\n3️⃣  RMSE (Raíz del Error Cuadrático Medio): ${:,.2f}".format(rmse))
print("    📌 Vuelve a las unidades originales de la variable objetivo.")
print("    💡 Más interpretable que MSE, en la misma escala que el precio.")

# 4. R² - Coeficiente de Determinación
print("\n4️⃣  R² (Coeficiente de Determinación): {:.4f} ({:.2f}%)".format(r2, r2*100))
print("    📌 Mide la proporción de la varianza en la variable dependiente (Y)")
print("       que es predecible a partir de las variables independientes (X).")
print("    💡 El modelo explica el {:.2f}% de la variabilidad del precio.".format(r2*100))

print("\n" + "="*70)

# Importancia de las características
feature_importance = pd.DataFrame({
    'feature': ['cut', 'color', 'carat', 'depth'],
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\n=== IMPORTANCIA DE LAS CARACTERÍSTICAS ===")
print(feature_importance)
print("\n💎 La variable más importante es '{}' con {:.2f}% de importancia".format(
    feature_importance.iloc[0]['feature'], 
    feature_importance.iloc[0]['importance']*100
))
