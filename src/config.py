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

JWT = {

    "secret": os.environ.get("JWT_SECRET"),
    "algorithm": os.environ.get("JWT_ALGORITHM")


}
