🤖 Agente Organizacional Inteligente – ISY0101

Integrantes: Bruno Araya – Jairo Huamán
Asignatura: Ingeniería de Soluciones con IA (ISY0101)
Docente: [Nombre del profesor]
Año: 2025

--------------------------------------------------------
🧩 DESCRIPCIÓN GENERAL
--------------------------------------------------------
Este proyecto implementa un agente funcional con herramientas
de consulta, escritura y razonamiento usando LangChain y Ollama.
El agente apoya la gestión organizacional mediante generación
automática de informes y reportes adaptativos.

Su propósito es demostrar la integración de modelos de lenguaje
locales (LLM) con procesos de memoria, planificación y toma de
decisiones en flujos organizacionales automatizados.

--------------------------------------------------------
⚙️ REQUISITOS
--------------------------------------------------------
- Python 3.10 o superior
- Ollama instalado y modelo local: llama3.2:3b

Instalación de dependencias:
pip install -r requirements.txt

--------------------------------------------------------
▶️ EJECUCIÓN
--------------------------------------------------------
Para iniciar el agente, ejecutar el siguiente comando
desde la carpeta principal del proyecto:

python main_agent.py

Durante la ejecución, puedes escribir instrucciones como:
- "Genera un informe de productividad semanal."
- "Crea un reporte detallado del área comercial."
- "Salir" para finalizar el agente.

--------------------------------------------------------
🧠 ARQUITECTURA DEL AGENTE
--------------------------------------------------------
Usuario → Agente → LLM (Ollama)
              ↘
           Tools (Consulta / Escritura)
              ↘
           Memoria de contexto (ConversationBufferMemory)

El agente usa el enfoque ReAct (razonamiento + acción) para
decidir automáticamente qué herramienta ejecutar en cada etapa.

--------------------------------------------------------
📚 REFERENCIAS
--------------------------------------------------------
- LangChain (2025). LangChain Documentation.
  https://python.langchain.com
- Ollama (2025). Local LLMs for Developers.
  https://ollama.ai
- Duoc UC (2025). Guía Evaluación Parcial N°2 – ISY0101.

--------------------------------------------------------
📦 ESTRUCTURA DEL PROYECTO
--------------------------------------------------------
AgenteOrganizacional_ISY0101_EP2/
 ┣ main_agent.py
 ┣ requirements.txt
 ┣ tools/
 ┃ ┣ consulta_tool.py
 ┃ ┗ escritura_tool.py
 ┗ README.txt

--------------------------------------------------------
✅ EVIDENCIAS DE FUNCIONAMIENTO
--------------------------------------------------------
El agente genera reportes de productividad y análisis
comerciales adaptativos en tiempo real, utilizando memoria
conversacional y razonamiento lógico. Se ejecuta con éxito
sobre el modelo local "llama3.2:3b" mediante Ollama.
