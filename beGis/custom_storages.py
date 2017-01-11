from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    bucket_name = 'begis-static'


class MediaStorage(S3BotoStorage):
    bucket_name = 'begis-media'
