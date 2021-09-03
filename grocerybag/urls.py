from django.urls import path
from . import views

# all the view urls goes here
urlpatterns = [
    path('', views.itemlist, name='itemlist'),
    path('additem', views.additem, name='additem'),
    path('update/<int:pk>', views.updateitem, name='updateitem'),
    path('delete/<int:pk>', views.deleteitem, name='deleteitem'),
    path('filter', views.filteritem, name='filteritem'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]
