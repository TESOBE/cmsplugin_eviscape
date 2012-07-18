# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EviscapeInstance.title'
        db.add_column('cmsplugin_eviscapeinstance', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Blog', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EviscapeInstance.title'
        db.delete_column('cmsplugin_eviscapeinstance', 'title')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_eviscape.eviscapeinstance': {
            'Meta': {'object_name': 'EviscapeInstance', 'db_table': "'cmsplugin_eviscapeinstance'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'evis_type': ('django.db.models.fields.CharField', [], {'default': "'blog'", 'max_length': '20'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5'}),
            'nod_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'server': ('django.db.models.fields.CharField', [], {'default': "'api.eviscape.com'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Blog'", 'max_length': '30'})
        }
    }

    complete_apps = ['cmsplugin_eviscape']