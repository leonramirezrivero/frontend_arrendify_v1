# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),    
    path('inquilinos/', views.path_inq, name='inquilinos'),    
    path('detalles_inquilino/<int:id>', views.path_inq_detalles, name='inquilinos_detalles'),    
    path('editar_inq/<int:id>', views.path_inq_edit, name='inquilinos_editar'),    
    path('documentos_inq/<int:id>', views.path_archivos_inq, name='archivos_inquilinos'),    
    path('detalles_documentos/<int:id>', views.path_detalles_archivos, name='detalles_archivos'),    

    path('inmuebles/', views.path_inmuebles, name='inmuebles'),   
    path('fiador_obligado/', views.path_foo, name='fiador_obligado'),   
    path('detalles_fiador/<str:slug>', views.path_foo_detalles, name='inquilinos_detalles'),    
    path('editar_fiador/<str:slug>', views.path_foo_edit, name='inquilinos_editar'),  
    path('prueba/', views.prueba, name='Arren'),  
    path('tyc/', views.tyc, name='tyc'),  
    
    path('archivos', views.path_doc_inquilino, name='inquilinos_docs'),  


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
