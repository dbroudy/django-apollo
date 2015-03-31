# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'landing_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='landing_pages', to=orm['sites.Site'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'landing', ['Page'])

        # Adding unique constraint on 'Page', fields ['site', 'slug']
        db.create_unique(u'landing_page', ['site_id', 'slug'])

        # Adding model 'PageContent'
        db.create_table(u'landing_pagecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content', to=orm['landing.Page'])),
            ('key', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'landing', ['PageContent'])

        # Adding unique constraint on 'PageContent', fields ['page', 'key']
        db.create_unique(u'landing_pagecontent', ['page_id', 'key'])

        # Adding model 'Button'
        db.create_table(u'landing_button', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='buttons', to=orm['landing.Page'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'landing', ['Button'])


    def backwards(self, orm):
        # Removing unique constraint on 'PageContent', fields ['page', 'key']
        db.delete_unique(u'landing_pagecontent', ['page_id', 'key'])

        # Removing unique constraint on 'Page', fields ['site', 'slug']
        db.delete_unique(u'landing_page', ['site_id', 'slug'])

        # Deleting model 'Page'
        db.delete_table(u'landing_page')

        # Deleting model 'PageContent'
        db.delete_table(u'landing_pagecontent')

        # Deleting model 'Button'
        db.delete_table(u'landing_button')


    models = {
        u'landing.button': {
            'Meta': {'object_name': 'Button'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'buttons'", 'to': u"orm['landing.Page']"})
        },
        u'landing.page': {
            'Meta': {'unique_together': "(['site', 'slug'],)", 'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'landing_pages'", 'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'landing.pagecontent': {
            'Meta': {'unique_together': "(['page', 'key'],)", 'object_name': 'PageContent'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content'", 'to': u"orm['landing.Page']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['landing']