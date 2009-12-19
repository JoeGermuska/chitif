from __future__ import with_statement
from fabric.api import prompt, local
from fabric.context_managers import cd
import re
YES_OR_NO = re.compile("^(y|n|yes|no)$",re.IGNORECASE)

def yes_no(val):
    if YES_OR_NO.match(val):
        return val.lower() == 'y' or val.lower() == 'yes'
    raise Exception("Enter y or n")    

def init_local():
    if prompt("Are you sure you want to reset your local database?", default='N', validate=yes_no):
        print "Resetting Local database"
        local('dropdb chitif')
        local('dropuser chitif')
        local('createuser -S -D -R chitif')
        local('createdb -T template_postgis chitif')
        local('psql -U chitif < data/gis/init_srid.sql')
        with cd('chitif'):
            local('python ./manage.py syncdb --noinput')
            local('python ./manage.py load_tif_shapes')
            local('python ./manage.py load_expenditures')

    else:
        print "Aborted."    