import os
from dotenv import load_dotenv


dotenv_path = ".env" 

#print(os.path.exists(dotenv_path)) #Test .env module 

load_dotenv(dotenv_path)


DATABASE = {

    "host": os.environ.get("DB_HOST"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "database": os.environ.get("DB_NAME")

}


FIREBASE = {
    "apiKey": "AIzaSyAVwksNpLY2dR4R6Po7g_MvAFcHaIjclS0",
    "authDomain": "etdservice-pr.firebaseapp.com",
    "projectId": "etdservice-pr",
    "storageBucket": "etdservice-pr.appspot.com",
    "messagingSenderId": "542453163805",
    "appId": "1:542453163805:web:d37220ef2a79832f7c23f4"
}