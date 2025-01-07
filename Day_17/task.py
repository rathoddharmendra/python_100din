class User:
    '''
    Models users on the website - has and can do!
    '''
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        if isinstance(user, User):  # Ensure user is a User instance
            user.followers += 1
            self.following += 1
        else:
            print(f"Cannot follow {user}: Not a valid User instance.")

# Create User objects
user_1 = User("001", "Dee")
user_2 = User("002", "Sheral")

# User interactions
user_1.follow(user_2)
user_2.follow(user_1)

# Avoid invalid follow attempts
user = {"followers": 10}
user_1.follow(user)  # Will print a warning instead of raising an error

# Print results
print(f'{user_1.username}, Followers: {user_1.followers}, Following: {user_1.following}')
print(f'{user_2.username}, Followers: {user_2.followers}, Following: {user_2.following}')
print(user)