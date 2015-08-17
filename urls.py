from django.conf.urls import url

from . import router

urlpatterns = [
	url(r'^', router.route),
]
