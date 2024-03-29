# Generated by Django 2.2.8 on 2020-05-16 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23, verbose_name='название')),
                ('active', models.BooleanField(default=True, verbose_name='активен')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram.Category', verbose_name='надкатегория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='MonthStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('doneorders', models.IntegerField(null=True, verbose_name='всего заказов')),
                ('monthsum', models.IntegerField(null=True, verbose_name='месячная сумма')),
            ],
            options={
                'verbose_name': 'статистика',
                'verbose_name_plural': 'статистика за месяц',
            },
        ),
        migrations.CreateModel(
            name='StatDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='день')),
                ('doneorders', models.IntegerField(null=True, verbose_name='всего в день')),
                ('daysum', models.IntegerField(null=True, verbose_name='сумма в день')),
            ],
            options={
                'verbose_name': 'статистика',
                'verbose_name_plural': 'статистика за день',
            },
        ),
        migrations.CreateModel(
            name='StatWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('doneorders', models.IntegerField(null=True, verbose_name='всего заказов')),
                ('weeksum', models.IntegerField(null=True, verbose_name='недельная сумма')),
            ],
            options={
                'verbose_name': 'статистика',
                'verbose_name_plural': 'статистика за неделю',
            },
        ),
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(unique=True, verbose_name='id пользователя')),
                ('phone', models.CharField(max_length=12, null=True, verbose_name='телефон')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='имя')),
                ('lang', models.CharField(max_length=2, null=True, verbose_name='язык')),
                ('location', models.CharField(max_length=100, null=True, verbose_name='местоположение')),
                ('step', models.IntegerField(default=0, null=True, verbose_name='шаг')),
                ('payment', models.CharField(max_length=100, null=True, verbose_name='способ оплаты')),
                ('delivery', models.BooleanField(default=True, verbose_name='доставка')),
                ('deferred', models.BooleanField(default=False, verbose_name='отложенный')),
                ('messageid', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23, verbose_name='название')),
                ('caption', models.CharField(max_length=1024, verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('pic', models.ImageField(blank=True, help_text='БЕЗ ИЗОБРАЖЕНИЯ НЕАКТИВЕН', null=True, upload_to='bot/', verbose_name='изображение')),
                ('photo', models.CharField(blank=True, max_length=1024, null=True)),
                ('active', models.BooleanField(default=True, verbose_name='активен')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram.Category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemandcost', models.CharField(default=None, max_length=2096, verbose_name='товары')),
                ('withmarkup', models.CharField(default=None, max_length=2096, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='время заказа')),
                ('total', models.CharField(max_length=101, verbose_name='сумма')),
                ('geo', models.CharField(max_length=100, null=True, verbose_name='локация')),
                ('deliver', models.BooleanField(default=False, null=True, verbose_name='доставка')),
                ('deferred', models.BooleanField(default=False, null=True, verbose_name='отложенный')),
                ('messageid', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100, verbose_name='состояние')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram.TgUser', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram.TgUser')),
            ],
        ),
    ]
