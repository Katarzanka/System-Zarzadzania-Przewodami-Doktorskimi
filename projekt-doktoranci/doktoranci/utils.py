from django.shortcuts import redirect
from functools import wraps

def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user, 'profiluzytkownika') and request.user.profiluzytkownika.rola == required_role:
                return view_func(request, *args, **kwargs)
            return redirect('no_permission')  # upewnij się, że masz taką ścieżkę w urls.py
        return _wrapped_view
    return decorator
