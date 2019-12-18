from database import Database
from models.post import Post

__author__ = 'Cate'

Database.initialize()

blog = Blog(author="Cate",
            title="Sample title",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

blog.from_mongo()

blog.get_posts()

# post = Post(blog_id="123",
#             title="Another great post",
#             content="This is some sample content",
#             author="Cate")
#
# post.save_to_mongo()

# post = Post("Post1 title", "Post1 content", "Post1 author")
# post2 = Post("Post2 title", "Post2 content", "Post2 author")
#
# print(post.content)
#
# print(post2.content)

# import pymongo
#
# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']

# students = collection.find({})
# student_list = []
#
# for student in students:
#     student_list.append(student)

# List comprehension
# students = [student['mark']] for student in collection.find({}) if student['mark'] == 99.0]
#
# print(students)
