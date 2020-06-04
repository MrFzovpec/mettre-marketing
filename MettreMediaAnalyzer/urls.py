from django.contrib import admin
from django.urls import path
import access.views as access
import api.views as api
import mettre_main.views as pages

urlpatterns = [
    # Pages
    path('', pages.index),
    path('info/', pages.information),
    path('description/', pages.usage_description),
    path('analyze/marketing/', pages.marketing_analyze),
    path('analyze/category/', pages.category_analyze),
    path('analyze/statistic/', pages.post_stat),

    # Access
    path('login/', access.userLogin),
    path('logout/', access.userLogout),
    path('signup/', access.userSignup),

    # Api
    path('check-username/', api.checkUserInsist),
    path('check-email/', api.checkEmailInsist),
    path('admin/', admin.site.urls),

]
