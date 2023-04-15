import pandas as pd 
import pandas as pd
import os
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin


from Preprocess import converted_array


TRAIN_DATA = converted_array
#nlp = spacy.blank("en") # load a new spacy model
nlp = spacy.load("en_core_web_sm") # load other spacy model

db = DocBin() # create a DocBin object

for text, annot in tqdm(TRAIN_DATA): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("./train.spacy") # save the docbin object

# python -m spacy init fill-config base_config.cfg config.cfg

# python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy 
