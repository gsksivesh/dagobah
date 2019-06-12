from setuptools import setup

setup(name='dagobah',
      version='0.3.3',
      description='Simple DAG-based job scheduler',
      url='https://github.com/gsksivesh/dagobah',
      author='Travis Thieman, Sivesh Guttula',
      author_email='kittusrikrishnasivesh@gmail.com',
      license='WTFPL',
      packages=['dagobah',
                'dagobah.backend',
                'dagobah.core',
                'dagobah.daemon',
                'dagobah.email'],
      package_data={'dagobah': ['email/templates/basic/*',
                                'daemon/static/css/*',
                                'daemon/static/js/*',
                                'daemon/static/img/*',
                                'daemon/static/lib/*.js',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/*.js',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/*.ks',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/affix/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/alert/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/button/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/carousel/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/collapse/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/dropdown/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/modal/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/popover/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/scrollspy/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/tab/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/tooltip/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/transition/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/bootstrap/typeahead/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/extras/fontawesome/font/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/retina/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/apps/tinygrowl/*',
                                'daemon/static/lib/Kickstrap1.3.2/Kickstrap/js/*.js',
                                'daemon/templates/*',
                                'daemon/dagobahd.yml']},
      install_requires=['croniter==0.3.30',
                        'python-dateutil==2.8.0',
                        'PyYAML==5.1',
                        'Flask==1.0.2',
                        'premailer==3.4.1',
                        'Flask-Login==0.4.1',
                        'semantic-version==2.6.0',
                        'paramiko==2.4.2',
                        'typing==3.6.6',
                        'future==0.17.1',
                        'py-dag==3.0.1',
                        'boto3'],
      test_suite='nose.collector',
      tests_require=['nose', 'pymongo'],
      entry_points={'console_scripts':
                        ['dagobahd = dagobah.daemon.app:daemon_entrypoint',
                         'echo_dagobah_conf = dagobah:print_standard_conf']
                    },
      zip_safe=False)
