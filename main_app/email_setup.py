from .views import sender_email_view


'''
NOT TESTED. WROTE AS PSEUDO CODE!
'''


class EmailHostConfig():

    # get email
    def get_host_user():
        return EMAIL-HERE
        pass


     # get pass
    def get_email_pass():
        return PASS - HERE
        pass



    # configure  EMAIL_HOST_USER in settings.py

    def email_host_user_config(filename, keyword):
        with open(filename, 'r+') as f:
            content = f.read()
            f.write(line.rstrip('\r\n') + '\n' + content)

    email_host_user_config('settings.py', EMAIL_HOST_USER='EMAIL-HERE')
    email_host_user_config('settings.py', EMAIL_HOST_PASS='PASS-HERE')