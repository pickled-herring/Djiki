from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('p/<page_url>', views.page, name='page'),
	path('edit/<page_url>', views.edit, name='edit'),
	path('new', views.new, name='new'),
	path('submit-edit/', views.submit_edit, name='submit_edit'),
	path('submit-new/', views.submit_new, name='submit_new'),
	path('list-edit/', views.list_edits_all, name='list_edit_all'),
	path('list-edit/<page_url>', views.list_edits, name='list_edit'),
	path('view-edit/<int:edit_id>', views.view_edit, name='view_edit'),
	]
