from werkzeug.security import safe_str_cmp
# from resources.user import user
from models.user import UserModel

# users = [
#    User(1, 'bob', 'secretp')
# ]
                                                # NB u equals u.username therefore "u = 'bob'" " in the first pass of th efor statement - .get gives value of key
# username_mapping = {u.username: u for u in users}  # u indexes the first dictionary.  i.e., 'u' becomes the argument of the keyword of keywork username
# userid_mapping = {u.id: u for u in users}       #becomes the argument of the keyword of keywork 'id' that the for statement searches through the users list
                                                # assign key value pairs NB 'key' is u.id and value is 'u'
def authenticate(username, password):
      # user = username_mapping.get(username, None)   # using get() instead of ['...'] because can retunn default value None if no userna  in the list
      user = UserModel.find_by_username(username)
      if user and safe_str_cmp(user.password, password):
          return user


def identity(payload):  #unique to JWT and  payload is contents of JWY token
    user_id = payload['identity']    # extract userid from payload
    return UserModel.find_by_id(user_id)
    # return userid_mapping.get(user_id, None)
