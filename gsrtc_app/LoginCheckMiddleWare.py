from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__

        user = request.user

        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "gsrtc_app.HodViews":
                    pass
                elif modulename == "gsrtc_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_home")
            
            elif user.user_type == "2":
                if modulename == "gsrtc_app.StaffViews":
                    pass
                elif modulename == "gsrtc_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("staff_home")

            else:
                return redirect("login")

        else:
            if request.path == reverse("login") or request.path == reverse("doLogin"):
                pass
            else:
                return redirect("login")
