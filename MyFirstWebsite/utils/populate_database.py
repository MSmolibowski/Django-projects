####
import os
import sys

PROJECT_DIR = '/Users/andrzej/Desktop/venv/myproject'
os.chdir(PROJECT_DIR)

# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
sys.path.append(PROJECT_DIR)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
####

from blog.models import Post

# instances = []
# for i in range(1, 200):
# 	post = Post(title=f'Title {i}', body=f'Body {i}')
# 	instances.append(post)
# Post.objects.bulk_create(instances)

p = Post(title='My first post', body='This is body of my post.')
p.save()
p = Post(title='My second post', body='This is body of my second post.')
p.save()
p = Post(title='Hello world!', body='Third post')
p.save()
p = Post(title="My title", body="My body")
p.save()