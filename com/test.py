import os
import re
import io
import string
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
import multidict as multidict


# first
text='zkmzone'
x,y=np.ogrid[:600,:600]

mask=(x-300)**2 +(y-300)**2>250**2
mask=255*mask.astype(int)

wc=WordCloud(background_color='white',repeat=True,mask=mask)
wc.generate(text)
wc.to_file('zkmzone.png')

plt.axis('off')
plt.imshow(wc,interpolation='bilinear')
plt.show()


# second
# d=path.dirname(__file__) if '__file__' in locals() else os.getcwd()
#
# text=open(path.join(d,'text.txt')).read()
#
# wc=WordCloud().generate(text)
# wc.to_file('text.png')



# third
# d=path.dirname(__file__) if '__file__' in locals() else os.getcwd()
# text=open(path.join(d,'text.txt')).read()
#
# alice=np.array(Image.open(path.join(d,'cc.png')))
#
# stopwords=set(STOPWORDS)
# stopwords.add('said')
#
# wc=WordCloud(background_color='white',max_words=2000,mask=alice,stopwords=stopwords,contour_width=3,contour_color='steelblue')
# wc.generate(text)
# wc.to_file(path.join(d,'bc.png'))


# fourth

# def getFrequencyDictForText(sentence):
#     fullTermsDict=multidict.MultiDict()
#     tmpDict={}
#
#     for text in sentence.split(" "):
#         if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be",text):
#             continue
#         val=tmpDict.get(text,0)
#         tmpDict[text.lower()]=val+1
#
#     for key in tmpDict:
#         fullTermsDict.add(key,tmpDict[key])
#     return fullTermsDict
#
# def makeImage(text):
#     alice=np.array(Image.open('cc.png'))
#
#     wc=WordCloud(background_color='white',max_words=1000,mask=alice)
#     wc.generate_from_frequencies(text)
#
#     plt.imshow(wc,interpolation='bilinear')
#     plt.axis('off')
#     plt.show()
#
# d=path.dirname(__file__) if '__file__' in locals() else os.getcwd()
# text=open(path.join(d,'text.txt'),encoding='utf-8')
# text=text.read()
# makeImage(getFrequencyDictForText(text))


# fifth
# d=path.dirname(__file__) if '__file__' in locals() else os.getcwd()
#
# text=open(path.join(d,'text.txt')).read()
#
# alice_coloring=np.array(Image.open(path.join(d,'mm.png')))
# stopwords=set(STOPWORDS)
# stopwords.add('said')
#
# wc=WordCloud(background_color='white',max_words=2000,mask=alice_coloring,stopwords=stopwords,max_font_size=40,random_state=42)
# wc.generate(text)
# wc.to_file('mc.png')
# image_colors=ImageColorGenerator(alice_coloring)


# sixth

# d=path.dirname(__file__) if '__file__' in locals() else os.getcwd()
#
# text=io.open(path.join(d,'happy-emoji.txt')).read()
#
# normal_word=r"(?:\w[\w']+)"
# ascii_art=r"(?:[{punctuation}][{punctuation}]+)".format(punctuation=string.punctuation)
# emoji=r"(?:[^\s])(?<![\w{ascii_printable}])".format(ascii_printable=string.printable)
#
# regexp=r"{normal_word}|{ascii_art}|{emoji}".format(normal_word=normal_word,ascii_art=ascii_art,emoji=emoji)
#
# # font_path=path.join(d,'fonts','Symbola','Symbola.ttf')
# wc=WordCloud(regexp=regexp)
# wc.generate(text)
# wc.to_file('happy.png')
#
# plt.imshow(wc)
# plt.axis('off')
# plt.show()


# seventh

















