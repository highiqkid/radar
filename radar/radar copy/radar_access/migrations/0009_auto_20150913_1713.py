# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('radar_access', '0008_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fetched', models.BooleanField(default=False)),
                ('location_country', models.CharField(max_length=3, choices=[(b'USA', b'USA'), (b'CAN', b'CAN'), (b'KOR', b'KOR')])),
                ('location_city', models.CharField(max_length=50, choices=[(b'USA', b'USA'), (b'CAN', b'CAN'), (b'KOR', b'KOR')])),
                ('stage_min', models.IntegerField(choices=[(0, b'Seed'), (1, b'Series A'), (2, b'Series B'), (3, b'Series C'), (4, b'Series D')])),
                ('stage_max', models.IntegerField(choices=[(0, b'Seed'), (1, b'Series A'), (2, b'Series B'), (3, b'Series C'), (4, b'Series D')])),
                ('founded_min', models.IntegerField(choices=[(2015, b'2015'), (2014, b'2014'), (2013, b'2013'), (2012, b'2012'), (2011, b'2011'), (2010, b'2010'), (2009, b'2009'), (2008, b'2008'), (2007, b'2007'), (2006, b'2006'), (2005, b'2005'), (2004, b'2004'), (2003, b'2003'), (2002, b'2002'), (2001, b'2001'), (2000, b'2000'), (1999, b'1999'), (1998, b'1998'), (1997, b'1997'), (1996, b'1996'), (1995, b'1995'), (1994, b'1994'), (1993, b'1993'), (1992, b'1992'), (1991, b'1991'), (1990, b'1990'), (1989, b'1989'), (1988, b'1988'), (1987, b'1987'), (1986, b'1986'), (1985, b'1985'), (1984, b'1984'), (1983, b'1983'), (1982, b'1982'), (1981, b'1981'), (1980, b'1980'), (1979, b'1979'), (1978, b'1978'), (1977, b'1977'), (1976, b'1976'), (1975, b'1975'), (1974, b'1974'), (1973, b'1973'), (1972, b'1972'), (1971, b'1971'), (1970, b'1970'), (1969, b'1969'), (1968, b'1968'), (1967, b'1967'), (1966, b'1966'), (1965, b'1965'), (1964, b'1964'), (1963, b'1963'), (1962, b'1962'), (1961, b'1961'), (1960, b'1960'), (1959, b'1959'), (1958, b'1958'), (1957, b'1957'), (1956, b'1956'), (1955, b'1955'), (1954, b'1954'), (1953, b'1953'), (1952, b'1952'), (1951, b'1951'), (1950, b'1950'), (1949, b'1949'), (1948, b'1948'), (1947, b'1947'), (1946, b'1946'), (1945, b'1945'), (1944, b'1944'), (1943, b'1943'), (1942, b'1942'), (1941, b'1941'), (1940, b'1940'), (1939, b'1939'), (1938, b'1938'), (1937, b'1937'), (1936, b'1936'), (1935, b'1935'), (1934, b'1934'), (1933, b'1933'), (1932, b'1932'), (1931, b'1931'), (1930, b'1930'), (1929, b'1929'), (1928, b'1928'), (1927, b'1927'), (1926, b'1926'), (1925, b'1925'), (1924, b'1924'), (1923, b'1923'), (1922, b'1922'), (1921, b'1921'), (1920, b'1920'), (1919, b'1919'), (1918, b'1918'), (1917, b'1917'), (1916, b'1916'), (1915, b'1915'), (1914, b'1914'), (1913, b'1913'), (1912, b'1912'), (1911, b'1911'), (1910, b'1910'), (1909, b'1909'), (1908, b'1908'), (1907, b'1907'), (1906, b'1906'), (1905, b'1905'), (1904, b'1904'), (1903, b'1903'), (1902, b'1902'), (1901, b'1901'), (1900, b'1900')])),
                ('founded_max', models.IntegerField(choices=[(2015, b'2015'), (2014, b'2014'), (2013, b'2013'), (2012, b'2012'), (2011, b'2011'), (2010, b'2010'), (2009, b'2009'), (2008, b'2008'), (2007, b'2007'), (2006, b'2006'), (2005, b'2005'), (2004, b'2004'), (2003, b'2003'), (2002, b'2002'), (2001, b'2001'), (2000, b'2000'), (1999, b'1999'), (1998, b'1998'), (1997, b'1997'), (1996, b'1996'), (1995, b'1995'), (1994, b'1994'), (1993, b'1993'), (1992, b'1992'), (1991, b'1991'), (1990, b'1990'), (1989, b'1989'), (1988, b'1988'), (1987, b'1987'), (1986, b'1986'), (1985, b'1985'), (1984, b'1984'), (1983, b'1983'), (1982, b'1982'), (1981, b'1981'), (1980, b'1980'), (1979, b'1979'), (1978, b'1978'), (1977, b'1977'), (1976, b'1976'), (1975, b'1975'), (1974, b'1974'), (1973, b'1973'), (1972, b'1972'), (1971, b'1971'), (1970, b'1970'), (1969, b'1969'), (1968, b'1968'), (1967, b'1967'), (1966, b'1966'), (1965, b'1965'), (1964, b'1964'), (1963, b'1963'), (1962, b'1962'), (1961, b'1961'), (1960, b'1960'), (1959, b'1959'), (1958, b'1958'), (1957, b'1957'), (1956, b'1956'), (1955, b'1955'), (1954, b'1954'), (1953, b'1953'), (1952, b'1952'), (1951, b'1951'), (1950, b'1950'), (1949, b'1949'), (1948, b'1948'), (1947, b'1947'), (1946, b'1946'), (1945, b'1945'), (1944, b'1944'), (1943, b'1943'), (1942, b'1942'), (1941, b'1941'), (1940, b'1940'), (1939, b'1939'), (1938, b'1938'), (1937, b'1937'), (1936, b'1936'), (1935, b'1935'), (1934, b'1934'), (1933, b'1933'), (1932, b'1932'), (1931, b'1931'), (1930, b'1930'), (1929, b'1929'), (1928, b'1928'), (1927, b'1927'), (1926, b'1926'), (1925, b'1925'), (1924, b'1924'), (1923, b'1923'), (1922, b'1922'), (1921, b'1921'), (1920, b'1920'), (1919, b'1919'), (1918, b'1918'), (1917, b'1917'), (1916, b'1916'), (1915, b'1915'), (1914, b'1914'), (1913, b'1913'), (1912, b'1912'), (1911, b'1911'), (1910, b'1910'), (1909, b'1909'), (1908, b'1908'), (1907, b'1907'), (1906, b'1906'), (1905, b'1905'), (1904, b'1904'), (1903, b'1903'), (1902, b'1902'), (1901, b'1901'), (1900, b'1900')])),
                ('money_raised_min', models.IntegerField(choices=[(0, b'$0'), (100000, b'$100K'), (500000, b'$500K'), (1000000, b'$1M'), (5000000, b'$5M'), (15000000, b'$15M'), (15000001, b'$15M+')])),
                ('money_raised_max', models.IntegerField(choices=[(0, b'$0'), (100000, b'$100K'), (500000, b'$500K'), (1000000, b'$1M'), (5000000, b'$5M'), (15000000, b'$15M'), (15000001, b'$15M+')])),
                ('employees_min', models.IntegerField(default=0, choices=[(1, b'1'), (5, b'5'), (15, b'15'), (25, b'25'), (50, b'50'), (100, b'100'), (250, b'250'), (251, b'250+')])),
                ('employees_max', models.IntegerField(default=0, choices=[(1, b'1'), (5, b'5'), (15, b'15'), (25, b'25'), (50, b'50'), (100, b'100'), (250, b'250'), (251, b'250+')])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='startup',
            name='is_my_company',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='is_prefiltered',
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='radar_access.Startup'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hidden',
            field=models.ManyToManyField(related_name='+', to='radar_access.Startup'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='filter',
            name='owner',
            field=models.ForeignKey(related_name='filters', to='radar_access.Profile'),
        ),
        migrations.AddField(
            model_name='filter',
            name='result',
            field=models.ManyToManyField(to='radar_access.Startup'),
        ),
        migrations.AddField(
            model_name='collection',
            name='owner',
            field=models.ForeignKey(related_name='collections', to='radar_access.Profile'),
        ),
        migrations.AddField(
            model_name='collection',
            name='startups',
            field=models.ManyToManyField(related_name='collections', to='radar_access.Startup'),
        ),
    ]
