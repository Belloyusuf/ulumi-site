from django.shortcuts import render, get_object_or_404
from .models import News, Comment
from .forms import CommentForm
from django.contrib import messages

def index(request):
    return render(request, 'ulumi/index.html')


def news_detail(request):
    news = News.objects.all()
    return render(request, 'ulumi/news.html', {'news':news})

def history(request):
    return render(request,'ulumi/history.html')


def full_detail(request, year, month, day, news):
    news = get_object_or_404(News,
                        slug=news,
                        written__year = year,
                        written__month = month, 
                        written__day = day)

    # list of active comment for this news
    comments = news.comments.filter(active=True)
    new_comment = None
    
    if request.method == 'POST':
        # A comment was sent
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # create comment object but don't save to db
            new_comment = comment_form.save(commit=False)
            # Assign the current news to the comment 
            new_comment.news = news
            # save the comment to the database
            new_comment.save()
            messages.success(request, messages)
    else:
        comment_form = CommentForm()
    return render(request, 'ulumi/full_detail.html',
                           {'news':news,
                           'comments':comments,
                           'new_comment':new_comment,
                           'comment_form':comment_form})
