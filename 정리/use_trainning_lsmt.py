import tensorflow as tf
tf.config.experimental.list_physical_devices('GPU')
from tensorflow.python.keras.models import Sequential

from tensorflow.keras.layers import Dense, SimpleRNN, Embedding, LSTM, Concatenate
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer

import pickle

def train_model():
    print("???asdasd")

    # encoding은 보통 utf-8, cp949 로 하면되지만 이번 파일은 latin1
    data = pd.read_csv('1.3만_워크맨_m8JrVquHNsY.csv', header = None, names = ['review','date','like'])
    data2 = pd.read_csv('1.6만_워크맨_UQYCWLrCUy4.csv', header = None, names = ['review','date','like'])
    data3 = pd.read_csv('2.4만_워크맨_BWROdI-AgAU.csv', header = None, names = ['review','date','like'])

    data_all = pd.concat([data,data2,data3])

    Mean = data_all['like'].mean()
    print(Mean)

    data_all.loc[data_all["like"] < Mean, "like"] = 0
    data_all.loc[data_all["like"] >= Mean, "like"] = 1

    data_all['review'] = data_all['review'].str.replace("[^\w]", " ")
    data_all['review'] = data_all['review'].str.replace("[0-9]", "")
    data_all['review'] = data_all['review'].str.replace("[a-z]", "")
    data_all['review'] = data_all['review'].str.replace("[A-Z]", "")
    data_all['review'] = data_all['review'].str.strip()
    data_all['review'] = data_all['review'].replace('', np.nan)
    data_all = data_all.dropna(how='any')

    data_all['date'] = data_all['date'].str.replace("[^\w]", " ")
    data_all['date'] = data_all['date'].str.replace("전", "")
    data_all['date'] = data_all['date'].str.replace("개", "")
    data_all['date'] = data_all['date'].str.strip()

    review_train, review_test,date_train, date_test, y_train, y_test = train_test_split(data_all['review'],data_all['date'], data_all['like'], test_size=0.2, shuffle=False)

    print("2")

    stopwords = ['이', '가', '을', '를','은','는','에','의','도']

    cnt = 0
    X_train = []
    for stc in review_train:
        words = Okt().morphs(stc)
        token = []
        for word in words:
            if word not in stopwords:
                token.append(word)
        X_train.append(token)
        
    X_test = []
    for stc in review_test:
        words = Okt().morphs(stc)
        token = []
        for word in words:
            if word not in stopwords:
                token.append(word)
        X_test.append(token)    

        
    X_train_2 = []
    for stc in date_train:
        X_train_2.append(stc.split())
        
    X_test_2 = []
    for stc in date_test:
        X_test_2.append(stc.split())
        
    print(len(X_train))
    print(len(X_test))
    print(len(X_train_2))
    print(len(X_test_2))

    for i in range(len(X_train)):
        X_train[i]+=X_train_2[i]
    for i in range(len(X_test)):
        X_test[i]+=X_test_2[i]

    # X_train 단어들을 토대로 정수 인덱스 설정
    # 빈도수가 높은 것부터 4000개만 정수 인덱스로 변환하겠다!
    tokenizer = Tokenizer(4000)
    tokenizer.fit_on_texts(X_train)

    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # 위에서 설정된 정수 인덱스를 토대로 변환
    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)


    print('# int_encoding done')



    max_len = 40
    X_train = pad_sequences(X_train, maxlen=max_len)
    X_test = pad_sequences(X_test, maxlen=max_len)
    # X_train_2 = pad_sequences(X_train_2, maxlen=2)
    # X_test_2 = pad_sequences(X_test_2, maxlen=2)

    model = Sequential()
    model.add(Embedding(4000, 32))
    model.add(LSTM(32))
    model.add(Dense(1, activation='sigmoid'))

    # 혹시 5회 이상 검증데이터 loss가 증가하면, 과적합될 수 있으므로 학습을 조기종료!
    early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=5)
    # 훈련을 거듭하면서, 가장 검증데이터 정확도가 높았던 순간을 체크포인트로 저장
    model_check = ModelCheckpoint('the_best.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)

    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['acc'])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10)

    # 정확도 측정
    print(model.evaluate(X_test, y_test))

    model.save('saved_model/my_model') 
    model.save('my_model.h5') 

    print("문장과 날짜를 입력하세요")
    sentence = input()
    date = input()

    # 토큰화
    sentence = sentence.replace("[^\w]", " ")
    sentence = sentence.replace("[0-9]", "")
    sentence = sentence.replace("[a-z]", "")
    sentence = sentence.replace("[A-Z]", "")
    sentence = sentence.strip()

    date = date.replace("[^\w]", " ")
    date = date.replace("전", "")
    date = date.replace("개", "")
    date = date.strip()

    sentence+=date

    words = Okt().morphs(sentence)

    words_re = []
    for word in words:
        if word not in stopwords:
            words_re.append(word)

    encode_stc = tokenizer.texts_to_sequences([words_re])

    pad_stc = pad_sequences(encode_stc, maxlen = 40)
    print(pad_stc)
    print(model.predict(pad_stc))

def use_model(sentence, date):

    model = tf.keras.models.load_model('saved_model/my_model')
    print("문장과 날짜를 입력하세요")
    

    # 토큰화
    sentence = sentence.replace("[^\w]", " ")
    sentence = sentence.replace("[0-9]", "")
    sentence = sentence.replace("[a-z]", "")
    sentence = sentence.replace("[A-Z]", "")
    sentence = sentence.strip()

    date = date.replace("[^\w]", " ")
    date = date.replace("전", "")
    date = date.replace("개", "")
    date = date.strip()

    sentence+=date

    stopwords = ['이', '가', '을', '를','은','는','에','의','도']

    words = Okt().morphs(sentence)

    words_re = []
    for word in words:
        if word not in stopwords:
            words_re.append(word)

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    encode_stc = tokenizer.texts_to_sequences([words_re])

    pad_stc = pad_sequences(encode_stc, maxlen = 40)
    print(pad_stc)
    print(model.predict(pad_stc))