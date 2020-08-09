import os
import numpy as np
from utils import read_wordvec

if not os.path.exists('wiki.en.align.vec'):
    os.system('wget https://s3.amazonaws.com/aligned-en-zh-wordvec/wiki.en.align.vec')
if not os.path.exists('wiki.zh.align.vec'):
    os.system('wget https://s3.amazonaws.com/aligned-en-zh-wordvec/wiki.zh.align.vec')
    
en_words, en_vectors, en_word2id = read_wordvec('wiki.en.align.vec')
zh_words, zh_vectors, zh_word2id = read_wordvec('wiki.zh.align.vec')

# Find the closest words to 'cat' in Chinese 
scores = zh_vectors.dot(en_vectors[en_word2id['cat']])
for idx in np.argsort(-scores)[0:5]:
    print('%s: %.4f' % (zh_words[idx], scores[idx]))


scores = en_vectors.dot(zh_vectors[zh_word2id['猫']])
for idx in np.argsort(-scores)[0:10]:
    print('%s: %.4f' % (en_words[idx], scores[idx]))