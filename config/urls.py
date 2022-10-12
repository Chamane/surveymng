from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from surveymng.main.views import (
    agent_looking,
    ajax_create_survey,
    ajax_get_questions,
    ajax_post_formsurvey,
    create_agent,
    create_formsurvey,
    create_survey,
    formsurvey_lookup,
    index,
    survey_lookup,
)

urlpatterns = [
    path("", index, name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("surveymng.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff:
    # create agent
    path("create/agent", create_agent, name="create-agent"),
    path("search/agent", agent_looking, name="search-agent"),
    path("create/survey", create_survey, name="create-survey"),
    path("search/survey", survey_lookup, name="search-survey"),
    path("create/form-survey", create_formsurvey, name="create-formsurvey"),
    path("search/form-survey", formsurvey_lookup, name="search-formsurvey"),
    path("ajax/create-survey", ajax_create_survey, name="ajax-create-survey"),
    path("ajax/questions", ajax_get_questions, name="ajax-get-question"),
    path("ajax/post/formsurvey", ajax_post_formsurvey, name="ajax-post-formsurvey"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
