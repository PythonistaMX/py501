# Aplicaciones Agénticas Profesionales con LangChain (Py501)

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://codespaces.new/PythonistaMX/py501)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg?style=for-the-badge)](LICENSE)
[![LangChain](https://img.shields.io/badge/Agentes-LangChain%201.4-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://docs.langchain.com/)
[![LangGraph](https://img.shields.io/badge/Runtime-LangGraph-1C3C3C?style=for-the-badge)](https://docs.langchain.com/oss/python/langgraph/overview)

Este repositorio contiene el material oficial del curso **Py501 · Aplicaciones Agénticas Profesionales con LangChain** de **Pythonista®**, impartido por José Luis Chiquete. El curso enseña a diseñar, controlar, evaluar y operar agentes de IA con el ecosistema *LangChain* 1.x: herramientas, RAG, MCP, *middleware*, *LangGraph*, memoria, *Deep Agents*, evaluación, seguridad y despliegue.

---

## 🗺️ Ruta de Aprendizaje

### Prerequisitos recomendados

Este curso asume *Python* intermedio: funciones, clases, tipos, `async`/`await` y consumo de APIs.

| Curso | Título | Repositorio |
| :--- | :--- | :--- |
| Py101 | Introducción a la Programación con Python | [PythonistaMX/py101](https://github.com/PythonistaMX/py101) |
| Py111 | Programación Orientada a Objetos con Python | [PythonistaMX/py111](https://github.com/PythonistaMX/py111) |

---

## 🚀 Acerca del Curso

Un curso de **8 sesiones en vivo de 2 horas** (16 horas) sobre *notebooks* de *Jupyter* que corren en **GitHub Codespaces**: cerca de 60% teoría y casos de diseño, 30% laboratorios guiados y 10% demo final. Al completarlo serás capaz de:

* **Decidir cuándo usar un agente:** niveles de autonomía, patrones de diseño y modos de falla.
* **Construir agentes con `create_agent`:** herramientas bien diseñadas, salida estructurada y *streaming*, con cualquier proveedor de modelos.
* **Conectar agentes a datos y sistemas:** RAG como herramienta y servidores MCP.
* **Controlar el ciclo del agente:** *middleware* de aprobación humana, redacción de datos personales y límites.
* **Diseñar flujos con *LangGraph*:** estado, ejecución durable, interrupciones y patrones multiagente.
* **Dar memoria a los agentes:** memoria por hilo y por usuario, y agentes profundos para tareas largas.
* **Llevar un agente a producción:** evaluación de respuesta y trayectoria, observabilidad, seguridad, costos y despliegue.

A lo largo del curso se construye un mismo sistema: el **asistente de soporte interno** de *Andina Logística*, una empresa ficticia, que consulta políticas, gestiona tickets por MCP y escala casos a una persona.

---

## 📅 Temario y Estructura

El curso consta de **8 sesiones en vivo de 2 horas**, divididas en 10 módulos. Los *notebooks* se numeran por tema y cada sesión abarca uno o varios.

| Módulo | Temas | Notebooks |
| :--- | :--- | :--- |
| 1. Fundamentos | Qué es un agente, ciclo de razonar-actuar-observar, autonomía, patrones y modos de falla | `01`-`02` |
| 2. Ecosistema *LangChain* v1 | Paquetes, modelos intercambiables, bloques de contenido, salida estructurada, `create_agent` | `03`-`04` |
| 3. Herramientas, contexto y RAG | Ingeniería de contexto, diseño de herramientas, fragmentación, *embeddings*, reordenamiento | `05`-`06` |
| 4. MCP | Clientes y servidores MCP, riesgos, comunicación entre agentes (A2A) | `07` |
| 5. *Middleware* | Aprobación humana, datos personales, límites, *middleware* propio | `08` |
| 6. *LangGraph* | Estado, reductores, *checkpointers*, interrupciones, ejecución durable, supervisor y especialistas | `09`-`10` |
| 7. Memoria y *Deep Agents* | Memoria de corto y largo plazo, *store*, planificación, archivos y subagentes | `11`-`12` |
| 8. Evaluación y observabilidad | Conjuntos de prueba, respuesta y trayectoria, LLM como juez, experimentos en *LangSmith* | `13` |
| 9. Seguridad, costos y despliegue | Inyección indirecta, costo por conversación, opciones de despliegue, lista de verificación | `14` |
| 10. Demo final | El sistema completo integrado | `15` |

### Práctica

* Los *notebooks* `02` a `14` tienen **ejercicios básicos** y **retos opcionales**; se trabajan en clase y como práctica.
* `15_demo_final_integradora.ipynb` es la demo del instructor y la referencia para el proyecto final.

### 📚 Contenidos

#### 🧭 Tabla de contenidos (enlaces rápidos)
- [01_bienvenida_y_entorno.ipynb](01_bienvenida_y_entorno.ipynb)
- [02_que_es_un_agente.ipynb](02_que_es_un_agente.ipynb)
- [03_ecosistema_langchain_v1.ipynb](03_ecosistema_langchain_v1.ipynb)
- [04_primer_agente_con_create_agent.ipynb](04_primer_agente_con_create_agent.ipynb)
- [05_herramientas_y_contexto.ipynb](05_herramientas_y_contexto.ipynb)
- [06_rag_como_herramienta.ipynb](06_rag_como_herramienta.ipynb)
- [07_mcp.ipynb](07_mcp.ipynb)
- [08_middleware.ipynb](08_middleware.ipynb)
- [09_langgraph_estado_y_grafos.ipynb](09_langgraph_estado_y_grafos.ipynb)
- [10_patrones_multiagente.ipynb](10_patrones_multiagente.ipynb)
- [11_memoria_de_largo_plazo.ipynb](11_memoria_de_largo_plazo.ipynb)
- [12_deep_agents.ipynb](12_deep_agents.ipynb)
- [13_evaluacion_y_observabilidad.ipynb](13_evaluacion_y_observabilidad.ipynb)
- [14_seguridad_costos_y_despliegue.ipynb](14_seguridad_costos_y_despliegue.ipynb)
- [15_demo_final_integradora.ipynb](15_demo_final_integradora.ipynb)

#### 🔹 Módulo 1: Fundamentos de sistemas agénticos
* `01` - Bienvenida, reglas del curso, claves de API como secretos de *Codespaces* y verificación del entorno.
* `02` - Qué es un agente; el ciclo de razonar, actuar y observar construido a mano; niveles de autonomía; patrones (ReAct, planificar y ejecutar, reflexión, orquestador); modos de falla.

#### 🔹 Módulo 2: El ecosistema *LangChain* v1
* `03` - Mapa de paquetes; `init_chat_model` con `"proveedor:modelo"`; `content_blocks` y `usage_metadata`; comparación de modelos; salida estructurada con *Pydantic*; procesamiento en lote.
* `04` - Laboratorio: herramientas con `@tool`, `create_agent`, el grafo que genera, `response_format`, *streaming* y trazas en *LangSmith*.

#### 🔹 Módulo 3: Herramientas, contexto y RAG
* `05` - Ingeniería de contexto; diseño de herramientas (nombres, descripciones, tipos, granularidad, errores útiles); proteger el contexto.
* `06` - Laboratorio: fragmentación por estructura y tamaño, *embeddings*, índice vectorial, RAG agéntico y reordenamiento.

#### 🔹 Módulo 4: MCP y comunicación entre agentes
* `07` - Arquitectura de MCP y transportes; agente con políticas y tickets; servidor MCP propio; riesgos de MCP, inyección por resultados y A2A.

#### 🔹 Módulo 5: *Middleware*
* `08` - *Middleware* incluido (aprobación humana, datos personales, límites); decisiones aprobar, editar y rechazar; *middleware* propio con `@wrap_tool_call`; orden de la pila.

#### 🔹 Módulo 6: *LangGraph*
* `09` - Estado, reductores, nodos y aristas condicionales; *checkpointers*, `interrupt` y viaje en el tiempo; el asistente como grafo; falla y reanudación.
* `10` - Patrones multiagente; supervisor con especialistas como herramientas; comparación de latencia y tokens contra un solo agente.

#### 🔹 Módulo 7: Memoria y *Deep Agents*
* `11` - Memoria de corto y largo plazo; *store* por usuario con `ToolRuntime`; olvidar; memoria semántica.
* `12` - `create_deep_agent`: lista de tareas, sistema de archivos virtual y subagentes; cuándo usar cada nivel de abstracción.

#### 🔹 Módulo 8: Evaluación y observabilidad
* `13` - Conjunto de 15 casos típicos, límite y adversarios; evaluación de respuesta y trayectoria; regresiones; LLM como juez; experimentos en *LangSmith*.

#### 🔹 Módulo 9: Seguridad, costos y despliegue
* `14` - Inyección indirecta y defensa en profundidad; costo por conversación; *LangGraph* Platform, contenedor propio y *runtimes* de nube; lista de verificación de 20 puntos.

#### 🔹 Módulo 10: Demo final
* `15` - Sistema completo: RAG, MCP, grafo con clasificador, *middleware*, memoria por usuario y prueba de regresión.

> **📝 Nota:** Las celdas `# TU CÓDIGO AQUÍ` y **✍️ Tu respuesta** son para ti. Las versiones resueltas están en `soluciones/` (`NN_..._soluciones.ipynb`); `01` y `15` no tienen ejercicios. Cada *notebook* es independiente y se puede abrir y ejecutar por separado.

#### 📁 Datos y servicios
* `data/politicas/` - Políticas internas de *Andina Logística* (empresa ficticia): vacaciones, equipo de cómputo y gastos de viaje.
* `mcp_servers/tickets_server.py` - Servidor MCP simulado de tickets (transporte `stdio`); guarda los tickets en `data/tickets.db`.

---

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales! Este repositorio está configurado para **GitHub Codespaces**.

### 1. Claves de API

Antes de crear el *Codespace*, agrega tus claves como **secretos de Codespaces** en **github.com/settings/codespaces** y dales acceso a este repositorio:

| Secreto | Obligatorio | Dónde se obtiene |
| :--- | :--- | :--- |
| `GOOGLE_API_KEY` | Sí (modelo por defecto: *Gemini*) | [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key) |
| `LANGSMITH_API_KEY` | Recomendado (trazas y evaluación) | [smith.langchain.com](https://smith.langchain.com/) |
| `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` | No (comparar modelos) | Consola de cada proveedor |

> ⚠️ **Nunca** escribas una clave en un *notebook* ni en un archivo del repositorio: es público.

### 2. Crear el *Codespace*

1. Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2. Ve a la pestaña **"Codespaces"**.
3. Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con:
* *Python* 3.12
* Extensiones de *Python* y *Jupyter* para VS Code
* *Docker* (para el módulo de despliegue)
* Todas las librerías del curso con versiones fijadas en `requirements.txt`: *LangChain*, *LangGraph*, *LangSmith*, integraciones de *Gemini*, *OpenAI* y *Anthropic*, adaptadores de MCP y *Deep Agents*.

> ⚠️ **ADVERTENCIA: el ecosistema cambia rápido.** El curso usa *LangChain* 1.4 y *LangGraph* 1.2. Los tutoriales anteriores a la versión 1.0 (octubre de 2025) usan `AgentExecutor`, `initialize_agent` o `create_react_agent`, que hoy son código heredado. `deepagents` aún no llega a la versión 1.0 y puede romper compatibilidad entre versiones menores. No actualices `requirements.txt` durante el curso.

La primera vez tarda unos minutos porque instala las librerías. Después abre `01_bienvenida_y_entorno.ipynb`, elige el kernel **Python 3.12** (`/usr/local/bin/python`) en **Select Kernel** y ejecuta las celdas en orden con `Shift + Enter`.

> 💡 Cada ejecución llama a un modelo de lenguaje y consume tokens de tu clave. Codespaces se detiene solo tras un rato de inactividad; para no gastar tus horas gratuitas, detenlo al terminar: **github.com/codespaces** → `…` → **Stop codespace**.

### Ejecución Local (Opcional)
Si prefieres trabajar en tu máquina:

```bash
# Clonar el repositorio
git clone https://github.com/PythonistaMX/py501.git
cd py501

# Crear entorno virtual (Python 3.12)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar claves
cp .env.example .env      # y completa los valores

# Iniciar Jupyter
jupyter lab
```

En local, la celda de preparación de cada *notebook* carga `.env` automáticamente.

---

## 📖 Recursos Adicionales

* [Documentación oficial de *LangChain*](https://docs.langchain.com/oss/python/langchain/overview)
* [Documentación oficial de *LangGraph*](https://docs.langchain.com/oss/python/langgraph/overview)
* [Documentación oficial de *LangSmith*](https://docs.smith.langchain.com/)
* [Especificación de *Model Context Protocol*](https://modelcontextprotocol.io/)
* [Anuncio de *LangChain* y *LangGraph* 1.0](https://www.langchain.com/blog/langchain-langgraph-1dot0)

---

## 📝 Licencia

Este proyecto está bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC-BY 4.0)**.

**Eres libre de:**
- ✅ Compartir el material en cualquier medio o formato
- ✅ Adaptar, remezclar y crear contenido derivado
- ✅ Usar con fines comerciales

**Con la condición de:**
- 📌 **Atribución:** Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se han realizado cambios.

Para más información, visita: https://creativecommons.org/licenses/by/4.0/

Véase el archivo [LICENSE](LICENSE) para los términos completos.

&copy; José Luis Chiquete Valdivieso. 2017-2026.
