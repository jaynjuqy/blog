from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.login_view, name="login"),
    path("logout/", views.logout, name="logout"),
    path('feed/', views.feed_view, name='myfeed'),
    path('post/<int:id>/', views.post_details_veiw, name='post_details'),
    path('post_form/', views.post_form, name='postform'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('comment_on_post/<int:id>/', views.comment_form, name='commentform'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)