# Contributing to Kickstart Learning Agent

Thank you for your interest in contributing to the Kickstart Learning Agent! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Getting Started

1. **Fork the Repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/Agentic-AI-2025.git
   cd Agentic-AI-2025/kickstart-learning-using-agents
   ```

2. **Set Up Development Environment**
   ```bash
   # Use the setup script
   ./setup.sh  # Linux/Mac
   setup.bat   # Windows
   
   # Or manually
   python -m venv kickstart_env
   source kickstart_env/bin/activate  # Linux/Mac
   kickstart_env\Scripts\activate     # Windows
   pip install -r requirements-dev.txt
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Development Guidelines

#### Code Style
- **Python**: Follow PEP 8 standards
- **JavaScript/TypeScript**: Use Prettier formatting
- **Line Length**: 88 characters max for Python, 120 for JS/TS
- **Comments**: Write clear, concise comments for complex logic

#### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_setup.py
```

#### Code Formatting
```bash
# Format Python code
black .
isort .

# Check linting
flake8 .
mypy .
```

### Types of Contributions

#### 🐛 Bug Fixes
1. Check existing issues first
2. Create a new issue if needed
3. Reference the issue in your PR
4. Include tests for the fix

#### ✨ New Features
1. Discuss in GitHub Issues first
2. Follow existing architecture patterns
3. Add comprehensive tests
4. Update documentation

#### 📚 Documentation
1. Use clear, concise language
2. Include code examples
3. Test all examples work
4. Update README if needed

#### 🎨 UI/UX Improvements
1. Maintain accessibility standards
2. Follow existing design patterns
3. Test on multiple browsers
4. Include screenshots in PR

## 🏗️ Architecture Guidelines

### Agent Development
- Use `@task` decorator for LangGraph functions
- Pass `student_profile` dict between components
- Handle API key injection properly
- Follow the retrieval → planning → explanation pattern

### Flask Development  
- Keep routes simple and focused
- Use Jinja2 templates for HTML
- Implement proper error handling
- Follow REST principles for API endpoints

### React Development
- Use TypeScript for type safety
- Follow component composition patterns
- Implement proper error boundaries
- Use modern React hooks

### API Integration
- Handle rate limiting gracefully
- Implement proper error handling
- Use environment variables for keys
- Add retry logic for failed requests

## 📝 Pull Request Process

### Before Submitting
1. **Test Your Changes**
   ```bash
   # Run all tests
   pytest
   
   # Test the web app
   python app.py
   
   # Test CLI
   python main.py
   ```

2. **Update Documentation**
   - Update README if needed
   - Add docstrings to new functions
   - Update type hints

3. **Check Code Quality**
   ```bash
   black .
   flake8 .
   mypy .
   ```

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature  
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Manual testing completed

## Screenshots (if applicable)
Include screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## 🎯 Priority Areas for Contribution

### High Priority
- **Performance Optimization**: Caching, async processing
- **Error Handling**: Better user feedback and recovery
- **Testing**: Increase test coverage
- **Documentation**: More examples and tutorials

### Medium Priority  
- **UI/UX**: Better responsive design and accessibility
- **Features**: New learning styles and domains
- **Integration**: Additional AI model support
- **Deployment**: More deployment options

### Low Priority
- **Refactoring**: Code organization improvements
- **Tooling**: Development workflow enhancements
- **Analytics**: Usage tracking and metrics

## 🔍 Code Review Guidelines

### For Reviewers
- Be constructive and specific
- Test the changes locally
- Check for security issues
- Verify documentation updates
- Consider performance impact

### For Authors
- Respond to feedback promptly
- Make requested changes
- Explain design decisions
- Keep PRs focused and small

## 🚀 Release Process

### Versioning
- Follow Semantic Versioning (SemVer)
- Major: Breaking changes
- Minor: New features
- Patch: Bug fixes

### Release Checklist
1. Update version numbers
2. Update CHANGELOG.md
3. Test deployment
4. Tag release
5. Update documentation

## 🐛 Bug Reporting

### Before Reporting
1. Check existing issues
2. Try latest version
3. Reproduce consistently
4. Gather system info

### Bug Report Template
```markdown
**Describe the bug**
A clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What should have happened

**Environment:**
- OS: [e.g. Ubuntu 20.04]
- Python version: [e.g. 3.9.7]
- Browser: [e.g. Chrome 96]

**Additional context**
Any other relevant information
```

## 💡 Feature Requests

### Request Template
```markdown
**Is your feature request related to a problem?**
Description of the problem

**Describe the solution**
What you'd like to happen

**Describe alternatives**
Alternative solutions considered

**Additional context**
Mockups, examples, etc.
```

## 📞 Getting Help

### Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas  
- **Email**: [your-email@example.com] for private matters

### Response Times
- **Bug reports**: 1-3 days
- **Feature requests**: 1-7 days  
- **Pull requests**: 1-5 days

## 📜 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

## 🙏 Recognition

Contributors will be:
- Listed in README.md
- Credited in release notes
- Mentioned in announcements

Thank you for helping make Kickstart Learning Agent better! 🎉
