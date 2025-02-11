from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.logger import setup_logger
from pipeline.summarize_document import summarize_document
import os

logger = setup_logger()

app = Flask(__name__)
CORS(app)

FILE_PATH = "uploads"

# Store file mappings (id -> filename)
file_mappings = {}

if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)
    logger.info(f"Created directory: {FILE_PATH}")

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Document Summarizer API'})

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    File Upload Endpoint.

    Expects a file to be included in the POST request with the key 'file'.
    The file is saved to the FILE_PATH directory with its original filename.
    A unique ID is generated and stored in the file_mappings dictionary.

    Returns:
        JSON response containing:
            - A success message.
            - The unique file ID.
            - The original filename.
        On error, returns a JSON error message with an appropriate HTTP status code.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Generate a unique ID for the file
        import uuid
        file_id = str(uuid.uuid4())
        
        # Save the file
        file_path = os.path.join(FILE_PATH, file.filename)
        file.save(file_path)
        
        # Store the mapping
        file_mappings[file_id] = file.filename
        
        logger.info(f"File uploaded: {file.filename} with ID: {file_id}")
        return jsonify({
            'message': 'File uploaded successfully',
            'id': file_id,
            'filename': file.filename
        })
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        return jsonify({'error': 'Error uploading file'}), 500

@app.route('/documents/<doc_id>', methods=['DELETE'])
def delete_document(doc_id):
    """
    Document Deletion Endpoint.

    Deletes a document using its unique identifier.
    It retrieves the filename from the file_mappings dictionary and removes the file from the filesystem.

    Args:
        doc_id (str): The unique identifier for the document.

    Returns:
        JSON response confirming deletion if successful.
        JSON error message with appropriate HTTP status code if the document is not found or an error occurs.
    """
    try:
        # Get filename from mappings
        filename = file_mappings.get(doc_id)
        if not filename:
            logger.error(f"Document ID not found: {doc_id}")
            return jsonify({'error': 'Document not found'}), 404

        # Delete the file
        file_path = os.path.join(FILE_PATH, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            # Remove from mappings
            del file_mappings[doc_id]
            logger.info(f"File deleted: {filename}")
            return jsonify({'message': 'Document deleted successfully'})
        else:
            logger.error(f"File not found: {file_path}")
            return jsonify({'error': 'File not found'}), 404

    except Exception as e:
        logger.error(f"Error deleting document: {str(e)}")
        return jsonify({'error': 'Error deleting document'}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """
    Chat/Summarize Endpoint.

    Accepts a JSON payload containing a message. The message is logged,
    and then the summarize_document function is invoked to process and summarize the documents
    stored in the FILE_PATH directory. The summarization response is returned as JSON.

    Returns:
        JSON response containing the summarization result.
    """
    data = request.json
    message = data.get('message', '')
    logger.info(f"Received message: {message}")
    response = summarize_document(FILE_PATH)
    logger.info(f"Response: {response}")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    logger.info("App setup complete.")