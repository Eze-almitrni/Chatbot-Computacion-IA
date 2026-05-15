# Chatbot: Historia de la Computación e Inteligencia Artificial

Proyecto desarrollado para simular un asistente virtual que responde consultas sobre la historia, evolución y conceptos fundamentales de la computación y la Inteligencia Artificial.

**Estado del proyecto:** Finalizado | **Versión:** 2.0 (Unión de modelos + Prueba completa)

---

## DESCRIPCIÓN GENERAL
Este chatbot combina dos versiones de desarrollo en un solo sistema funcional:

1. **Modelo Original (`modeloCL.py`):** Versión base, con procesamiento de texto, normalización, tokenización y búsqueda inteligente por palabras clave. Leía su conocimiento desde un archivo JSON externo.
2. **Modelo Simplificado (`modelo_simplificado.py`):** Versión optimizada, con la misma lógica, pero con la base de conocimientos integrada y la **Prueba de Humo de 100 preguntas** automatizada.
3. **Conjunción de Modelos (`conjunción_modelos`):** Versión definitiva donde se unió todo:
    * Funciones avanzadas de limpieza y búsqueda.
    * Base de conocimientos completa.
    * Prueba de efectividad con 100 preguntas y respuestas verificadas.
    * Código unificado, sin depender de archivos externos.

El sistema identifica el tema de la pregunta, busca coincidencias y devuelve la respuesta más adecuada de su base de datos.

---

## ESTRUCTURA DE ARCHIVOS Y EXPLICACIÓN

### 📄 Archivos Principales
* **`conjunción_modelos`** **(Archivo principal actual)**
    > Versión definitiva unida. Contiene **todo el código**: funciones de limpieza, base de datos, chat interactivo y prueba automática de 100 preguntas. **No modifica ni necesita leer otros archivos externos**, es autónomo.

* **`modeloCL.py`**
    > Primera versión del chatbot. Funcional, pero estructurado para leer información del archivo `datos.json`. Incluye:
    > * `normalizar_texto()`: Quita tildes, símbolos y pasa todo a minúsculas.
    > * `tokenizar()`: Separa las palabras para buscar coincidencias.
    > * `buscar_respuesta()`: Lógica de inteligencia para elegir la mejor respuesta.
    > * `iniciar_chat()`: Interfaz de diálogo con el usuario.

* **`modelo_simplificado.py`**
    > Versión optimizada donde se integró la base de datos directamente en el código y se agregó la función de evaluación:
    > * `prueba_de_efectividad()`: Ejecuta automáticamente 100 preguntas predefinidas, compara con las respuestas correctas y calcula el porcentaje de aciertos.

---

### 📄 Archivos de Datos y Pruebas
* **`datos.json`**
    > Base de conocimientos original en formato JSON. Contiene temas, palabras clave y respuestas. Ya no es necesario para el archivo `conjunción_modelos`, se conserva como referencia histórica.

* **`test_modelo.py`**
    > Archivo dedicado exclusivamente a pruebas unitarias y de corrección del sistema. Verifica que las respuestas sean coherentes y que el procesamiento de texto funcione bien.

* **`resultados_test.json`**
    > Almacena de forma estructurada los resultados de las pruebas: cantidad de aciertos, errores y porcentaje de efectividad obtenido.

* **`requisitos.txt`**
    > Lista de librerías y paquetes necesarios para ejecutar el proyecto.
    > *Contenido:* `re`, `unicodedata`, `json` *(todas incluidas en Python estándar)*.

* **`.gitignore`**
    > Configuración para ignorar archivos temporales, de configuración local o archivos generados automáticamente.

---

## ¿CÓMO FUNCIONA EL SISTEMA?

El proceso interno sigue estos pasos lógicos:

1. **ENTRADA:** El usuario escribe una pregunta o saludo.
2. **LIMPIEZA:** El sistema limpia el texto: todo a minúsculas, sin tildes, sin signos de puntuación.
3. **ANÁLISIS:** Busca palabras clave de la pregunta dentro de su base de conocimientos.
4. **PUNTUACIÓN:** Cuenta cuántas palabras coinciden con cada tema. El tema con **mayor coincidencia** es el seleccionado.
5. **RESPUESTA:** Devuelve el texto guardado para ese tema.
    * Si es un saludo ("hola", "buenas", "chau"), responde directamente con frases amigables.
    * Si no encuentra información, avisa educadamente.

---

## PRUEBA DE HUMO - 100 PREGUNTAS

Se implementó una prueba completa de **100 preguntas divididas por temas** para medir la precisión del modelo:

### Temas evaluados:
1. **Origen e Historia (25):** Inicios, herramientas, evolución histórica.
2. **Inteligencia Artificial (25):** Definición, funcionamiento, objetivos, capacidades.
3. **Evolución y Desarrollo (25):** Avances tecnológicos, años 50, algoritmos, redes neuronales.
4. **Máquinas y Automatización (15):** Necesidad de cálculo, velocidad, precisión.
5. **Saludos y frases comunes (10):** Interacción básica.

### Resultado de la prueba:
El sistema compara automáticamente la respuesta generada vs. la respuesta esperada y muestra:
> `Aciertos: X de 100`
> `Efectividad: XX.X %`

*(Actualmente configurado para 100% de coincidencia en temas definidos)*

---

## ¿CÓMO USARLO?

### Opción 1: Charlar normalmente
Ejecutá el archivo y llamá a la función:
```python
iniciar_chat()
