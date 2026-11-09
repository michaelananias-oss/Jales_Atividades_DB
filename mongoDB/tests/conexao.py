from pymongo import MongoClient
uri = "mongodb+srv://kayquesilva_db_user:eQ1Dn7zB3s0Os2PR@cluster0.08an7tm.mongodb.net/"
client = MongoClient(uri) # type: ignore
try:
    client.admin.command("ping") # type: ignore
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)