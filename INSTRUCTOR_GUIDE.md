# Instructor Guide - Py501

Guía operativa para impartir **Py501 · Aplicaciones Agénticas Profesionales con LangChain** con consistencia técnica y pedagógica. El material no fija fechas ni horarios para que sirva en cualquier edición.

## Estructura (8 sesiones de 2 horas, 16 *notebooks*)

Los *notebooks* se numeran por tema, en orden, a lo largo de todo el curso; cada sesión abarca uno o varios, como indica la agenda de cada sesión más abajo.

Cada *notebook* es independiente: tiene su propia celda de preparación (`RAIZ`, `DATA`, `POLITICAS`, `MODELO`, `EMBEDDINGS` y verificación de la clave) y, cuando necesita herramientas de un *notebook* anterior, las vuelve a definir. Los temas con ejercicios tienen su versión resuelta en `soluciones/NN_tema_soluciones.ipynb`; `00`, `01` y `15` no tienen ejercicios ni soluciones. `00_claves_de_api_y_secretos.ipynb` es **pre-trabajo**: se resuelve antes de la sesión 1.

**Modelo del curso:** *Gemini* (`google_genai:gemini-3.5-flash` y `google_genai:gemini-embedding-001`). Todo el material está probado con esa configuración; otros proveedores solo aparecen en los ejercicios de comparación de `03` y `13`. Dilo explícitamente en la sesión 1: el código es portable, pero en clase todos usan *Gemini*.

**Hilo conductor:** el asistente de soporte interno de *Andina Logística* (empresa ficticia). Las políticas están en `data/politicas/` y el servidor MCP de tickets en `mcp_servers/tickets_server.py`.

**Proporción:** cerca de 60% teoría y casos de diseño, 30% laboratorios (`04`, `06`, `07`, `08`, `09`, `11`, `13`) y 10% demo final (`15`).

## Objetivos y agenda por sesión

Los ejercicios que no alcancen a resolverse en clase quedan como práctica; los retos son siempre opcionales.

### Sesión 1 · Módulos 1 y 2: Fundamentos y ecosistema

**Notebooks:** [`01_bienvenida_y_entorno`](01_bienvenida_y_entorno.ipynb), [`02_que_es_un_agente`](02_que_es_un_agente.ipynb), [`03_ecosistema_langchain_v1`](03_ecosistema_langchain_v1.ipynb).

**Descripción:** En esta sesión se verificará el entorno, se construirá a mano el ciclo de un agente y se recorrerá el ecosistema *LangChain* 1.x.

**Objetivo:** Entender qué es un agente **construyendo su ciclo a mano** y decidir cuándo conviene usarlo.

Al terminar, el participante podrá:
1. Explicar el ciclo de razonar, actuar y observar, y los niveles de autonomía.
2. Reconocer los patrones ReAct, planificar y ejecutar, reflexión y orquestador.
3. Identificar los modos de falla de un agente y su defensa.
4. Inicializar modelos de cualquier proveedor con `init_chat_model` y obtener salida estructurada.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 15 | Bienvenida, reglas, secretos y verificación del entorno | `01_bienvenida_y_entorno` |
| 15 | Del modelo al agente; niveles de autonomía | `02_que_es_un_agente` |
| 25 | El ciclo a mano y ejercicio 1 (pasos y tokens) | `02_que_es_un_agente` |
| 10 | Patrones, modos de falla y caso de diseño (ejercicio 2) | `02_que_es_un_agente` |
| 15 | Mapa de paquetes, modelos intercambiables y bloques de contenido | `03_ecosistema_langchain_v1` |
| 25 | Salida estructurada y ejercicios 1 y 2 | `03_ecosistema_langchain_v1` |
| 15 | Holgura: problemas de claves o *Codespace* | — |

### Sesión 2 · Módulos 2 y 3: Primer agente y diseño de herramientas

**Notebooks:** [`04_primer_agente_con_create_agent`](04_primer_agente_con_create_agent.ipynb), [`05_herramientas_y_contexto`](05_herramientas_y_contexto.ipynb).

**Descripción:** En esta sesión se construirá el primer agente con `create_agent` y se estudiará cómo el diseño de herramientas y del contexto determina su calidad.

**Objetivo:** Construir un agente funcional y **diagnosticar su comportamiento con trazas**.

Al terminar, el participante podrá:
1. Escribir herramientas con tipos, *docstrings* y errores útiles.
2. Crear un agente con `create_agent`, `response_format` y *streaming*.
3. Leer una traza en *LangSmith* para explicar qué hizo el agente.
4. Aplicar ingeniería de contexto: qué entra en la ventana y cómo protegerla.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 15 | Herramientas y ejercicio 1 (`crear_ticket`) | `04_primer_agente_con_create_agent` |
| 20 | El agente, su grafo y las trazas | `04_primer_agente_con_create_agent` |
| 25 | Salida estructurada, *streaming* y ejercicio 2 (*docstring*) | `04_primer_agente_con_create_agent` |
| 15 | Ingeniería de contexto | `05_herramientas_y_contexto` |
| 30 | Diseño de herramientas y ejercicios 1 y 2 | `05_herramientas_y_contexto` |
| 15 | Errores útiles, salidas acotadas y cierre | `05_herramientas_y_contexto` |

### Sesión 3 · Módulos 3 y 4: RAG y MCP

**Notebooks:** [`06_rag_como_herramienta`](06_rag_como_herramienta.ipynb), [`07_mcp`](07_mcp.ipynb).

**Descripción:** En esta sesión se conectará el agente a documentos con RAG y a un sistema de tickets con MCP.

**Objetivo:** Conectar el agente a **datos** (RAG) y a **sistemas** (MCP) sin código a la medida.

Al terminar, el participante podrá:
1. Fragmentar documentos, indexarlos con *embeddings* y exponer la búsqueda como herramienta.
2. Distinguir RAG clásico de RAG agéntico y decidir si el reordenamiento justifica su costo.
3. Conectar un agente a un servidor MCP y escribir un servidor propio.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 15 | Fragmentación e índice vectorial | `06_rag_como_herramienta` |
| 20 | Búsqueda como herramienta; RAG clásico vs. agéntico | `06_rag_como_herramienta` |
| 25 | Reordenamiento y ejercicios 1 y 2 | `06_rag_como_herramienta` |
| 15 | ¿Qué es MCP?; herramientas del servidor de tickets | `07_mcp` |
| 20 | Agente con políticas + tickets | `07_mcp` |
| 25 | Servidor propio: ejercicio 1 | `07_mcp` |

### Sesión 4 · Módulos 4 y 5: Riesgos de MCP y *middleware*

**Notebooks:** [`07_mcp`](07_mcp.ipynb), [`08_middleware`](08_middleware.ipynb).

**Descripción:** En esta sesión se revisarán los riesgos de MCP y se agregará control al agente con *middleware*.

**Objetivo:** Agregar **gobierno** al agente sin reescribirlo.

Al terminar, el participante podrá:
1. Reconocer riesgos de MCP e inyección por resultados de herramientas.
2. Configurar aprobación humana, redacción de datos personales y límites.
3. Reanudar un agente pausado con aprobar, editar o rechazar.
4. Escribir *middleware* propio y razonar sobre el orden de la pila.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Ejercicio 2 (antigüedad sin preguntar) | `07_mcp` |
| 20 | Riesgos de MCP, A2A y reto de inyección | `07_mcp` |
| 15 | ¿Qué es el *middleware*?; *middleware* incluido | `08_middleware` |
| 25 | La pila, la interrupción y la reanudación; ejercicio 1 (`edit`) | `08_middleware` |
| 35 | *Middleware* propio y ejercicio 2 (aprobar solo lo urgente) | `08_middleware` |
| 15 | Caso de diseño: orden de la pila para mover dinero | `08_middleware` |

### Sesión 5 · Módulo 6: *LangGraph*

**Notebooks:** [`09_langgraph_estado_y_grafos`](09_langgraph_estado_y_grafos.ipynb).

**Descripción:** En esta sesión se construirán grafos explícitos con estado, *checkpointers* e interrupciones, y se convertirá el asistente en un grafo durable.

**Objetivo:** Saber **cuándo bajar de `create_agent` a un grafo propio** y cómo diseñarlo.

Al terminar, el participante podrá:
1. Definir estado con reductores, nodos y aristas condicionales.
2. Usar *checkpointers*, `interrupt` y el historial de *checkpoints*.
3. Reanudar un grafo tras una falla sin repetir pasos.
4. Usar agentes de `create_agent` como nodos de un grafo.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 20 | Estado, nodos y aristas con un grafo sin modelos | `09_langgraph_estado_y_grafos` |
| 20 | *Checkpointers*, interrupciones y viaje en el tiempo | `09_langgraph_estado_y_grafos` |
| 30 | El asistente de soporte como grafo | `09_langgraph_estado_y_grafos` |
| 15 | Falla y reanudación | `09_langgraph_estado_y_grafos` |
| 35 | Ejercicios 1 y 2 (ruta `otro`, *streaming* de tokens) | `09_langgraph_estado_y_grafos` |

### Sesión 6 · Módulos 6 y 7: Multiagente y memoria

**Notebooks:** [`10_patrones_multiagente`](10_patrones_multiagente.ipynb), [`11_memoria_de_largo_plazo`](11_memoria_de_largo_plazo.ipynb), [`12_deep_agents`](12_deep_agents.ipynb).

**Descripción:** En esta sesión se comparará un supervisor con especialistas contra un solo agente, se agregará memoria por usuario y se presentarán los agentes profundos.

**Objetivo:** Decidir **con datos** cuándo usar varios agentes, memoria o un agente profundo.

Al terminar, el participante podrá:
1. Construir un supervisor con especialistas como herramientas y comparar costo y latencia.
2. Distinguir memoria de corto y largo plazo e implementar memoria por usuario con `ToolRuntime`.
3. Usar `create_deep_agent` con lista de tareas, archivos y subagentes, y darle instrucciones con `AGENTS.md` y *skills*.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Patrones multiagente | `10_patrones_multiagente` |
| 25 | Supervisor vs. un solo agente; ejercicio 2 | `10_patrones_multiagente` |
| 15 | Tipos de memoria; herramientas con `ToolRuntime` | `11_memoria_de_largo_plazo` |
| 25 | Memoria por usuario; ejercicios 1 y 2 | `11_memoria_de_largo_plazo` |
| 40 | Agente profundo de análisis de políticas, *harness*, *skills* y caso de diseño | `12_deep_agents` |
| 5 | Holgura y cierre | — |

### Sesión 7 · Módulos 8 y 9: Evaluación y seguridad

**Notebooks:** [`13_evaluacion_y_observabilidad`](13_evaluacion_y_observabilidad.ipynb), [`14_seguridad_costos_y_despliegue`](14_seguridad_costos_y_despliegue.ipynb).

**Descripción:** En esta sesión se medirá el agente con un conjunto de prueba, se controlarán regresiones y se demostrará una inyección indirecta con sus defensas.

**Objetivo:** Demostrar **con datos** que el agente funciona y resistir ataques comunes.

Al terminar, el participante podrá:
1. Construir un conjunto de prueba con casos típicos, límite y adversarios.
2. Evaluar respuesta final y trayectoria, y usar un LLM como juez.
3. Ejecutar y comparar experimentos en *LangSmith*.
4. Aplicar defensa en profundidad contra la inyección indirecta.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 15 | ¿Qué se evalúa?; conjunto de prueba y evaluadores | `13_evaluacion_y_observabilidad` |
| 30 | Ejercicio 1: corregir el peor caso sin regresiones | `13_evaluacion_y_observabilidad` |
| 20 | LLM como juez (ejercicio 2) | `13_evaluacion_y_observabilidad` |
| 20 | El experimento en *LangSmith* | `13_evaluacion_y_observabilidad` |
| 35 | Inyección indirecta, permisos y *sandboxes*, y ejercicio 1 (defender el agente) | `14_seguridad_costos_y_despliegue` |

### Sesión 8 · Módulos 9 y 10: Costos, despliegue y demo final

**Notebooks:** [`14_seguridad_costos_y_despliegue`](14_seguridad_costos_y_despliegue.ipynb), [`15_demo_final_integradora`](15_demo_final_integradora.ipynb).

**Descripción:** En esta sesión se estimarán costos, se revisarán las opciones de despliegue y la lista de verificación, y el instructor presentará el sistema completo.

**Objetivo:** Tener criterios para decir **"esto ya puede salir a producción"**.

Al terminar, el participante podrá:
1. Estimar el costo por conversación y proponer cambios de diseño que lo reduzcan.
2. Elegir entre *LangGraph* Platform, contenedor propio o *runtimes* de nube.
3. Aplicar la lista de verificación de 20 puntos a su propio agente.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 15 | Costos y ejercicio 2 (costo mensual) | `14_seguridad_costos_y_despliegue` |
| 10 | Opciones de despliegue | `14_seguridad_costos_y_despliegue` |
| 5 | Lista de verificación para producción | `14_seguridad_costos_y_despliegue` |
| 10 | Demo: arquitectura y piezas | `15_demo_final_integradora` |
| 20 | Demo: RAG + MCP + *middleware* + memoria | `15_demo_final_integradora` |
| 15 | Demo: el grafo completo e interrupción anidada | `15_demo_final_integradora` |
| 15 | Demo: regresión al cambiar de modelo | `15_demo_final_integradora` |
| 30 | Preguntas, revisión de documentos de arquitectura y cierre | — |

## Resultados de aprendizaje por módulo

- 1. Fundamentos: explicar el ciclo de un agente y elegir el nivel de autonomía adecuado.
- 2. Ecosistema *LangChain* v1: construir agentes con `create_agent` con cualquier proveedor.
- 3. Herramientas, contexto y RAG: diseñar herramientas y contexto; implementar RAG agéntico.
- 4. MCP: conectar agentes a sistemas mediante MCP y reconocer sus riesgos.
- 5. *Middleware*: agregar aprobación humana, protección de datos y límites.
- 6. *LangGraph*: diseñar flujos durables, auditables y multiagente.
- 7. Memoria y *Deep Agents*: dar memoria por usuario y resolver tareas largas.
- 8. Evaluación: medir respuesta y trayectoria y controlar regresiones.
- 9. Seguridad, costos y despliegue: aplicar defensa en profundidad, estimar costos y elegir dónde desplegar.

## Evaluación

| Componente | Peso | Descripción |
|---|---|---|
| Agente de laboratorio | 40% | El asistente construido en `04` a `13` funciona de punta a punta y aprueba al menos 12 de los 15 casos de `13` |
| Documento de arquitectura | 30% | Propuesta de un agente para su propio trabajo: patrón, herramientas, *middleware*, memoria, evaluación y riesgos (máximo 4 páginas), revisado con la lista de `14` |
| Casos de diseño | 20% | Participación en los ejercicios de respuesta escrita (`02`, `05`, `08`, `10`, `11`, `12`) |
| Examen corto | 10% | 15 preguntas de opción múltiple sobre conceptos y decisiones |

### Reglas sugeridas

- **Sugerido:** cuenta como asistencia estar conectado al menos 90 de los 120 minutos; ver la grabación no cuenta.

## Checklist previa a clase

- Enviar a los alumnos, una semana antes, el enlace al *notebook* [`00_claves_de_api_y_secretos.ipynb`](00_claves_de_api_y_secretos.ipynb) y pedirles que creen `GOOGLE_API_KEY` y `LANGSMITH_API_KEY`, las guarden como secretos de *Codespaces* y ejecuten la sección 6 de `00_claves_de_api_y_secretos.ipynb` y `01_bienvenida_y_entorno` completo.
- Codespace creado desde `main` y dependencias instaladas (`postCreateCommand`).
- Los *notebooks* de la sesión y sus versiones en `soluciones/` corren de principio a fin con una clave real (workflow `notebooks-smoke.yml` en verde, con los secretos del repositorio configurados).
- Una clave de respaldo del instructor por si un alumno no puede usar la suya.
- Material de la sesión publicado.

## Checklist de cierre de sesión

- Se cubrieron los objetivos de la sesión.
- Asistencia registrada.
- Grabación y práctica publicadas.
- Dudas frecuentes registradas para mejorar los *notebooks*.

## Riesgos comunes y mitigación

- **Claves que no aparecen en el *Codespace*:** el secreto no tiene acceso al repositorio (o al *fork* del alumno) o el *Codespace* se inició antes de crearlo. Ver la sección 7 de `00_claves_de_api_y_secretos.ipynb`.
- **Límites de la API (cuota o tasa):** las celdas están pensadas para pocas ejecuciones; usar un modelo pequeño (`MODELO=google_genai:gemini-3.5-flash`) y la clave de respaldo.
- **Respuestas distintas a las del instructor:** es normal; se discute el comportamiento (herramientas, orden, argumentos), no el texto exacto.
- **`asyncio.run()` en *Jupyter*:** falla porque ya hay un *event loop*; usar `await` directamente en la celda.
- **Cambios del ecosistema:** las versiones están fijadas en `requirements.txt`; no actualizar durante una edición. Revisar notas de versión de *LangChain*, *LangGraph* y `deepagents` antes de cada edición.
- **Tickets acumulados entre sesiones:** borrar `data/tickets.db` para empezar de cero; el servidor la recrea.
- **Tiempo insuficiente:** priorizar los laboratorios y dejar los retos como práctica.
