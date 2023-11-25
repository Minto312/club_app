from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        permit_urls = [
            '/account/register/',
            '/account/sign_in/',
            '/account/sign_out/',
            # '/var/www/mysql',
            # '/',
        ]
        if request.path not in permit_urls and not request.user.is_authenticated:
            return redirect('account:sign_in')
        return response