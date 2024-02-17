from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from food_track.celery import app as celery_app  # noqa: F401
from food_track.tasks import async_send_messages  # noqa: F401
