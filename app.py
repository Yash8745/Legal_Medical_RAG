# backend/routes.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.logger import setup_logger

logger = setup_logger()

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend


@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Document Summarizer API'})


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']

    file.save(f"uploads/{file.filename}")  # Save file locally

    return jsonify({'message': 'File uploaded successfully'})


# @app.route('/documents', methods=['GET'])
# def fetch_documents():
#     docs = ["doc1.pdf", "doc2.pdf"]  # Replace with actual logic
#     return jsonify({'documents': docs})


# @app.route('/summary/<doc_id>', methods=['GET'])
# def get_summary(doc_id):
#     return jsonify({'doc_id': doc_id, 'summary': 'Sample summary'})




@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    logger.info(f"Received message: {message}")
    response = f"Received: {message}"  # Replace with AI logic
    return jsonify({'response': response})





if __name__ == '__main__':
    app.run(debug=True, port=5000)
