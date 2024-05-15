from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from core.utils import *

def is_group(group):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            user = request.user
            if has_group(user, group):
                return function(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        return wrap
    return decorator