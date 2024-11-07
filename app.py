from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Route to render the main page with the form
@app.route('/')
def index():
    return render_template('index.html')  # Your HTML form will be in 'templates/index.html'

# Route to handle form submission and generate questions
@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    # Get data sent from the front-end
    data = request.get_json()
    topic = data.get('topic')
    num_questions = int(data.get('numQuestions'))

    # Here you can replace this with actual logic to fetch real questions based on the topic
    # For now, we will generate dummy questions for the topic
    if not topic or num_questions <= 0:
        return jsonify({"error": "Invalid topic or number of questions"}), 400

    questions = []
    for i in range(num_questions):
        questions.append(f"Sample question {i+1} on {topic}")
    
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)