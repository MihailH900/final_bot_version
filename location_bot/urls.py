"""aplication urls"""

from django.conf.urls import url
from location_bot.views import index, cartGenerate, generate_meet_point, MessageView

urlpatterns = [
    url('', index, name='location_bot'),
    url('cartGenerate/', cartGenerate, name='cartGenerate'),
    url('generate_meet_point/', generate_meet_point, name='generate_meet_point'),
    url('api/MessageView/', MessageView.as_view(), name='MessageView')
]
