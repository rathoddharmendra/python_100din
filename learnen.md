### Important learning notes

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPyuDjp7MR54frNziP9erEnW2xO63Glpgsgz9hr2w7po rathoddharmendra.business@gmail.com

her way of talking
slow thinking -- structurtally down to - breaking down
result oriented

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 3:
            return func(*args, **kwargs)
        else:
            abort(403)
    return wrapper