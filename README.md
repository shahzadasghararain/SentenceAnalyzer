# Flask Sentence Predictor and Assistant

This Flask web application allows users to input sentences and receive predicted labels and assistant responses. Users can also provide feedback on the predictions and responses.

## Features

- Accepts user input sentences.
- Provides predicted labels and assistant responses.
- Allows users to give feedback on the accuracy of the predictions and responses.
- Saves feedback to a CSV file for further analysis.

## Requirements

- Python 3.x
- Flask
- CSV module (included in Python's standard library)

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Clone this repository or download the script files directly.

3. Install the required Python packages:
    ```bash
    pip install flask
    ```

## Usage

1. Modify the `predict` and `get_assistant_response` functions in the script to include your actual prediction and assistant response logic:
    ```python
    def predict(sentence):
        # Replace this with your actual prediction code
        return 'Predicted Label'

    def get_assistant_response(sentence):
        # Replace this with your actual assistant response code
        return 'Assistant Response'
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Application Structure

- `app.py`: Main application file containing the Flask routes and logic.
- `templates/index.html`: HTML template for the main page where users can input sentences.
- `templates/results.html`: HTML template for displaying the results.
- `templates/thanks.html`: HTML template for the feedback thank you page.
- `feedback.csv`: CSV file where feedback is saved.

## Example

```python
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
