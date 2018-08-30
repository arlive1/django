from django.conf.urls import url
from django.contrib import admin
from MyApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^idealweight/',views.IdealWeight),
    url(r'^test1/',views.ts),
    url(r'^string/$',views.ts2),
]