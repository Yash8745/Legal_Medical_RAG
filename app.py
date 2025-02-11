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
    data = request.json
    message = data.get('message', '')
    logger.info(f"Received message: {message}")
    response = summarize_document(FILE_PATH)
    logger.info(f"Response: {response}")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    logger.info("App setup complete.")