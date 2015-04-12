# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'apollo_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stem', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'apollo', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'apollo_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['apollo.Question'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'apollo', ['Answer'])

        # Adding model 'Page'
        db.create_table(u'apollo_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='landing_pages', to=orm['sites.Site'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'apollo', ['Page'])

        # Adding unique constraint on 'Page', fields ['site', 'slug']
        db.create_unique(u'apollo_page', ['site_id', 'slug'])

        # Adding model 'PageContent'
        db.create_table(u'apollo_pagecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content', to=orm['apollo.Page'])),
            ('key', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'apollo', ['PageContent'])

        # Adding unique constraint on 'PageContent', fields ['page', 'key']
        db.create_unique(u'apollo_pagecontent', ['page_id', 'key'])

        # Adding model 'Button'
        db.create_table(u'apollo_button', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='buttons', to=orm['apollo.Page'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
            ('confirm', self.gf('ckeditor.fields.RichTextField')()),
            ('clicks', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'apollo', ['Button'])

        # Adding M2M table for field questions on 'Button'
        m2m_table_name = db.shorten_name(u'apollo_button_questions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('button', models.ForeignKey(orm[u'apollo.button'], null=False)),
            ('question', models.ForeignKey(orm[u'apollo.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['button_id', 'question_id'])

        # Adding model 'Survey'
        db.create_table(u'apollo_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('button', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['apollo.Button'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'apollo', ['Survey'])

        # Adding model 'SurveyAnswer'
        db.create_table(u'apollo_surveyanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['apollo.Survey'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['apollo.Question'])),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['apollo.Answer'])),
        ))
        db.send_create_signal(u'apollo', ['SurveyAnswer'])


    def backwards(self, orm):
        # Removing unique constraint on 'PageContent', fields ['page', 'key']
        db.delete_unique(u'apollo_pagecontent', ['page_id', 'key'])

        # Removing unique constraint on 'Page', fields ['site', 'slug']
        db.delete_unique(u'apollo_page', ['site_id', 'slug'])

        # Deleting model 'Question'
        db.delete_table(u'apollo_question')

        # Deleting model 'Answer'
        db.delete_table(u'apollo_answer')

        # Deleting model 'Page'
        db.delete_table(u'apollo_page')

        # Deleting model 'PageContent'
        db.delete_table(u'apollo_pagecontent')

        # Deleting model 'Button'
        db.delete_table(u'apollo_button')

        # Removing M2M table for field questions on 'Button'
        db.delete_table(db.shorten_name(u'apollo_button_questions'))

        # Deleting model 'Survey'
        db.delete_table(u'apollo_survey')

        # Deleting model 'SurveyAnswer'
        db.delete_table(u'apollo_surveyanswer')


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
            'key': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
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