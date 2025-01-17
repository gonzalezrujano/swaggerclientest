from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://fjrd12:Rjon2457@cluster0.6zswh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["ServiceCatalog"]
    collection = db["ServiceCatalog"]
    #document = collection.find_one({})
    #print("Found document:", document)
    source_url = "https://petstore.swagger.io/v2"
    Catalogname = "Petstore"
    document = collection.find({"$or": [ { "source_url":  source_url}, { "catalogname": Catalogname } ]})
    print("Found document:", document)
except Exception as e:
    print(e)