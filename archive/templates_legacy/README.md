# Legacy Templates Directory

This directory contains the HTML templates that were previously used by the FastAPI backend for server-side rendering.

## What was moved here:

### Active Templates (Previously used by FastAPI):
- **`base.html`** - Bootstrap-based layout template
- **`index.html`** - HTML form for manual input
- **`result.html`** - Results display with markdown rendering

### Unused Template Variants:
- **`base_initial.html`** - Original base template
- **`generate.html`** - Unused generation page
- **`index_clean.html`** - Clean version of index
- **`index_enhanced.html`** - Enhanced index with extra features
- **`index_initial.html`** - Original index template

## Why templates were removed:

1. **React Frontend Primary**: The project now uses React as the primary frontend interface
2. **API-Only Backend**: FastAPI backend now serves only JSON APIs, no HTML rendering
3. **Cleaner Architecture**: Separation of backend (API) and frontend (React) concerns
4. **Modern Development**: React provides better user experience and development workflow

## If you need templates again:

If you want to restore HTML template functionality:

1. Move templates back to `/templates/` directory
2. Restore template imports in `app_fastapi_new.py`:
   ```python
   from fastapi.templating import Jinja2Templates
   from fastapi.responses import HTMLResponse
   templates = Jinja2Templates(directory="templates")
   ```
3. Add template routes back to FastAPI
4. Ensure `jinja2` is in requirements.txt

## Current Architecture (No Templates):

```
FastAPI Backend (Port 8000) → API Endpoints Only
React Frontend (Port 5173) → Full UI Experience
```

## Date Moved: 
August 27, 2025

## Status: 
**ARCHIVED** - Not used in current implementation
