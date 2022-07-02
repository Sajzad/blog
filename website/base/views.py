from django.shortcuts import redirect, render, reverse, get_object_or_404

from .models import *


def home_view(request):
    
    posts = ''

    try:    
        posts = BlogPost.objects.all()
    except Exception as e:
        print(e)

    context = {
        'posts': posts
    }

    return render(request, 'base/index.html', context)

def user_view(request):
    users = ""
    message = ""
    if request.user.is_superuser or request.user.is_staff:

        if request.method == "POST":
            user_id = request.POST.get('user_id')
            obj = User.objects.get(id=user_id)
            print(obj)
            obj.delete()
            message = "User deleted"

        try:
            users = User.objects.exclude(is_superuser=True, is_staff=True)
        except:
            pass

        context = {
            "users": users,
            "message": message
        }

        return render(request, 'base/all-user.html', context)

def add_post_view(request):

    if request.method == "POST" or request.FILES:
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES['image']

        BlogPost.objects.create(
                user_id = request.user.id,
                title = title,
                description = description,
                image = image
            )

        return redirect(reverse("base:home"))

    context = {

    }

    return render(request, 'base/add-post.html', context)

def post_detail_view(request, post_id):

    if request.method == "POST":
        check = request.POST.get("check")

        if check == "comment":
            comment = request.POST.get("comment")
            Comment.objects.create(
                    user_id = request.user.id,
                    blog_post_id = post_id,
                    comment = comment
                )

        elif check == "delete":
            obj = BlogPost.objects.get(id=post_id)
            obj.delete()
            return redirect(reverse("base:home"))

    post = BlogPost.objects.get(id=post_id)

    try:
        comments = Comment.objects.filter(blog_post_id=post_id)
    except Exception as e:
        print(e)

    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'base/post.html', context)

def server_error(request):

    return render(request, "500.html")