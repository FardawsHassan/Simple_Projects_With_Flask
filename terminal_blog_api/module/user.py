from database import Database
from module.post import Posts
import datetime
import uuid

class Users(object):
    
    def __init__(self,author="none",user_id=uuid.uuid4().hex,discription="none"):
        self.author = author
        self.user_id = user_id
        self.discription = discription
        self.save_to_db()

    def new_post(self,title="none",date=datetime.datetime.utcnow(),content="none"):
        date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Posts(title=title,date=date,user_id=self.user_id,content=content)

    def save_to_db(self):
        retJson = self.json()
        Database.insert("users",retJson)

    def json(self):
        return {
            "author": self.author,
            "user_id": self.user_id,
            "discription": self.discription
        }
        
