from flask import Flask, render_template, request
import joblib
from textblob import TextBlob
import smtplib
from email.mime.text import MIMEText
# from sklearn.feature_extraction.text import TfidfVectorizer
# tfidf_vectorizer=TfidfVectorizer()
tfidf_vectorizer=joblib.load('tfidf_joblib')
model=joblib.load('model_joblib')
app = Flask(__name__)
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment>0:
      s=1
    elif sentiment<0:
      s=-1
    else:
      s=0
    return s
# Replace this with your actual prediction function
# Ensure it takes the message as input and returns the prediction
def predict(message):
    # Your prediction logic here
    # (e.g., load your model, preprocess text, make prediction)
    senti=get_sentiment(message)
    prediction=model.predict(tfidf_vectorizer.transform([message]))
    if senti==1 or senti==0:
        prediction=["Not Cyberbullying"]
    return prediction

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/complaint')
def complaint():
    return render_template('complaint.html')

@app.route('/contact')
def contact():
    return render_template('contact_new.html',image='address.png')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/predict', methods=['POST'])
def handle_prediction():
    message = request.form.get('msg')
    if not message:
        return render_template('home.html',message="Please enter a message.")

    prediction = predict(message)
    prediction=prediction[0]

    return render_template('home.html', message=message, prediction=prediction)

@app.route('/submit',methods=['POST'])
def submit():
    em=request.form.get('email')
    if not em:
        return render_template('contact_new.html',email="Please enter email",msg="No")
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = ''
    password = ''
    mesg=f"<h3>Thanks for contacting us </h3>"
    sender_email = ''
    receiver_email = em
    msg = MIMEText(mesg, 'html')
    msg['Subject'] = "Contact Us Initial Response"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    return render_template('contact_new.html',msg="Yes")

if __name__ == '__main__':
    app.run(debug=True)
