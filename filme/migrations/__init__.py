

class Migration(migration.Migration):

    initial= True
    dependencies = [
    ]

    operations = [
    
    migrations.CreateModel(

            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('ano', models.IntegerField()),
                ('sinopse', models.CharField(max_length=1000)),
                ('genero', models.CharField(max_length=15)),
                ('diretor', models.CharField(max_length=60)),
            ],
        ),
    ]