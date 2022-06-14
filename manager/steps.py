from .database import DB

def steps():
    return DB.get_key("USER_STEPS") or {}

def sstep(user_id, step):
    all = steps()
    all.update({user_id: step})
    DB.set_key("USER_STEPS", all)

def gstep(user_id):
    return steps()[user_id]
