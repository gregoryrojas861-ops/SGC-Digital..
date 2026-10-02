# SGC Digital — Estandarización del Sistema de Gestión de Calidad

Aplicación web local en Python + Streamlit para apoyar la gestión documental,
estandarización, indicadores, alertas y trazabilidad de un Sistema de Gestión
de Calidad.

## Marco de referencia

El proyecto está preparado para trabajar académica/operativamente con la
estructura temática de ISO 9001:2015:

- 4 Contexto de la organización
- 5 Liderazgo
- 6 Planificación
- 7 Apoyo
- 8 Operación
- 9 Evaluación del desempeño
- 10 Mejora

IMPORTANTE: el programa no reproduce el texto de ISO 9001 ni certifica una
organización. La evaluación automática es una ayuda para revisión humana.

## Funciones incluidas

- Carga de PDF, DOCX, TXT, CSV y Excel.
- Extracción automática de texto.
- Clasificación automática del documento.
- Sugerencia de referencia temática ISO.
- Índice de estandarización de documentos.
- Detección de elementos básicos faltantes.
- Análisis asistido por IA de tipo, proceso, calidad orientativa, cantidades, indicadores y hallazgos.
- Comparación local con documentos anteriores y relaciones explicadas con evidencia.
- Búsqueda web opcional con fuentes citadas en el informe y borrador.
- Informe persistente y borrador DOCX separado del original; requiere aprobación humana.
- Flujo documental: borrador/revisión, envío a aprobación, aprobación o rechazo con usuario y fecha.
- Registro de usuarios con invitación; las cuentas nuevas reciben rol Calidad.
- Gestión de indicadores.
- Límites inferior y superior.
- Meta.
- Detección de variación porcentual respecto a la lectura anterior.
- Alertas automáticas.
- Centro de alertas.
- Cierre de alertas.
- Historial y auditoría.
- Dashboard con tendencias.
- SQLite local.
- Arquitectura preparada para migrar a PostgreSQL.

## Instalación en Windows / VS Code

1. Instala Python 3.11 o superior.
2. Abre esta carpeta en VS Code.
3. Abre una terminal.
4. Ejecuta:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

5. Abre la dirección que muestre Streamlit.

Para habilitar IA en ejecución local, define `OPENAI_API_KEY` en el entorno de PowerShell antes de iniciar Streamlit. La clave se obtiene en OpenAI y nunca debe pegarse en el chat ni guardarse en el código. En cada carga, la autorización principal envía a OpenAI el texto extraído, nombre y clasificación. La comparación interna es opcional: si se autoriza, busca en todos los documentos locales y envía solo los cinco fragmentos más relacionados. La búsqueda web en vivo requiere otra autorización; sus términos pueden derivarse del documento y sus costos dependen del proveedor. Las fuentes citadas se guardan en el informe. No se reproduce el texto de ISO 9001 ni se determina conformidad. Los PDF escaneados sin texto legible requieren OCR, que aún no está incluido.

## Despliegue en un VPS propio

El despliegue usa Docker Compose, PostgreSQL con volumen persistente, un volumen separado para documentos y Caddy para HTTPS automático. Los contenedores se reinician después de una caída; PostgreSQL no publica puertos en Internet.

Requisitos: un VPS Linux con Docker Compose, un dominio cuyo DNS apunte al VPS y los puertos 80 y 443 habilitados.

1. Copia `.env.example` como `.env` y configura el dominio, la base de datos y el usuario administrador. Para habilitar la IA, agrega una clave válida en `OPENAI_API_KEY`.
2. Reemplaza las contraseñas y `SGC_REGISTRATION_CODE` por secretos propios. `openssl rand -hex 32` genera valores seguros compatibles con la URL de conexión.
3. Desde la carpeta del proyecto ejecuta `docker compose up -d --build`.
4. Consulta el arranque con `docker compose logs -f app caddy`; la app quedará disponible en `https://<DOMAIN>`.

Los volúmenes conservan la base de datos y los documentos al recrear contenedores, pero no protegen contra la pérdida del VPS. Programa copias de seguridad externas de PostgreSQL y del volumen `uploaded_documents`.

## Acceso local de demostración

Usuario: `MarianaDelValle`
Contraseña: `Mariana0526*`

Estas credenciales son solo para desarrollo local. En producción configura `SGC_ADMIN_USER` y `SGC_ADMIN_PASSWORD` en `.env`; usa una contraseña única de al menos 16 caracteres.

## Registro de cuentas

En producción el registro requiere `SGC_ALLOW_REGISTRATION=true` y un `SGC_REGISTRATION_CODE` secreto que solo se comparte con personal autorizado. Las cuentas nuevas reciben el rol `CALIDAD`; únicamente `ADMIN` puede aprobar documentos. Todas las cuentas ven los mismos registros del sistema, así que no compartas el código fuera de la organización. Para cerrar nuevos registros, configura `SGC_ALLOW_REGISTRATION=false`.

## Ejemplo de alerta

Si un indicador tiene:

- Límite inferior: 90
- Límite superior: 100
- Variación máxima: 10 %

y una lectura pasa de 95 a 75, el sistema genera una alerta automática.

## Próxima ampliación recomendada

Para una versión empresarial se pueden agregar:

- Roles y permisos completos.
- Firma/aprobación electrónica.
- Control formal de versiones.
- Matriz de riesgos y oportunidades.
- No conformidades y acciones correctivas.
- Auditorías internas.
- Evaluación de proveedores.
- Capacitación y competencias.
- Revisión por la dirección.
- Notificaciones por correo.
- OCR para documentos escaneados.
- Copias de seguridad programadas.
- Exportación de reportes PDF/Excel.
