# To interact with Django models from an external script.
import os, sys, django

def active_django_environ(project_path):
    project_settings = project_path.split('/')[-1] + '.settings'
    sys.path.append(project_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_settings)
    django.setup()

def load_django_resources():
    #Users and current date.
    from django.contrib.auth.models import User
    from django.utils.timezone import now

    return now, User


active_django_environ("your-project-path")
now, User = load_django_resources()


# We get the users who have logged in today.
current_date = now().date()
login_users_today = User.objects.filter(last_login__date = current_date)

# If there are logged in users, it records them in the log file.
if login_users_today.exists():
    with open("login_users.log", "a") as f:
        f.write(f"[ {current_date} ]\n")
        for user in login_users_today:
            f.write('\t' + user.username + ' | ' + user.email + '\n')