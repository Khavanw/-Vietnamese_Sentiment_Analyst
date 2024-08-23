import pandas as pd
import string
import re
from pyvi import ViTokenizer

def remove_punctuation(comment):
  # Tạo ra một bảng dịch
  translator = str.maketrans('', '', string.punctuation)
  # Xóa dấu câu trong chuỗi
  new_string = comment.translate(translator)
  # Xóa khoảng trắng thừa và dấu ngắt
  new_string = re.sub('[\n ]+', ' ', new_string)
  # Remove emoji icon
  emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                           "]+", flags=re.UNICODE)
  new_string = re.sub(emoji_pattern, '', new_string)

  return new_string

def read_filestopwords():
    with open('G:\\VietNamese-Sentiment-Analyst\\data\\data_stopword\\vietnamese-stopwords.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = [line.split('\n')[0] for line in lines]
    return words

def remove_stopword(comment):
  stop_words = read_filestopwords()
  filtered = [word for word in comment.split() if word not in stop_words]
  return ' '.join(filtered)

def remove_repeated_words(text):
    words = text.split()
    new_words = []
    for i in range(len(words)):
        if i == 0 or words[i] != words[i-1]:
            new_words.append(words[i])
    return ' '.join(new_words)
