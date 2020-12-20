import pyresparser
from pyresparser import ResumeParser
import pandas as pd

import nltk
nltk.download('stopwords')



def executefunc():
	r1 = ResumeParser('Resume.pdf').get_extracted_data()
	r2 = ResumeParser('Daniyal.pdf').get_extracted_data()
	r3 = ResumeParser('Saad.pdf').get_extracted_data()


	#Creating list of dictionaries
	list_resume = [r1, r2, r3]

	#Creating dataframe from dictonaries
	df = pd.DataFrame(list_resume)

	return df
