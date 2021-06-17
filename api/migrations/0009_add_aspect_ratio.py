from django.db import migrations, models
import exiftool

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_image_path'),
    ]

    def forwards_func(apps, schema):
        Photo = apps.get_model('api', 'Photo')
        with exiftool.ExifTool() as et:
            for obj in Photo.objects.all():
                try:
                    height = et.get_tag('ImageHeight', obj.thumbnail_big.path)
                    width = et.get_tag('ImageWidth', obj.thumbnail_big.path)
                    obj.aspect_ratio = round((width /height), 2)
                    obj.save()
                except:
                    print('Cannot convert {} object'.format(obj.image_path))

    operations = [    
        migrations.AddField(model_name='Photo', name='aspect_ratio', field=models.FloatField(blank=True, null=True)),
        migrations.RunPython(forwards_func),
    ]