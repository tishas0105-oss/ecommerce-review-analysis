from pydoc import text

import pandas as pd
df= pd.read_csv('Womens Clothing E-Commerce Reviews.csv')
a= df.head()
print(a)
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
review_text= df.dropna(subset=['Review Text']).copy() #removing the rows with null values in the 'Review Text' then copying them to a new dataframe 'reiew_text'
print(review_text.shape) 
print(review_text.isnull().sum()) #to print the number of null values in each column of the 'review_text' dataframe
review_text['clean_text']=review_text['Review Text'].str.lower() #converting the 'Review Text' column to lowercase and storing it in 'clean_text' column
print(review_text[['clean_text', 'Review Text']].head()) # to print 'clean_text' and 'Revew Text' columnn
review_text['clean_text']=review_text['clean_text'].str.replace(r'[^\w\s]+', '', regex=True) #'[^\w\s]+' this is used to remove all the punctuations
print(review_text[['clean_text', 'Review Text']].head())
review_text['clean_text']= review_text['clean_text'].str.replace(r'\s+', ' ',regex=True) #'\s+' this is used to remove all the extra spaces
print(review_text[['clean_text', 'Review Text']].head())

negative_review= review_text[review_text['Rating']<=2].copy() #copying the rows with 'Rating' less than or equal to 2 to a new dataframe 'negative_review'
print(negative_review.shape)

print(negative_review[['Rating', 'clean_text']].head(10)) #to print the first 10 rows of 'Rating' and 'clean_text' columns of the 'negative_review' dataframe
all_text= ' '.join(negative_review['clean_text']) # to join all the text in the 'clean_text' column of the 'negative_review' dataframe into a single string as 'all_text'
words= all_text.split() #to split the 'all_text' string into a list of words

from collections import Counter
word_count=Counter(words) #to count the frequency of each word in the 'words' list and store it in a 'word_count' variable
print(word_count.most_common(20)) #to print the 20 most common words in the 'word_count' variable

import nltk
nltk.download('stopwords') #to download the stopwords from the nltk library
from nltk.corpus import stopwords
stop_word=set(stopwords.words('english')) #to create a set of stopwords from the nltk library
filtered_word=[]
for word in words:#to iterate through each word in the 'words' list
    if word not in stop_word: #to check if the word is not in the stopwords set
        filtered_word.append(word) #if the word is not in the stopwords set, then append it to the 'filtered_word' list
        #words → stopwords check → stopwords remove → filtered_words

word_filtered_count=Counter(filtered_word) #to count the frequency of each word in the 'filtered_word' list and store it in a 'word_filtered_count' variable
print(word_filtered_count.most_common(20)) #to print the 20 most common words in the 'word_filtered_count' variable

size_fit= negative_review [negative_review['clean_text'].str.contains(r'\b(size|sizing|fit|fitting|small|large|tight|loose|short|long)\b',na=False)]
print(size_fit.shape[0]) #to print the number of rows in the 'size_fit' dataframe

fabric_material= negative_review[
    negative_review['clean_text'].str.contains(
        r'\b(fabric|material|cloth|cotton|linen|polyester|silk|wool|nylon)\b',
          na=False
    )
]
print(fabric_material.shape[0]) #to print the number of rows in the 'fabric

quality = negative_review[
    negative_review['clean_text'].str.contains(
        'quality',
        regex=False,
        na=False
    )
]
print(quality.shape[0]) #to print the number of rows in the 'negative_review' dataframe that contain the word 'quality' in the 'clean_text' column

comfort= negative_review[
    negative_review['clean_text'].str.contains(
        r'\b(comfortable|comfort|itchy|rough|scratchy)\b',
                        na=False
    )
]
print(comfort.shape[0]) #to print the number of rows in the 'negative_review' dataframe that contain the words 'comfortable', 'comfort', 'itchy', 'rough', or 'scratchy' in the 'clean_text' column

color=negative_review[negative_review['clean_text'].str.contains(
    r'\b(color|colour|dye|faded|bleached|stained|discolored)\b',
    na=False
    )
]
print(color.shape[0]) #to print the number of rows in the 'negative_review' dataframe that contain the words 'color', 'colour', 'dye', 'faded', 'bleached', 'stained', or 'discolored' in the 'clean_text' 

complaint_data= pd.DataFrame({
    'complaint theme':['size/fit','fabric/material','quality', 'comfort', 'color'],
    'review_count':[size_fit.shape[0], fabric_material.shape[0], quality.shape[0], comfort.shape[0], color.shape[0]]
})
print(complaint_data) #to print the 'complaint_data' dataframe

# import matplotlib.pyplot as plt
# plt.figure(figsize=(8,5))

# plt.bar(
#     complaint_data['complaint theme'],
#     complaint_data['review_count']
# )

# plt.xlabel('complaint theme')
# plt.ylabel('number of reviews')
# plt.title('Number of reviews for each complaint theme')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show() #to show the bar chart of the number of reviews for each complaint theme

complaint_data['percentage']=round((complaint_data['review_count']/complaint_data['review_count'].sum())*100,2) #to calculate the percentage of reviews for each complaint theme and store it in a new column 'percentage' in the 'complaint_data' dataframe
print(complaint_data) #to print the 'complaint_data' dataframe with the new 'percentage' column
import re
print(negative_review['clean_text']) #to print the columns of the 'negative_review' dataframe
def get_complaint_theme(text):
    if pd.isna(text):
        return 'other'

    if re.search(r'\b(size|sizing|fit|fitting|small|large|tight|loose|short|long)\b', text):
        return 'size/fit'
    elif re.search(r'\b(fabric|material|cloth|cotton|linen|polyester|silk|wool|nylon)\b', text):
        return 'fabric/material'
    elif re.search(r'\b(quality)\b', text):
        return 'quality'
    elif re.search(r'\b(comfortable|comfort|itchy|rough|scratchy)\b', text):
        return 'comfort'
    elif re.search(r'\b(color|colour|dye|faded|bleached|stained|discolored)\b', text):
        return 'color'
    else:
        return 'other'
negative_review['complaint_theme']= negative_review['clean_text'].apply(get_complaint_theme) #to apply the 'get_complaint_theme' function to the 'clean_text' column of the 'negative_review' dataframe and store the result in a new column 'complaint_theme'
print(negative_review[['Class Name', 'complaint_theme']].head(10)) #to print the first 10 rows of the 'clean_text' and 'complaint_theme' columns of the 'negative_review' dataframe
complaint_by_class = (
     negative_review
    .groupby(['Class Name', 'complaint_theme']) #to group the 'negative_review' dataframe by 'Class Name' and 'Complaint Theme' columns
    .size() #to count the number of rows in each group
    .reset_index(name='review_count') #to reset the index of the grouped dataframe and store the count in a new column 'review_count'
)
print(complaint_by_class) #to print the 'complaint_by_class' dataframe

complaint_pivot = complaint_by_class.pivot(
    index='Class Name',
    columns='complaint_theme',
    values='review_count'
).fillna(0)

complaint_pivot=complaint_pivot.drop(columns=['other'])

print(complaint_pivot)

top_complaint=complaint_pivot.idxmax(axis=1) #to get the column name of the maximum value in each row of the 'complaint_pivot' dataframe
top_count=complaint_pivot.max(axis=1) #to get the maximum value in each row of the 'complaint_pivot' dataframe
top_complaint_df=pd.DataFrame({
    'Top Complaint': top_complaint,
    'Count': top_count
})
print(top_complaint_df) #to print the 'top_complaint_df' dataframe