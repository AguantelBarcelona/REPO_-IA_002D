# -*- coding: utf-8 -*-
from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory


# CONFIGURACIÓN DEL MODELO

llm = Ollama(model="llama3.2:3b")


# MEMORIA CONVERSACIONAL

memory = ConversationBufferMemory(memory_key="historial")


# HERRAMIENTAS DEL AGENTE

def generar_informe_productividad(input_text=None):
    return (
        "📊 Informe de productividad semanal:\n"
        "- Incremento del 15% respecto a la semana anterior.\n"
        "- 95 ventas cerradas con una tasa de conversión del 17%.\n"
        "- Se observó un mejor aprovechamiento del tiempo en llamadas comerciales."
    )

def generar_reporte_detallado(input_text=None):
    return (
        "📘 Informe detallado del área comercial:\n"
        "- Ventas totales: $150.000\n"
        "- Llamadas realizadas: 120\n"
        "- Tasa de conversión: 18%\n"
        "- Conclusión: mejora sostenida en la eficiencia operativa del equipo, "
        "gracias a la automatización de tareas y mejor gestión del tiempo."
    )


# REGISTRO DE HERRAMIENTAS

tools = [
    Tool(
        name="Generar informe de productividad",
        func=generar_informe_productividad,
        description="Crea un informe breve sobre la productividad del equipo de ventas."
    ),
    Tool(
        name="Generar reporte detallado",
        func=generar_reporte_detallado,
        description="Genera un reporte completo con métricas, conclusiones y análisis del desempeño semanal."
    )
]


# INICIALIZACIÓN DEL AGENTE

agente = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    memory=memory,
    verbose=True
)

print("🤖 Agente Organizacional Inteligente (Ollama) en ejecución...\n")


# EJECUCIÓN DE PRUEBA

resultado = agente.invoke({"input": "Genera un informe breve sobre productividad semanal del equipo de ventas."})
print("\n🧾 Resultado del agente:")
print(resultado["output"])
# MODO INTERACTIVO EN CONSOLA
print("\n🟢 Modo interactivo iniciado. Escribe tus instrucciones (o 'salir' para terminar).")

while True:
    entrada = input("\n🧑‍💼 Ingreso del usuario: ")
    if entrada.lower() in ["salir", "exit", "quit"]:
        print("\n👋 Finalizando agente organizacional. ¡Hasta luego!")
        break
    try:
        resultado = agente.invoke({"input": entrada})
        print("\n🤖 Respuesta del agente:")
        print(resultado["output"])
    except Exception as e:
        print(f"⚠️ Error al procesar la solicitud: {e}")
