# Getting Started Guide

This guide will help you set up and run the Legal/Medical Document RAG System on your local machine.

## System Requirements

- Python 3.8 or higher
- Node.js 16.x or higher
- 8GB RAM minimum (16GB recommended)
- GPU recommended for better performance
- Operating System: Windows 10/11, macOS, or Linux

## Initial Setup

### 1. Environment Setup

First, set up your Python virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. API Keys Configuration

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Configure the following API keys in your `.env` file:

```plaintext
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create production build
npm run build
```

## Running the Application

### 1. Start the Backend Server

From the project root directory:

```bash
python app.py
```

The backend server will start on `http://localhost:5000`

### 2. Start the Frontend Development Server

In a new terminal, from the frontend directory:

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Verifying Installation

1. Open your browser and navigate to `http://localhost:5173`
2. Try uploading a PDF document
3. Use the "Briefing Doc" feature to generate a summary
4. Verify that dark mode toggle works

## Common Issues and Solutions

### Backend Issues

1. **ModuleNotFoundError**:
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt` again

2. **API Key Errors**:
   - Verify all API keys are correctly set in `.env`
   - Check API key permissions in respective platforms

### Frontend Issues

1. **npm dependencies errors**:
   - Delete `node_modules` and `package-lock.json`
   - Run `npm install` again

2. **CORS errors**:
   - Verify backend is running on port 5000
   - Check CORS configuration in `app.py`

## Next Steps

- Review the [Technical Documentation](technical.md) for in-depth understanding
- Explore the notebooks in the `notebooks/` directory for example implementations
- Check out the [API Documentation](api.md) for backend endpoints details



## Environment Configuration
```plaintext
GROQ_API_KEY=''        # Groq API access
PINECONE_API_KEY=''    # Pinecone vector DB
GEMINI_API_KEY=''      # Google Gemini AI
```
## Running the System

### Backend Setup:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup:
```bash
cd frontend
npm install
npm run dev
```
