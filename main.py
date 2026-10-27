
import asyncio
import time


# --------------------------------------------------
# Simulación de consultas a modelos de IA
# --------------------------------------------------

def registrar(mensaje, inicio):
    tiempo = time.perf_counter() - inicio
    print(f"[{tiempo:.2f}s] {mensaje}")


async def gpt_4_call(sem, inicio):
    async with sem:
        registrar("Consultando GPT-4...", inicio)

        try:
            await asyncio.sleep(1)
            registrar("GPT-4 respondió", inicio)

        except asyncio.CancelledError:
            registrar("Consulta a GPT-4 cancelada", inicio)
            raise


async def claude_3_call(sem, inicio):
    async with sem:
        registrar("Consultando Claude 3...", inicio)

        try:
            await asyncio.sleep(2)
            registrar("Claude 3 respondió", inicio)

        except asyncio.CancelledError:
            registrar("Consulta a Claude 3 cancelada", inicio)
            raise


async def local_llama_call(sem, inicio):
    async with sem:
        registrar("Consultando Llama...", inicio)

        try:
            await asyncio.sleep(3)
            registrar("Llama respondió", inicio)

        except asyncio.CancelledError:
            registrar("Consulta a Llama cancelada", inicio)
            raise


# --------------------------------------------------
# Prueba 1: modelos con timeout global
# --------------------------------------------------

async def probar_modelos():
    print("\n--- PRUEBA 1: MODELOS CON TIMEOUT ---")

    inicio = time.perf_counter()
    sem = asyncio.Semaphore(2)

    try:
        async with asyncio.timeout(2):
            await asyncio.gather(
                gpt_4_call(sem, inicio),
                claude_3_call(sem, inicio),
                local_llama_call(sem, inicio)
            )

    except TimeoutError:
        registrar(
            "TimeoutError: se superó el límite de 2 segundos",
            inicio
        )

    registrar("Prueba de modelos finalizada", inicio)


# --------------------------------------------------
# Prueba 2: diez consultas con semáforo
# --------------------------------------------------

async def probar_concurrencia():
    print("\n--- PRUEBA 2: CONTROL DE CONCURRENCIA ---")

    inicio = time.perf_counter()
    sem = asyncio.Semaphore(2)

    activas = 0
    maximo_activas = 0
    completadas = 0

    async def ejecutar_consulta(numero):
        nonlocal activas, maximo_activas, completadas

        async with sem:
            activas += 1
            maximo_activas = max(maximo_activas, activas)

            registrar(
                f"Consulta {numero} iniciada | Activas: {activas}",
                inicio
            )

            try:
                await asyncio.sleep(1)
                completadas += 1

                registrar(
                    f"Consulta {numero} finalizada",
                    inicio
                )

            finally:
                activas -= 1

    await asyncio.gather(
        *(ejecutar_consulta(i) for i in range(1, 11))
    )

    print("\n--- RESULTADOS ---")
    print(f"Consultas completadas: {completadas}/10")
    print(f"Máximo de consultas simultáneas: {maximo_activas}")

    registrar("Prueba de concurrencia finalizada", inicio)

    assert completadas == 10, "No se completaron las 10 consultas"
    assert maximo_activas == 2, "El límite de concurrencia no fue respetado"


# --------------------------------------------------
# Punto de entrada
# --------------------------------------------------

async def main():
    await probar_modelos()
    await probar_concurrencia()

    print("\nTodas las pruebas finalizaron correctamente.")


if __name__ == "__main__":
    asyncio.run(main())
