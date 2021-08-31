from pymongo import MongoClient
from random import randint


def getDB():
    client = MongoClient('mongodb://localhost:27017/')
    db=client.business
    return db

def createDB(db):
    names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
    company_type = ['LLC','Inc','Company','Corporation']
    company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
    for x in range(1, 501):
        business = {
            'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
            'rating' : randint(1, 5),
            'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
        }
        #Step 3: Insert business object directly into MongoDB via insert_one
        result=db.reviews.insert_one(business)
        #Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
    #Step 5: Tell us that you are done
    print('finished creating 500 business reviews')


def find_a_rating(db, rating):
    rat = db.reviews.find_one({'rating': rating})
    print(rat)
    return rat['name']


def find_count_of_a_rating(db, rating):
    print('The number of 5 star reviews:')
    count = db.reviews.find({'rating': rating}).count()
    print(count)
    return count


def find_count_of_all_rating(db):
    # Now let's use the aggregation framework to sum the occurrence of each rating across the entire data set
    print('\nThe sum of each rating occurance across all data grouped by rating ')
    stargroup=db.reviews.aggregate(
    # The Aggregation Pipeline is defined as an array of different operations
    [
    # The first stage in this pipe is to group data
    { '$group':
        { '_id': "$rating",
         "count" : 
                     { '$sum' :1 }
        }
    },
    # The second stage in this pipe is to sort the data
    {"$sort":  { "_id":1}
    }
    # Close the array with the ] tag             
    ] )
    # Print the result
    for group in stargroup:
        print(group)


def list_all_reviews(db):
    # To find() all the entries inside collection name 'myTable'
    cursor = db.reviews.find()
    s = ""
    for record in cursor:
        s = s + record['name'] + " - " + record['cuisine'] + "\n"
        print(record['name'] + " - " + record['cuisine'])
    return s
