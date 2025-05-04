import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'przewody.settings')
django.setup()

from django.contrib.auth.models import User
from doktoranci.models import ProfilUzytkownika

def create_user_with_role(username, password, role):
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()
        print(f"Utworzono użytkownika: {username}")
    else:
        print(f"Użytkownik {username} już istnieje")

    profile, _ = ProfilUzytkownika.objects.get_or_create(user=user)
    profile.rola = role
    profile.save()
    print(f"Przypisano rolę '{role}' użytkownikowi {username}")

create_user_with_role('sekretarz_test', 'haslo123', 'sekretarz')
create_user_with_role('rada_test', 'haslo123', 'rada')
create_user_with_role('admin_test', 'haslo123', 'admin')

print("Gotowe!")
