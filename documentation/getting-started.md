
# Getting Started Guide 🚀

This guide will help you set up and run the Legal/Medical Document RAG System on your local machine.

## System Requirements 🔧

- Python 3.10
- Node.js 16.x or higher
- 8GB RAM minimum (16GB recommended)
- GPU recommended for better performance (not compulsory)
- Operating System: Windows 10/11

## Initial Setup

### 1. Create and Activate Your Conda Environment

Open your terminal and run the following commands:

```bash
conda create --name myenv python=3.10

# Activate the newly created environment
conda activate myenv
```

### 2. Install Python Dependencies

With the Conda environment activated, install the required Python packages using your requirements file:

```bash
pip install -r requirements.txt
```

### 3. API Keys Configuration

Copy the provided environment example file to create your own configuration file:

```bash
cp .env.example .env
```

Then open the `.env` file and configure your API keys:

```plaintext
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Frontend Setup

Navigate to the frontend directory and set up the project by installing the necessary dependencies and creating the production build:

```bash
# Navigate to the frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Create the production build
npm run build
```

## 5. Google Cloud SDK Setup (Optional if already installed and configured for project authentication)

### For Windows

1. **Download and Install the SDK**  
   - Visit the [Google Cloud SDK installation page](https://cloud.google.com/sdk/docs/install#windows) for detailed instructions.
   - Download the Windows installer and follow the on-screen prompts.

2. **Initialize the SDK**  
   Open a new Command Prompt or PowerShell window and run:
   ```bash
   gcloud init
   ```

### B. Generating Local Application Default Credentials

1. **Generate Credentials**  
   Run the following command:
   ```bash
   gcloud auth application-default login
   ```
   This will open a browser window for you to log in with your Google account.

2. **Credential Storage**  
   After successful authentication, the SDK will save a JSON credentials file locally (typically located at `~/.config/gcloud/application_default_credentials.json` on macOS/Linux or `%APPDATA%\gcloud\application_default_credentials.json` on Windows).

3. **Usage in Your Project**  
   Google Cloud client libraries will automatically detect and use these credentials. If needed, you can also point your application explicitly to this file using the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:
 
   - **Windows (Command Prompt):**
     ```cmd
     set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\application_default_credentials.json"
     ```
   - **Windows (PowerShell):**
     ```powershell
     $env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\application_default_credentials.json"
     ```

## Running the Application

### 1. Start the Backend Server

From the project root directory:

```bash
python app.py
```

The backend server will start on `http://localhost:5000`.

### 2. Start the Frontend Development Server

In a new terminal, got to from the frontend directory:

```bash
cd frontend

npm run dev
```

The frontend will be available at `http://localhost:5173`.

# Flow of Program

1. **Upload PDFs**  
   - Click on "Upload PDF" and upload a minimum of 2 PDFs.

2. **Click Brief Document**  
   - Click on the "Brief Document" button (the only working button right now).  
   - Only click the button once or press Enter once.

3. **Wait for Summary**  
   - Wait for the summary to be generated (this can take up to 4 minutes).

4. **Check Application Logs**  
   - Check the `logs/app.logs` file to review logs generated during the process to ensure everything is running smoothly.

5. **Check Console Log**  
   - Open the browser's console log to check for any errors.

6. **Delete Documents After Summary**  
   - When the summary is generated, delete the documents from the left tab by hovering over the document name and clicking the delete button in the pop-up.

7. **Refresh and Re-upload**  
   - Refresh the page; you can then upload documents again to generate a new summary.

8. **Manual Cleanup (if necessary)**  
   - If you refreshed without deleting documents and the PDFs do not appear, manually delete the PDFs from the uploads folder.

## Troubleshooting 🚑

If you encounter issues with **Google Gemini**—for example, if the logs show that a summary wasn't generated due to resource quota limits or another Google API issue—follow these steps to temporarily switch to the **Chat Groq** model:

1. **Open the File:**  
   Navigate to `pipeline/summarize_document.py` in your code editor.

2. **Disable Google Gemini:**  
   - Find line **51**, which initializes the **Chat Google Generate** LLM.  
   - Comment out this line.

3. **Enable Chat Groq:**  
   - Locate line **49**, which initializes the **Chat Groq** LLM.  
   - Uncomment this line.

4. **Restart the Application:**  
   Save your changes and restart the application to apply the update.

This temporary workaround will switch summary generation to use the **LLaMA 3 8B** model until the Google Gemini issues are resolved.

## Next Steps 👉

- See the [Idea and Methodology](idea.md) behind the project.
- Review the [Technical Documentation](technical.md) for an in-depth understanding.
- Explore the notebooks in the `notebooks/` directory for example implementations.
- Check out the [API Documentation](api.md) for backend endpoint details.
