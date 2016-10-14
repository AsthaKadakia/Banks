from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', (views.BranchDetails.as_view()), name='branch-details'),
    url(r'^city/$', (views.CityWiseBranchesDetails.as_view()), name='city-branches')
                       ]