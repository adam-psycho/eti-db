# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EtiImage(models.Model):
    md5 = models.TextField(primary_key=True)
    filename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eti_image'


class EtiPost(models.Model):
    id = models.IntegerField(primary_key=True)
    topic = models.ForeignKey('EtiTopic', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    eti_user = models.ForeignKey('EtiUser', models.DO_NOTHING, db_column='eti_user', blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    sig = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eti_post'


class EtiTag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eti_tag'


class EtiTopic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    closed = models.NullBooleanField()
    archived = models.NullBooleanField()
    created = models.DateTimeField(blank=True, null=True)
    eti_user = models.ForeignKey('EtiUser', models.DO_NOTHING, db_column='eti_user', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    post_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eti_topic'


class EtiTopicsImages(models.Model):
    topic = models.ForeignKey(EtiTopic, models.DO_NOTHING, primary_key=True)
    image = models.ForeignKey(EtiImage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eti_topics_images'
        unique_together = (('topic', 'image'),)


class EtiUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    level = models.TextField(blank=True, null=True)
    formerly = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eti_user'
