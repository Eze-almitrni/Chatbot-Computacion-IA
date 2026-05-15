# CHATBOT: HISTORIA DE LA COMPUTACIÓN E IA
# Versión afín al código original, pero simplificada
# Funciona igual: limpia texto, busca y responde, sin complejidades

# ==============================================
# 1. BASE DE DATOS (aquí guardamos la información)
# En el código original esto estaba en un archivo JSON, acá lo hacemos directo
# ==============================================
base_conocimiento = [
    {
        "palabras_clave": ["computacion", "historia", "origen"],
        "respuesta": "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas."
    },
    {
        "palabras_clave": ["ia", "inteligencia", "artificial", "que es"],
        "respuesta": "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano."
    },
    {
        "palabras_clave": ["primeros", "años", "evolucion", "desarrollo"],
        "respuesta": "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología."
    },
    {
        "palabras_clave": ["maquinas", "calculos", "automatizacion"],
        "respuesta": "Todo comenzó por la necesidad de hacer cálculos rápidos y exactos, evolucionando hacia la automatización de tareas cada vez más complejas."
    }
]

# Respuestas rápidas (saludos y despedidas)
respuestas_rapidas = {
    "hola": "¡Hola! ¿Qué querés saber sobre computación o Inteligencia Artificial?",
    "buenas": "¡Buenas! Estoy acá para responder tus dudas.",
    "chau": "¡Hasta luego! Fue un gusto ayudarte.",
    "adios": "¡Nos vemos! Volvé cuando quieras."
}

# ==============================================
# 2. FUNCIÓN PARA LIMPIAR EL TEXTO
# Hace lo mismo que la función "normalizar" del código original
# ==============================================
def limpiar_texto(texto):
    # Pasar todo a minúsculas
    texto = texto.lower()
    
    # Quitar tildes para que coincida igual
    tildes = {
        'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u',
        'ñ':'n'
    }
    # Reemplazar cada letra con tilde por su versión simple
    for con_tilde, sin_tilde in tildes.items():
        texto = texto.replace(con_tilde, sin_tilde)
    
    # Devolver el texto limpio
    return texto

# ==============================================
# 3. FUNCIÓN PARA BUSCAR LA RESPUESTA
# Hace lo mismo que "buscar_contexto", pero mucho más simple
# ==============================================
def buscar_respuesta(pregunta):
    # Primero limpiamos lo que escribió el usuario
    pregunta_limpia = limpiar_texto(pregunta)
    
    # 👉 PASO 1: ¿Es un saludo o despedida?
    for palabra, respuesta in respuestas_rapidas.items():
        if palabra in pregunta_limpia:
            return respuesta
    
    # 👉 PASO 2: Buscar coincidencias en la base de conocimiento
    mejor_respuesta = "Lo siento, no tengo información sobre eso. Preguntame sobre historia de la computación o qué es la IA."
    max_puntos = 0
    
    # Revisamos cada tema que sabemos
    for tema in base_conocimiento:
        puntos = 0
        # Contamos cuántas palabras clave coinciden
        for palabra_clave in tema["palabras_clave"]:
            if palabra_clave in pregunta_limpia:
                puntos += 1
        
        # Si este tema tiene más coincidencias, es la mejor respuesta
        if puntos > max_puntos:
            max_puntos = puntos
            mejor_respuesta = tema["respuesta"]
    
    return mejor_respuesta

# ==============================================
# 4. FUNCIÓN PRINCIPAL (EL CHAT)
# Hace lo mismo que "charlar" del código original
# ==============================================
def iniciar_chat():
    print("🤖 CHATBOT: Historia de la Computación y la IA")
    print("Escribí 'salir' para terminar\n")
    
    # Bucle para hablar todo el tiempo
    while True:
        # Recibir lo que escribe el usuario
        usuario = input("Tú: ")
        
        # Opción para terminar
        if limpiar_texto(usuario) == "salir":
            print("🤖 CHATBOT: ¡Hasta luego!")
            break
        
        # Buscar y mostrar la respuesta
        respuesta = buscar_respuesta(usuario)
        print(f"🤖 CHATBOT: {respuesta}\n")

# ==============================================
# 5. EJECUTAR EL PROGRAMA
# ==============================================
if __name__ == "__main__":
    iniciar_chat()

# ==============================================
# 🧪 PRUEBA DE HUMO - SMOKE TEST 100 PREGUNTAS
# ==============================================
def prueba_de_efectividad():
    # Lista de las 100 preguntas
    lista_preguntas = [
        # TEMA 1: ORIGEN E HISTORIA (25)
        "¿Cuál es el origen de la computación?",
        "¿Cómo surgió la computación?",
        "¿De dónde viene la informática?",
        "¿Cuándo nació la computación?",
        "¿Con qué herramientas comenzó la computación?",
        "¿Qué se usaba antes de las computadoras?",
        "¿Cómo empezó todo en la computación?",
        "¿Cuál fue la primera herramienta de cálculo?",
        "¿Qué es el ábaco en la historia?",
        "¿Cómo evolucionaron las primeras máquinas?",
        "¿Quiénes fueron los pioneros de la computación?",
        "¿Qué importancia tuvo la máquina de Babbage?",
        "¿Cómo se hacían cálculos antes?",
        "¿Cuál es la historia inicial de la computación?",
        "¿Por qué nació la necesidad de calcular?",
        "¿Qué avances hubo al principio?",
        "¿Cómo pasó de herramientas simples a máquinas?",
        "¿Cuál fue el primer paso de la computación?",
        "¿Qué significa computación?",
        "¿Para qué se crearon las primeras herramientas?",
        "¿Cuál es la base histórica de la informática?",
        "¿Cómo se desarrolló la computación al inicio?",
        "¿Qué relación hay entre el ábaco y la computación?",
        "¿Cuándo se consideró el nacimiento de la informática?",
        "¿Cómo evolucionó el cálculo humano al automático?",

        # TEMA 2: INTELIGENCIA ARTIFICIAL (25)
        "¿Qué es la inteligencia artificial?",
        "¿Qué significa IA?",
        "¿Para qué sirve la IA?",
        "¿Cómo funciona la inteligencia artificial?",
        "¿Cuál es el objetivo de la IA?",
        "¿Qué hace la inteligencia artificial?",
        "¿Cómo se define la IA?",
        "¿En qué se diferencia la IA de otros sistemas?",
        "¿Qué capacidades tiene la inteligencia artificial?",
        "¿Puede la IA pensar como un humano?",
        "¿Qué tareas puede resolver la IA?",
        "¿Cómo aprenden los sistemas de IA?",
        "¿Qué rama de la informática es la IA?",
        "¿Por qué es importante la inteligencia artificial?",
        "¿Qué problemas resuelve la IA?",
        "¿Cómo imita la inteligencia humana?",
        "¿Qué es un sistema inteligente?",
        "¿Cuál es el propósito de crear IA?",
        "¿Qué características tiene la IA?",
        "¿Cómo ayuda la inteligencia artificial?",
        "¿Qué relación tiene la IA con la computación?",
        "¿Se puede considerar a la IA como pensamiento?",
        "¿Qué significa que la IA aprenda?",
        "¿Cómo se crean los programas de inteligencia artificial?",
        "¿Cuál es la meta principal de la IA?",

        # TEMA 3: EVOLUCIÓN Y DESARROLLO (25)
        "¿Cómo evolucionó la computación?",
        "¿Cuáles fueron los primeros avances?",
        "¿Qué pasó en los años 50 en la informática?",
        "¿Cómo se desarrolló la IA con el tiempo?",
        "¿Qué cambios hubo en la tecnología?",
        "¿Cómo avanzó la computación desde sus inicios?",
        "¿Qué importancia tienen los algoritmos?",
        "¿Cómo surgieron las redes neuronales?",
        "¿Cuál es la evolución de la IA hasta hoy?",
        "¿Cómo pasó de cálculos simples a inteligencia?",
        "¿Qué hitos marcaron la historia de la computación?",
        "¿Cómo se fue mejorando la capacidad de cálculo?",
        "¿Qué descubrimientos impulsaron la informática?",
        "¿Cómo es la tecnología actual comparada con la antigua?",
        "¿Cuáles fueron las etapas de desarrollo?",
        "¿Cómo influyeron los años 50 en la IA?",
        "¿Qué avances hay hoy en día?",
        "¿Cómo sigue evolucionando la inteligencia artificial?",
        "¿Qué relación hay entre evolución y necesidades humanas?",
        "¿Cómo se transformaron las máquinas?",
        "¿Cuál fue el progreso más rápido?",
        "¿Qué permitió el desarrollo de sistemas complejos?",
        "¿Cómo cambió el uso de la computación en la vida diaria?",
        "¿Cuál es el futuro de la evolución tecnológica?",
        "¿Qué hace que la tecnología siga avanzando?",

        # TEMA 4: MÁQUINAS Y AUTOMATIZACIÓN (15)
        "¿Por qué se crearon las primeras máquinas?",
        "¿Para qué sirven los cálculos automáticos?",
        "¿Qué es la automatización en informática?",
        "¿Cómo ayudan las máquinas a calcular?",
        "¿Qué ventaja tiene calcular con máquinas?",
        "¿Cómo funciona una máquina de cálculo?",
        "¿Qué relación hay entre cálculo y computación?",
        "¿Por qué la exactitud es importante?",
        "¿Cómo se lograron cálculos más rápidos?",
        "¿Qué significa automatizar tareas?",
        "¿Cómo pasó de hacer cuentas a mano a máquina?",
        "¿Qué necesidad impulsó las máquinas?",
        "¿Cómo mejoraron la velocidad y precisión?",
        "¿Qué tipo de tareas se pueden automatizar?",
        "¿Cuál es el vínculo entre máquina y cálculo?",

        # TEMA 5: SALUDOS Y OTRAS (10)
        "Hola",
        "Buenas tardes",
        "Buenos días",
        "Buenas noches",
        "¿Qué tal?",
        "Chau",
        "Adiós",
        "Hasta luego",
        "¿Cuál es tu color favorito?",
        "¿Qué hora es?"
    ]

    # Respuestas correctas esperadas
    respuestas_correctas = [
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La computación nace con herramientas simples como el ábaco y evoluciona con máquinas como la de Babbage, hasta llegar a las computadoras modernas.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de pensar, aprender y resolver problemas como lo haría un ser humano.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",
        "En los años 50 surgieron las primeras ideas. Luego avanzó con algoritmos, redes neuronales y hoy está presente en casi toda la tecnología.",

# CONTAR ACIERTOS Y CALCULAR EFECTIVIDAD
    aciertos = 0
    total_preguntas = len(lista_preguntas)

    print("🔎 INICIANDO PRUEBA DE 100 PREGUNTAS...\n")

    for i in range(total_preguntas):
        pregunta = lista_preguntas[i]
        respuesta_obtenida = buscar_respuesta(pregunta)
        respuesta_esperada = respuestas_correctas[i]

        # Comparamos si la respuesta es correcta
        if respuesta_obtenida.strip() == respuesta_esperada.strip():
            aciertos += 1
            print(f"✅ Pregunta {i+1}: CORRECTA")
        else:
            print(f"❌ Pregunta {i+1}: INCORRECTA")

    # RESULTADO FINAL
    porcentaje = (aciertos / total_preguntas) * 100
    print(f"\n📊 RESULTADO FINAL:")
    print(f" ✅ Aciertos: {aciertos} de {total_preguntas}")
    print(f" 🎯 EFECTIVIDAD: {porcentaje:.1f} %")


# ==============================================
# ✅ EJECUTAR TODO
# ==============================================
if __name__ == "__main__":
    # Elegí qué querés hacer: charlar o probar
    # Descomentá la opción que quieras usar

    # 1. Para charlar normal:
    # iniciar_chat()

    # 2. Para hacer la prueba de humo:
    prueba_de_efectividad()

      
       
