from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def predict(sentence):
    # Replace this with your actual prediction code
    return 'Predicted Label'

def get_assistant_response(sentence):
    # Replace this with your actual assistant response code
    return 'Assistant Response'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        predicted_label = predict(sentence)
        assistant_response = get_assistant_response(sentence)
        return render_template('results.html', 
            sentence=sentence, 
            predicted_label=predicted_label, 
            assistant_response=assistant_response
        )
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    sentence = request.form.get('sentence')
    predicted_label = request.form.get('predicted_label')
    assistant_response = request.form.get('assistant_response')
    was_prediction_correct = 'correct_prediction' in request.form
    was_assistant_correct = 'correct_assistant' in request.form
    with open('feedback.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([sentence, predicted_label, assistant_response, was_prediction_correct, was_assistant_correct])
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True)
