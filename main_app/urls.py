from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('birds/', views.birds_index, name='index'),
  path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
  path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
  path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='birds_update'),
  path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='birds_delete'),
  path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  # associate an enclosure with a bird (M:M)
  path('birds/<int:bird_id>/assoc_enclosure/<int:enclosure_id>/', views.assoc_enclosure, name='assoc_enclosure'),
  # unassociate an enclosure and bird
  path('birds/<int:bird_id>/unassoc_enclosure/<int:enclosure_id>/', views.unassoc_enclosure, name='unassoc_enclosure'),
  path('enclosures/', views.EnclosureList.as_view(), name='enclosures_index'),
  path('enclosures/<int:pk>/', views.EnclosureDetail.as_view(), name='enclosures_detail'),
  path('enclosures/create/', views.EnclosureCreate.as_view(), name='enclosures_create'),
  path('enclosures/<int:pk>/update/', views.EnclosureUpdate.as_view(), name='enclosures_update'),
  path('enclosures/<int:pk>/delete/', views.EnclosureDelete.as_view(), name='enclosures_delete'),
]