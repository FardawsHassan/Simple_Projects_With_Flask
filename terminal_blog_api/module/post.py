from database import Database
import datetime
import uuid

class Posts(object):

    def __init__(self,title="None",date=datetime.datetime.utcnow(),user_id="none",post_id=uuid.uuid4().hex,content="none"):
        self.title = title
        self.date = date
        self.user_id = user_id
        self.post_id = post_id
        self.content = content
        self.save_to_db()

    def save_to_db(self):
        retJson = self.jsonify()
        Database.insert("post",retJson)

    def jsonify(self):
        return {
            "Title":self.title,
            "date":self.date,
            "user_id":self.user_id,
            "post_id":self.post_id,
            "content":self.content,
        }

    @staticmethod
    def find_post(post_id):
        return Database.find_one("post",{"post_id":post_id})

    @staticmethod
    def find_all_posts(post_id):
        return [post for post in Database.find("post",{"post_id":post_id})]
