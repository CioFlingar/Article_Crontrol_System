from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from app_dj.models import Articles

# from django.shortcuts import  redirect, render
# from .forms import CreateArticleForm

# def home(request):
#     articles = Articles.objects.all()
#     return render(request, "app_dj/home.html", {"articles": articles})


# def create_article(request):  # type:ignore
#     if request.method == "POST":
#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             new_article = Articles(
#                 title=form_data["title"],
#                 status=form_data["status"],
#                 content=form_data["content"],
#                 word_count=form_data["word_count"],
#                 twitter_post=form_data["twitter_post"],
#             )
#             new_article.save()

#             return redirect("home")
#     else:
#         form = CreateArticleForm()
#         return render(request, "app_dj/article_create.html", {"form": form})


class ArticleListView(ListView):
    template_name = "app_dj/home.html"
    model = Articles
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    template_name = "app_dj/article_create.html"
    model = Articles
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"


class AritcleUpdateView(UpdateView):
    template_name = "app_dj/article_update.html"
    model = Articles
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = "app_dj/article_delete.html"
    model = Articles
    success_url = reverse_lazy("home")
    context_object_name = "article"
