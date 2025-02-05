from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Create uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('chat', filename=filename))
    return redirect(request.url)

@app.route('/chat/<filename>')
def chat(filename):
    return render_template('chat.html', filename=filename)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    filename = data.get('filename')
    
    # Here you would add your RAG processing logic
    # For now, just return a dummy response
    response = f"Received question: '{question}' for file: {filename}"
    
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)