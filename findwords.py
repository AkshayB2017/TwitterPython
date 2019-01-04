import pandas as pd 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
df=pd.read_csv(r"tweet_activity_metrics_TheCoolFanBoi_20181208_20190105_en.csv",encoding="latin-1")

comment_words=' '
stopwords=set(STOPWORDS)

for val in df.Tweet_text:
    val=str(val)
    tokens=val.split()
    for i in range(len(tokens)):
        tokens[i]=tokens[i].lower()
    for words in tokens:
        comment_words=comment_words+words+' '
wordcloud=WordCloud(width=1000,height=1000, background_color='blue', stopwords=stopwords,min_font_size=10).generate(comment_words)

plt.figure(figsize=(10,10),facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
    
