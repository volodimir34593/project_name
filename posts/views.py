from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post

def post_counter(request):
    posts_count = Post.objects.count()
    return render(request, 'post_counter.html', {'posts_count': posts_count})

def check_session(request):
    if 'last_login' in request.session:
        last_login_time = request.session['last_login']
        current_time = timezone.now()
        time_difference = current_time - last_login_time
        if time_difference.total_seconds() >= 600:  # 10 minutes in seconds
            return redirect('login_view_name')  # Replace 'login_view_name' with the actual name of your login view
    return None
