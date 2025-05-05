from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['msg'].lower()

    # Responses based on user input
    if "admission requirements" in user_input:
        return jsonify({'response': "You need a minimum GPA of 3.0 and SAT score of 1200."})
    elif "how do i apply" in user_input:
        return jsonify({'response': "You can apply through our online portal at apply.university.edu."})
    elif "programs" in user_input or "courses" in user_input:
        return jsonify({'response': "We offer programs in Engineering, Business, Arts, and Science."})
    elif "deadline" in user_input:
        return jsonify({'response': "The application deadline is July 31st."})
    elif "scholarships" in user_input:
        return jsonify({'response': "We offer various scholarships for undergraduate and graduate students. Check our website for more information."})
    elif "contact" in user_input:
        return jsonify({'response': "You can contact our admissions office at admissions@university.edu."})
    elif "campus tour" in user_input:
        return jsonify({'response': "You can schedule a campus tour through our online portal at tours.university.edu."})
    elif "admission fee" in user_input:
        return jsonify({'response': "The admission fee is $50. You can pay it through the application portal."})
    elif "international students" in user_input:
        return jsonify({'response': "We welcome international students! Please visit our international student section on the website for more details."})
    else:
        return jsonify({'response': "I'm sorry, I didn't quite understand that. Can you rephrase?"})

if __name__ == '__main__':
    app.run(debug=True)
