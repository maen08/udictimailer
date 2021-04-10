from .views import sender_email_view





class EmailHostConfig():

    # get the dev email here
    def get_the_email():
        return EMAIL-HERE
        pass

    def get_email_pass():
        return PASS-HERE



    # configure it as EMAIL_HOST_USER in settings.py
    def email_host_user_config(filename, keyword):
        with open(filename, 'r+') as f:
            content = f.read()
            f.write(line.rstrip('\r\n') + '\n' + content)

    email_host_user_config('settings.py', EMAIL_HOST_USER='EMAIL-HERE')