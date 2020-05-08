from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from tutorial.quickstart import views as quickstartViews
from snippets import views as snippetsViews

router = routers.DefaultRouter()
router.register(r'users', quickstartViews.UserViewSet)
router.register(r'groups', quickstartViews.GroupViewSet)
router.register(r'snippets', snippetsViews.SnippetsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('snippets.urls')),
]
