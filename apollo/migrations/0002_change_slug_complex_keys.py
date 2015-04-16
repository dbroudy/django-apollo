# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PageContent.key'
        db.alter_column(u'apollo_pagecontent', 'key', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Removing index on 'PageContent', fields ['key']
        db.delete_index(u'apollo_pagecontent', ['key'])


    def backwards(self, orm):
        # Adding index on 'PageContent', fields ['key']
        db.create_index(u'apollo_pagecontent', ['key'])


        # Changing field 'PageContent.key'
        db.alter_column(u'apollo_pagecontent', 'key', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        u'apollo.answer': {
            'Meta': {'object_name': 'Answer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['apollo.Question']"})
        },
        u'apollo.button': {
            'Meta': {'object_name': 'Button'},
            'clicks': ('django.db.models.fields.IntegerField', [], {}),
            'confirm': ('ckeditor.fields.RichTextField', [], {}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'buttons'", 'to': u"orm['apollo.Page']"}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'+'", 'blank': 'True', 'to': u"orm['apollo.Question']"})
        },
        u'apollo.page': {
            'Meta': {'unique_together': "(['site', 'slug'],)", 'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'landing_pages'", 'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'apollo.pagecontent': {
            'Meta': {'unique_together': "(['page', 'key'],)", 'object_name': 'PageContent'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content'", 'to': u"orm['apollo.Page']"})
        },
        u'apollo.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stem': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'apollo.survey': {
            'Meta': {'object_name': 'Survey'},
            'button': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['apollo.Button']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apollo.surveyanswer': {
            'Meta': {'object_name': 'SurveyAnswer'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['apollo.Answer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['apollo.Question']"}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['apollo.Survey']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['apollo']