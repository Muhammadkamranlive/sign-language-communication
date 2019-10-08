#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import files
files.upload()


# In[ ]:


get_ipython().system('unzip signdata.zip')


# In[ ]:





# In[ ]:


from __future__ import absolute_import, division, print_function

# Import TensorFlow >= 1.10 and enable eager execution
import tensorflow as tf

tf.enable_eager_execution()

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import unicodedata
import re
import numpy as np
import os
import time

print(tf.__version__)


# In[ ]:


import pandas as pd
train=pd.read_csv('/content/signdata/PHOENIX-2014-T.train.corpus.csv',sep='|')
test=pd.read_csv('/content/signdata/PHOENIX-2014-T.test.corpus.csv',sep='|')
dev=pd.read_csv('/content/signdata/PHOENIX-2014-T.dev.corpus.csv',sep='|')
dev.columns


# In[ ]:


train.sample(10)


# In[ ]:


gertrain=train['translation'].tolist()
glosstrain=train['orth'].tolist()

gertest=test['translation'].tolist()
glosstest=test['orth'].tolist()

gerdev=dev['translation'].tolist()
glossdev=dev['orth'].tolist()


# In[ ]:


#data.head()


# In[ ]:


#len(german[1])


# In[ ]:


german=[]
gloss=[]
for i in range(len(gertrain)):
  german.append(gertrain[i])
  gloss.append(glosstrain[i])

for i in range(len(gertest)):
  german.append(gertest[i])
  gloss.append(glosstest[i])

for i in range(len(gerdev)):
  german.append(gerdev[i])
  gloss.append(glossdev[i])


# In[ ]:


len(gertrain)+len(gertest)+len(gerdev)


# In[ ]:


len(german)


# In[ ]:


original_word_pairs=[[gloss[i],german[i]] for i in range(len(gloss))]

data = pd.DataFrame(original_word_pairs, columns=["eng", "es"])


# In[ ]:


data.sample(10)


# In[ ]:


data.shape


# In[ ]:


# Converts the unicode file to ascii
def unicode_to_ascii(s):
    """
    Normalizes latin chars with accent to their canonical decomposition
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')

def preprocess_sentence(w):
    w = unicode_to_ascii(w.lower().strip())
    
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ." 
    # Reference:- https://stackoverflow.com/questions/3645931/python-padding-punctuation-with-white-spaces-keeping-punctuation
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w)
    
    w = w.rstrip().strip()
    
    # adding a start and an end token to the sentence
    # so that the model know when to start and stop predicting.
    w = '<start> ' + w + ' <end>'
    return w


# In[ ]:


# Now we do the preprocessing using pandas and lambdas
data["eng"] = data.eng.apply(lambda w: preprocess_sentence(w))
data["es"] = data.es.apply(lambda w: preprocess_sentence(w))
data.sample(10)


# In[ ]:


data.columns
testgerman=data['eng'].tolist()
testgloss=data['es'].tolist()


# In[ ]:


len(testgerman)


# In[ ]:


# This class creates a word -> index mapping (e.g,. "dad" -> 5) and vice-versa 
# (e.g., 5 -> "dad") for each language,
class LanguageIndex():
    def __init__(self, lang):
        """ lang are the list of phrases from each language"""
        self.lang = lang
        self.word2idx = {}
        self.idx2word = {}
        self.vocab = set()
        
        self.create_index()
        
    def create_index(self):
        for phrase in self.lang:
            # update with individual tokens
            self.vocab.update(phrase.split(' '))
            
        # sort the vocab
        self.vocab = sorted(self.vocab)

        # add a padding token with index 0
        self.word2idx['<pad>'] = 0
        
        # word to index mapping
        for index, word in enumerate(self.vocab):
            self.word2idx[word] = index + 1 # +1 because of pad token
        
        # index to word mapping
        for word, index in self.word2idx.items():
            self.idx2word[index] = word        


# In[ ]:


# index language using the class above
inp_lang = LanguageIndex(data["es"].values.tolist())
targ_lang = LanguageIndex(data["eng"].values.tolist())
# Vectorize the input and target languages
input_tensor = [[inp_lang.word2idx[s] for s in es.split(' ')]  for es in data["es"].values.tolist()]
target_tensor = [[targ_lang.word2idx[s] for s in eng.split(' ')]  for eng in data["eng"].values.tolist()]
input_tensor[:10]


# In[ ]:


target_tensor[:10]


# In[ ]:


def max_length(tensor):
    return max(len(t) for t in tensor)


# In[ ]:


# calculate the max_length of input and output tensor
max_length_inp, max_length_tar = max_length(input_tensor), max_length(target_tensor)


# In[ ]:


print(max_length_inp, max_length_tar)


# In[ ]:


def pad_sequences(x, max_len):
    padded = np.zeros((max_len), dtype=np.int64)
    if len(x) > max_len: padded[:] = x[:max_len]
    else: padded[:len(x)] = x
    return padded


# In[ ]:


# inplace padding
input_tensor = [pad_sequences(x, max_length_inp) for x in input_tensor]
target_tensor = [pad_sequences(x, max_length_tar) for x in target_tensor]
len(target_tensor)


# In[ ]:


len(gertrain)


# In[ ]:


len(gertest)+len(gertrain)


# In[ ]:


#len(input_tensor)
input_tensor_train=input_tensor[0:len(gertrain)]
input_tensor_val=input_tensor[len(gertest)+len(gertrain):len(gertrain)+len(gertest)+len(gerdev)]
target_tensor_train=target_tensor[0:len(gertrain)]
target_tensor_val=target_tensor[len(gertest)+len(gertrain) : len(gertrain)+len(gertest)+len(gerdev)]


# In[ ]:


# Creating training and validation sets using an 80-20 split
#input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor, target_tensor, test_size=0.2)

# Show length
len(input_tensor_train), len(target_tensor_train), len(input_tensor_val), len(target_tensor_val)


# In[ ]:


BUFFER_SIZE = len(input_tensor_train)
BATCH_SIZE = 64
N_BATCH = BUFFER_SIZE//BATCH_SIZE
embedding_dim = 256
units = 1024
vocab_inp_size = len(inp_lang.word2idx)
vocab_tar_size = len(targ_lang.word2idx)

dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train, target_tensor_train)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)


# In[ ]:


vocab_inp_size


# In[ ]:


vocab_tar_size


# In[ ]:


def gru(units):
  # If you have a GPU, we recommend using CuDNNGRU(provides a 3x speedup than GRU)
  # the code automatically does that.
  if tf.test.is_gpu_available():
    return tf.keras.layers.CuDNNGRU(units, 
                                    return_sequences=True, 
                                    return_state=True, 
                                    recurrent_initializer='glorot_uniform')
  else:
    return tf.keras.layers.GRU(units, 
                               return_sequences=True, 
                               return_state=True, 
                               recurrent_activation='sigmoid', 
                               recurrent_initializer='glorot_uniform')


# In[ ]:


class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, batch_sz):
        super(Encoder, self).__init__()
        self.batch_sz = batch_sz
        self.enc_units = enc_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = gru(self.enc_units)
        
    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state = hidden)        
        return output, state
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.enc_units))


# In[ ]:


class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, batch_sz):
        super(Decoder, self).__init__()
        self.batch_sz = batch_sz
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = gru(self.dec_units)
        self.fc = tf.keras.layers.Dense(vocab_size)
        
        # used for attention
        self.W1 = tf.keras.layers.Dense(self.dec_units)
        self.W2 = tf.keras.layers.Dense(self.dec_units)
        self.V = tf.keras.layers.Dense(1)
        
    def call(self, x, hidden, enc_output):
        # enc_output shape == (batch_size, max_length, hidden_size)
        
        # hidden shape == (batch_size, hidden size)
        # hidden_with_time_axis shape == (batch_size, 1, hidden size)
        # we are doing this to perform addition to calculate the score
        hidden_with_time_axis = tf.expand_dims(hidden, 1)
        
        # score shape == (batch_size, max_length, 1)
        # we get 1 at the last axis because we are applying tanh(FC(EO) + FC(H)) to self.V
        score = self.V(tf.nn.tanh(self.W1(enc_output) + self.W2(hidden_with_time_axis)))
        
        # attention_weights shape == (batch_size, max_length, 1)
        attention_weights = tf.nn.softmax(score, axis=1)
        
        # context_vector shape after sum == (batch_size, hidden_size)
        context_vector = attention_weights * enc_output
        context_vector = tf.reduce_sum(context_vector, axis=1)
        
        # x shape after passing through embedding == (batch_size, 1, embedding_dim)
        x = self.embedding(x)
        
        # x shape after concatenation == (batch_size, 1, embedding_dim + hidden_size)
        x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1)
        
        # passing the concatenated vector to the GRU
        output, state = self.gru(x)
        
        # output shape == (batch_size * 1, hidden_size)
        output = tf.reshape(output, (-1, output.shape[2]))
        
        # output shape == (batch_size * 1, vocab)
        x = self.fc(output)
        
        return x, state, attention_weights
        
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.dec_units))


# In[ ]:


encoder = Encoder(vocab_inp_size, embedding_dim, units, BATCH_SIZE)
decoder = Decoder(vocab_tar_size, embedding_dim, units, BATCH_SIZE)


# In[ ]:


optimizer = tf.train.AdamOptimizer()


def loss_function(real, pred):
  mask = 1 - np.equal(real, 0)
  loss_ = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=real, logits=pred) * mask
  return tf.reduce_mean(loss_)


# In[ ]:


checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                 encoder=encoder,
                                 decoder=decoder)


# In[ ]:


loss=[]
EPOCHS = 100

for epoch in range(EPOCHS):
    start = time.time()
    
    hidden = encoder.initialize_hidden_state()
    total_loss = 0
    
    for (batch, (inp, targ)) in enumerate(dataset):
        loss = 0
        
        with tf.GradientTape() as tape:
            enc_output, enc_hidden = encoder(inp, hidden)
            
            dec_hidden = enc_hidden
            
            dec_input = tf.expand_dims([targ_lang.word2idx['<start>']] * BATCH_SIZE, 1)       
            
            # Teacher forcing - feeding the target as the next input
            for t in range(1, targ.shape[1]):
                # passing enc_output to the decoder
                predictions, dec_hidden, _ = decoder(dec_input, dec_hidden, enc_output)
                
                loss += loss_function(targ[:, t], predictions)
                
                # using teacher forcing
                dec_input = tf.expand_dims(targ[:, t], 1)
        
        batch_loss = (loss / int(targ.shape[1]))
        
        total_loss += batch_loss
        
        variables = encoder.variables + decoder.variables
        
        gradients = tape.gradient(loss, variables)
        
        optimizer.apply_gradients(zip(gradients, variables))
        
        if batch % 100 == 0:
            print('Epoch {} Batch {} Loss {:.4f}'.format(epoch + 1,
                                                         batch,
                                                         batch_loss.numpy()))
    # saving (checkpoint) the model every 2 epochs
    if (epoch + 1) % 2 == 0:
      checkpoint.save(file_prefix = checkpoint_prefix)
    
    print('Epoch {} Loss {:.4f}'.format(epoch + 1,
                                        total_loss / N_BATCH))
    #loss.append([total_loss / N_BATCH])
    print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))


# In[ ]:


def evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    attention_plot = np.zeros((max_length_targ, max_length_inp))
    
    sentence = preprocess_sentence(sentence)

    inputs = [inp_lang.word2idx[i] for i in sentence.split(' ')]
    inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs], maxlen=max_length_inp, padding='post')
    inputs = tf.convert_to_tensor(inputs)
    
    result = ''

    hidden = [tf.zeros((1, units))]
    enc_out, enc_hidden = encoder(inputs, hidden)

    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([targ_lang.word2idx['<start>']], 0)

    for t in range(max_length_targ):
        predictions, dec_hidden, attention_weights = decoder(dec_input, dec_hidden, enc_out)
        
        # storing the attention weights to plot later on
        attention_weights = tf.reshape(attention_weights, (-1, ))
        attention_plot[t] = attention_weights.numpy()

        predicted_id = tf.argmax(predictions[0]).numpy()

        result += targ_lang.idx2word[predicted_id] + ' '

        if targ_lang.idx2word[predicted_id] == '<end>':
            return result, sentence, attention_plot
        
        # the predicted ID is fed back into the model
        dec_input = tf.expand_dims([predicted_id], 0)

    return result, sentence, attention_plot


# In[ ]:


# function for plotting the attention weights
def plot_attention(attention, sentence, predicted_sentence):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(attention, cmap='viridis')
    
    fontdict = {'fontsize': 14}
    
    ax.set_xticklabels([''] + sentence, fontdict=fontdict, rotation=90)
    ax.set_yticklabels([''] + predicted_sentence, fontdict=fontdict)

    plt.show()


# In[ ]:


def translate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    result, sentence, attention_plot = evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
        
    #print('Input: {}'.format(sentence))
    #print('Predicted translation: {}'.format(result))
    
    #attention_plot = attention_plot[:len(result.split(' ')), :len(sentence.split(' '))]
    #plot_attention(attention_plot, sentence.split(' '), result.split(' '))
    return(result)


# In[ ]:


# restoring the latest checkpoint in checkpoint_dir
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))


# In[ ]:


te=pd.read_csv('/content/signdata/PHOENIX-2014-T.test.corpus.csv',sep='|')
ge=te['translation'].tolist()
go=te['orth'].tolist()


# In[ ]:


len(go)


# In[ ]:


#ger[1]


# In[ ]:


from nltk.translate.bleu_score import sentence_bleu


# In[ ]:


pred=[]
bleu=[]
no=[]


# In[ ]:


pred=[]
bleu1=[]
bleu2=[]
bleu3=[]
bleu4=[]
no=[]


# In[ ]:


import csv


# In[ ]:


len(train)
len(test)


# In[ ]:


from nltk.translate.bleu_score import sentence_bleu
reference = [['this', 'is', 'a', 'test'], ['this', 'is' 'test']]
candidate = ['this', 'is', 'a', 'test']
score = sentence_bleu(reference, candidate)
score


# In[ ]:


def preprocess_sentence(w):
    w = unicode_to_ascii(w.lower().strip())
    
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ." 
    # Reference:- https://stackoverflow.com/questions/3645931/python-padding-punctuation-with-white-spaces-keeping-punctuation
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w)
    
    w = w.rstrip().strip()
    
    # adding a start and an end token to the sentence
    # so that the model know when to start and stop predicting.
    #w =   w 
    return w


# In[ ]:



for i in range(len(go)):
  #no.append(i)
  pred=translate(ge[i], encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ=34)
  #pred.append(translate(go[i], encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ=20))
  # cumulative BLEU scores
  #print(pred)
  pred1=pred.split(' ')
  reference = [ pred1[0:-2] ]
  print(reference)
  candidate = (preprocess_sentence(go[i]).split(' '))
  print(candidate)
  
  bleu1=(sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
  bleu2=(sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
  bleu3=(sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
  bleu4=(sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))
  
  bleu= sentence_bleu(reference, candidate)
  #print('Cumulative 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
  #print('Cumulative 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
  #print('Cumulative 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
  #print('Cumulative 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))
  row=[go[i],ge[i],pred,bleu1,bleu2,bleu3,bleu4,bleu]
  with open('nmttest.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

  csvFile.close()
  print(i," is done")


# In[ ]:


len(pred)


# In[ ]:


import pandas as pd
nmt=pd.read_csv('/content/nmttest.csv')
#tdata.head()


# In[ ]:


nmt.columns


# In[ ]:


txt=nmt[nmt.columns[0]].tolist()
pred=nmt[nmt.columns[2]].tolist()
b1=nmt[nmt.columns[3]].tolist()
b2=nmt[nmt.columns[4]].tolist()
b3=nmt[nmt.columns[5]].tolist()
b4=nmt[nmt.columns[6]].tolist()
b=nmt[nmt.columns[7]].tolist()


# In[ ]:


def Nmaxelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    print(final_list)
    return(final_list)
# Calling the function 
N=100
bs1=Nmaxelements(b1, N) 
bs2=Nmaxelements(b2, N) 
bs3=Nmaxelements(b3, N) 
bs4=Nmaxelements(b4, N) 
bs=Nmaxelements(b, N) 


# In[ ]:


txt=nmt[nmt.columns[0]].tolist()
pred=nmt[nmt.columns[2]].tolist()
b1=nmt[nmt.columns[3]].tolist()
b2=nmt[nmt.columns[4]].tolist()
b3=nmt[nmt.columns[5]].tolist()
b4=nmt[nmt.columns[6]].tolist()
b=nmt[nmt.columns[7]].tolist()


# In[ ]:


for i in range(len(b4)):
  if(b4[i]==1):
    print('txt:  ',txt[i])
    print('pre:  ',pred[i])
    print("i",i)


# In[ ]:





# In[ ]:


b1=nmt[nmt.columns[3]].tolist()
b2=nmt[nmt.columns[4]].tolist()
b3=nmt[nmt.columns[5]].tolist()
b4=nmt[nmt.columns[6]].tolist()
b=nmt[nmt.columns[7]].tolist()


# In[ ]:


#position in nmt
bd1=[]
bd2=[]
bd3=[]
bd4=[]
bd=[]
for i in range(len(bs1)):
  #print(bs1[i])
  bd1.append(b1.index(bs1[i]))
  bd2.append(b2.index(bs2[i]))
  bd3.append(b3.index(bs3[i]))
  bd4.append(b4.index(bs4[i]))
  bd.append(b4.index(bs[i]))


# In[ ]:


bl1 = list(set(bd1))
bl2 = list(set(bd2))
bl3 = list(set(bd3))
bl4 = list(set(bd4))
bl=list(set(bd))


# In[ ]:


bl


# In[ ]:


for i in bl:
  print('original:',txt[i])
  print("predicted:",pred[i])
  print("___________________________________________________")
print("=====================================================================")
print("=====================================================================")

print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")

for i in bl1:
  print('original:',txt[i])
  print("predicted:",pred[i])
  print("___________________________________________________")
print("=====================================================================")
print("=====================================================================")

print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")

for i in bl2:
  print('original:',txt[i])
  print("predicted:",pred[i])
  print("___________________________________________________")
print("=====================================================================")
print("=====================================================================")

print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")

for i in bl3:
  print('original:',txt[i])
  print("predicted:",pred[i])
  print("___________________________________________________")
print("=====================================================================")

print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")

print("=====================================================================")

for i in bl4:
  print('original:',txt[i])
  print("predicted:",pred[i])
  print("___________________________________________________")
print("=====================================================================")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("                                                                                   ")
print("=====================================================================")


# In[ ]:


get_ipython().system('pip install googletrans')


# In[ ]:


from googletrans import Translator
translator = Translator()


# In[ ]:


for i in bl1:
  print(txt[i])


# In[ ]:


txt=nmt[nmt.columns[1]].tolist()
pred=nmt[nmt.columns[2]].tolist()


# In[ ]:


translator.translate('안녕하세요.')


# In[ ]:


btt1=translator.translate([txt[i] for i in bl1], dest='en')
bpt1=translator.translate([pred[i] for i in bl1], dest='en')


btt2=translator.translate([txt[i] for i in bl2], dest='en')
bpt2=translator.translate([pred[i] for i in bl2], dest='en')

btt3=translator.translate([txt[i] for i in bl3], dest='en')
bpt3=translator.translate([pred[i] for i in bl3], dest='en')


btt4=translator.translate([txt[i] for i in bl4], dest='en')
bpt4=translator.translate([pred[i] for i in bl4], dest='en')

btt=translator.translate([txt[i] for i in bl], dest='en')
bpt=translator.translate([pred[i] for i in bl], dest='en')


# In[ ]:





# In[ ]:


for translation,translations in zip(btt1,bpt1):
  #for  in bpt1:
  print("origin:",translation.origin)
  print("pred  :",translations.origin)
  print("origin:",translation.text)
  print("pred  :",translations.text)
  print(" ____________________________________________________________________________________________ ")


# In[ ]:


for translation,translations in zip(btt2,bpt2):
  #for  in bpt1:
  print("origin:",translation.origin)
  print("pred  :",translations.origin)
  print("origin:",translation.text)
  print("pred  :",translations.text)
  print(" ____________________________________________________________________________________________ ")


# In[ ]:


for translation,translations in zip(btt3,bpt3):
  #for  in bpt1:
  print("origin:",translation.origin)
  print("pred  :",translations.origin)
  print("origin:",translation.text)
  print("pred  :",translations.text)
  print(" ____________________________________________________________________________________________ ")


# In[ ]:


for translation,translations in zip(btt4,bpt4):
  #for  in bpt1:
  print("origin:",preprocess_sentence(translation.origin))
  print("pred  :",translations.origin)
  print("origin:",translation.text)
  print("pred  :",translations.text)
  print(" ____________________________________________________________________________________________ ")


# In[ ]:


import pandas as pd
fin=pd.read_csv('./nmttest.csv')


# In[ ]:


fin.head()


# In[ ]:


number4=fin[]

