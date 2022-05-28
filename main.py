# With Python 3.9.7

from fastapi import FastAPI 
import uvicorn 
import pickle 
import numpy as np 
import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import texthero as hero 
from texthero import stopwords
# # Save le model : 
# model = ...  # Get model (Sequential, Functional Model, or Model subclass)
# model.save('path/to/location')

# # Load model 
# model = keras.models.load_model('model89')

app = FastAPI()

def preprocessing_pred(sentence):
    texte = np.array([sentence])
    df_pred = pd.DataFrame(texte)
    df_pred.columns = ['Texte']

    default_stopwords = stopwords.DEFAULT
    custom_stopwords = default_stopwords.union(set(["feel",'aa','ab','http','anything','less','ever',"im",'href','actualy','enough','actually','look','come','sure','many','I','got','able','year','help','take','feels','felt','like','lot','go','around','makes','back','work','need','pretty','way','though','see','ive','good','also','right','dont','cant','say','didnt','could','even','day','every','make','made','much','going','one',"feeling",'things','something',"feelings",'always','never','today','days','life',"like","really",'know','time','get','little','bit','would','want','think','people','still']))
    texte = hero.remove_urls(df_pred.Texte)
    texte = hero.remove_stopwords(texte, custom_stopwords)
    texte = hero.remove_punctuation(texte)
    texte = hero.remove_digits(texte)
    texte = hero.remove_urls(texte)

    # loading tokenizer
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Text to sequences 
    df_pred['processed'] = tokenizer.texts_to_sequences(df_pred.Texte)

    max_length = 30
    pad_sentences = pad_sequences(df_pred.processed, maxlen=max_length,padding='post')

    model = keras.models.load_model('model89.h5')
    result = np.argmax(model.predict(np.array(pad_sentences)))

    if result == 0 :
        return 'sadness'
    elif result == 1 :
        return 'anger'
    elif result == 2 :
        return 'love'
    elif result == 3 :
        return 'surprise' 
    elif result == 4 :
        return 'fear'
    elif result == 5 :
        return 'happy'
    else:
        return 'error'

@app.post("/predict/")
async def prediction_lgbm(data : str):
    return await preprocessing_pred(data)

@app.get("/")
def pred():
    return {'NLP-predict-emotions' : "/predict/"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=6705, log_level="info", reload=True)

