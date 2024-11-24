from flask import Flask, request, jsonify # Flask Web App Frame Work
from transformers import pipeline # Hugging Face :)

app = Flask(__name__)
# Distibert ML Model(Why.? Because it's light weight enough for demo deployement process.!)
# Model Inilization 
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

#Flask route when predict path got pingged 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    # Model inference
    result = model(text)[0]
    return jsonify(result)

if __name__ == '__main__':
    # Here Flask app run on port 5000 recive and send communication to "Gunicorn" which is running on port 8000 
    app.run(host='0.0.0.0', port=5000)
