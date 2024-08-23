from flask import Flask, render_template, request, redirect, url_for, session, flash
from transformers import RobertaForSequenceClassification, RobertaConfig
from function.datapreprocessing import DataPreprocessing
from function.User_file import User
from function.Phone_file import Phone
from function.UserDao_file import UserDao
from function.Comment_file import Comment
from function.CommentDao_File import CommentDao
from function.PhoneDao_file import PhoneDao
import csv
import torch
from PhoBert.model import RobertaForAIViVN

app = Flask(__name__)
app.secret_key = 'sentiment'

dp = DataPreprocessing("H:\\VietNamese-Sentiment-Analyst\\data\\data_process\\train.csv")

config = RobertaConfig.from_pretrained(
    "H:\\VietNamese-Sentiment-Analyst\\PhoBert\\PhoBERT_base_transformers\\config.json", from_tf=False, num_labels = 3, output_hidden_states=True,
)

model = RobertaForAIViVN(config)

model.load_state_dict(torch.load("H:\\VietNamese-Sentiment-Analyst\\PhoBert\\best_weights\\model_0.bin", map_location=torch.device('cpu')))


def predict_sentiment(inputs):
    model.eval()  # Đặt mô hình ở chế độ dự đoán
    with torch.no_grad():
        outputs = model(**inputs)
        if isinstance(outputs, torch.Tensor):
            logits = outputs
        else:
            logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()
        return prediction


@app.route('/sentiment_analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    userDao = UserDao()
    commentDao = CommentDao()
    phoneDao = PhoneDao()
    user = User(userid=session['user_id'], username=session['username'])
    
    if user.getUserId == 1:
        if request.method == 'POST' and 'predict' in request.form:
            comment_of_user = commentDao.get_comment_by_user()
            results = []
            for comment_user in comment_of_user:
                comment = Comment(comment_id=comment_user[0], comment=comment_user[1])
                if comment.getComment:  # Kiểm tra giá trị của comment.getComment
                    processed_comment = dp.fit_transform(comment.getComment)
                    full_name = userDao.get_full_name(user)  # Sửa: truyền đối tượng user thay vì comment
                    prediction = predict_sentiment(processed_comment)
                    prediction_s = dp.Standardization(prediction)
                    user_result = User(userid=user.getUserId, username=full_name, comment=comment.getComment, predict=prediction_s)
                    comment_result = Comment(comment_id=comment.getId, predict=prediction)
                    commentDao.update_comment(comment_result)
                    results.append(user_result)

            # Call the statistical function
            statistics = commentDao.statistical()

            # Export statistics to CSV
            with open('statistics.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Phone Name', 'Number of Positives', 'Number of Negatives', 'Number of Neutrals']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in statistics:
                    writer.writerow({
                        'Phone Name': row[0],
                        'Number of Positives': row[1],
                        'Number of Negatives': row[2],
                        'Number of Neutrals': row[3]
                    })

            return render_template('sentiment_analysis.html', user_id=user.getUserId, results=results)
        
    else:
         if request.method == 'POST':
            comment_input = request.form.get('comment_input')
            if comment_input:  # Kiểm tra comment_input không phải là None hoặc trống
                user = User(userid=session['user_id'], username=session['username'], comment=comment_input)
                phone = Phone(id=session['phone_id'])
                comment = Comment(comment=comment_input)
                commentDao.insert_comment(user, comment)
                comment_id = commentDao.get_comment_id_by_user()
                comment_idp = Comment(comment_id=comment_id)
                phoneDao.insert_comment_phone(phone, comment_idp)
                flash('Comment posted successfully!', 'success')
                return redirect(url_for('phone_detail', phone_id=phone.getId))
            else:
                flash('Comment cannot be empty!', 'error')  # Thêm thông báo lỗi nếu comment_input trống
    return render_template('sentiment_analysis.html', user_id=user.getUserId, username=user.getUserName)

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    phoneDao = PhoneDao()
    phone_of_db = phoneDao.get_list_phone()
    results = []
    for phone in phone_of_db[:30]:
        if phone[0] is not None:
            phone_result = Phone(id=phone[0], phone_name=phone[1], specifications=phone[2], photo=phone[3])
            results.append(phone_result)
    return render_template('phone.html', results=results)

@app.route('/phone/<int:phone_id>', methods=['GET', 'POST'])
def phone_detail(phone_id):
    phoneDao = PhoneDao()
    phone_of_db = phoneDao.get_phone(phone_id)
    phone = Phone(id=phone_of_db[0], phone_name=phone_of_db[1], specifications=phone_of_db[2], photo=phone_of_db[3])
    session['phone_id'] = phone_id
    user = User(username=session['username'], userid=session['user_id'])
    return render_template('sentiment_analysis.html', user_id=user.getUserId, user_name=user.getUserName,phone=phone)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username, password)
        userDao = UserDao()

        if userDao.check_login(user):
            user_id = userDao.get_user_id(user)
            session['username'] = username
            session['user_id'] = user_id
            if session['user_id'] == 1:
                return redirect(url_for('sentiment_analysis'))
            else:
                return redirect(url_for('phone'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)