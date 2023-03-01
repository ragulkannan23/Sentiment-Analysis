import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer



text=open('read.txt',encoding='utf-8').read() #take text from a text file
lower_case=text.lower()#make everything lower
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
#maketrans(str1,str2,str3)
#str1:Specifies the list of characters that need to be replaced
#str2:Specifies the list of characters with which the charcters need to be replaced
#str3:Specifies the list of characters that needs to be deleted

tokenized_words=word_tokenize(cleaned_text,"english")


final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word) #removing stop words from sentence

emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line=line.replace("\n",'').replace(",",'').replace("'",'').strip()
        #replace new line,comma,single quote with no string
        word,emotion=clear_line.split(':') # splitting words & emotions from emotions text file
        if word in final_words:
            emotion=emotion.strip()
            emotion_list.append(emotion)#appending the emotions of the sentence to emotions list

w=Counter(emotion_list)#counting the emotions 

def sentiment_analysis(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if(neg>pos):
        print("Negative Sentiment")
    elif(pos>neg):
        print("Postive Sentiment")
    else:
        print("Neutral Vibe")
    
sentiment_analysis(cleaned_text)

fig,ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()#visualizing 