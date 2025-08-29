from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from agent import adaptive_learning_agent
import logging
from contextlib import asynccontextmanager

# Configure logging for Cloud Run
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables (if .env exists)
load_dotenv()

# Health check state
health_check_passed = False

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events for Cloud Run optimization"""
    global health_check_passed
    
    # Startup
    logger.info("Starting up Adaptive Learning Agent API...")
    
    # Perform minimal startup checks
    try:
        # You can add startup validations here
        health_check_passed = True
        logger.info("Startup completed successfully")
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        health_check_passed = False
    
    yield
    
    # Shutdown
    logger.info("Shutting down Adaptive Learning Agent API...")

app = FastAPI(
    title="Adaptive Learning Agent API", 
    version="1.0.0",
    description="AI-powered personalized learning pathway generator",
    lifespan=lifespan
)

# Add CORS middleware - optimized for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://*.vercel.app",  # Vercel deployments
        "https://*.netlify.app",  # Netlify deployments  
        "https://*.onrender.com", # Render deployments
        "https://*.run.app",      # Cloud Run deployments
        "http://localhost:3000",  # Local React dev
        "http://localhost:5173",  # Local Vite dev
        "http://localhost:5174",  # Local Vite dev alt
        "http://localhost:4173",  # Local Vite preview
        "https://agentic-ai-2025-cr4e.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    max_age=600,  # Cache preflight requests for 10 minutes
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
    """Root endpoint - health check and API info"""
    return {
        "status": "healthy",
        "message": "Adaptive Learning Agent API", 
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "endpoints": {
            "generate_pathway": "/api/generate-pathway",
            "generate_pathway_direct": "/api/generate-pathway-direct"
        }
    }

@app.get("/health")
async def health_check():
    """Kubernetes/Cloud Run health check endpoint"""
    if health_check_passed:
        return {
            "status": "healthy", 
            "message": "FastAPI backend is running",
            "backend": "FastAPI",
            "version": "1.0.0"
        }
    else:
        raise HTTPException(status_code=503, detail="Service not ready")

@app.post("/api/generate-pathway")
async def generate_pathway_api(preferences: ReactLearningPreferences):
    """API endpoint for React frontend - maps React format to backend format"""
    try:
        logger.info(f"Received pathway generation request for topic: {preferences.topic}")
        
        # Get API keys from environment variables
        google_api_key = os.getenv("GOOGLE_API_KEY")
        tavily_api_key = os.getenv("TAVILY_API_KEY")
        
        if not google_api_key or not tavily_api_key:
            logger.error("API keys not found in environment variables")
            raise HTTPException(
                status_code=500, 
                detail="Server configuration error: API keys not configured on server."
            )
        
        # Map React frontend format to backend format with environment API keys
        student_profile = {
            "learning_style": preferences.learningStyle,
            "progress": preferences.topic,  # React uses 'topic', backend uses 'progress'
            "hobby": preferences.hobbies,
            "domain": preferences.domain,
            "google_api_key": google_api_key,
            "tavily_api_key": tavily_api_key
        }
        
        result = adaptive_learning_agent.invoke(student_profile)
        logger.info("Pathway generation completed successfully")
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating pathway: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-pathway-direct")
async def generate_pathway_direct_api(profile: StudentProfile):
    """API endpoint for direct calls with full profile including API keys"""
    try:
        logger.info(f"Received direct pathway generation request for: {profile.progress}")
        
        # Convert to dict for the agent
        student_profile = profile.dict()
        
        # Use provided API keys or fall back to environment variables
        if not student_profile.get("google_api_key"):
            student_profile["google_api_key"] = os.getenv("GOOGLE_API_KEY")
        if not student_profile.get("tavily_api_key"):
            student_profile["tavily_api_key"] = os.getenv("TAVILY_API_KEY")
        
        # Validate API keys are available
        if not student_profile["google_api_key"] or not student_profile["tavily_api_key"]:
            raise HTTPException(
                status_code=500, 
                detail="Server configuration error: API keys not available."
            )
        
        result = adaptive_learning_agent.invoke(student_profile)
        logger.info("Direct pathway generation completed successfully")
        return result
        
    except Exception as e:
        logger.error(f"Error in direct pathway generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

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
        ],
        "environment": "production" if os.getenv("ENVIRONMENT") == "production" else "development"
    }

# For Cloud Run, the port is automatically set via $PORT environment variable
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        workers=1,
        access_log=True,
        loop="uvloop"
    )
