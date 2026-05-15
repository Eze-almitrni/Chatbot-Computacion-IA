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
