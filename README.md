# PDF ExtractText

Sistema que permite extraer texto de archivos PDF y convertir ese contenido en un archivo en formato Markdown (.md), el cual ademas quedara resumido.

###### Estado actual
Este sistema se encuentra actualmente en desarrollo.

## Descripción

PDF ExtractText es una API REST desarrollada en Python que permite:
- **Extraer texto** de archivos PDF
- **Convertir** el contenido extraído a formato Markdown (.md)
- **Almacenar** documentos en MongoDB
- **Gestionar** documentos extraídos mediante endpoints REST

## Características

- Extracción de texto de archivos PDF
- Conversión inteligente a Markdown usando IA (Kimi)
- API REST con FastAPI
- Almacenamiento en MongoDB
- Desarrollo guiado por pruebas (TDD)
- Código limpio siguiendo principios SOLID y Clean Code

## Tecnología

| Categoría | Tecnología |
|-----------|------------|
| Lenguaje | Python 3.10+ |
| Framework | FastAPI |
| Base de Datos | MongoDB |
| IA | "Actualizar" |
| Gestión de dependencias | UV |
| Testing | Pytest |

### Dependencias Principales

- **fastapi**: Framework web moderno y rápido
- **pydantic**: Validación de datos
- **uvicorn**: Servidor ASGI
- **python-multipart**: Manejo de archivos multipart

## Estructura del Proyecto

```
pdf-extractext/
├── .agents/
│   └── skills/
│       ├── clean-code/
│       │   └── SKILL.md
│       └── tdd/
│           ├── SKILL.md
│           ├── deep-modules.md
│           ├── interface-design.md
│           ├── mocking.md
│           ├── refactoring.md
│           └── tests.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── data/
│   │   ├── database/
│   │   │   └── connection.py
│   │   └── repositories/
│   │       ├── __init__.py
│   │       └── document_repository.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   └── document.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── document_repository.py
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       └── document_use_cases.py
│   └── presentation/
│       ├── __init__.py
│       ├── routes/
│       │   ├── __init__.py
│       │   └── document.py
│       └── schemas/
│           ├── __init__.py
│           └── document.py
├── tests/
│   ├── conftest.py
│   ├── data/
│   │   └── test_document_repository.py
│   ├── domain/
│   │   └── test_document.py
│   └── presentation/
│       └── test_routes.py
├── main.py
├── pyproject.toml
├── README.md
└── skills-lock.json
```

### Arquitectura (Clean Architecture)

El proyecto sigue una arquitectura limpia con las siguientes capas:

```
┌─────────────────────────────────────────┐
│           PRESENTATION                  │
│  (Routes, Schemas, API Endpoints)       │
├─────────────────────────────────────────┤
│             DOMAIN                      │
│  (Entities, Use Cases, Repository       │
│   Interfaces)                           │
├─────────────────────────────────────────┤
│              DATA                       │
│  (Repository Implementations, Database  │
│   Connection, External Services)        │
└─────────────────────────────────────────┘
```

#### Descripción de Carpetas

- **`app/`**: Código principal de la aplicación
  - **`config/`**: Configuración centralizada de la aplicación
  - **`data/`**: Implementaciones de repositorios y acceso a datos
    - **`database/`**: Conexiones a bases de datos
    - **`repositories/`**: Implementaciones concretas de repositorios
  - **`domain/`**: Lógica de negocio pura
    - **`entities/`**: Entidades del dominio
    - **`repositories/`**: Interfaces de repositorios (contratos)
    - **`use_cases/`**: Casos de uso de la aplicación
  - **`presentation/`**: Capa de presentación
    - **`routes/`**: Definición de rutas y endpoints
    - **`schemas/`**: Esquemas Pydantic para validación
- **`tests/`**: Suite de pruebas unitarias e integradas
- **`.agents/`**: Configuración de skills para el agente de IA

## Instalación y Configuración

### Requisitos Previos

- Python 3.10 - 3.13
- UV (gestor de paquetes y entornos virtuales)
- MongoDB (local o remoto)

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <repository-https://github.com/FrancoCarballoPratsUTN/pdf-extractext>
   cd pdf-extractext
   ```

2. **Instalar dependencias con UV:**
   ```bash
   uv sync
   ```

3. **Instalar dependencias de desarrollo:**
   ```bash
   uv sync --extra dev
   ```

### Ejecución

**Modo desarrollo:**
```bash
uv run python main.py
```

**Modo producción:**
```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

La API estará disponible en `http://localhost:8000`

**Documentación interactive:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Uso de la API

### Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/documents/extract` | Extrae texto de un PDF y convierte a MD |
| GET | `/api/documents/` | Lista todos los documentos |
| GET | `/api/documents/{id}` | Obtiene un documento por ID |
| DELETE | `/api/documents/{id}` | Elimina un documento |

### Ejemplo de Uso

**Extraer texto de un PDF:**

```bash
curl -X POST "http://localhost:8000/api/documents/extract" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@ruta/al/archivo.pdf"
```

**Respuesta esperada:**
```json
{
  "id": "60d5ecb74e...",
  "filename": "archivo.pdf",
  "markdown_content": "# Título del Documento\n\nContenido extraído...",
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Pruebas

### Ejecutar todas las pruebas:
```bash
uv run pytest
```

### Ejecutar con cobertura:
```bash
uv run pytest --cov=app --cov-report=html
```

### Linting y type checking:
```bash
uv run ruff check .
uv run mypy app
```

## Metodología

### Desarrollo Guiado por Pruebas (TDD)

El proyecto sigue el ciclo Red-Green-Refactor:

1. **Red**: Escribir pruebas que inicialmente fallan
2. **Green**: Implementar código mínimo para que las pruebas pasen
3. **Refactor**: Mejorar el código manteniendo las pruebas en verde

### Principios de Clean Code

- Nombres descriptivos que reflejan la intención del código
- Principio de responsabilidad única (SRP)
- Principio DRY (Don't Repeat Yourself)
- Funciones pequeñas y bien organizadas
- Código orientado a la legibilidad y mantenibilidad

## Principios de Programación

### Principios Fundamentales

| Principio | Descripción |
|-----------|-------------|
| **KISS** | Keep It Simple, Stupid - Priorizar soluciones simples |
| **DRY** | Don't Repeat Yourself - Evitar duplicación de código |
| **YAGNI** | You Aren't Gonna Need It - No implementar funcionalidades prematuras |

### Principios SOLID

| Principio | Nombre | Descripción |
|-----------|--------|-------------|
| **S** | Responsabilidad Única | Una clase tiene una sola razón para cambiar |
| **O** | Abierto/Cerrado | Abierto para extensión, cerrado para modificación |
| **L** | Sustitución de Liskov | Objetos de subclase deben poder sustituir a los padres |
| **I** | Segregación de Interfaces | Preferir muchas interfaces específicas a una general |
| **D** | Inversión de Dependencias | Depender de abstracciones, no de concreciones |

### Twelve-Factor App (Parcial)

- **Codebase**: Una única base de código versionada
- **Dependencies**: Declarar y aislar las dependencias
- **Config**: Guardar configuración en el entorno
- **Backing Services**: Servicios tratados como recursos conectables
- **Build, Release, Run**: Separar construcción de ejecución
- **Processes**: Ejecución como procesos sin estado

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE.txt` para más detalles.
