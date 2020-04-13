# pip-requirements-check
Simple tool for compare two requirements.txt files.

Example usage:
user@pc ~ $ python3 /some/path/rech.py --source1 /some/requirements.txt  --source2 ~/other/requirements.txt

Exaple output:
alembic==1.4.2  alembic==1.0
apache-airflow==1.10.9  None
apispec==1.3.3  None
argcomplete==1.11.1  argcomplete==1.10
attrs==19.3.0  attrs==19.3
Babel==2.8.0  None
zope.deprecation==4.4.0  zope.deprecation==4.0   
None  cached_property==1.5
None  enum34==1.1.6
None  flask==1.1.0
None  flask-admin==1.5.4
None  flask-appbuilder==1.12.2
None  flask-appbuilder==2.2

