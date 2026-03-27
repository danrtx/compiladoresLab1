# Construcción de un Compilador: Analizador Léxico y Sintáctico con ANTLR4 

Este repositorio contiene el desarrollo progresivo de un analizador léxico y sintáctico (Lexer y Parser) utilizando **ANTLR4** y **Python**. El proyecto está estructurado en 20 ejercicios prácticos que evolucionan desde el reconocimiento de tokens básicos hasta la construcción de un Árbol de Sintaxis Abstracta (AST) para un mini lenguaje de programación completo.

## Objetivos del Proyecto
* Comprender el funcionamiento interno de un compilador en sus primeras fases (análisis léxico y sintáctico).
* Diseñar gramáticas libres de contexto utilizando el formato `.g4` de ANTLR.
* Resolver problemas clásicos de compilación, como la **ambigüedad** y la **precedencia de operadores** matemáticos.
* Construir y recorrer Árboles de Sintaxis Abstracta (AST) mediante scripts en Python.

## Tecnologías Utilizadas
* **ANTLR 4.13.2**: Generador de analizadores (Lexer y Parser).
* **Python 3**: Lenguaje anfitrión para la ejecución, recorrido de los árboles y pruebas.
* **Java (JRE)**: Requerido para compilar las gramáticas de ANTLR.

## Estructura del Proyecto
El proyecto se divide en 5 niveles de complejidad, cada uno contenido en su respectiva carpeta (`Ejercicio1` a `Ejercicio20`):

1. **Nivel 1 - Reconocimiento Léxico:** Tokens básicos (números, identificadores, palabras clave y operadores).
2. **Nivel 2 - Primeras Reglas Sintácticas:** Agrupación de tokens en reglas como saludos y listas separadas por comas.
3. **Nivel 3 - Expresiones Recursivas:** Implementación de sumas, restas y multiplicaciones simples.
4. **Nivel 4 - Precedencia de Operadores:** Solución a la ambigüedad matemática forzando la jerarquía de operaciones (términos y factores) y uso de paréntesis.
5. **Nivel 5 - Mini Lenguaje y Calculadora:** Unificación de todos los conceptos para permitir asignación de variables (`x = 5`), instrucción `print`, y evaluación de expresiones complejas.

## Cómo ejecutar los ejercicios

Cada carpeta contiene su propio archivo de gramática (`.g4`) y un script de prueba (`test.py`). Para ejecutar cualquier ejercicio, sigue estos pasos desde la terminal:

**1. Generar el Lexer y Parser (Ejemplo para el Ejercicio 20):**
```bash
cd Ejercicio20
java -jar ../antlr-4.13.2-complete.jar -Dlanguage=Python3 Calc.g4
