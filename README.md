# Async AI Model Orchestrator

Simulación de un orquestador concurrente de modelos de inteligencia artificial desarrollado con Python y `asyncio`.

El proyecto demuestra cómo ejecutar operaciones asíncronas, controlar la concurrencia, establecer límites de tiempo y gestionar cancelaciones.

## Tecnologías

- Python 3.12+
- `asyncio`
- `time` (biblioteca estándar)

No requiere dependencias externas.

## Funcionalidades

- Simulación de consultas a GPT-4, Claude 3 y Llama.
- Ejecución concurrente mediante `asyncio.gather()`.
- Límite de dos operaciones simultáneas con `asyncio.Semaphore(2)`.
- Timeout global de dos segundos mediante `asyncio.timeout()`.
- Manejo de `TimeoutError` y `asyncio.CancelledError`.
- Registro de tiempos de ejecución con `time.perf_counter()`.
- Prueba de diez consultas para verificar el límite de concurrencia.
- Validaciones automáticas mediante `assert`.

## Estructura del proyecto

```text
ejercicio-01/
├── .gitignore
├── main.py
└── README.md
```

## Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone https://github.com/USUARIO/python-async-orchestrator.git
cd python-async-orchestrator
```

Reemplazar `USUARIO` por el usuario correspondiente de GitHub.

**2. Ejecutar el programa**

```bash
python main.py
```

Es necesario contar con Python 3.12 o superior.

## Pruebas

### Prueba 1: orquestación de modelos

Se simulan tres consultas con diferentes tiempos de respuesta:

| Modelo | Duración simulada |
|---|---|
| GPT-4 | 1 segundo |
| Claude 3 | 2 segundos |
| Llama | 3 segundos |

El sistema permite un máximo de dos consultas simultáneas y establece un timeout global de dos segundos.

Cuando se supera el tiempo permitido, las tareas pendientes se cancelan y la excepción se maneja sin interrumpir inesperadamente el programa.

### Prueba 2: control de concurrencia

Se ejecutan diez consultas simuladas de un segundo cada una, utilizando un semáforo con capacidad para dos operaciones simultáneas.

**Resultados verificados:**

```text
Consultas completadas: 10/10
Máximo de consultas simultáneas: 2
Prueba de concurrencia finalizada: 5.02 segundos
```

Los tiempos pueden variar ligeramente según el entorno de ejecución.

## Conceptos aplicados

- Programación asíncrona con `async` y `await`.
- Event Loop.
- Corrutinas y concurrencia cooperativa.
- Control de concurrencia mediante semáforos.
- Gestión de timeouts y cancelaciones.
- Medición del tiempo de ejecución.

## Objetivo académico

Proyecto práctico de arquitectura asíncrona con Python, orientado a comprender y aplicar mecanismos de concurrencia y control de ejecución en sistemas que realizan múltiples operaciones de entrada y salida.