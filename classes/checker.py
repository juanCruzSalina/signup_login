import string


class data_check:
    def __init__(self, username, password):
        self.user = username
        self.password = password

    def user_check(self):
        user_error = 0
        if 7 > int(len(self.user)) > 13:
            user_error = 1
        elif not self.user.isalnum():
            user_error = 2
        else:
            for x in self.user:
                if x == "@" "/":
                    user_error = 4
        user_error_dict = {1: "The username must have between 8 and 12 characters.",
                           2: "The user name must have alphanumeric.",
                           3: "The username must not have a '@' or '/'",
                           0: "Valid Username."}
        error_user = user_error_dict.get(user_error)
        return error_user

    def pass_check(self):
        pass_error = 0
        if 5 > int(len(self.password)) > 33:
            pass_error = 1
        else:
            if not set(self.password).difference(string.punctuation):
                pass_error = 3
        pass_error_dict = {1: "The password must be between 6 and 32.",
                           2: "The password must ne alphanumeric.",
                           3: "The password must have one special character at least.",
                           0: "Valid password."}
        error_pass = pass_error_dict.get(pass_error)
        return error_pass
