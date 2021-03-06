# Generated by Django 3.1.6 on 2021-02-01 17:12

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.models.promo


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A client with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and -/_ only.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid username. This value may contain only letters, -,_', regex='^([a-z]|[a-zA-Z_-]){4,12}$')], verbose_name='username')),
                ('first_name', models.CharField(help_text='should be characters only with max length 50', max_length=150, validators=[django.core.validators.RegexValidator(message='Enter characters only', regex='^[a-zA-Z]+$')], verbose_name='first name')),
                ('last_name', models.CharField(help_text='should be characters only with max length 50', max_length=150, validators=[django.core.validators.RegexValidator(message='Enter characters only', regex='^[a-zA-Z]+$')], verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='email address')),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the client can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this client should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('type_account', models.SmallIntegerField(choices=[(1, 'Admin'), (2, 'Client')], null=True, verbose_name='type account')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_type', models.CharField(help_text='Required. 100 characters or fewer. Letters and numbers only.', max_length=100, validators=[django.core.validators.RegexValidator(message='Enter a valid promo type. Minimum 4 characters and should be contains letters and numbers only', regex='^[a-zA-Z0-9]{4,100}$')])),
                ('promo_code', models.CharField(default=users.models.promo.generate_promo_code, editable=False, max_length=300, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('promo_amount', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_promo',
            },
        ),
    ]
