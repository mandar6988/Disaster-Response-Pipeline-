# Importing Required Liabraries
import sys
import pandas as pd
import numpy as np
import random
from sqlalchemy import create_engine
import sqlite3

def load_data(messages_filepath, categories_filepath):
    """ 
    Function has two arguments:
    messages_filepath-- message path of database 
    categories_filepath-- categories path of dataset
    
    Return: It returns merge data
    """
    messages = pd.read_csv(messages_filepath)# message database is loaded
    categories =pd.read_csv(categories_filepath) # categories database is loaded
    
    df =pd.merge(messages,categories) # Two database has been merged
    
    return df


def clean_data(df):
    """
    df: input argument to this function
    
    Returns clean data
    """
    categories = df.categories.str.split(pat=';',expand=True)
    row = categories.loc[0]
    category_colnames = row.apply(lambda temp1: temp1[0:-2])
    categories.columns = category_colnames#
    for column in categories:
    # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
    
    # convert column from string to numeric
        categories[column] = categories[column].astype(int) 
    df=df.drop(['categories','original'],axis=1)# Removed unnecessary columns
    
    df = pd.concat([df,categories],axis=1)
    temp=df.duplicated().sum()
    print("Total Number of duplicates=",temp) # Printing count of duplicates present
    
    df=df.drop_duplicates() # duplicates are dropped
    print(type(df)) # to see type of dataframe
    print(df.shape)
    return df
def save_data(df, database_filename):
    """
    Args:
    database frame is take as first argumnets
    second arguments is name of sql database
    
    """
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('message_table',engine,index=False,if_exists='replace') # sql database 
    
    pass
    
def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        
        save_data(df, database_filepath)
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()