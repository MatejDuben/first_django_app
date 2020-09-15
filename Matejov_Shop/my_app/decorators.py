from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_page_for_unlogged_user(view_func): #ak je user nepryhlaseny vrati homePage
  def wrapper_func(request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('homePage:home')
    else:
      return view_func(request, *args, **kwargs)

  return wrapper_func


def unauthenticated_page_for_logged_user(view_func): #ak je user pryhlaseny vrati homePage
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('homePage:home')
    else:
      return view_func(request, *args, **kwargs)

  return wrapper_func