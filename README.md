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
Using dataset UIT-ViSFD preprcessing in file notebook:
```train\data_preprocessing.ipynb```

### Installing VnCoreNLP

Install the python bindings:

```$pip3 install  vncorenlp```

Clone the VNCoreNLP repo: https://github.com/vncorenlp/VnCoreNLP

### Downloading PhoBERT 

Follow the instructions in the original repo:

PhoBERT-base:

```
$wget https://public.vinai.io/PhoBERT_base_transformers.tar.gz
$tar -xzvf PhoBERT_base_transformers.tar.gz
```
## Experiments
The training/test loss curves for each experiment are shown below:
- CNN + BiLSTM:
  
  ![image](https://github.com/user-attachments/assets/098f7be9-c740-4b27-a074-15e14bf2b92c)
- PhoBERT Fine-tuning: The model achieved excellent results in fold 0 within the first 20 epochs
  - UC (Area Under the Curve): An AUC score close to 1 indicates that the model has a very good ability to distinguish between classes.
  - F1 Score: The F1 score reflects the balance between precision and recall. A score of 0.7773 is a good result.

## Result Classification report and confussion matrix
- CNN + BiLSTM:

![image](https://github.com/user-attachments/assets/b0c19fd4-d060-4e52-940a-e122d0fd8560)

- PhoBERT Fine-tuning:

![image](https://github.com/user-attachments/assets/5ef00bf4-2c82-4773-a6be-86974b9eb08e)



  
