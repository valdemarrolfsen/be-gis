from django.conf.urls import url

from .views import TutorialListCreateView, TutorialDetailView, ResultListCreateView

urlpatterns = [

    # Tutorials
    url(r'^$',
        TutorialListCreateView.as_view(),
        name='tutorial-list-create'),

    url(r'^(?P<pk>[0-9]+)/$',
        TutorialDetailView.as_view(),
        name='tutorial-detail'
        ),

    url(r'^(?P<tutorial_pk>[0-9]+)/results/$',
        ResultListCreateView.as_view(),
        name='tutorial-result-list-create'
        )
]
