# Archive Folder - Moved Files Documentation

This folder contains files that are no longer actively used in the current FastAPI-based implementation of the Kickstart Learning Agent.

## Files Moved to Archive (Date: August 27, 2025)

### 📁 backend_versions/
- **app.py** - Original Flask web application (legacy)
- **app_fastapi.py** - First FastAPI version (superseded by app_fastapi_new.py)

### 📁 unused_modules/
- **planning.py** - Old planning module (functionality moved to structured_agent.py)
- **model_provider.py** - Unused model provider abstraction

### 📁 scripts_and_config/
- **setup.bat** - Windows setup script (legacy)
- **setup.sh** - Unix setup script (legacy)
- **Dockerfile** - Docker configuration (not currently used)
- **.dockerignore** - Docker ignore file

### 📁 frontend_assets/
- **static/** - Static CSS/JS files (replaced by React frontend)

### 📁 cache/
- **__pycache__/** - Python bytecode cache files

## Why These Files Were Archived

### Backend Evolution
- **Flask → FastAPI Migration**: Moved from Flask to FastAPI for better performance and modern async support
- **Consolidation**: Multiple backend versions consolidated into single FastAPI implementation

### Module Cleanup
- **Unused Code**: planning.py and model_provider.py were not being imported or used
- **Refactored Logic**: Their functionality was integrated into other modules

### Deployment Simplification
- **Setup Scripts**: Replaced by simpler pip install + uvicorn commands
- **Docker**: Not needed for current Render.com deployment strategy

### Frontend Migration
- **Static Assets**: Replaced by React frontend with Tailwind CSS
- **Template-only**: HTML templates now used only for FastAPI HTML rendering option

## Current Active Architecture

The project now uses:
- **Backend**: app_fastapi_new.py (FastAPI)
- **Frontend**: adaptive-learning-agent/ (React)
- **Core Agents**: agent.py, retrieval.py, structured_agent.py, explanation.py
- **Models**: data_models.py
- **CLI**: main.py
- **Templates**: templates/ (for FastAPI HTML option)

## Recovery Instructions

If you need to restore any archived files:

```bash
# Example: Restore Flask app for reference
cp archive/backend_versions/app.py ./

# Example: Restore Docker configuration
cp archive/scripts_and_config/Dockerfile ./
```

## File Sizes and Dates

Last updated: August 27, 2025
Total archived files: ~15 files + directories
Space saved in main directory: Significant reduction in clutter
