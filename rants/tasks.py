from celery.utils.log import get_task_logger
from celery.decorators import task
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model


from config import celery_app

User = get_user_model()
logger = get_task_logger(__name__)

@task(name='create_user')
def create_user():
    email = 'test@test.com'
    user = User.objects.create_user(email=email, username=get_random_string(),
                                    password=get_random_string())
    logger.info("User Created")
    return user
