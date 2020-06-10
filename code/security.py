from werkzeug.security import safe_str_cmp
from models.user import UserModel

# users = [
#     # {
#     #     'id': 1,
#     #     'username': 'bob',
#     #     'password': 'asdf'
#     # }
#     User(1, 'bob', 'asdf')
# ]
# # username_mapping = { 'bob': {
# #         'id': 1,
# #         'username': 'bob',
# #         'password': 'asdf'
# #     }
# # }
#
# username_mapping = {u.username: u for u in users} # set comprehension, assigning kv pairs
# userid_mapping = {u.id: u for u in users}

# userid_mapping = { 1: {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# }

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # if no username return none
    # user = username_mapping.get(username, None)
    # safe_str_cmp compares all different systems, servers, encodings
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    # return userid_mapping.get(user_id, None)
    return UserModel.find_by_id(user_id)
