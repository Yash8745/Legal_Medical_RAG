# API Endpoints 🚀


## 1. **File Upload** 🔄
- **URL:** `/upload`
- **Method:** `POST`
- **Description:**  
  Uploads a PDF file. The API saves the file, generates a unique ID, and returns the file ID along with its original filename.
- **Example:**
  ```python
  @app.route('/upload', methods=['POST'])
  # Handles PDF file uploads and returns file ID and status
  ```

---

## 2. **Document Deletion** 🗑️
- **URL:** `/documents/<doc_id>`
- **Method:** `DELETE`
- **Description:**  
  Deletes a specified document based on its unique identifier. The endpoint removes the file from storage and updates the file mappings.
- **Example:**
  ```python
  @app.route('/documents/<doc_id>', methods=['DELETE'])
  # Deletes specified document and manages file storage
  ```

---

## 3. **Chat / Summarize** 💬
- **URL:** `/chat`
- **Method:** `POST`
- **Description:**  
  Accepts a JSON payload with a message. This endpoint logs the message, processes the uploaded documents through a summarization pipeline (text extraction, embedding, clustering, and summarization), and returns an AI-generated summary.
- **Example:**
  ```python
  @app.route('/chat', methods=['POST'])
  # Processes document summarization requests and returns AI-generated summaries
  ```
