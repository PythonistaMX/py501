# Tutorial: claves de API y secretos de GitHub Codespaces (Py501)

Este tutorial explica, paso a paso, cómo obtener las claves de API que usa el curso y cómo guardarlas de forma segura para que los *notebooks* las lean **sin que nunca aparezcan escritas en el código**. Hazlo **antes de la sesión 1**: toma unos 20 minutos.

---

## 0. Antes de empezar: qué es un secreto y por qué importa

* Una **clave de API** es una contraseña que identifica tu cuenta ante un servicio (*Gemini*, *LangSmith*). Quien la tenga puede consumir tu cuota y generar cargos a tu nombre.
* Un **secreto de Codespaces** es una variable cifrada que guardas en tu cuenta de GitHub. Cuando abres un *Codespace* de un repositorio autorizado, GitHub la inyecta como **variable de entorno** (por ejemplo, `GOOGLE_API_KEY`). El código la lee con `os.environ["GOOGLE_API_KEY"]` y la clave nunca se escribe en un archivo.
* Este repositorio es **público**. Una clave escrita en un *notebook*, aunque la borres después, queda en el historial de Git y cualquiera puede encontrarla.

**Regla del curso:** las claves solo viven en los secretos de Codespaces (o en un archivo `.env` local que Git ignora). Nunca en un *notebook*, nunca en un mensaje, nunca en una captura de pantalla.

---

## 1. El modelo del curso: Gemini

**En este curso se usa *Gemini* de Google como modelo por defecto** (`google_genai:gemini-3.5-flash`) y sus *embeddings* (`google_genai:gemini-embedding-001`). Todos los ejemplos, ejercicios y soluciones están probados con esa configuración.

*LangChain* permite usar **cualquier proveedor** cambiando una sola cadena (`"proveedor:modelo"`), y el *notebook* `03` lo demuestra con *OpenAI* y *Anthropic*. Aun así, para que todos veamos el mismo comportamiento en clase, **todos usaremos Gemini**. Las claves de otros proveedores son **opcionales** y solo sirven para los ejercicios de comparación.

| Variable | ¿Obligatoria? | Para qué | Dónde se obtiene |
| :--- | :--- | :--- | :--- |
| `GOOGLE_API_KEY` | **Sí** | Modelo y *embeddings* de *Gemini* | [Google AI Studio](https://aistudio.google.com/) |
| `LANGSMITH_API_KEY` | Muy recomendada | Trazas (todos los *notebooks*) y evaluaciones (`13`) | [smith.langchain.com](https://smith.langchain.com/) |
| `OPENAI_API_KEY` | No | Comparar modelos (`03`, `13`) | Consola de *OpenAI* |
| `ANTHROPIC_API_KEY` | No | Comparar modelos (`03`, `13`) | Consola de *Anthropic* |

> 💡 *Gemini* acepta la clave en `GOOGLE_API_KEY` o en `GEMINI_API_KEY`; si existen las dos, gana `GOOGLE_API_KEY`. **En este curso usamos siempre `GOOGLE_API_KEY`.**

---

## 2. Obtener la clave de Gemini

1. Entra a **[aistudio.google.com](https://aistudio.google.com/)** con tu cuenta de Google y acepta los términos de servicio.
2. Si es tu primera vez, *AI Studio* crea automáticamente un proyecto de Google Cloud y una clave. Si ya tenías proyectos de Google Cloud, primero impórtalos desde **Dashboard → Projects → Import projects**.
3. Abre la página **API Keys** y haz clic en **Create API key**. Elige el proyecto.
4. Copia la clave. **No la pegues en ningún otro lado** que no sea el secreto del paso 4.
5. Recomendado: en la misma página, verifica que la clave esté **restringida a la *Gemini API***. Las claves nuevas ya se crean así; si alguna aparece como *Unrestricted*, usa **Add restrictions → Restrict to Gemini API only**. Las claves estándar sin restricción ya no son aceptadas por la *Gemini API*.

> ⚠️ **Costos y límites.** La *Gemini API* tiene un nivel gratuito con límites de solicitudes por minuto y por día que Google cambia con frecuencia. Consulta los límites vigentes en *AI Studio* antes del curso. Si vinculas facturación a tu proyecto, configura una **alerta de presupuesto** en la consola de Google Cloud.

---

## 3. Obtener la clave de LangSmith (recomendada)

1. Entra a **[smith.langchain.com](https://smith.langchain.com/)** y crea una cuenta gratuita.
2. Ve a **Settings → API Keys → Create API Key**.
3. Ponle una descripción (por ejemplo, `py501`) y copia la clave: solo se muestra una vez.

Sin esta clave los *notebooks* funcionan igual, pero no verás las trazas y fallarán las celdas de experimentos del *notebook* `13`.

---

## 4. Guardar las claves como secretos de Codespaces

Hazlo una vez por clave. Los nombres deben escribirse **exactamente** como aparecen en la tabla de la sección 1.

1. En GitHub, haz clic en tu foto de perfil (esquina superior derecha) → **Settings**.
2. En la barra lateral, en la sección **Code, planning, and automation**, haz clic en **Codespaces**.
3. A la derecha de **Codespaces secrets**, haz clic en **New secret**.
4. En **Name**, escribe `GOOGLE_API_KEY`.
5. En **Value**, pega la clave de *Gemini*. Sin comillas ni espacios al inicio o al final.
6. En **Repository access**, selecciona el repositorio del curso: tu copia (*fork*) de `py501` o `PythonistaMX/py501`, según desde dónde vayas a crear el *Codespace*.
7. Haz clic en **Add secret**.
8. Repite los pasos 3 a 7 con `LANGSMITH_API_KEY` y, si las tienes, con `OPENAI_API_KEY` y `ANTHROPIC_API_KEY`.

**Reglas de los nombres** (las aplica GitHub): solo letras, números y guion bajo; no pueden empezar con número ni con `GITHUB_`; no distinguen mayúsculas de minúsculas. Puedes guardar hasta 100 secretos de 48 KB cada uno.

### Alternativa: capturarlas al crear el *Codespace*

El archivo `.devcontainer/devcontainer.json` declara estos secretos como **recomendados**. Si creas el *Codespace* con **Code → Codespaces → `…` → New with options**, GitHub muestra los campos para capturarlos ahí mismo. Lo que escribas se guarda en tus secretos personales y no tendrás que volver a capturarlo.

---

## 5. Abrir (o recargar) el *Codespace*

* **Si aún no tienes *Codespace*:** créalo desde **Code → Codespaces → Create codespace on main**. Los secretos ya estarán disponibles.
* **Si ya tenías uno abierto:** los secretos se cargan **al iniciar** el *Codespace*. Si GitHub te ofrece recargarlo, acepta. Si no, deténlo (**github.com/codespaces** → `…` → **Stop codespace**) y vuelve a abrirlo.

---

## 6. Verificar sin mostrar la clave

En la terminal del *Codespace* (**Terminal → New Terminal**), ejecuta:

```bash
python -c "import os; [print(f'{v:20} {\"✅ configurada\" if os.environ.get(v) else \"❌ falta\"}') for v in ['GOOGLE_API_KEY','LANGSMITH_API_KEY','OPENAI_API_KEY','ANTHROPIC_API_KEY']]"
```

Debes ver ✅ al menos en `GOOGLE_API_KEY`. Después abre `01_bienvenida_y_entorno.ipynb` y ejecútalo completo: su celda de verificación hace lo mismo y además llama al modelo.

> ⚠️ **Nunca** ejecutes `echo $GOOGLE_API_KEY` ni `print(os.environ["GOOGLE_API_KEY"])`: la clave quedaría en la salida de la celda, y la salida se guarda dentro del *notebook*.

---

## 7. Errores comunes

| Síntoma | Causa probable | Solución |
| :--- | :--- | :--- |
| `RuntimeError: Falta GOOGLE_API_KEY` | El secreto no existe, tiene otro nombre o no tiene acceso al repositorio | Revisa el nombre exacto y la sección **Repository access** del secreto |
| El secreto existe pero el *Codespace* no lo ve | El *Codespace* se inició antes de crear el secreto | Detén y vuelve a abrir el *Codespace* (sección 5) |
| `API key not valid` o `PERMISSION_DENIED` | Clave mal copiada, revocada o no restringida a la *Gemini API* | Crea una clave nueva en *AI Studio* y actualiza el secreto (**Update** junto al secreto) |
| `429` o `RESOURCE_EXHAUSTED` | Se agotó el límite del nivel gratuito | Espera unos minutos, ejecuta menos celdas o pide la clave de respaldo al instructor |
| Las celdas de *LangSmith* fallan | Falta `LANGSMITH_API_KEY` | Agrega el secreto (sección 3 y 4) o sáltate esas celdas |
| Creaste el *Codespace* desde tu *fork* y no ve los secretos | Diste acceso a `PythonistaMX/py501`, no a tu *fork* | Agrega tu *fork* en **Repository access** |

---

## 8. Si una clave se filtra

1. **Revócala de inmediato:** en *AI Studio* (o en *LangSmith*), elimina la clave.
2. Crea una clave nueva.
3. Actualiza el secreto en **Settings → Codespaces → Codespaces secrets → Update**.
4. Revisa el uso y la facturación del proyecto para detectar consumo que no reconozcas.

Borrar la clave del *notebook* **no basta**: sigue en el historial de Git y en cualquier copia que alguien haya hecho.

---

## 9. Ejecución local (sin Codespaces)

1. Copia la plantilla: `cp .env.example .env`.
2. Abre `.env` y completa `GOOGLE_API_KEY=` (y las demás si las tienes). Sin comillas.
3. La celda de preparación de cada *notebook* carga `.env` automáticamente con `python-dotenv`.

`.env` está en `.gitignore`: Git nunca lo sube. **No** edites `.env.example` con claves reales: ese archivo sí se sube.

---

## 10. Para el instructor: secretos de GitHub Actions

Los secretos de Codespaces **no** están disponibles para GitHub Actions. Para que el workflow `notebooks-smoke.yml` ejecute los *notebooks* con un modelo real:

1. En el repositorio: **Settings → Secrets and variables → Actions → New repository secret**.
2. Crea `GOOGLE_API_KEY` y `LANGSMITH_API_KEY` con claves **dedicadas a CI** (no tu clave personal), con presupuesto propio.

Sin esos secretos, el workflow solo valida la estructura y la sintaxis de los *notebooks* y el servidor MCP, y omite la ejecución.

---

&copy; José Luis Chiquete Valdivieso. 2017-2026. Licencia [CC-BY 4.0](LICENSE).
