import numpy as np   
import pandas as pd #tratamiento de datos
import joblib
import os
import re
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
# NLTK Stop words
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('spanish')
import spacy
nlp = spacy.load('es_core_news_sm')
# Show top n keywords for each topic

stop_words_exceptions=["no"]



#Machine Learning Models
lda_model=joblib.load(os.getcwd()+'/../modelo_entrenado.pkl')
vectorizer = joblib.load(os.getcwd()+'/../modelo_vectorizer.pkl')


def show_topics(vectorizer, lda_model, n_words):
    keywords = np.array(vectorizer.get_feature_names())
    topic_keywords = []
    for topic_weights in lda_model.components_:
        top_keyword_locs = (-topic_weights).argsort()[:n_words]
        topic_keywords.append(keywords.take(top_keyword_locs))
    return topic_keywords


def topic_keywords(vectorizer, lda_model ):
    topic_keywords = show_topics(vectorizer=vectorizer, lda_model=lda_model, n_words=20)        

    # Topic - Keywords Dataframe
    df_topic_keywords = pd.DataFrame(topic_keywords)
    df_topic_keywords.columns = ['Word '+str(i) for i in range(df_topic_keywords.shape[1])]
    df_topic_keywords.index = ['Topic '+str(i) for i in range(df_topic_keywords.shape[0])]
    return df_topic_keywords


df_topic_keywords=topic_keywords(vectorizer,lda_model)



def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc= True))  # deacc=True removes punctuations


def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if (word not in stop_words) or (word in stop_words_exceptions)] for doc in texts]
    
def bigram_model(data_tokenized):
    bigram = gensim.models.Phrases(data_tokenized, min_count=7, threshold=5) 
    bigram_mod= gensim.models.phrases.Phraser(bigram)
    return bigram_mod


def make_bigrams(texts, data_tokenized):
    bigram_mod=bigram_model(data_tokenized)
    return [bigram_mod[doc] for doc in texts]



def prepared_data(data_bigrams_nonstops):
    data = data_bigrams_nonstops

    data_prepared=[]
    for row in data:
        text=""
        for word in row:
            if(len(word) > 3):
                text+=word + " "
        data_prepared.append(text.rstrip())
    return data_prepared

def lemmatization_process(data_prepared):
    allowed_postags=['ADJ', 'VERB', 'ADV']
    stopwordsToken=["demas","tener","mismo", "poder","cada","tambien", "hacer"]
    unifiedWord={"respetar":"respeto", "violencia":"no_violencia","musicar":"musica","guerra":"no_guerra"}
    data_list=[]

    token_list=""
    text=nlp(data_prepared[0])
    for token in text:
        if (token.pos_ in allowed_postags) and (token.lemma_ not in stopwordsToken) and (token.text not in stopwordsToken):
            if token.lemma_ in unifiedWord:
                token_list+=unifiedWord[token.lemma_]+" "
            else :
                token_list+=token.lemma_+" "

        elif (token.is_stop is not True) and (token.lemma_ not in stopwordsToken) and (token.text not in stopwordsToken):
            if token.text in unifiedWord:
                token_list+=unifiedWord[token.text]+" "
            else :
                token_list+=token.text+" "
    data_list.append(token_list.rstrip())
    return data_list





def clean_text(text):
    text= re.sub('[,\.\'\"!\)(?0-9]', '', text).lower().strip()
    data = [text]
    data_tokenized = list(sent_to_words(data)) 
    data_tokenized_nostops= remove_stopwords(data_tokenized)
    data_bigrams_nonstops=make_bigrams(data_tokenized_nostops,data_tokenized)
    data_prepared=prepared_data(data_bigrams_nonstops)
    data_list=lemmatization_process(data_prepared)
    return data_list


def obtain_topics(data_list):
    text_processed=vectorizer.transform(data_list)
    topic_probability_scores = lda_model.transform(text_processed)
    listAct=np.argsort(topic_probability_scores)[0].tolist()
    #obtengo los dos topicos con mayor probabilidad
    firstTopic=listAct.pop()
    secondTopic=listAct.pop()
    #obtengo las palabras mas representativas de los dos topicos
    topic1 = df_topic_keywords.iloc[firstTopic, :].values.tolist()
    topic2 = df_topic_keywords.iloc[secondTopic, :].values.tolist()
    topic1String=', '.join(topic1)
    topic2String=', '.join(topic2)
    topic_list=[]
    topic_list.append(topic1String)
    topic_list.append(topic2String)
    return topic_list
