# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SurveyAnswer'
        db.create_table(u'landing_surveyanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['landing.Survey'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['landing.Question'])),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['landing.Answer'])),
        ))
        db.send_create_signal(u'landing', ['SurveyAnswer'])

        # Adding model 'Survey'
        db.create_table(u'landing_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('button', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['landing.Button'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'landing', ['Survey'])


    def backwards(self, orm):
        # Deleting model 'SurveyAnswer'
        db.delete_table(u'landing_surveyanswer')

        # Deleting model 'Survey'
        db.delete_table(u'landing_survey')


    models = {
        u'landing.answer': {
            'Meta': {'object_name': 'Answer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['landing.Question']"})
        },
        u'landing.button': {
            'Meta': {'object_name': 'Button'},
            'clicks': ('django.db.models.fields.IntegerField', [], {}),
            'confirm': ('ckeditor.fields.RichTextField', [], {}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'buttons'", 'to': u"orm['landing.Page']"}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'+'", 'blank': 'True', 'to': u"orm['landing.Question']"})
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
        u'landing.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stem': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'landing.survey': {
            'Meta': {'object_name': 'Survey'},
            'button': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['landing.Button']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'landing.surveyanswer': {
            'Meta': {'object_name': 'SurveyAnswer'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['landing.Answer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['landing.Question']"}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['landing.Survey']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['landing']