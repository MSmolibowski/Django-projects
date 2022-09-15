from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Author, Category, Post

def post_list_view(request, category_name=None, author_id=None):
    queryset = Post.objects.all()
    if category_name:
        queryset = queryset.filter(category__name=category_name)
    if author_id:
        author = Author.objects.get(id=author_id)
        queryset = queryset.filter(author=author)
        
    queryset = queryset.filter(public=True).order_by('-date_publish')
    paginator = Paginator(queryset, 3) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category_list': Category.objects.all(),
        'category_name': category_name,
        'page_obj': page_obj,
        'n_posts': queryset.count(),
    }
    return render(request, 'blog/post_list.html', context)


def post_detail_view(request, post_id):
    context = {
         'object': get_object_or_404(Post, id=post_id),
         'category_list': Category.objects.all(),
         'category_name': None,
    }
    return render(request, 'blog/post_detail.html', context)