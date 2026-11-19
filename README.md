# WatermarksRemover IA Libre

Proyecto comunitario para integrar el servicio [watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) con herramientas locales mediante MCP.

## Objetivos
- Mantener una instalación local y controlada por el usuario.
- Proporcionar un adaptador MCP desacoplado del servicio original.
- Permitir el uso opcional de modelos locales mediante Ollama.
- Automatizar validaciones y pruebas con GitHub Actions.

## Estado
**Etapa inicial: estructura y adaptador en desarrollo.** No se declara todavía una integración completa ni se garantiza compatibilidad con todas las funciones del proyecto upstream.

## Requisitos
- Python 3.11 o superior.
- El servicio upstream instalado y ejecutándose localmente.
- Dependencias Python indicadas en `requirements.txt`.

## Inicio del adaptador MCP (modo local)
1. Copiar `.env.example` a `.env`.
2. Ajustar `WMR_BASE_URL` a la dirección del servicio local.
3. Crear entorno virtual e instalar dependencias:
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
4. Iniciar el servidor MCP por transporte stdio:
   ```powershell
   python -m mcp_server
   ```

El cliente MCP debe configurarse para ejecutar ese comando en el equipo local. No expongas el servicio a Internet ni compartas la clave API.

## Uso responsable
Utiliza las funciones únicamente con contenido propio o para el que tengas autorización. Las marcas de procedencia pueden comunicar información importante sobre el origen del contenido. La detección estadística puede producir falsos positivos y negativos.

## Licencias y atribución
Este repositorio contiene código de integración propio bajo MIT (ver `LICENSE`). El proyecto upstream mantiene su licencia y derechos de autor originales; consulta su [repositorio](https://github.com/guillaumemeyer/watermarks-remover) antes de redistribuirlo o integrarlo. Las licencias de modelos descargados desde Ollama dependen de cada modelo.

## Próximas etapas
- Verificar los contratos reales de los endpoints upstream.
- Añadir pruebas de integración contra una instancia local.
- Añadir instalador Windows probado.
- Incorporar configuración de LibreChat/Ollama opcional.
