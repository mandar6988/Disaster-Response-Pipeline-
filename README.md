# Diaster Response Pipeline Project

**1. Installation**


      to run this program , following packages are needed.
          1. Wordnet
          2. nltk
          3. Flask
          
      
**2. File Description**
  
  It consist of three files.
  
    1. process_data.py: This file is used to do ETL i.e Extract, Transform, Load. First data is loaded, cleaned and saved into sqlite               database.
    2. train_classifier.py: It consist of machine learninh algorithm operation. 
    3. run.py: Classified data is diasplayed with the help of webpage. 
    


** 3.Instruction to run program:**


    1. Run the following commands in the project's root directory to set up your database and model.

        - To run ETL pipeline that cleans data and stores in database
            `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
        - To run ML pipeline that trains classifier and saves
            `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`   

    2. Run the following command in the app's directory to run your web app.
        `python run.py`

    3. Go to http://0.0.0.0:3001/

