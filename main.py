import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
text = """
A purple octopus wearing a top hat strolled through the bustling marketplace, humming a tune that sounded suspiciously like a mix of jazz and whale songs. Nearby, a group of toaster-like robots were arguing over the best way to butter toast, while a llama on roller skates zoomed past, shouting something about pineapple pizza being the ultimate truth. In the corner of the market, a wizard was selling enchanted cheese graters that could supposedly predict the weather, but only if you asked them nicely. Meanwhile, the clouds above decided to rain tiny marshmallows, which everyone agreed was both delightful and extremely inconvenient.
"""
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
#k-statements
tks = 2
smry = " ".join(rnk[:tks])
print("Summary:")
print(smry)
