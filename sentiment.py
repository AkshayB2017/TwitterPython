import pandas as pd 
from textblob import TextBlob
df=pd.read_csv(r"tweet_activity_metrics_TheCoolFanBoi_20181208_20190105_en.csv",encoding="latin-1")

#comment_words=' '
#stopwords=set(STOPWORDS)
print('Sentiments                Polarity')
for val in df.Tweet_text:
    sentiments=TextBox(val)
    print(sentiments.sentiment)
    print('   ')
    print(sentiments.polarity)

    
    
