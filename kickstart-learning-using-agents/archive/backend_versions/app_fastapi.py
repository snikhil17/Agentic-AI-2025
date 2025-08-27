from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import os
from dotenv import load_dotenv
from agent import adaptive_learning_agent

# Load environment variables
load_dotenv()

app = FastAPI(title="Adaptive Learning Agent", description="AI-powered personalized learning pathways")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    """Render the main form page"""
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}
    )

@app.post("/", response_class=HTMLResponse)
async def post_index(
    request: Request,
    learning_style: Annotated[str, Form()],
    progress: Annotated[str, Form()], 
    hobby: Annotated[str, Form()],
    domain: Annotated[str, Form()],
    google_api_key: Annotated[str, Form()],
    tavily_api_key: Annotated[str, Form()]
):
    """Process form submission and generate learning pathway"""
    try:
        student_profile = {
            "learning_style": learning_style,
            "progress": progress,
            "hobby": hobby,
            "domain": domain,
            "google_api_key": google_api_key,
            "tavily_api_key": tavily_api_key
        }
        
        result = adaptive_learning_agent.invoke(student_profile)
        
        return templates.TemplateResponse(
            request=request,
            name="result.html", 
            context={"result": result}
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-pathway")
async def generate_pathway(request: Request):
    """API endpoint for React frontend"""
    try:
        data = await request.json()
        
        # Map React frontend format to backend format
        student_profile = {
            "learning_style": data.get("learningStyle"),
            "progress": data.get("topic"),  # React uses 'topic', backend uses 'progress'
            "hobby": data.get("hobbies"),
            "domain": data.get("domain"),
            "google_api_key": os.getenv("GOOGLE_API_KEY"),
            "tavily_api_key": os.getenv("TAVILY_API_KEY")
        }
        
        result = adaptive_learning_agent.invoke(student_profile)
        return JSONResponse(content=result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
