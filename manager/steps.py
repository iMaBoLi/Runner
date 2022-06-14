from .database import DB

def steps():
    return DB.get_key("USER_STEPS") or {}

def sstep(user_id, step):
    steps = steps()
    steps.update({user_id: step})
    DB.set_key("USER_STEPS", steps)

def gstep(user_id):
    return steps()[user_id]
