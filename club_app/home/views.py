import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    logger.info(f'User {request.user.username} accessed home')
    return render(request, 'home/home.html')