#!/bin/bash

sudo pip install -U nltk
pip install --upgrade gensim
pip install -U spacy
python -m spacy download en

pip install pyldavis
pip install bokeh

