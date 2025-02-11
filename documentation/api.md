
### API Endpoints
```python
@app.route('/upload', methods=['POST'])
# Handles PDF file uploads and returns file ID and status

@app.route('/documents/<doc_id>', methods=['DELETE'])
# Deletes specified document and manages file storage

@app.route('/chat', methods=['POST'])
# Processes document summarization requests and returns AI-generated summaries
```
