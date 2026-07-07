from flask import Flask, render_template, request
from config import Config

from analyzer.length_checker import check_length
from analyzer.recommendations import generate_recommendations
from analyzer.personal_info import check_personal_info
from analyzer.breach_checker import check_breach
from analyzer.pattern_detector import detect_pattern
from analyzer.complexity_checker import check_complexity
from analyzer.entropy_calculator import calculate_entropy
from analyzer.score_calculator import calculate_score

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.form.get("password","").strip()

    name = request.form.get('name', '').strip()
    username = request.form.get('username', '').strip()
    dob = request.form.get('dob', '').strip()
    email = request.form.get('email', '').strip()

    if not password:
        return render_template('result.html', error='Password cannot be empty.')

    length_result = check_length(password)
    complexity_result = check_complexity(password)
    entropy_result = calculate_entropy(password)
    pattern_result = detect_pattern(password)
    breach_result = check_breach(password)
    personal_info_result = check_personal_info(password, name=name, dob=dob, username=username, email=email)
    score = calculate_score(
        length_result=length_result,
        complexity_result= complexity_result,
        entropy_result=entropy_result,
        pattern_result=pattern_result,
        breach_result=breach_result,
        personal_info_result=personal_info_result)

    # Score Result
    if score <= 30:
        strength = "Weak"
        strength_class = "weak"
    elif score <= 60:
        strength = "Moderate"
        strength_class = "moderate"
    elif score <= 80:
        strength = "Strong"
        strength_class = "strong"
    else:
        strength = "Very Strong"
        strength_class = "very-strong"

    recommendations = generate_recommendations(
        length_result,
        complexity_result,
        pattern_result,
        breach_result,
        personal_info_result
    )

    print(f'length_result: {length_result}\n'
          f'complexity_result: {complexity_result}\n'
          f'pattern_result: {pattern_result}\n',
          f'breach_result: {breach_result}\n',
          f'personal_info_result: {personal_info_result}\n,'
          f'recommendations: {recommendations}',
          f'Score: {score}')

    return render_template(
        'result.html',
        password="*"*len(password),
        score=score,
        strength=strength,
        strength_class=strength_class,
        entropy=entropy_result,
        length_result=length_result,
        complexity_result=complexity_result,
        pattern_result=pattern_result,
        breach_result=breach_result,
        personal_info_result=personal_info_result,
        recommendations=recommendations)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(
        host = app.config["HOST"],
        port = app.config["PORT"],
        debug = app.config["DEBUG"],
    )