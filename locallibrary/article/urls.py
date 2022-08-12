from django.urls import path
from . import views
from django.views.generic import RedirectView # 重定向
# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # path('', RedirectView.as_view(url='/article/article-list/')),
    path('article-list/', views.article_list, name='article_list'),
]