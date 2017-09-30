import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lamdabotweb.settings")
django.setup()

from lamdabotweb.settings import SOURCEIMG_DIR, ALLOWED_EXTENSIONS
from memeviewer.models import MemeSourceImageOverride

deldir = os.path.join(SOURCEIMG_DIR, "deleted")
os.makedirs(deldir, exist_ok=True)

for file in os.listdir(SOURCEIMG_DIR):
    if re.match(ALLOWED_EXTENSIONS, file, re.IGNORECASE):
        img = MemeSourceImageOverride.objects.filter(name=file).first()
        if img is None:
            print(file)
            os.rename(os.path.join(SOURCEIMG_DIR, file), os.path.join(deldir, file))
