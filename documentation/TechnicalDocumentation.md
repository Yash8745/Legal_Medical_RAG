# Technical Documentation

## Architecture Overview

The Legal/Medical Document RAG System implements a sophisticated document processing pipeline using modern NLP techniques and a RAG (Retrieval Augmented Generation) architecture.

### High-Level Architecture

```
[Frontend (React)] <-> [Backend (Flask)] <-> [LLM Services]
                                       <-> [Embedding Models]
                                       <-> [Document Processing]
```

## Core Components

### 1. Document Processing Pipeline

The system processes documents through several stages:

1. **Text Extraction** (`utils/data_ingestion_util.py`)
   - Uses PyPDFLoader for PDF parsing
   - Implements RecursiveCharacterTextSplitter for chunk management
   - Handles large documents through streaming

2. **Embedding Generation** (`model/embedding.py`)
   - Uses HuggingFaceBgeEmbeddings
   - Model: "BAAI/bge-base-en-v1.5"
   - Optimized for semantic understanding

3. **Text Clustering** (`model/cluster.py`)
   - Implements EmbeddingsClusteringFilter
   - Groups similar content for better summarization
   - Configurable number of clusters

4. **Summarization** (`model/summarization.py`)
   - Supports multiple LLM providers
   - Implements different summarization strategies
   - Handles context management

### 2. Language Models

The system supports multiple LLM providers:

1. **Groq Integration**
   - Model: llama3-8b-8192
   - Optimized for speed and accuracy
   - Used for detailed analysis

2. **Google Gemini Integration**
   - Model: gemini-2.0-flash
   - Excellent for general summarization
   - Strong multilingual support

### 3. Frontend Architecture

Built with React and TypeScript, following modern best practices:

1. **State Management**
   - React Hooks for local state
   - Custom hooks for business logic
   - Efficient document management

2. **UI Components**
   - Tailwind CSS for styling
   - Lucide icons for consistent design
   - Dark mode support

3. **API Integration**
   - Axios for HTTP requests
   - Error handling middleware
   - File upload management

## Key Technologies

### Backend Technologies

1. **Flask**
   - Lightweight web framework
   - CORS support
   - File handling capabilities

2. **LangChain**
   - LLM orchestration
   - Document processing
   - Chain management

3. **Hugging Face**
   - Embedding models
   - Tokenization
   - Model management

### Frontend Technologies

1. **React 18**
   - Functional components
   - Hooks architecture
   - Strict mode enabled

2. **TypeScript**
   - Type safety
   - Enhanced IDE support
   - Better code organization

3. **Tailwind CSS**
   - Utility-first CSS
   - Responsive design
   - Dark mode support

## Implementation Details

### Document Processing Flow

1. **Upload Phase**
   ```python
   @app.route('/upload', methods=['POST'])
   def upload_file():
       file = request.files['file']
       file_id = str(uuid.uuid4())
       file_mappings[file_id] = file.filename
   ```

2. **Processing Phase**
   ```python
   def summarize_document(file_path):
       embeddings = get_embeddings_model()
       texts = extract_text_from_pdf(file_path)
       clustered_texts = cluster_texts(texts, embeddings)
       return summarize_texts(clustered_texts, llm)
   ```

3. **Response Phase**
   ```python
   @app.route('/chat', methods=['POST'])
   def chat():
       message = data.get('message', '')
       response = summarize_document(FILE_PATH)
       return jsonify({'response': response})
   ```

## Performance Considerations

1. **Memory Management**
   - Chunk-based processing
   - Streaming responses
   - Resource cleanup

2. **Scalability**
   - Stateless design
   - Asynchronous operations
   - Caching strategies

3. **Error Handling**
   - Graceful degradation
   - Comprehensive logging
   - User feedback

## Security Considerations

1. **API Security**
   - Environment variables for secrets
   - Input validation
   - Rate limiting

2. **File Security**
   - File type validation
   - Size limitations
   - Secure storage

3. **Data Privacy**
   - Local processing
   - No permanent storage
   - Secure transmission