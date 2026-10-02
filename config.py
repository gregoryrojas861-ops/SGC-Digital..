import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

APP_NAME = "SGC Digital Enterprise"
APP_VERSION = "2.0.0"
APP_ENV = os.getenv("SGC_APP_ENV", os.getenv("SGC_ENV", "development")).strip().lower()

DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
PROCESSED_DIR = DATA_DIR / "processed"
BACKUP_DIR = DATA_DIR / "backups"
TEMPLATE_DIR = DATA_DIR / "templates"
LEARNING_DIR = DATA_DIR / "learning"
LOG_DIR = BASE_DIR / "logs"

for directory in (
    DATA_DIR,
    UPLOAD_DIR,
    PROCESSED_DIR,
    BACKUP_DIR,
    TEMPLATE_DIR,
    LEARNING_DIR,
    LOG_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)

_DATABASE_URL = os.getenv("DATABASE_URL")
_NEW_SQLITE_PATH = DATA_DIR / "sgc.db"
_LEGACY_SQLITE_PATH = DATA_DIR / "sgc.sqlite3"
if _DATABASE_URL:
    DATABASE_URL = _DATABASE_URL
elif _LEGACY_SQLITE_PATH.exists() and not _NEW_SQLITE_PATH.exists():
    DATABASE_URL = f"sqlite:///{_LEGACY_SQLITE_PATH.as_posix()}"
else:
    DATABASE_URL = f"sqlite:///{_NEW_SQLITE_PATH.as_posix()}"


def _positive_int(name, default):
    try:
        value = int(os.getenv(name, str(default)))
    except ValueError as error:
        raise ValueError(f"{name} debe ser un número entero.") from error
    if value < 1:
        raise ValueError(f"{name} debe ser mayor que cero.")
    return value


SESSION_TIMEOUT_MINUTES = _positive_int("SESSION_TIMEOUT_MINUTES", 30)
MAX_UPLOAD_SIZE_MB = _positive_int("MAX_UPLOAD_SIZE_MB", 25)
MAX_UPLOAD_SIZE_BYTES = MAX_UPLOAD_SIZE_MB * 1024 * 1024
BCRYPT_ROUNDS = 12

ALLOWED_DOCUMENT_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".xlsx",
    ".xls",
    ".csv",
    ".txt",
}

ISO_STANDARD = "ISO 9001:2015"
ISO_CLAUSES = {
    "4": "Contexto de la organización",
    "5": "Liderazgo",
    "6": "Planificación",
    "7": "Apoyo",
    "8": "Operación",
    "9": "Evaluación del desempeño",
    "10": "Mejora",
}

try:
    DEFAULT_VARIATION_THRESHOLD = float(os.getenv("DEFAULT_VARIATION_THRESHOLD", "10"))
except ValueError as error:
    raise ValueError("DEFAULT_VARIATION_THRESHOLD debe ser un número.") from error
if DEFAULT_VARIATION_THRESHOLD < 0:
    raise ValueError("DEFAULT_VARIATION_THRESHOLD no puede ser negativo.")

PRIMARY_COLOR = "#10B981"
SECONDARY_COLOR = "#064E3B"
BACKGROUND_COLOR = "#F3FAF6"
WHITE = "#FFFFFF"
BORDER_COLOR = "#D1FAE5"
WARNING_COLOR = "#F59E0B"
CRITICAL_COLOR = "#EF4444"

ROLES = [
    "ADMINISTRADOR",
    "SUPERVISOR",
    "AUDITOR",
    "PRODUCCION",
    "INVENTARIO",
    "COMPRAS",
    "CONSULTA",
]
PERMISSIONS = ["VIEW", "CREATE", "UPDATE", "DELETE", "APPROVE", "EXPORT", "ADMIN"]
ADMIN_ROLE = "ADMINISTRADOR"
ADMIN_ROLES = {ADMIN_ROLE, "ADMIN"}

ROLE_PERMISSIONS = {
    "ADMINISTRADOR": set(PERMISSIONS),
    "SUPERVISOR": {"VIEW", "CREATE", "UPDATE", "APPROVE", "EXPORT"},
    "AUDITOR": {"VIEW", "CREATE", "UPDATE", "EXPORT"},
    "PRODUCCION": {"VIEW", "CREATE", "UPDATE"},
    "INVENTARIO": {"VIEW", "CREATE", "UPDATE"},
    "COMPRAS": {"VIEW", "CREATE", "UPDATE", "EXPORT"},
    "CONSULTA": {"VIEW"},
}

DOCUMENT_STATUSES = [
    "BORRADOR",
    "EN_REVISION",
    "PENDIENTE_APROBACION",
    "APROBADO",
    "VIGENTE",
    "OBSOLETO",
    "RECHAZADO",
]
ALERT_STATUSES = ["ABIERTA", "EN_REVISION", "ATENDIDA", "CERRADA"]
NC_STATUSES = ["ABIERTA", "EN_ANALISIS", "EN_ACCION", "VERIFICACION", "CERRADA"]
ACTION_STATUSES = ["ABIERTA", "EN_CURSO", "PENDIENTE_EVIDENCIA", "VERIFICACION", "CERRADA"]
RISK_LEVELS = ["BAJO", "MEDIO", "ALTO", "CRITICO"]
AUDIT_STATUSES = ["PLANIFICADA", "EN_EJECUCION", "HALLAZGOS", "SEGUIMIENTO", "CERRADA"]
APPROVAL_ACTIONS = ["SUBMIT", "REVIEW", "APPROVE", "REJECT", "PUBLISH", "OBSOLETE"]

AI_MIN_SAMPLES_ZSCORE = 5
AI_MIN_SAMPLES_IQR = 8
AI_MIN_SAMPLES_ISOLATION = 15
AI_INSUFFICIENT_DATA_MESSAGE = "Datos insuficientes para realizar un análisis confiable."

AUDIT_EVENTS = [
    "LOGIN",
    "LOGOUT",
    "CREATE",
    "UPDATE",
    "DELETE",
    "APPROVE",
    "REJECT",
    "UPLOAD",
    "VERSION_CHANGE",
    "AI_ACTION",
    "EXPORT",
    "CONFIG_CHANGE",
]

STANDARD_ELEMENTS = [
    "titulo",
    "codigo",
    "version",
    "objetivo",
    "alcance",
    "responsabilidades",
    "procedimiento",
    "registros",
    "indicadores",
    "riesgos",
    "controles",
    "aprobacion",
    "referencias",
]
