# [PhoBERT Fine-tuning] Vietnamese_Sentiment_Analyst

## Overview
In today's digital age, the amount of textual data generated and shared on digital platforms is increasing exponentially. From social media comments, product reviews, to customer feedback, text has become a valuable source of information about human emotions and opinions. However, understanding and analyzing emotions within this massive amount of textual data manually is not feasible.

Sentiment analysis is a task in natural language processing (NLP) that aims to determine the attitude or emotion of the writer towards a specific topic. This project focuses on sentiment analysis for Vietnamese text.

This project performs sentiment analysis on Vietnamese text using two main approaches:

1. A model combining CNN and BiLSTM
2. Fine-tuning the PhoBERT model

## Method
### CNN + BiLSTM
This model combines Convolutional Neural Network (CNN) and Bidirectional Long Short-Term Memory (BiLSTM) to learn features from textual data and classify sentiments.

### PhoBERT Fine-tuning
We use the best model from the AIViVN's competition by [Khoi Nguyen](https://github.com/suicao). The model scored 0.90849 on the public leaderboard

### Model architecture
Here we created a custom classification head on top of the BERT backbone. We concatenated the last 4 hidden representations of the ```[CLS]``` token, which is actually ```<s>``` in this case, and fed it to a simple MLP.

![](https://i.imgur.com/1bYD5dq.png)
## Dataset
### UIT-ViSFD
Dowload dataset from https://github.com/LuongPhan/UIT-ViSFD/blob/main/UIT-ViSFD.zip

### Data Information
- Train: 7,786.
- Dev: 1,112.
- Test: 2,224.

## Setup model traning
### Data preprocessing
Using dataset UIT-ViSFD run:
```$python crash2csv.py```

