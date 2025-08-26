# 🚀 Kickstart AI Learning – Personalized Pathways Using Your Interests

**Kickstart** is an intelligent learning assistant powered by Agentic AI that transforms how you learn by creating personalized educational pathways tailored to **your hobbies**, **learning style**, and **domain interests**.

Whether you're passionate about **Cricket**, fascinated by **Harry Potter**, or love **Photography**, Kickstart uses your interests as bridges to make complex topics engaging, memorable, and relevant to your life.

---

## 🎯 Problem Statement & Solution

### The Problem
Traditional learning approaches often:
- 📚 Use generic, one-size-fits-all content
- 🥱 Lack personal relevance and engagement
- ⚡ Fail to connect new concepts to learner's existing interests
- 🔄 Don't adapt to individual learning styles
- 🌐 Struggle to incorporate latest trends and developments

### Our Solution
Kickstart leverages **Agentic AI architecture** with **LangGraph** to create truly personalized learning experiences:

1. **Hobby-Driven Learning**: Transforms abstract concepts using your personal interests as analogies
2. **Intelligent Research**: Uses Tavily API to gather latest information and trends
3. **Adaptive Pathways**: Google Gemini generates structured, progressive learning plans
4. **Multi-Modal Interfaces**: Both CLI and web interfaces for different use cases
5. **Real-time Personalization**: Dynamically adjusts content based on your profile

---

## 🌟 Live Demo

🔗 **Web Interface**: [Kickstart Learning Agent](https://kickstart-learning.onrender.com) _(Deployed on Render)_

---

## 🎯 Key Features

✅ **Personalized Learning Pathways** - Structured 7-phase learning plans  
✅ **Hobby-Based Examples** - Complex concepts explained through your interests  
✅ **Real-Time Research** - Latest trends and developments via Tavily API  
✅ **Historical Context** - Rich background with key milestones  
✅ **Project Ideas** - Practical applications in your domain  
✅ **Dual Interfaces** - CLI for developers, Web UI for general users  
✅ **Agentic Architecture** - Intelligent task orchestration with LangGraph  

---

## 🖼️ Screenshots

![Landing Page](https://github.com/snikhil17/Agentic-AI-2025/blob/main/kickstart-learning-using-agents/images/landing_page.png?raw=true)
*Clean, intuitive input form for learning preferences*

![Example using ADK by Google](https://github.com/snikhil17/Agentic-AI-2025/blob/main/kickstart-learning-using-agents/images/ADK_example.png?raw=true)
*Real example: Learning Android Development Kit through cricket analogies*

![Adaptive Learning Pathway-1](https://github.com/snikhil17/Agentic-AI-2025/blob/main/kickstart-learning-using-agents/images/initial_pathway.png?raw=true)
*Structured 7-phase learning pathway with clear progression*

![Adaptive Learning Pathway-2](https://github.com/snikhil17/Agentic-AI-2025/blob/main/kickstart-learning-using-agents/images/learning_pathway_2.png?raw=true)
*Detailed breakdown of each learning phase with actionable steps*

![Explanation of Learning Pathway](https://github.com/snikhil17/Agentic-AI-2025/blob/main/kickstart-learning-using-agents/images/explanation_kickstart.png?raw=true)
*Rich explanations with hobby-specific analogies and examples*

![Relevant Links](https://github.com/snikhil17/Agentic-AI-2025/blob/main/kickstart-learning-using-agents/images/relevant_links.png?raw=true)
*Curated resources and links for deeper learning*

---

## 🏗️ Architecture Overview

### Agentic AI Pipeline
```mermaid
graph LR
    A[User Input] --> B[Retrieval Agent]
    B --> C[Planning Agent]
    C --> D[Explanation Agent]
    D --> E[Structured Output]
    
    B --> F[Tavily API]
    C --> G[Google Gemini]
    D --> G
```

### Core Components
1. **`agent.py`** - Main entrypoint with `@entrypoint()` decorator
2. **`retrieval.py`** - Tavily-powered research and context gathering
3. **`structured_agent.py`** - Gemini-based pathway generation
4. **`explanation.py`** - Hobby-specific content creation
5. **`app.py`** - Flask web interface
6. **`main.py`** - CLI interface

---

## 🛠️ Tech Stack

### Backend
- **🤖 LangGraph 0.3.31** - Agentic AI orchestration
- **🧠 Google Gemini 2.5 Flash** - Language model for content generation
- **� Tavily API** - Real-time web search and research
- **🌐 Flask 3.1.0** - Web framework
- **� Pydantic** - Structured data validation

### Frontend
- **⚛️ React 19.1.1** - Modern UI framework
- **🎨 Tailwind CSS** - Utility-first styling
- **📝 React Markdown** - Rich content rendering
- **⚡ Vite** - Fast build tool

### Deployment
- **☁️ Render.com** - Cloud platform
- **🦄 Gunicorn** - WSGI server
- **🔧 Gevent** - Async worker handling

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** 
- **Node.js 16+** (for React frontend)
- **Google API Key** (for Gemini AI)
- **Tavily API Key** (for web search)

### Option 1: Web Interface (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/snikhil17/Agentic-AI-2025.git
   cd Agentic-AI-2025/kickstart-learning-using-agents
   ```

2. **Set up Python environment**
   ```bash
   # Create virtual environment
   python -m venv kickstart_env
   
   # Activate virtual environment
   # On Linux/Mac:
   source kickstart_env/bin/activate
   # On Windows:
   kickstart_env\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env file with your API keys
   echo "GOOGLE_API_KEY=your_google_api_key_here" >> .env
   echo "TAVILY_API_KEY=your_tavily_api_key_here" >> .env
   ```

5. **Run the Flask web server**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser to `http://localhost:5000`
   - Fill in your learning preferences
   - Get your personalized learning pathway!

### Option 2: CLI Interface (For Developers)

1. **Follow steps 1-4 from above**

2. **Run the CLI version**
   ```bash
   python main.py
   ```

3. **Interactive prompts will guide you through:**
   - Learning style preferences
   - Topic of interest
   - Your hobbies
   - Domain focus

### Option 3: React Frontend (Advanced)

1. **Complete Python setup (steps 1-4 above)**

2. **Set up React frontend**
   ```bash
   cd adaptive-learning-agent
   npm install
   ```

3. **Configure frontend environment**
   ```bash
   # Create environment file
   echo "VITE_API_URL=http://localhost:5000" > .env.local
   ```

4. **Run both servers**
   ```bash
   # Terminal 1: Python backend
   cd ..
   python app.py
   
   # Terminal 2: React frontend
   cd adaptive-learning-agent
   npm run dev
   ```

5. **Access React app at** `http://localhost:5173`

---

## 🔑 API Key Setup Guide

### Google API Key (Gemini AI)
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" → "Create API Key"
4. Copy your API key

### Tavily API Key (Web Search)
1. Visit [Tavily API](https://app.tavily.com/)
2. Sign up for a free account
3. Go to your dashboard
4. Copy your API key from the dashboard

### Environment Configuration
```bash
# .env file format
GOOGLE_API_KEY=AIzaSyC-your-actual-key-here
TAVILY_API_KEY=tvly-your-actual-key-here
```

---

## 📁 Project Structure

```
kickstart-learning-using-agents/
├── 🤖 Core Agent Files
│   ├── agent.py                 # Main LangGraph entrypoint
│   ├── structured_agent.py      # Gemini-powered pathway generation
│   ├── retrieval.py             # Tavily search & research
│   ├── explanation.py           # Hobby-specific content creation
│   ├── planning.py              # Learning pathway planning
│   └── data_models.py           # Pydantic data structures
├── 🌐 Web Interface
│   ├── app.py                   # Flask web application
│   ├── main.py                  # CLI interface
│   └── templates/               # Jinja2 HTML templates
│       ├── index.html           # Input form
│       ├── result.html          # Learning pathway display
│       └── base.html            # Base template
├── ⚛️ React Frontend
│   └── adaptive-learning-agent/
│       ├── App.tsx              # Main React app
│       ├── components/          # UI components
│       ├── services/            # API integration
│       └── types.ts             # TypeScript definitions
├── 📋 Configuration
│   ├── requirements.txt         # Python dependencies
│   ├── render.yaml              # Deployment config
│   └── .env.example            # Environment template
└── 📸 Assets
    └── images/                  # Screenshots and demos
```

---

## 🔧 Advanced Configuration

### Customizing the AI Models

**Change Gemini Model Version**
```python
# In structured_agent.py
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or "gemini-1.5-pro"
    api_key=student_profile.get("google_api_key")
)
```

**Adjust Search Parameters**
```python
# In retrieval.py
retriever = TavilySearchAPIRetriever(
    k=5,  # Number of search results
    search_depth="advanced",  # "basic" or "advanced"
    api_key=student_profile.get("tavily_api_key")
)
```

### Adding Custom Learning Styles

Edit the form options in `templates/index.html`:
```html
<option value="visual-learner">Visual Learning with Diagrams</option>
<option value="hands-on">Hands-on Project-Based Learning</option>
<option value="theoretical">Deep Theoretical Understanding</option>
```

---

## 🧪 Testing Your Setup

### Quick Health Check
```bash
# Test Python dependencies
python -c "import langchain, flask; print('Dependencies OK')"

# Test API connectivity
python -c "
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', api_key=os.getenv('GOOGLE_API_KEY'))
print('API Keys working!')
"
```

### Sample Test Run
```bash
# CLI test with sample data
python main.py
# When prompted, enter:
# Learning Style: "practical examples"
# Topic: "Machine Learning"
# Hobbies: "Photography, Cooking"
# Domain: "Healthcare"
```

---

## 🚀 Deployment Guide

### Deploy to Render.com (Recommended)

1. **Fork this repository**

2. **Connect to Render**
   - Go to [Render.com](https://render.com)
   - Create new Web Service
   - Connect your forked repository

3. **Configure Environment Variables**
   ```
   GOOGLE_API_KEY = your_google_api_key
   TAVILY_API_KEY = your_tavily_api_key
   ```

4. **Deploy**
   - Render will automatically use `render.yaml` configuration
   - Build time: ~5-10 minutes
   - Your app will be live at `https://your-app-name.onrender.com`

### Deploy to Other Platforms

**Heroku**
```bash
# Add Procfile
echo "web: gunicorn app:app --workers 1 --timeout 240" > Procfile
git add . && git commit -m "Deploy to Heroku"
heroku create your-app-name
heroku config:set GOOGLE_API_KEY=your_key
heroku config:set TAVILY_API_KEY=your_key
git push heroku main
```

**Docker**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
```

---

## 🤔 How It Works Internally

### 1. **Input Processing**
```python
student_profile = {
    "learning_style": "hands-on projects",
    "progress": "Agentic AI", 
    "hobby": "Photography, Rock Climbing",
    "domain": "Healthcare"
}
```

### 2. **Agentic Pipeline Execution**

**Step 1: Research Agent (`retrieval.py`)**
- Tavily API searches for latest information
- Gathers multiple perspectives on the topic
- Filters and ranks relevant content

**Step 2: Planning Agent (`structured_agent.py`)**  
- Google Gemini analyzes research + user profile
- Generates structured learning pathway
- Creates hobby-specific analogies

**Step 3: Output Generation**
- Combines research, pathway, and explanations
- Formats as structured JSON/HTML
- Returns comprehensive learning package

### 3. **Output Structure**
```json
{
  "title": "Photography-Inspired Guide to Agentic AI",
  "learning_phases": [...],
  "explanations": [...],
  "milestones": [...],
  "next_steps": [...],
  "relevant_links": [...]
}
```

---

## 🔍 Troubleshooting

### Common Issues

**❌ "API Key not found" Error**
```bash
# Check environment variables
python -c "import os; print(os.getenv('GOOGLE_API_KEY'))"
# Should return your key, not None
```

**❌ "Module not found" Error**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**❌ "Port already in use" Error**
```bash
# Kill process using port 5000
lsof -ti:5000 | xargs kill -9
# Or use different port
python app.py --port 5001
```

**❌ "Tavily API Limit Exceeded"**
- Free tier: 1000 requests/month
- Upgrade at [Tavily Pricing](https://app.tavily.com/pricing)

**❌ React Build Issues**
```bash
cd adaptive-learning-agent
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Debug Mode

Enable detailed logging:
```python
# In app.py
app.run(debug=True, host='0.0.0.0', port=5000)
```

Check logs:
```bash
# View detailed agent execution
tail -f logs/agent.log
```

---

## 📊 Performance Optimization

### Response Time Improvements
- **Caching**: Implement Redis for repeated queries
- **Async Processing**: Use Celery for background tasks
- **Model Selection**: Switch to Gemini-1.5-flash for faster responses

### Cost Optimization
- **Request Batching**: Combine similar queries
- **Smart Caching**: Cache Tavily searches for popular topics
- **Model Tiers**: Use appropriate Gemini model sizes

---

## 🤝 Contributing

### Development Workflow

1. **Fork & Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Agentic-AI-2025.git
   cd Agentic-AI-2025/kickstart-learning-using-agents
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Development Setup**
   ```bash
   pip install -r requirements-dev.txt  # Includes testing tools
   ```

4. **Run Tests**
   ```bash
   python -m pytest tests/
   ```

5. **Submit PR**
   - Ensure all tests pass
   - Add documentation for new features
   - Follow existing code style

### Areas for Contribution
- 🎨 **UI/UX**: Improve React components and styling
- 🔧 **Features**: Add new learning styles or domains
- 📚 **Content**: Expand hobby-based examples
- 🚀 **Performance**: Optimize API calls and caching
- 🧪 **Testing**: Add comprehensive test coverage

---

## 📈 Roadmap & Future Features

### 🔄 Version 2.0 (Coming Soon)
- [ ] **Multi-language Support** - Learn in your preferred language
- [ ] **Learning Progress Tracking** - Save and resume pathways
- [ ] **Community Features** - Share and rate learning paths
- [ ] **Mobile App** - Native iOS/Android experience

### 🚀 Version 3.0 (Vision)
- [ ] **AI Tutor Chat** - Interactive Q&A during learning
- [ ] **Adaptive Assessments** - Smart quizzes and evaluations  
- [ ] **Learning Analytics** - Detailed progress insights
- [ ] **Enterprise Features** - Team learning and administration

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **LangGraph Team** - For the amazing agentic AI framework
- **Google AI** - For Gemini's powerful language capabilities  
- **Tavily** - For reliable web search API
- **Open Source Community** - For all the wonderful libraries used

---

## 🔗 Links & Resources

- 📖 **Documentation**: [Project Wiki](https://github.com/snikhil17/Agentic-AI-2025/wiki)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/snikhil17/Agentic-AI-2025/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/snikhil17/Agentic-AI-2025/discussions)
- 📺 **Demo Videos**: [YouTube Playlist](https://youtube.com/playlist?list=your-playlist-id)

---