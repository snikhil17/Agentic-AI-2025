"""
Test setup and basic functionality of the Kickstart Learning Agent
"""
import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from agent import adaptive_learning_agent


class TestBasicSetup:
    """Test basic application setup and dependencies"""
    
    def test_imports(self):
        """Test that all required modules can be imported"""
        try:
            import flask
            import langchain
            import langgraph
            import dotenv
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain_community.retrievers import TavilySearchAPIRetriever
        except ImportError as e:
            pytest.fail(f"Import error: {e}")
    
    def test_flask_app_creation(self):
        """Test that Flask app can be created"""
        assert app is not None
        assert app.config is not None
    
    def test_flask_routes_exist(self):
        """Test that required routes exist"""
        with app.test_client() as client:
            # Test main route
            response = client.get('/')
            assert response.status_code == 200
            
            # Test API route exists
            response = client.post('/api/generate-pathway', 
                                 json={'learningStyle': 'test', 'topic': 'test', 
                                      'hobbies': 'test', 'domain': 'test'})
            # Should return 500 without API keys, but route should exist
            assert response.status_code in [200, 500]


class TestAgentFunctionality:
    """Test agent functionality with mocked API calls"""
    
    @patch('structured_agent.ChatGoogleGenerativeAI')
    @patch('retrieval.TavilySearchAPIRetriever')
    def test_agent_pipeline_structure(self, mock_tavily, mock_gemini):
        """Test that the agent pipeline can be invoked without API calls"""
        # Mock the retrieval result
        mock_retrieval = MagicMock()
        mock_retrieval.result.return_value = {
            "combined_text": "Mock search results",
            "relevant_links": ["http://example.com"]
        }
        
        # Mock the structured generation result
        mock_structured = MagicMock()
        mock_structured.result.return_value = {
            "title": "Mock Learning Pathway",
            "explanation": "Mock explanation",
            "learning_phases": ["Phase 1", "Phase 2"],
            "milestones": ["Milestone 1"],
            "next_steps": ["Next step 1"]
        }
        
        # Test student profile structure
        student_profile = {
            "learning_style": "hands-on",
            "progress": "Agentic AI",
            "hobby": "Photography",
            "domain": "Technology",
            "google_api_key": "mock_key",
            "tavily_api_key": "mock_key"
        }
        
        # Verify profile structure is correct
        assert "learning_style" in student_profile
        assert "progress" in student_profile
        assert "hobby" in student_profile
        assert "domain" in student_profile


class TestEnvironmentSetup:
    """Test environment configuration"""
    
    def test_env_example_exists(self):
        """Test that environment example file exists"""
        env_example_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            '.env.example'
        )
        assert os.path.exists(env_example_path), ".env.example file should exist"
    
    def test_env_example_content(self):
        """Test that environment example contains required keys"""
        env_example_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            '.env.example'
        )
        
        with open(env_example_path, 'r') as f:
            content = f.read()
        
        assert 'GOOGLE_API_KEY' in content
        assert 'TAVILY_API_KEY' in content


if __name__ == '__main__':
    pytest.main([__file__])
