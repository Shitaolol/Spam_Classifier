# Spam_Classifier
## Creating a Spam Classifier Using Attention Model


## The Keys Points are : 
### 1. Data Processing: Clean the dataset using the Spacy Library. Cleaning includes:

    a. Remove all the stop words.
    b. Remove the Puntuations.
    c. Remove the non Ascii Characters.
    d. Lemmitization of words.
    e. Remove all single Character words like 'A','b','c' (that are not providing any meaning to the data).
    
### 2. Process the Data to be inserted into the model. Do some Visulization and figure out the outliers ways to do so is:

    a. Create histogram on the basis of number of Characters and words. Figure out how to truncate data and how much to truncate data.
    b. Remove the most used words that are mostly common.
    c. Figure out the distribution of dataset.
    d. Use the above information to find the sequence length.

### 3. Create the Model :

    a. In this we have use an attention model. 
#### What is Attention ? 
        In psychology, attention is the cognitive process of selectively concentrating on one or a few things while ignoring others.
