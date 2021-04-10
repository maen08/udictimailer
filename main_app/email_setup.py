from .views import sender_email_view

# get the dev email here
# call it - email
# awaits the dev, 2 min will be enough

class EmailHostConfig():
    
    # configure it as EMAIL_HOST_USER in settings.py
    def email_host_user_config():
        reading_file = open('settings.py', 'r')
        new_file_content = ""

        ALLOWED_HOSTS = domain_name + '.herokuapp.com'
        link = ALLOWED_HOSTS.split(' ')

        for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace(
            'ALLOWED_HOSTS = []', f'ALLOWED_HOSTS = {link}')  # user should not rewrite ALLOWED_HOSTS
                                                                # before the script. Let it handle everything
        new_file_content += new_line + "\n"


        reading_file.close()
        writing_file = open('settings.py', 'w')
        writing_file.write(new_file_content)

        writing_file.close()
