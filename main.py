import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from flask import Flask,request, jsonify

def summarize(text):
    sntc = nltk.sent_tokenize(text)
    vctrzr = TfidfVectorizer()
    tfidf = vctrzr.fit_transform(sntc)
    avgv = np.mean(tfidf.toarray(), axis=0)
    sim = []
    for i in range(len(sntc)):
        sentence_vector = tfidf[i].toarray().flatten()
        similarity = cosine_similarity([sentence_vector], [avgv])[0][0]
        sim.append(similarity)
    rnk = [sentence for _, sentence in sorted(zip(sim, sntc), reverse=True)]
    tks = 2
    smry = " ".join(rnk[:tks])

    return smry



text=""""""
app=Flask(__name__)

@app.route("/api/summary", methods=['POST'])
def get():
    requestData=request.get_json()
    text=requestData['text']
    return summarize(text)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
