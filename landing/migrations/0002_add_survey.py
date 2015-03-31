# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answer'
        db.create_table(u'landing_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['landing.Question'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'landing', ['Answer'])

        # Adding model 'Question'
        db.create_table(u'landing_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stem', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'landing', ['Question'])

        # Adding field 'Button.confirm'
        db.add_column(u'landing_button', 'confirm',
                      self.gf('ckeditor.fields.RichTextField')(default=''),
                      keep_default=False)

        # Adding field 'Button.clicks'
        db.add_column(u'landing_button', 'clicks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding M2M table for field questions on 'Button'
        m2m_table_name = db.shorten_name(u'landing_button_questions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('button', models.ForeignKey(orm[u'landing.button'], null=False)),
            ('question', models.ForeignKey(orm[u'landing.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['button_id', 'question_id'])


    def backwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table(u'landing_answer')

        # Deleting model 'Question'
        db.delete_table(u'landing_question')

        # Deleting field 'Button.confirm'
        db.delete_column(u'landing_button', 'confirm')

        # Deleting field 'Button.clicks'
        db.delete_column(u'landing_button', 'clicks')

        # Removing M2M table for field questions on 'Button'
        db.delete_table(db.shorten_name(u'landing_button_questions'))


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
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['landing']