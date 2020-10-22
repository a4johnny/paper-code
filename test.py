import os
import numpy as np
import  pandas as pd
from keras.models import Sequential ,load_model
#keras的接入層(列入特徵)
from keras.layers import Dense, Dropout, Activation, Flatten, LSTM, TimeDistributed, RepeatVector
#標準化層(用線性變換把輸入的東東平移到穩定的均值和標準差)
from keras.layers.normalization import BatchNormalization
#最佳化函式 隨機梯度下降(SGD) > Adam 是它的簡化版(訓練成本低)
from keras.optimizers import Adam
#訪問模型狀態與性能，還能對模型採取行動，中斷、保存、改變模型狀態等
from keras.callbacks import EarlyStopping, ModelCheckpoint
#資料視覺化
import matplotlib.pyplot as plt
#model = Sequential()
path = 'C:\\Users\\a4\\Desktop\\202004.csv'

def readTrain(): #讀資料
    train = pd.read_csv(path, encoding='utf-8') #開記事本 把檔案改成utf-8 另存新檔
    return train

def augFeatures(train): #除了data的feature外 自己增加額外的feature
    #目前沒有使用到(加新的一欄)
    return train

def normalize(train): #資料正規化 統一型態 還有資料壓縮
    train = train.drop(["日期"], axis=1) #把日期那欄丟掉
    train_norm = train.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x))) #正規化 表示成跟平均值差多少(資料壓縮 數值差減少)
    return train_norm

def buildTrain(train, pastDay, futureDay): #位移資料並疊加在一起
    x_train, y_train = [], []
    count = 0;
    for i in range(train.shape[0]-pastDay-futureDay): #資料>shpae[0] 有幾列 #每次從第i筆資料開始
        x_train.append(np.array(train.iloc[i:i+pastDay])) #一次加i到i+pastDay的資料到 全部欄位都用到
        y_train.append(np.array(train.iloc[i+pastDay:i+pastDay+futureDay]["松山機場"])) #只拿其中一欄當作特徵
        count = count+1; #if pastDay=60 futureDay=1 數字代表每個array有幾數值 append到list上(i是list數量)
    return np.array(x_train), np.array(y_train) #list轉成numpy的多維陣列存

def shuffle(X, Y): #打亂資料  #設置的seed值僅一次有效
    np.random.seed() #給系統一個依據產生亂數表 數字相同則能產生相同的亂數表 沒有seed則完全隨機 不設值則依照時間系統自己選值
    randomList = np.arange(X.shape[0]) #照shape長度產生一個陣列 從0開始間隔1  多載(a,b,c) a開始數字 b上限 c增加的級距
    np.random.shuffle(randomList) #打亂順序
    return X[randomList], Y[randomList]

def splitData(X, Y, rate): #分成訓練集和測試集(有shuffle)
    #x = train[0:77] #rate決定用多少資料當測試集
    X_train = X[int(X.shape[0]*rate):] #從int(X.shape[0]*rate)後開始取都當成訓練集
    Y_train = Y[int(Y.shape[0]*rate):]
    X_val = X[:int(X.shape[0]*rate)] #從0開始取 取int(X.shape[0]*rate)當測試集
    Y_val = Y[:int(Y.shape[0]*rate)]
    return  X_train, Y_train, X_val, Y_val

def buildLstmManyToOne(shape):
    model = Sequential()  #順序模型指引 要用怎樣子的模型 #add加層
    model.add(LSTM(10, input_length=shape[1], input_dim=shape[2], return_sequences=True)) #循環層
    model.add(Dense(1)) #dense 全連接層(隱藏層)
    model.compile(loss="mean_squared_error", optimizer="adam")
    model.summary()
    return model

if __name__ == '__main__':
    train = readTrain()
    train_norm = normalize(train)
    x_train, y_train = buildTrain(train_norm, 60, 1)
    x_train, y_train = shuffle(x_train, y_train)
    x_train, y_train, x_val, y_val = splitData(x_train, y_train, 0.1)
    print(x_train.shape, y_train.shape, x_val.shape, y_val.shape)
    #print(x_train.shape[1]) #列出矩陣大小 shape[0] (77, 1)

    model = buildLstmManyToOne(x_train.shape) #定義model
    callback = EarlyStopping(monitor="loss", patience=10, verbose=1, mode="auto")  #避免過擬合
    history = model.fit(x_train, y_train, epochs=1000, batch_size=128, validation_data=(x_val, y_val), callbacks=[callback]) #訓練
    predict = model.predict(x_val) #預測
    print(history.history)