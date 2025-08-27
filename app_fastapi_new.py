from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from agent import adaptive_learning_agent

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Adaptive Learning Agent API", 
    version="1.0.0",
    description="AI-powered personalized learning pathway generator"
)

# Add CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:5173", 
        "http://localhost:5174", 
        "http://localhost:4173",
        "https://your-react-app.vercel.app",  # Add production frontend URL when deployed
        "https://kickstart-learning.onrender.com"  # Current deployment URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentProfile(BaseModel):
    learning_style: str
    progress: str
    hobby: str
    domain: str
    google_api_key: str
    tavily_api_key: str

class ReactLearningPreferences(BaseModel):
    """Model for React frontend format"""
    learningStyle: str
    topic: str
    hobbies: str
    domain: str

@app.get("/")
async def root():
    """Root endpoint - redirects to API documentation"""
    return {
        "message": "Adaptive Learning Agent API", 
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "react_frontend": "http://localhost:5173"
    }

@app.post("/api/generate-pathway")
async def generate_pathway_api(preferences: ReactLearningPreferences):
    """API endpoint for React frontend - maps React format to backend format"""
    try:
        # Map React frontend format to backend format
        student_profile = {
            "learning_style": preferences.learningStyle,
            "progress": preferences.topic,  # React uses 'topic', backend uses 'progress'
            "hobby": preferences.hobbies,
            "domain": preferences.domain,
            "google_api_key": os.getenv("GOOGLE_API_KEY", ""),
            "tavily_api_key": os.getenv("TAVILY_API_KEY", "")
        }
        
        result = adaptive_learning_agent.invoke(student_profile)
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-pathway-direct")
async def generate_pathway_direct_api(profile: StudentProfile):
    """API endpoint for direct calls with full profile including API keys"""
    try:
        # Convert to dict for the agent
        student_profile = profile.dict()
        
        result = adaptive_learning_agent.invoke(student_profile)
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy", 
        "message": "FastAPI backend is running",
        "backend": "FastAPI",
        "version": "1.0.0",
        "frontend": "React (http://localhost:5173)"
    }

@app.get("/api/health")
async def api_health_check():
    """API health check endpoint"""
    return {
        "status": "healthy", 
        "backend": "FastAPI", 
        "version": "1.0.0",
        "endpoints": [
            "/api/generate-pathway",
            "/api/generate-pathway-direct",
            "/docs",
            "/health"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
