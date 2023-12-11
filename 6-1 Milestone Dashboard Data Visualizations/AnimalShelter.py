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

# Creates new entry in dataase.
    def create(self, data):
        print("in create method.....")
        
        if data is not None: # If the data eing entered is not empty
            self.database.animals.insert_one(data)  # data should be dictionary
            return True # Returns true for if statement in testing
        else:
            raise Exception("Nothing to save, because data parameter is empty") # Error message is the data is empty

# Reads database and returns entrys that match search term.
    def read(self, searchTerm):
        print("in read method.....")
        
        if searchTerm is not None: # If the search term is not empty
            result = self.database.animals.find(searchTerm,{"_id": False}) # sets result to a list of animals matching search term
            print(result)
        
        else:
            raise Exception("Nothing to find, because search parameter is empty") # Error message if search term is empty
    
        return result # Returns the list of results
    
# Updates entry after reading through database and finding matching entry
    def update(self, searchTerm, infoToChange):
        print("in update method....")
        numUpdatedAnimals = 0 # Variable for number of entries changed
        
        if searchTerm and infoToChange is not None: # if both search term and new info are not empty
            result = self.database.animals.find(searchTerm) # creates a list with matching results for loop
            for animal in result: # Itterates through list of results so all matching entries get changed
                self.database.animals.update(searchTerm, infoToChange) # Updates entries that match searchTerm with infoToChange
                numUpdatedAnimals += 1 # Updates number of changes so user can see how much many were changed
                
        else:
            # Error message if search term is empty
            raise Exception("Nothing to update, because search parameter  or changed info are empty") 
            
        # Print to user number of updated entries
        print("Numer of Updated entries: ", end="")
        print(numUpdatedAnimals)
        print()
        
# Deletes entries that match search results from dataase
    def delete(self, searchTerm):
        print("in delete method.....")
        numAnimalsDeleted = 0 # Variale for number of deleted entries
        
        if searchTerm is not None: # If the search term is not empty
            result = self.database.animals.find(searchTerm) # creates a list with matching results for loop
            for animal in result: # iterates through list of results to delete all matching entries
                self.database.animals.delete_one(searchTerm) # Deletes entries that match search term
                numAnimalsDeleted += 1 # Updates number of deletions so user can see how many were deleted
         
        else:
            raise Exception("Nothing to delete, because search parameter is empty") # Error message if search term is empty
            
        # Print to user number of deleted entries
        print("Number of deleted entries: ", end="")
        print(numAnimalsDeleted)
            
            