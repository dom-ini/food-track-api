from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from FoodTrack.celery import app as celery_app  # noqa: F401
from FoodTrack.tasks import async_send_messages  # noqa: F401
