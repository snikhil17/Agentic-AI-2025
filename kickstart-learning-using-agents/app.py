from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from agent import adaptive_learning_agent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_profile = {
            "learning_style": request.form.get("learning_style"),
            "progress": request.form.get("progress"),
            "hobby": request.form.get("hobby"),
            "domain": request.form.get("domain"),
            "google_api_key": os.getenv("GOOGLE_API_KEY"),
            "tavily_api_key": os.getenv("TAVILY_API_KEY")
        }
        result = adaptive_learning_agent.invoke(student_profile)
        return render_template("result.html", result=result)
    return render_template("index.html")

@app.route("/api/generate-pathway", methods=["POST"])
def generate_pathway():
    """API endpoint for React frontend"""
    try:
        data = request.get_json()
        
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
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
