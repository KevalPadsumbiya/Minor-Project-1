from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name="index"),
	path('test',views.Test,name="test"),
	path('sign-in',views.signin,name="signin"),
	path('sign-up',views.signup,name="signup"),
	path('byBrand',views.byBrand,name="byBrand"),
	path('view',views.model,name="model"),
	path('compare',views.compare,name="compare"),
	path('favourite',views.favourite,name="favourite"),
	path('news',views.news,name="news"),
	path('validate_register',views.validate_register,name="register_validate"),
    path('validate_login', views.validate_login, name="login_validate"),
	path('add-to-compare', views.addToCompare, name="add-to-compare"),
	path('add-to-favourite', views.addToFavourite, name="add-to-favourite"),
	path('logout',views.logout,name="logout"),
	path('post-a-comment', views.postComment, name="post-a-comment"),
	path('upvote-a-comment',views.upvoteComment,name="upvote-a-comment"),
	path('downvote-a-comment',views.downvoteComment,name="downvote-a-comment"),
	path('remove-from-compare',views.removeFromCompare,name="remove-from-compare"),
	path('remove-from-favourites',views.removeFromFavourites,name="remove-from-favourites"),
	path('forgot',views.forgot,name="forgot_password"),
	path('forgot_validate',views.forgot_validate,name="forgot_validate"),
	path('admin-dashboard',views.Admin,name="Admin"),
	path('update-database',views.updateDB,name="updateDB"),
	path('profile',views.profile,name="profile"),
	path('price_filter',views.price_filter,name="price_filter")
]