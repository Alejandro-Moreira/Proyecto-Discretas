# Proyecto-Discretas
## 🧠 Generador de Expresiones Lógicas (SOP / POS)

Este proyecto en Python genera **expresiones lógicas** en forma **SOP (Suma de Productos)** y **POS (Producto de Sumas)** a partir de una tabla de verdad introducida por el usuario.

### 🚀 ¿Qué hace este programa?

Dado un número de variables booleanas (`A`, `B`, `C`, ...), el programa:
- Genera automáticamente todas las combinaciones posibles de 0s y 1s.
- Solicita al usuario que introduzca la salida (0 o 1) para cada combinación.
- Construye la expresión lógica equivalente en:
  - **SOP**: para salidas 1.
  - **POS**: para salidas 0.
- Muestra la tabla de verdad con resultados.

---

### 📦 Estructura del Código

- `generar_tabla_verdad(n)`: Genera la tabla de verdad con `n` variables.
- `construir_SOP(tabla, salidas, variables)`: Construye una expresión en forma SOP.
- `construir_POS(tabla, salidas, variables)`: Construye una expresión en forma POS.
- `entrada_por_fila(tabla)`: Solicita la salida (0 o 1) para cada combinación binaria.
- `main()`: Controla el flujo completo del programa (menús, entradas, salidas).

---

### ▶️ Ejecución

1. Asegúrate de tener Python instalado (3.6+ recomendado).
2. Ejecuta el script:

```bash
python generador_logico.py
