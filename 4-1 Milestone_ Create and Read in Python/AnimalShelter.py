# Make sure to be signed in with proper user name and password with terminal, and have launched mongosh and are in the proper
# database

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, pwd):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # nv-desktop-services.apporto.com:31011 is host and port
        self.client = MongoClient('mongodb://%s:%s@nv-desktop-services.apporto.com:31011' % (user, pwd)) 
        
        self.database = self.client['AAC'] #AAC is name of database to be accessed
        print('Hello Animal Shelter')

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        print("in create method.....")
        
        if data is not None: # If the data eing entered is not empty
            self.database.animals.insert_one(data)  # data should be dictionary
            return True # Returns true for if statement in testing
        else:
            raise Exception("Nothing to save, because data parameter is empty") # Error message is the data is empty

# Create method to implement the R in CRUD.
    def read(self, searchTerm):
        print("in read method.....")
       
        if searchTerm is not None: # If the search term is not empty
            result = self.database.animals.find(searchTerm) # sets result to a list of animals matching search term
            for animal in result: # Itterates through list of results
                print(animal) # Prints animal at entry numer 'n' of result list
                print("") # New line for easier reading of results
        
        else:
            raise Exception("Nothing to find, because search parameter is empty") # Error message if search term is empty
    
        return result # Returns the list of results