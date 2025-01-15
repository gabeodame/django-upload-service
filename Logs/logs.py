2024-06-17 14:43:00.012397: Error occurred while reading WSGI handler:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 791, in main
    env, handler = read_wsgi_handler(response.physical_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 633, in read_wsgi_handler
    handler = get_wsgi_handler(os.getenv("WSGI_HANDLER"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 616, in get_wsgi_handler
    raise ValueError('"%s" could not be imported%s' % (handler_name, last_tb))
ValueError: "rduploadservice.wsgi.application" could not be imported: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 600, in get_wsgi_handler
    handler = __import__(module_name, fromlist=[name_list[0][0]])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\wsgi.py", line 16, in <module>
    application = get_wsgi_application()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\wsgi.py", line 12, in get_wsgi_application
    django.setup(set_prefix=False)
  File "C:\Python312\Lib\site-packages\django\__init__.py", line 19, in setup
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
                      ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 89, in __getattr__
    self._setup(name)
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 76, in _setup
    self._wrapped = Settings(settings_module)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 190, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'myproject'



StdOut: 

StdErr: 
2024-06-17 14:43:00.014393: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 791, in main
    env, handler = read_wsgi_handler(response.physical_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 633, in read_wsgi_handler
    handler = get_wsgi_handler(os.getenv("WSGI_HANDLER"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 616, in get_wsgi_handler
    raise ValueError('"%s" could not be imported%s' % (handler_name, last_tb))
ValueError: "rduploadservice.wsgi.application" could not be imported: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 600, in get_wsgi_handler
    handler = __import__(module_name, fromlist=[name_list[0][0]])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\wsgi.py", line 16, in <module>
    application = get_wsgi_application()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\wsgi.py", line 12, in get_wsgi_application
    django.setup(set_prefix=False)
  File "C:\Python312\Lib\site-packages\django\__init__.py", line 19, in setup
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
                      ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 89, in __getattr__
    self._setup(name)
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 76, in _setup
    self._wrapped = Settings(settings_module)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 190, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'myproject'

2024-06-17 14:43:00.017392: Running on_exit tasks
2024-06-17 14:43:00.062395: wfastcgi.py 3.0.0 closed
2024-06-17 14:44:07.148577: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-17 14:44:07.149597: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-17 14:44:07.151578: unable to import ptvsd to enable debugging
2024-06-17 14:44:07.152576: wfastcgi.py 3.0.0 initialized
2024-06-17 14:46:21.686933: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-17 14:46:21.688932: Running on_exit tasks
2024-06-17 14:46:34.757802: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-17 14:46:34.759802: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-17 14:46:34.760802: unable to import ptvsd to enable debugging
2024-06-17 14:46:34.761802: wfastcgi.py 3.0.0 initialized
2024-06-17 14:51:49.061408: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-17 14:51:49.062401: Running on_exit tasks
2024-06-17 14:51:49.063404: wfastcgi.py 3.0.0 closed
2024-06-17 14:56:25.021525: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-17 14:56:25.023525: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-17 14:56:25.024524: unable to import ptvsd to enable debugging
2024-06-17 14:56:25.027524: wfastcgi.py 3.0.0 initialized
2024-06-17 15:01:39.294012: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-17 15:01:39.295007: Running on_exit tasks
2024-06-17 15:01:39.296009: wfastcgi.py 3.0.0 closed
2024-06-18 10:20:14.126396: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 10:20:14.127396: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 10:20:14.128396: unable to import ptvsd to enable debugging
2024-06-18 10:20:14.130401: wfastcgi.py 3.0.0 initialized
2024-06-18 10:22:00.760657: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 10:22:00.762664: Running on_exit tasks
2024-06-18 10:22:07.077276: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 10:22:07.078257: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 10:22:07.080259: unable to import ptvsd to enable debugging
2024-06-18 10:22:07.081258: wfastcgi.py 3.0.0 initialized
2024-06-18 10:22:35.649737: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 10:22:35.650741: Running on_exit tasks
2024-06-18 10:22:40.073234: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 10:22:40.075243: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 10:22:40.077233: unable to import ptvsd to enable debugging
2024-06-18 10:22:40.078244: wfastcgi.py 3.0.0 initialized
2024-06-18 10:27:54.380817: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 10:27:54.382821: Running on_exit tasks
2024-06-18 10:27:54.383831: wfastcgi.py 3.0.0 closed
2024-06-18 10:29:42.571837: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 10:29:42.573829: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 10:29:42.574827: unable to import ptvsd to enable debugging
2024-06-18 10:29:42.575832: wfastcgi.py 3.0.0 initialized
2024-06-18 10:32:24.556115: wfastcgi.py exiting because uploadservice\urls.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 10:32:24.557121: Running on_exit tasks
2024-06-18 10:33:07.798815: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 10:33:07.800819: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 10:33:07.801814: unable to import ptvsd to enable debugging
2024-06-18 10:33:07.802813: wfastcgi.py 3.0.0 initialized
2024-06-18 10:34:31.742979: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 10:34:31.744987: Running on_exit tasks
2024-06-18 10:37:18.560685: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 10:37:18.561682: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 10:37:18.563687: unable to import ptvsd to enable debugging
2024-06-18 10:37:18.564697: wfastcgi.py 3.0.0 initialized
2024-06-18 10:44:52.864406: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 10:44:52.866404: Running on_exit tasks
2024-06-18 10:44:52.867405: wfastcgi.py 3.0.0 closed
2024-06-18 10:59:48.535792: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 10:59:48.536783: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 10:59:48.538803: unable to import ptvsd to enable debugging
2024-06-18 10:59:48.540786: wfastcgi.py 3.0.0 initialized
2024-06-18 11:05:02.846361: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 11:05:02.848346: Running on_exit tasks
2024-06-18 11:05:02.849335: wfastcgi.py 3.0.0 closed
2024-06-18 11:09:30.832883: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 11:09:30.834879: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 11:09:30.835875: unable to import ptvsd to enable debugging
2024-06-18 11:09:30.837896: wfastcgi.py 3.0.0 initialized
2024-06-18 11:19:25.112278: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 11:19:25.113284: Running on_exit tasks
2024-06-18 11:19:25.115277: wfastcgi.py 3.0.0 closed
2024-06-18 11:29:25.990258: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 11:29:25.992258: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 11:29:25.993261: unable to import ptvsd to enable debugging
2024-06-18 11:29:25.994265: wfastcgi.py 3.0.0 initialized
2024-06-18 11:38:10.229608: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 11:38:10.231615: Running on_exit tasks
2024-06-18 11:38:10.232609: wfastcgi.py 3.0.0 closed
2024-06-18 13:12:03.544130: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:12:03.545138: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:12:03.547129: unable to import ptvsd to enable debugging
2024-06-18 13:12:03.549130: wfastcgi.py 3.0.0 initialized
2024-06-18 13:17:17.757588: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 13:17:17.759592: Running on_exit tasks
2024-06-18 13:17:17.760584: wfastcgi.py 3.0.0 closed
2024-06-18 13:21:33.598576: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:21:33.600573: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:21:33.602565: unable to import ptvsd to enable debugging
2024-06-18 13:21:33.603570: wfastcgi.py 3.0.0 initialized
2024-06-18 13:23:38.217131: wfastcgi.py exiting because uploadservice\urls.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 13:23:38.218161: Running on_exit tasks
2024-06-18 13:23:53.357180: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:23:53.358187: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:23:53.360173: unable to import ptvsd to enable debugging
2024-06-18 13:23:53.361183: wfastcgi.py 3.0.0 initialized
2024-06-18 13:30:46.999450: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 13:30:47.000456: Running on_exit tasks
2024-06-18 13:30:47.002448: wfastcgi.py 3.0.0 closed
2024-06-18 13:31:29.565042: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:31:29.568042: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:31:29.569033: unable to import ptvsd to enable debugging
2024-06-18 13:31:29.570034: wfastcgi.py 3.0.0 initialized
2024-06-18 13:37:21.668886: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 13:37:21.670893: Running on_exit tasks
2024-06-18 13:52:49.987451: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:52:49.989459: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:52:49.991451: unable to import ptvsd to enable debugging
2024-06-18 13:52:49.992462: wfastcgi.py 3.0.0 initialized
2024-06-18 13:55:34.737738: wfastcgi.py exiting because uploadservice\serializers.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 13:55:34.739740: Running on_exit tasks
2024-06-18 13:56:42.870684: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:56:42.871686: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:56:42.873682: unable to import ptvsd to enable debugging
2024-06-18 13:56:42.874679: wfastcgi.py 3.0.0 initialized
2024-06-18 13:56:47.373760: Error occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    callback, callback_args, callback_kwargs = self.resolve_request(request)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 313, in resolve_request
    resolver_match = resolver.resolve(request.path_info)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 847, in main
    result = handler(record.params, response.start)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\wsgi.py", line 124, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
ImportError: cannot import name 'index' from 'uploadservice.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py)


StdOut: 

StdErr: 
2024-06-18 13:59:12.385357: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 13:59:12.389359: Running on_exit tasks
2024-06-18 13:59:23.167700: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:59:23.170694: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:59:23.173698: unable to import ptvsd to enable debugging
2024-06-18 13:59:23.175695: wfastcgi.py 3.0.0 initialized
2024-06-18 13:59:47.695076: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 13:59:47.699077: Running on_exit tasks
2024-06-18 13:59:51.804893: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 13:59:51.808877: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 13:59:51.811894: unable to import ptvsd to enable debugging
2024-06-18 13:59:51.813902: wfastcgi.py 3.0.0 initialized
2024-06-18 14:05:06.128844: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 14:05:06.133841: Running on_exit tasks
2024-06-18 14:05:06.137841: wfastcgi.py 3.0.0 closed
2024-06-18 14:07:12.091869: Error occurred while reading WSGI handler:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 791, in main
    env, handler = read_wsgi_handler(response.physical_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 633, in read_wsgi_handler
    handler = get_wsgi_handler(os.getenv("WSGI_HANDLER"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 600, in get_wsgi_handler
    handler = __import__(module_name, fromlist=[name_list[0][0]])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\wsgi.py", line 16, in <module>
    application = get_wsgi_application()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\wsgi.py", line 12, in get_wsgi_application
    django.setup(set_prefix=False)
  File "C:\Python312\Lib\site-packages\django\__init__.py", line 19, in setup
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
                      ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 89, in __getattr__
    self._setup(name)
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 76, in _setup
    self._wrapped = Settings(settings_module)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 190, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\settings.py", line 133, in <module>
    MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
                                              ^^
NameError: name 'os' is not defined. Did you forget to import 'os'


StdOut: 

StdErr: 
2024-06-18 14:07:12.095875: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 791, in main
    env, handler = read_wsgi_handler(response.physical_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 633, in read_wsgi_handler
    handler = get_wsgi_handler(os.getenv("WSGI_HANDLER"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 600, in get_wsgi_handler
    handler = __import__(module_name, fromlist=[name_list[0][0]])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\wsgi.py", line 16, in <module>
    application = get_wsgi_application()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\wsgi.py", line 12, in get_wsgi_application
    django.setup(set_prefix=False)
  File "C:\Python312\Lib\site-packages\django\__init__.py", line 19, in setup
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
                      ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 89, in __getattr__
    self._setup(name)
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 76, in _setup
    self._wrapped = Settings(settings_module)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\conf\__init__.py", line 190, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\settings.py", line 133, in <module>
    MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
                                              ^^
NameError: name 'os' is not defined. Did you forget to import 'os'
2024-06-18 14:07:12.098876: Running on_exit tasks
2024-06-18 14:07:12.100874: wfastcgi.py 3.0.0 closed
2024-06-18 14:07:52.394675: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:07:52.397738: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:07:52.400666: unable to import ptvsd to enable debugging
2024-06-18 14:07:52.404657: wfastcgi.py 3.0.0 initialized
2024-06-18 14:11:17.306814: wfastcgi.py exiting because uploadservice\models.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 14:11:17.311815: Running on_exit tasks
2024-06-18 14:15:53.017028: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:15:53.021028: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:15:53.026034: unable to import ptvsd to enable debugging
2024-06-18 14:15:53.028039: wfastcgi.py 3.0.0 initialized
2024-06-18 14:15:57.453089: Error occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    callback, callback_args, callback_kwargs = self.resolve_request(request)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 313, in resolve_request
    resolver_match = resolver.resolve(request.path_info)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 847, in main
    result = handler(record.params, response.start)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\wsgi.py", line 124, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?


StdOut: 

StdErr: 
2024-06-18 14:16:11.756188: Error occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    callback, callback_args, callback_kwargs = self.resolve_request(request)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 313, in resolve_request
    resolver_match = resolver.resolve(request.path_info)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 847, in main
    result = handler(record.params, response.start)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\wsgi.py", line 124, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 55
    "uploaded_file_id": uploaded_file_record.id
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?


StdOut: 

StdErr: 
2024-06-18 14:16:27.604256: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 14:16:27.611255: Running on_exit tasks
2024-06-18 14:16:33.651539: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:16:33.659577: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:16:33.665536: unable to import ptvsd to enable debugging
2024-06-18 14:16:33.672536: wfastcgi.py 3.0.0 initialized
2024-06-18 14:24:07.936064: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 14:24:07.998063: Running on_exit tasks
2024-06-18 14:24:08.055066: wfastcgi.py 3.0.0 closed
2024-06-18 14:28:28.500648: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:28:28.507651: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:28:28.512664: unable to import ptvsd to enable debugging
2024-06-18 14:28:28.517659: wfastcgi.py 3.0.0 initialized
2024-06-18 14:29:02.959968: wfastcgi.py exiting because uploadservice\urls.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 14:29:02.965969: Running on_exit tasks
2024-06-18 14:29:09.580473: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:29:09.587471: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:29:09.592476: unable to import ptvsd to enable debugging
2024-06-18 14:29:09.597466: wfastcgi.py 3.0.0 initialized
2024-06-18 14:31:02.045289: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 14:31:02.051923: Running on_exit tasks
2024-06-18 14:31:08.466054: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:31:08.472038: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:31:08.478040: unable to import ptvsd to enable debugging
2024-06-18 14:31:08.483045: wfastcgi.py 3.0.0 initialized
2024-06-18 14:31:13.140638: Error occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    callback, callback_args, callback_kwargs = self.resolve_request(request)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 313, in resolve_request
    resolver_match = resolver.resolve(request.path_info)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 847, in main
    result = handler(record.params, response.start)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\wsgi.py", line 124, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 2, in <module>
    from .views import FileUploadView, index
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\views.py", line 17
    def post(self, request, folder, brand_name, date=None, kind, *args, **kwargs):
                                                           ^^^^
SyntaxError: parameter without a default follows parameter with a default


StdOut: 

StdErr: 
2024-06-18 14:32:21.208474: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-18 14:32:21.216476: Running on_exit tasks
2024-06-18 14:32:28.305576: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:32:28.312580: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:32:28.318572: unable to import ptvsd to enable debugging
2024-06-18 14:32:28.325578: wfastcgi.py 3.0.0 initialized
2024-06-18 14:37:42.577506: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 14:37:42.585507: Running on_exit tasks
2024-06-18 14:37:42.593508: wfastcgi.py 3.0.0 closed
2024-06-18 14:41:09.535962: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-18 14:41:09.543946: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-18 14:41:09.552949: unable to import ptvsd to enable debugging
2024-06-18 14:41:09.559960: wfastcgi.py 3.0.0 initialized
2024-06-18 15:05:03.498082: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-18 15:05:03.506091: Running on_exit tasks
2024-06-18 15:05:03.514084: wfastcgi.py 3.0.0 closed
2024-06-19 09:51:36.320064: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 09:51:36.326073: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 09:51:36.333072: unable to import ptvsd to enable debugging
2024-06-19 09:51:36.339069: wfastcgi.py 3.0.0 initialized
2024-06-19 09:56:21.660962: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-19 09:56:21.669948: Running on_exit tasks
2024-06-19 09:56:28.915018: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 09:56:28.922016: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 09:56:28.927021: unable to import ptvsd to enable debugging
2024-06-19 09:56:28.935016: wfastcgi.py 3.0.0 initialized
2024-06-19 09:59:34.627833: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-19 09:59:34.636835: Running on_exit tasks
2024-06-19 11:32:17.885933: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 11:32:17.899932: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 11:32:17.906938: unable to import ptvsd to enable debugging
2024-06-19 11:32:17.913933: wfastcgi.py 3.0.0 initialized
2024-06-19 11:32:52.022885: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-19 11:32:52.029884: Running on_exit tasks
2024-06-19 11:32:57.109404: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 11:32:57.116393: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 11:32:57.121395: unable to import ptvsd to enable debugging
2024-06-19 11:32:57.128393: wfastcgi.py 3.0.0 initialized
2024-06-19 11:33:23.206810: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-19 11:33:23.216809: Running on_exit tasks
2024-06-19 11:33:26.371869: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 11:33:26.378872: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 11:33:26.384866: unable to import ptvsd to enable debugging
2024-06-19 11:33:26.390870: wfastcgi.py 3.0.0 initialized
2024-06-19 11:38:40.580993: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 11:38:40.592996: Running on_exit tasks
2024-06-19 11:38:40.600002: wfastcgi.py 3.0.0 closed
2024-06-19 11:58:05.947771: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 11:58:05.953786: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 11:58:05.953786: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 11:58:05.968772: unable to import ptvsd to enable debugging
2024-06-19 11:58:05.968772: unable to import ptvsd to enable debugging
2024-06-19 11:58:05.982778: wfastcgi.py 3.0.0 initialized
2024-06-19 11:58:05.982778: wfastcgi.py 3.0.0 initialized
2024-06-19 11:58:05.982778: wfastcgi.py 3.0.0 initialized
2024-06-19 12:03:14.832595: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 12:03:14.847595: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 12:03:14.996601: Running on_exit tasks
2024-06-19 12:03:14.997602: Running on_exit tasks
2024-06-19 12:03:15.113601: wfastcgi.py 3.0.0 closed
2024-06-19 12:03:15.136601: wfastcgi.py 3.0.0 closed
2024-06-19 12:04:59.732940: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 12:04:59.741928: Running on_exit tasks
2024-06-19 12:04:59.751932: wfastcgi.py 3.0.0 closed
2024-06-19 12:06:21.494793: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:06:21.504794: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:06:21.510795: unable to import ptvsd to enable debugging
2024-06-19 12:06:21.524791: wfastcgi.py 3.0.0 initialized
2024-06-19 12:06:59.835230: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-19 12:06:59.843229: Running on_exit tasks
2024-06-19 12:07:06.585153: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:07:06.592149: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:07:06.599142: unable to import ptvsd to enable debugging
2024-06-19 12:07:06.605158: wfastcgi.py 3.0.0 initialized
2024-06-19 12:10:59.822798: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:10:59.836799: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:10:59.836799: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:10:59.848797: unable to import ptvsd to enable debugging
etpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:10:59.856797: unable to import ptvsd to enable debugging
2024-06-19 12:10:59.867798: wfastcgi.py 3.0.0 initialized
2024-06-19 12:13:26.478092: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-19 12:13:26.478092: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-19 12:13:26.492099: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-19 12:13:26.492099: Running on_exit tasks
2024-06-19 12:13:26.522094: Running on_exit tasks
2024-06-19 12:16:36.044776: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:16:36.053775: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:16:36.060779: unable to import ptvsd to enable debugging
2024-06-19 12:16:36.067776: wfastcgi.py 3.0.0 initialized
2024-06-19 12:16:36.086777: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:16:36.094778: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:16:36.102777: unable to import ptvsd to enable debugging
2024-06-19 12:16:36.110780: wfastcgi.py 3.0.0 initialized
2024-06-19 12:16:36.132778: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:16:36.140790: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:16:36.149777: unable to import ptvsd to enable debugging
2024-06-19 12:16:36.157786: wfastcgi.py 3.0.0 initialized
2024-06-19 12:24:10.003619: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 12:24:10.003619: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 12:24:10.023621: Running on_exit tasks
2024-06-19 12:24:10.023621: Running on_exit tasks
wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 12:24:10.030615: wfastcgi.py 3.0.0 closed
2024-06-19 12:24:10.030615: wfastcgi.py 3.0.0 closed
2024-06-19 12:24:10.044611: wfastcgi.py 3.0.0 closed
2024-06-19 12:40:31.641096: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 12:40:31.647094: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 12:40:31.655103: unable to import ptvsd to enable debugging
2024-06-19 12:40:31.661100: wfastcgi.py 3.0.0 initialized
2024-06-19 12:45:45.803900: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 12:45:45.809892: Running on_exit tasks
2024-06-19 12:45:45.819891: wfastcgi.py 3.0.0 closed
2024-06-19 14:12:14.463984: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 14:12:14.470962: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 14:12:14.476962: unable to import ptvsd to enable debugging
2024-06-19 14:12:14.483960: wfastcgi.py 3.0.0 initialized
2024-06-19 14:13:22.248656: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 14:13:22.258660: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 14:13:22.267659: unable to import ptvsd to enable debugging
2024-06-19 14:13:22.274658: wfastcgi.py 3.0.0 initialized
2024-06-19 14:13:32.472247: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 14:13:32.736262: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 14:13:32.744263: unable to import ptvsd to enable debugging
2024-06-19 14:13:32.752264: wfastcgi.py 3.0.0 initialized
2024-06-19 14:18:32.538636: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 14:18:32.553631: Running on_exit tasks
2024-06-19 14:18:32.559627: wfastcgi.py 3.0.0 closed
2024-06-19 14:18:35.934758: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 14:18:35.940759: Running on_exit tasks
2024-06-19 14:18:35.941760: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 14:18:35.955759: wfastcgi.py 3.0.0 closed
2024-06-19 14:18:35.961761: wfastcgi.py 3.0.0 closed
2024-06-19 14:59:52.431743: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 14:59:52.437752: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 14:59:52.444758: unable to import ptvsd to enable debugging
2024-06-19 14:59:52.450743: wfastcgi.py 3.0.0 initialized
2024-06-19 15:00:06.425650: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 15:00:06.434652: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 15:00:06.453652: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 15:00:06.462653: wfastcgi.py 3.0.0 initialized
e debugging
2024-06-19 15:00:06.470651: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 15:00:06.470651: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 15:00:06.470651: wfastcgi.py 3.0.0 initialized
2024-06-19 15:00:06.485653: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 15:00:06.494654: unable to import ptvsd to enable debugging
2024-06-19 15:00:06.501656: wfastcgi.py 3.0.0 initialized
2024-06-19 15:00:06.898682: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 15:00:06.909675: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 15:00:06.919675: unable to import ptvsd to enable debugging
2024-06-19 15:00:06.925689: wfastcgi.py 3.0.0 initialized
2024-06-19 15:05:20.503780: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 15:05:20.576785: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 15:05:20.576785: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 15:05:20.576785: Running on_exit tasks
2024-06-19 15:05:20.621786: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 15:05:20.621786: Running on_exit tasks
2024-06-19 15:05:20.621786: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 15:05:20.649786: Running on_exit tasks
2024-06-19 15:05:20.651787: wfastcgi.py 3.0.0 closed
2024-06-19 15:05:20.672788: Running on_exit tasks
2024-06-19 15:05:20.715792: wfastcgi.py 3.0.0 closed
2024-06-19 15:05:21.001805: Running on_exit tasks
2024-06-19 15:05:21.031805: wfastcgi.py 3.0.0 closed
2024-06-19 15:05:21.266821: wfastcgi.py 3.0.0 closed
2024-06-19 15:05:21.279819: wfastcgi.py 3.0.0 closed
2024-06-19 15:05:38.404696: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 15:05:38.412692: Running on_exit tasks
2024-06-19 15:05:38.426694: wfastcgi.py 3.0.0 closed
2024-06-19 16:02:40.064636: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:02:40.072637: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:02:40.080636: unable to import ptvsd to enable debugging
2024-06-19 16:02:40.088643: wfastcgi.py 3.0.0 initialized
2024-06-19 16:02:46.815613: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:02:46.825614: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:02:46.892614: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:02:46.893617: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:02:46.908614: unable to import ptvsd to enable debugging
2024-06-19 16:02:46.908614: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:02:46.921617: wfastcgi.py 3.0.0 initialized
iles in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:02:46.922616: unable to import ptvsd to enable debugging
2024-06-19 16:02:46.942617: wfastcgi.py 3.0.0 initialized
e debugging
2024-06-19 16:02:47.081623: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:02:47.089620: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:02:47.098620: unable to import ptvsd to enable debugging
2024-06-19 16:02:47.104621: wfastcgi.py 3.0.0 initialized
2024-06-19 16:02:47.330628: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:02:47.339629: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:02:47.346636: unable to import ptvsd to enable debugging
2024-06-19 16:02:47.352628: wfastcgi.py 3.0.0 initialized
2024-06-19 16:07:51.841064: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:07:51.848021: Running on_exit tasks
2024-06-19 16:07:51.854026: wfastcgi.py 3.0.0 closed
2024-06-19 16:08:00.833342: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:08:00.840333: Running on_exit tasks
2024-06-19 16:08:00.840333: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:08:00.840333: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:08:00.859344: wfastcgi.py 3.0.0 closed
2024-06-19 16:08:00.859344: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:08:00.879334: Running on_exit tasks
d
2024-06-19 16:08:00.879334: wfastcgi.py 3.0.0 closed
2024-06-19 16:08:00.888342: wfastcgi.py 3.0.0 closed
2024-06-19 16:09:05.746672: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:09:05.794674: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:09:05.801675: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:09:05.803673: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:09:05.816724: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:09:05.816724: unable to import ptvsd to enable debugging
2024-06-19 16:09:05.816724: unable to import ptvsd to enable debugging
2024-06-19 16:09:05.838679: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:09:05.838679: wfastcgi.py 3.0.0 initialized
2024-06-19 16:09:05.838679: wfastcgi.py 3.0.0 initialized
2024-06-19 16:09:05.846706: unable to import ptvsd to enable debugging
2024-06-19 16:09:05.957679: wfastcgi.py 3.0.0 initialized
2024-06-19 16:09:05.957679: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:09:05.999680: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:09:06.007679: unable to import ptvsd to enable debugging
2024-06-19 16:09:06.015679: wfastcgi.py 3.0.0 initialized
2024-06-19 16:09:06.059680: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-19 16:09:06.066680: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-19 16:09:06.074680: unable to import ptvsd to enable debugging
2024-06-19 16:09:06.081680: wfastcgi.py 3.0.0 initialized
2024-06-19 16:14:19.842598: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:14:19.852596: Running on_exit tasks
2024-06-19 16:14:19.861590: wfastcgi.py 3.0.0 closed
2024-06-19 16:14:19.887589: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:14:19.887589: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:14:19.907590: Running on_exit tasks
2024-06-19 16:14:19.907590: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:14:19.907590: Running on_exit tasks
2024-06-19 16:14:19.934593: wfastcgi.py 3.0.0 closed
2024-06-19 16:14:19.934593: Running on_exit tasks
2024-06-19 16:14:19.935591: wfastcgi.py 3.0.0 closed
2024-06-19 16:14:20.044593: wfastcgi.py 3.0.0 closed
2024-06-19 16:14:20.091596: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:14:20.105599: Running on_exit tasks
2024-06-19 16:14:20.117594: wfastcgi.py 3.0.0 closed
2024-06-19 16:14:25.864615: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-19 16:14:25.875614: Running on_exit tasks
2024-06-19 16:14:25.884601: wfastcgi.py 3.0.0 closed
2024-06-20 09:03:06.356702: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 09:03:06.370710: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 09:03:06.377710: unable to import ptvsd to enable debugging
2024-06-20 09:03:06.384711: wfastcgi.py 3.0.0 initialized
2024-06-20 09:08:19.131266: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-20 09:08:19.141254: Running on_exit tasks
2024-06-20 09:08:19.151256: wfastcgi.py 3.0.0 closed
2024-06-20 14:31:43.453026: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:31:43.461032: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:31:43.469032: unable to import ptvsd to enable debugging
2024-06-20 14:31:43.475036: wfastcgi.py 3.0.0 initialized
2024-06-20 14:40:59.792814: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-20 14:40:59.802822: Running on_exit tasks
2024-06-20 14:40:59.813819: wfastcgi.py 3.0.0 closed
2024-06-20 14:41:14.571470: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:41:14.578448: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:41:14.585449: unable to import ptvsd to enable debugging
2024-06-20 14:41:14.591465: wfastcgi.py 3.0.0 initialized
2024-06-20 14:41:22.986903: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:41:23.005903: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:41:23.005903: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:41:23.022904: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:41:23.022904: unable to import ptvsd to enable debugging
2024-06-20 14:41:23.031904: unable to import ptvsd to enable debugging
2024-06-20 14:41:23.031904: wfastcgi.py 3.0.0 initialized
2024-06-20 14:41:23.039902: wfastcgi.py 3.0.0 initialized
2024-06-20 14:41:23.178907: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:41:23.186908: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:41:23.194907: unable to import ptvsd to enable debugging
2024-06-20 14:41:23.202907: wfastcgi.py 3.0.0 initialized
2024-06-20 14:41:23.280910: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:41:23.287909: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:41:23.294918: unable to import ptvsd to enable debugging
2024-06-20 14:41:23.294918: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:41:23.301914: wfastcgi.py 3.0.0 initialized
iles in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:41:23.308920: unable to import ptvsd to enable debugging
2024-06-20 14:41:23.315910: wfastcgi.py 3.0.0 initialized
2024-06-20 14:45:25.069023: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-20 14:45:25.069023: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-20 14:45:25.085030: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-20 14:45:25.085030: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-20 14:45:25.085030: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-20 14:45:25.085030: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-20 14:45:25.107038: Running on_exit tasks
2024-06-20 14:45:25.107038: Running on_exit tasks
2024-06-20 14:45:25.108026: Running on_exit tasks
2024-06-20 14:45:25.108026: Running on_exit tasks
2024-06-20 14:45:25.139026: Running on_exit tasks
2024-06-20 14:45:38.498408: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-20 14:45:38.506401: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-20 14:45:38.514411: unable to import ptvsd to enable debugging
2024-06-20 14:45:38.520418: wfastcgi.py 3.0.0 initialized
2024-06-20 14:52:02.739512: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-20 14:52:02.746500: Running on_exit tasks
2024-06-20 14:52:02.753501: wfastcgi.py 3.0.0 closed
2024-06-21 11:01:25.418776: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-21 11:01:25.428778: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-21 11:01:25.437780: unable to import ptvsd to enable debugging
2024-06-21 11:01:25.447771: wfastcgi.py 3.0.0 initialized
2024-06-21 11:06:36.465908: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-21 11:06:36.473905: Running on_exit tasks
2024-06-21 11:06:36.482904: wfastcgi.py 3.0.0 closed
<<<<<<< HEAD
2024-06-21 11:47:00.074230: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-21 11:47:00.086221: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-21 11:47:00.094221: unable to import ptvsd to enable debugging
2024-06-21 11:47:00.103237: wfastcgi.py 3.0.0 initialized
2024-06-21 11:53:21.928028: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-21 11:53:21.935037: Running on_exit tasks
2024-06-21 11:53:21.942023: wfastcgi.py 3.0.0 closed
2024-06-24 11:49:26.102530: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-24 11:49:26.109567: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-24 11:49:26.116533: unable to import ptvsd to enable debugging
2024-06-24 11:49:26.124532: wfastcgi.py 3.0.0 initialized
2024-06-24 11:54:38.777393: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-24 11:54:38.787399: Running on_exit tasks
2024-06-24 11:54:38.794402: wfastcgi.py 3.0.0 closed
2024-06-24 13:54:10.063184: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-24 13:54:10.071183: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-24 13:54:10.081179: unable to import ptvsd to enable debugging
2024-06-24 13:54:10.089244: wfastcgi.py 3.0.0 initialized
2024-06-24 14:29:41.825670: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-24 14:29:41.835675: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-24 14:29:41.843665: unable to import ptvsd to enable debugging
2024-06-24 14:29:41.850679: wfastcgi.py 3.0.0 initialized
2024-06-24 14:34:53.122732: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-24 14:34:53.129748: Running on_exit tasks
2024-06-24 14:34:53.137730: wfastcgi.py 3.0.0 closed
2024-06-25 07:00:55.656790: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 07:00:55.664797: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 07:00:55.671806: unable to import ptvsd to enable debugging
2024-06-25 07:00:55.678810: wfastcgi.py 3.0.0 initialized
2024-06-25 07:07:53.621846: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 07:07:53.629833: Running on_exit tasks
2024-06-25 07:07:53.636838: wfastcgi.py 3.0.0 closed
2024-06-25 07:40:52.942151: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 07:40:52.950167: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 07:40:52.961153: unable to import ptvsd to enable debugging
2024-06-25 07:40:52.968157: wfastcgi.py 3.0.0 initialized
2024-06-25 07:46:03.396147: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 07:46:03.403154: Running on_exit tasks
2024-06-25 07:46:03.410153: wfastcgi.py 3.0.0 closed
2024-06-25 08:33:45.890236: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 08:33:45.897243: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 08:33:45.905248: unable to import ptvsd to enable debugging
2024-06-25 08:33:45.913239: wfastcgi.py 3.0.0 initialized
2024-06-25 08:35:19.141925: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 08:35:19.149858: Running on_exit tasks
2024-06-25 08:35:24.094638: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 08:35:24.105701: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 08:35:24.114648: unable to import ptvsd to enable debugging
2024-06-25 08:35:24.124642: wfastcgi.py 3.0.0 initialized
2024-06-25 08:52:14.153796: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 08:52:14.153796: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 08:52:14.175803: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 08:52:14.183858: unable to import ptvsd to enable debugging
2024-06-25 08:52:14.183858: unable to import ptvsd to enable debugging
2024-06-25 08:52:14.200805: wfastcgi.py 3.0.0 initialized
2024-06-25 08:57:25.127117: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 08:57:25.137122: Running on_exit tasks
2024-06-25 08:57:25.137122: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 08:57:25.137122: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 08:57:25.155117: Running on_exit tasks
2024-06-25 08:57:25.156116: wfastcgi.py 3.0.0 closed
2024-06-25 08:57:25.173114: Running on_exit tasks
d
2024-06-25 08:57:25.182112: wfastcgi.py 3.0.0 closed
2024-06-25 09:19:56.706977: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 09:19:56.714983: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 09:19:56.723977: unable to import ptvsd to enable debugging
2024-06-25 09:19:56.730989: wfastcgi.py 3.0.0 initialized
2024-06-25 09:25:10.869465: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 09:25:10.877497: Running on_exit tasks
2024-06-25 09:25:10.886457: wfastcgi.py 3.0.0 closed
2024-06-25 09:41:24.681361: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 09:41:24.694359: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 09:41:24.703358: unable to import ptvsd to enable debugging
2024-06-25 09:41:24.715358: wfastcgi.py 3.0.0 initialized
2024-06-25 09:46:38.863062: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 09:46:38.870067: Running on_exit tasks
2024-06-25 09:46:38.877054: wfastcgi.py 3.0.0 closed
2024-06-25 10:18:07.804210: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 10:18:07.825275: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 10:18:07.834258: unable to import ptvsd to enable debugging
2024-06-25 10:18:07.845277: wfastcgi.py 3.0.0 initialized
2024-06-25 10:23:21.927514: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 10:23:21.937504: Running on_exit tasks
2024-06-25 10:23:21.944504: wfastcgi.py 3.0.0 closed
2024-06-25 10:39:29.446821: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 10:39:29.454820: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 10:39:29.462825: unable to import ptvsd to enable debugging
2024-06-25 10:39:29.470897: wfastcgi.py 3.0.0 initialized
2024-06-25 10:43:20.344996: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 10:43:20.356000: Running on_exit tasks
2024-06-25 10:43:50.899220: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 10:43:50.907215: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 10:43:50.915217: unable to import ptvsd to enable debugging
2024-06-25 10:43:50.922209: wfastcgi.py 3.0.0 initialized
2024-06-25 10:50:15.108628: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 10:50:15.117625: Running on_exit tasks
2024-06-25 10:50:15.125627: wfastcgi.py 3.0.0 closed
2024-06-25 11:39:40.996969: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 11:39:41.005972: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 11:39:41.013974: unable to import ptvsd to enable debugging
2024-06-25 11:39:41.021970: wfastcgi.py 3.0.0 initialized
2024-06-25 11:44:55.131774: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 11:44:55.141764: Running on_exit tasks
2024-06-25 11:44:55.150765: wfastcgi.py 3.0.0 closed
2024-06-25 11:59:24.882456: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 11:59:24.891454: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 11:59:24.899457: unable to import ptvsd to enable debugging
2024-06-25 11:59:24.907459: wfastcgi.py 3.0.0 initialized
2024-06-25 11:59:41.607399: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 11:59:41.616400: Running on_exit tasks
2024-06-25 11:59:46.117183: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 11:59:46.125178: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 11:59:46.133185: unable to import ptvsd to enable debugging
2024-06-25 11:59:46.141179: wfastcgi.py 3.0.0 initialized
2024-06-25 12:01:13.281039: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 12:01:13.290038: Running on_exit tasks
2024-06-25 12:11:58.342146: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:11:58.350132: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:11:58.358211: unable to import ptvsd to enable debugging
2024-06-25 12:11:58.365139: wfastcgi.py 3.0.0 initialized
2024-06-25 12:13:03.473223: wfastcgi.py exiting because uploadservice\backends.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 12:13:03.484222: Running on_exit tasks
2024-06-25 12:13:08.673685: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:13:08.682697: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:13:08.690684: unable to import ptvsd to enable debugging
2024-06-25 12:13:08.699709: wfastcgi.py 3.0.0 initialized
2024-06-25 12:13:47.536336: wfastcgi.py exiting because uploadservice\backends.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 12:13:47.549338: Running on_exit tasks
2024-06-25 12:14:01.384850: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:14:01.393851: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:14:01.404859: unable to import ptvsd to enable debugging
2024-06-25 12:14:01.413948: wfastcgi.py 3.0.0 initialized
2024-06-25 12:18:38.845811: wfastcgi.py exiting because uploadservice\backends.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 12:18:38.856811: Running on_exit tasks
2024-06-25 12:35:37.291970: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:35:37.299977: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:35:37.307972: unable to import ptvsd to enable debugging
2024-06-25 12:35:37.314972: wfastcgi.py 3.0.0 initialized
2024-06-25 12:36:20.615690: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:36:20.661691: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:36:20.661691: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:36:20.671691: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:36:20.694692: unable to import ptvsd to enable debugging
2024-06-25 12:36:20.694692: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:36:20.711693: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:36:20.711693: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:36:20.711693: wfastcgi.py 3.0.0 initialized
2024-06-25 12:36:20.711693: unable to import ptvsd to enable debugging
2024-06-25 12:36:20.740692: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:36:20.742694: wfastcgi.py 3.0.0 initialized
2024-06-25 12:36:20.760695: wfastcgi.py 3.0.0 initialized
2024-06-25 12:36:20.763693: unable to import ptvsd to enable debugging
2024-06-25 12:36:20.798694: wfastcgi.py 3.0.0 initialized
2024-06-25 12:36:20.963697: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 12:36:20.972698: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 12:36:20.982699: unable to import ptvsd to enable debugging
2024-06-25 12:36:20.992698: wfastcgi.py 3.0.0 initialized
2024-06-25 12:41:34.719652: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 12:41:34.729653: Running on_exit tasks
2024-06-25 12:41:34.729653: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 12:41:34.729653: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 12:41:34.755656: wfastcgi.py 3.0.0 closed
2024-06-25 12:41:34.755656: Running on_exit tasks
2024-06-25 12:41:34.755656: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 12:41:34.756647: Running on_exit tasks
2024-06-25 12:41:34.799655: wfastcgi.py 3.0.0 closed
2024-06-25 12:41:34.799655: Running on_exit tasks
2024-06-25 12:41:34.800652: wfastcgi.py 3.0.0 closed
2024-06-25 12:41:34.916651: wfastcgi.py 3.0.0 closed
2024-06-25 12:42:01.514575: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 12:42:01.522570: Running on_exit tasks
2024-06-25 12:42:01.531568: wfastcgi.py 3.0.0 closed
2024-06-25 13:10:09.370975: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:10:09.380967: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:10:09.389965: unable to import ptvsd to enable debugging
2024-06-25 13:10:09.401981: wfastcgi.py 3.0.0 initialized
2024-06-25 13:10:10.857987: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:10:10.871988: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:10:10.871988: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:10:10.895987: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:10:10.895987: unable to import ptvsd to enable debugging
2024-06-25 13:10:10.909988: unable to import ptvsd to enable debugging
2024-06-25 13:10:10.919988: wfastcgi.py 3.0.0 initialized
2024-06-25 13:10:11.067989: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:10:11.080988: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:10:11.090988: unable to import ptvsd to enable debugging
2024-06-25 13:10:11.100988: wfastcgi.py 3.0.0 initialized
2024-06-25 13:10:11.202990: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:10:11.214992: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:10:11.226991: unable to import ptvsd to enable debugging
2024-06-25 13:10:11.234989: wfastcgi.py 3.0.0 initialized
2024-06-25 13:10:11.403994: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:10:11.435995: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:10:11.450994: unable to import ptvsd to enable debugging
2024-06-25 13:10:11.465995: wfastcgi.py 3.0.0 initialized
2024-06-25 13:12:46.880194: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 13:12:46.880194: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 13:12:46.902204: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 13:12:46.903195: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 13:12:46.925201: Running on_exit tasks
2024-06-25 13:12:46.925201: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 13:12:46.954195: Running on_exit tasks
2024-06-25 13:12:46.955200: Running on_exit tasks
2024-06-25 13:12:46.981194: Running on_exit tasks
2024-06-25 13:12:46.981194: Running on_exit tasks
2024-06-25 13:15:12.923978: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:15:12.932975: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:15:12.942017: unable to import ptvsd to enable debugging
2024-06-25 13:15:12.950971: wfastcgi.py 3.0.0 initialized
2024-06-25 13:21:37.090104: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 13:21:37.099109: Running on_exit tasks
2024-06-25 13:21:37.107111: wfastcgi.py 3.0.0 closed
2024-06-25 13:46:19.953393: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:46:19.962390: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:46:19.970391: unable to import ptvsd to enable debugging
2024-06-25 13:46:19.979405: wfastcgi.py 3.0.0 initialized
2024-06-25 13:46:36.537470: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-25 13:46:36.546464: Running on_exit tasks
2024-06-25 13:47:03.200744: Failed to import applicationinsights: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 639, in read_wsgi_handler
    from applicationinsights.requests import WSGIApplication
ModuleNotFoundError: No module named 'applicationinsights'
2024-06-25 13:47:03.208739: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 13:47:03.215743: unable to import ptvsd to enable debugging
2024-06-25 13:47:03.223739: wfastcgi.py 3.0.0 initialized
2024-06-25 13:52:52.486603: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-25 13:52:52.495600: Running on_exit tasks
2024-06-25 13:52:52.503602: wfastcgi.py 3.0.0 closed
2024-06-25 15:13:51.378706: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 15:13:51.415717: unable to import ptvsd to enable debugging
2024-06-25 15:13:51.424704: wfastcgi.py 3.0.0 initialized
2024-06-25 15:19:05.444620: Running on_exit tasks
2024-06-25 15:21:27.453989: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-25 15:21:27.488981: unable to import ptvsd to enable debugging
2024-06-25 15:21:27.499144: wfastcgi.py 3.0.0 initialized
2024-06-25 15:26:41.555197: Running on_exit tasks
2024-06-25 15:26:41.556189: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-28 06:48:45.189802: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 06:48:45.213805: unable to import ptvsd to enable debugging
2024-06-28 06:48:45.226807: wfastcgi.py 3.0.0 initialized
2024-06-28 06:53:53.918443: Running on_exit tasks
2024-06-28 06:53:53.919445: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-28 07:40:29.364079: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:40:29.379078: unable to import ptvsd to enable debugging
2024-06-28 07:40:29.381080: unable to import ptvsd to enable debugging
2024-06-28 07:40:29.427081: wfastcgi.py 3.0.0 initialized
2024-06-28 07:40:29.452087: wfastcgi.py 3.0.0 initialized
2024-06-28 07:40:29.453084: wfastcgi.py 3.0.0 initialized
2024-06-28 07:41:29.200756: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:41:29.212768: Running on_exit tasks
ause rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:41:29.232754: Running on_exit tasks
2024-06-28 07:41:29.233752: Running on_exit tasks
2024-06-28 07:42:08.863632: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:42:08.885633: unable to import ptvsd to enable debugging
2024-06-28 07:42:08.890630: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:42:08.937634: wfastcgi.py 3.0.0 initialized
e debugging
2024-06-28 07:42:08.939636: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:42:08.958634: wfastcgi.py 3.0.0 initialized
e debugging
2024-06-28 07:42:08.975635: wfastcgi.py 3.0.0 initialized
2024-06-28 07:42:45.213671: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:42:45.216740: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:42:45.251668: Running on_exit tasks
ause web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:42:45.280676: Running on_exit tasks
2024-06-28 07:45:54.046462: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:45:54.047462: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:45:54.078464: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:45:54.095458: unable to import ptvsd to enable debugging
2024-06-28 07:45:54.108456: wfastcgi.py 3.0.0 initialized
2024-06-28 07:45:54.108456: unable to import ptvsd to enable debugging
2024-06-28 07:45:54.122457: wfastcgi.py 3.0.0 initialized
2024-06-28 07:45:54.134456: unable to import ptvsd to enable debugging
2024-06-28 07:45:54.150458: wfastcgi.py 3.0.0 initialized
2024-06-28 07:46:18.268391: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:46:18.279385: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:46:18.279385: Running on_exit tasks
2024-06-28 07:46:18.291385: Running on_exit tasks
2024-06-28 07:46:18.292385: Running on_exit tasks
2024-06-28 07:47:12.631363: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:47:12.633360: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:47:12.669360: unable to import ptvsd to enable debugging
2024-06-28 07:47:12.681361: unable to import ptvsd to enable debugging
2024-06-28 07:47:12.690369: wfastcgi.py 3.0.0 initialized
2024-06-28 07:47:12.690369: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:47:12.735358: unable to import ptvsd to enable debugging
2024-06-28 07:47:12.745367: wfastcgi.py 3.0.0 initialized
2024-06-28 07:48:16.912828: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:48:17.010825: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 07:48:17.011830: Running on_exit tasks
2024-06-28 07:48:17.079826: Running on_exit tasks
2024-06-28 07:48:17.079826: Running on_exit tasks
2024-06-28 07:53:34.163668: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:53:34.163668: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:53:34.163668: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 07:53:34.192646: unable to import ptvsd to enable debugging
2024-06-28 07:53:34.208645: unable to import ptvsd to enable debugging
2024-06-28 07:53:34.212647: unable to import ptvsd to enable debugging
2024-06-28 07:53:34.235649: wfastcgi.py 3.0.0 initialized
2024-06-28 07:53:34.235649: wfastcgi.py 3.0.0 initialized
2024-06-28 07:53:34.235649: wfastcgi.py 3.0.0 initialized
2024-06-28 07:58:48.107922: Running on_exit tasks
2024-06-28 07:58:48.110880: Running on_exit tasks
2024-06-28 07:58:48.133880: Running on_exit tasks
2024-06-28 07:58:48.133880: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-28 08:40:56.313964: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 08:40:56.357965: unable to import ptvsd to enable debugging
2024-06-28 08:40:56.365971: wfastcgi.py 3.0.0 initialized
2024-06-28 08:46:09.053839: Running on_exit tasks
2024-06-28 09:25:10.928825: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 09:25:10.965838: unable to import ptvsd to enable debugging
2024-06-28 09:25:10.975837: wfastcgi.py 3.0.0 initialized
2024-06-28 09:30:24.931248: Running on_exit tasks
2024-06-28 09:30:24.931248: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-28 09:56:08.746763: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 09:56:08.785764: unable to import ptvsd to enable debugging
2024-06-28 09:56:08.796768: wfastcgi.py 3.0.0 initialized
2024-06-28 10:04:17.795423: Running on_exit tasks
2024-06-28 10:08:13.691191: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 10:08:13.729187: unable to import ptvsd to enable debugging
2024-06-28 10:08:13.739192: wfastcgi.py 3.0.0 initialized
2024-06-28 10:15:12.700916: Running on_exit tasks
2024-06-28 10:15:21.645959: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 10:15:21.681958: unable to import ptvsd to enable debugging
2024-06-28 10:15:21.691958: wfastcgi.py 3.0.0 initialized
2024-06-28 10:21:10.774495: Running on_exit tasks
2024-06-28 10:21:47.571310: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 10:21:47.613307: unable to import ptvsd to enable debugging
2024-06-28 10:21:47.622311: wfastcgi.py 3.0.0 initialized
2024-06-28 10:27:36.562442: Running on_exit tasks
2024-06-28 10:32:46.217543: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 10:32:46.257530: unable to import ptvsd to enable debugging
2024-06-28 10:32:46.266535: wfastcgi.py 3.0.0 initialized
2024-06-28 10:44:25.204722: Running on_exit tasks
2024-06-28 10:44:25.204722: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-28 10:58:11.297666: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 10:58:11.334665: unable to import ptvsd to enable debugging
2024-06-28 10:58:11.343671: wfastcgi.py 3.0.0 initialized
2024-06-28 11:06:55.416332: Running on_exit tasks
2024-06-28 11:45:40.920697: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 11:45:40.931699: unable to import ptvsd to enable debugging
2024-06-28 11:45:40.941703: wfastcgi.py 3.0.0 initialized
2024-06-28 11:50:53.754485: Running on_exit tasks
2024-06-28 11:54:01.582033: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 11:54:01.628042: unable to import ptvsd to enable debugging
2024-06-28 11:54:01.638038: wfastcgi.py 3.0.0 initialized
2024-06-28 12:01:09.755218: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-28 12:01:09.764218: Running on_exit tasks
2024-06-28 12:01:57.982413: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 12:01:57.984415: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 12:01:58.043415: unable to import ptvsd to enable debugging
etpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-28 12:01:58.054413: wfastcgi.py 3.0.0 initialized
2024-06-28 12:01:58.054413: wfastcgi.py 3.0.0 initialized
2024-06-28 12:01:58.054413: unable to import ptvsd to enable debugging
2024-06-28 12:01:58.079434: wfastcgi.py 3.0.0 initialized
2024-06-28 12:07:11.993612: Running on_exit tasks
2024-06-28 12:07:11.995613: Running on_exit tasks
2024-06-28 12:07:12.017614: Running on_exit tasks
2024-06-28 12:07:12.017614: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-06-30 17:21:30.590427: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-30 17:21:30.599430: unable to import ptvsd to enable debugging
2024-06-30 17:21:30.608421: wfastcgi.py 3.0.0 initialized
2024-06-30 17:29:29.117783: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-06-30 17:29:29.126781: Running on_exit tasks
2024-06-30 17:30:02.439181: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-30 17:30:02.520183: unable to import ptvsd to enable debugging
2024-06-30 17:30:02.538182: wfastcgi.py 3.0.0 initialized
2024-06-30 17:30:59.877909: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-06-30 17:30:59.891908: Running on_exit tasks
2024-06-30 17:41:05.501767: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-06-30 17:41:05.539772: unable to import ptvsd to enable debugging
2024-06-30 17:41:05.548762: wfastcgi.py 3.0.0 initialized
2024-06-30 17:55:04.552624: Running on_exit tasks
2024-06-30 17:55:04.552624: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-08 09:03:24.457429: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-08 09:03:24.479431: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-08 09:03:24.496461: unable to import ptvsd to enable debugging
2024-07-08 09:03:24.505433: wfastcgi.py 3.0.0 initialized
2024-07-08 09:08:17.974915: Running on_exit tasks
2024-07-08 09:08:56.538593: Running on_exit tasks
2024-07-08 09:08:56.538593: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-09 09:29:57.144697: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 09:29:57.155680: unable to import ptvsd to enable debugging
2024-07-09 09:29:57.164685: wfastcgi.py 3.0.0 initialized
2024-07-09 09:31:23.254439: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 09:31:23.254439: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 09:31:23.267435: unable to import ptvsd to enable debugging
2024-07-09 09:31:23.305441: unable to import ptvsd to enable debugging
2024-07-09 09:31:23.321468: wfastcgi.py 3.0.0 initialized
2024-07-09 09:36:37.500713: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-09 09:36:37.500713: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-09 09:36:37.501714: Running on_exit tasks
2024-07-09 09:36:37.510710: Running on_exit tasks
2024-07-09 09:36:37.643713: Running on_exit tasks
2024-07-09 09:36:37.643713: Running on_exit tasks
2024-07-09 09:36:55.064248: Running on_exit tasks
2024-07-09 09:36:55.064248: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-09 10:12:22.966346: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 10:12:22.966346: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 10:12:23.008338: unable to import ptvsd to enable debugging
2024-07-09 10:12:23.019339: unable to import ptvsd to enable debugging
2024-07-09 10:12:23.029338: wfastcgi.py 3.0.0 initialized
2024-07-09 10:17:37.043041: Running on_exit tasks
2024-07-09 10:19:22.039456: Running on_exit tasks
2024-07-09 10:19:22.051445: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-09 11:25:57.295378: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 11:25:57.312382: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 11:25:57.313381: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 11:25:57.331388: unable to import ptvsd to enable debugging
2024-07-09 11:25:57.331388: unable to import ptvsd to enable debugging
2024-07-09 11:25:57.331388: unable to import ptvsd to enable debugging
2024-07-09 11:25:57.348380: wfastcgi.py 3.0.0 initialized
2024-07-09 11:31:10.041257: Running on_exit tasks
2024-07-09 11:31:10.050264: Running on_exit tasks
2024-07-09 11:36:25.028753: Running on_exit tasks
2024-07-09 11:40:55.920391: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 11:40:55.921411: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 11:40:55.962402: unable to import ptvsd to enable debugging
2024-07-09 11:40:55.974403: wfastcgi.py 3.0.0 initialized
2024-07-09 11:40:55.974403: unable to import ptvsd to enable debugging
2024-07-09 11:40:55.983397: wfastcgi.py 3.0.0 initialized
2024-07-09 11:46:09.905268: Running on_exit tasks
2024-07-09 11:46:09.905268: Running on_exit tasks
2024-07-09 11:57:14.643930: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 11:57:14.680931: unable to import ptvsd to enable debugging
2024-07-09 11:57:14.691947: wfastcgi.py 3.0.0 initialized
2024-07-09 12:02:28.763333: Running on_exit tasks
2024-07-09 12:02:28.763333: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-09 12:06:52.952251: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 12:06:52.996250: unable to import ptvsd to enable debugging
2024-07-09 12:06:53.007272: wfastcgi.py 3.0.0 initialized
2024-07-09 12:17:57.058507: Running on_exit tasks
2024-07-09 12:17:57.058507: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-09 12:27:35.903789: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 12:27:35.943784: unable to import ptvsd to enable debugging
2024-07-09 12:27:35.955793: wfastcgi.py 3.0.0 initialized
2024-07-09 12:34:34.986072: Running on_exit tasks
2024-07-09 13:48:42.142234: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-09 13:48:42.182204: unable to import ptvsd to enable debugging
2024-07-09 13:48:42.196212: wfastcgi.py 3.0.0 initialized
2024-07-09 13:53:56.172161: Running on_exit tasks
2024-07-09 13:53:56.172161: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-10 07:02:52.292526: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 07:02:52.304519: unable to import ptvsd to enable debugging
2024-07-10 07:02:52.314520: wfastcgi.py 3.0.0 initialized
2024-07-10 07:08:04.898168: Running on_exit tasks
2024-07-10 07:24:18.664110: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 07:24:18.699111: unable to import ptvsd to enable debugging
2024-07-10 07:24:18.709117: wfastcgi.py 3.0.0 initialized
2024-07-10 07:29:32.775507: Running on_exit tasks
2024-07-10 07:50:57.527187: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 07:50:57.563187: unable to import ptvsd to enable debugging
2024-07-10 07:50:57.573199: wfastcgi.py 3.0.0 initialized
2024-07-10 07:53:38.115684: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-10 07:53:38.124676: Running on_exit tasks
2024-07-10 07:53:45.357011: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 07:53:45.398006: unable to import ptvsd to enable debugging
2024-07-10 07:53:45.406019: wfastcgi.py 3.0.0 initialized
2024-07-10 08:00:58.267845: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-10 08:00:58.290844: Running on_exit tasks
2024-07-10 08:15:14.795160: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 08:15:14.835151: unable to import ptvsd to enable debugging
2024-07-10 08:15:14.847162: wfastcgi.py 3.0.0 initialized
2024-07-10 08:20:28.855922: Running on_exit tasks
2024-07-10 08:40:07.242095: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 08:40:07.279101: unable to import ptvsd to enable debugging
2024-07-10 08:40:07.289101: wfastcgi.py 3.0.0 initialized
2024-07-10 08:45:56.382439: Running on_exit tasks
2024-07-10 08:45:56.382439: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-10 09:17:53.454306: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 09:17:53.495300: unable to import ptvsd to enable debugging
2024-07-10 09:17:53.504293: wfastcgi.py 3.0.0 initialized
2024-07-10 09:23:42.554289: Running on_exit tasks
2024-07-10 09:23:42.554289: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-10 10:24:51.087235: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 10:24:51.130224: unable to import ptvsd to enable debugging
2024-07-10 10:24:51.141218: wfastcgi.py 3.0.0 initialized
2024-07-10 10:29:03.488601: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-10 10:29:03.501599: Running on_exit tasks
2024-07-10 15:10:20.346392: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-10 15:10:20.359383: unable to import ptvsd to enable debugging
2024-07-10 15:10:20.367389: wfastcgi.py 3.0.0 initialized
2024-07-10 15:20:13.203691: Running on_exit tasks
2024-07-12 07:18:47.836569: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:18:47.862570: unable to import ptvsd to enable debugging
2024-07-12 07:18:47.874572: wfastcgi.py 3.0.0 initialized
2024-07-12 07:23:59.237143: Running on_exit tasks
2024-07-12 07:35:21.236222: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:35:21.276222: unable to import ptvsd to enable debugging
2024-07-12 07:35:21.290213: wfastcgi.py 3.0.0 initialized
2024-07-12 07:35:52.184010: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 07:35:52.197010: Running on_exit tasks
2024-07-12 07:36:32.485904: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:36:32.526914: unable to import ptvsd to enable debugging
2024-07-12 07:36:32.536898: wfastcgi.py 3.0.0 initialized
2024-07-12 07:38:43.481527: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 07:38:43.494530: Running on_exit tasks
2024-07-12 07:39:14.727250: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:39:14.767270: unable to import ptvsd to enable debugging
2024-07-12 07:39:14.779259: wfastcgi.py 3.0.0 initialized
2024-07-12 07:39:30.371920: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 07:39:30.385920: Running on_exit tasks
2024-07-12 07:39:50.926091: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:39:50.964081: unable to import ptvsd to enable debugging
2024-07-12 07:39:50.974097: wfastcgi.py 3.0.0 initialized
2024-07-12 07:41:25.828020: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 07:41:25.841021: Running on_exit tasks
2024-07-12 07:53:52.914701: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:53:52.952701: unable to import ptvsd to enable debugging
2024-07-12 07:53:52.963708: wfastcgi.py 3.0.0 initialized
2024-07-12 07:55:22.331511: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 07:55:22.343514: Running on_exit tasks
2024-07-12 07:56:31.094653: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:56:31.132647: unable to import ptvsd to enable debugging
2024-07-12 07:56:31.141648: wfastcgi.py 3.0.0 initialized
2024-07-12 07:56:37.422754: Error occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    callback, callback_args, callback_kwargs = self.resolve_request(request)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 313, in resolve_request
    resolver_match = resolver.resolve(request.path_info)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\corsheaders\middleware.py", line 56, in __call__
    result = self.get_response(request)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 849, in main
    for part in result:
  File "C:\Python312\Lib\site-packages\applicationinsights\requests\WSGIApplication.py", line 82, in __call__
    for part in self._wsgi_application(environ, status_interceptor):
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\wsgi.py", line 124, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 23, in <module>
    path('', include('uploadservice.urls')),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\uploadservice\urls.py", line 12, in <module>
    path('api/login/', LoginView.as_view(), name='login'),
                       ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'as_view'


StdOut: 

StdErr: 
2024-07-12 07:57:01.897119: wfastcgi.py exiting because uploadservice\urls.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 07:57:01.914119: Running on_exit tasks
2024-07-12 07:57:26.248804: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 07:57:26.287797: unable to import ptvsd to enable debugging
2024-07-12 07:57:26.298797: wfastcgi.py 3.0.0 initialized
2024-07-12 08:02:40.448748: Running on_exit tasks
2024-07-12 08:02:40.448748: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-12 08:03:11.578331: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:03:11.616354: unable to import ptvsd to enable debugging
2024-07-12 08:03:11.627357: wfastcgi.py 3.0.0 initialized
2024-07-12 08:08:27.324302: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 08:08:27.339300: Running on_exit tasks
2024-07-12 08:08:47.995855: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:08:48.036864: unable to import ptvsd to enable debugging
2024-07-12 08:08:48.048868: wfastcgi.py 3.0.0 initialized
2024-07-12 08:10:59.994088: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 08:11:00.013116: Running on_exit tasks
2024-07-12 08:11:07.541716: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:11:07.582713: unable to import ptvsd to enable debugging
2024-07-12 08:11:07.595713: wfastcgi.py 3.0.0 initialized
2024-07-12 08:11:12.761649: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 08:11:12.779731: Running on_exit tasks
2024-07-12 08:11:45.628587: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:11:45.672593: unable to import ptvsd to enable debugging
2024-07-12 08:11:45.686584: wfastcgi.py 3.0.0 initialized
2024-07-12 08:17:34.735293: Running on_exit tasks
2024-07-12 08:23:35.347304: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:23:35.386308: unable to import ptvsd to enable debugging
2024-07-12 08:23:35.398296: wfastcgi.py 3.0.0 initialized
2024-07-12 08:24:01.415255: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 08:24:01.432255: Running on_exit tasks
2024-07-12 08:24:07.049449: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:24:07.089462: unable to import ptvsd to enable debugging
2024-07-12 08:24:07.104462: wfastcgi.py 3.0.0 initialized
2024-07-12 08:24:33.591873: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 08:24:33.614872: Running on_exit tasks
2024-07-12 08:28:46.153511: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:28:46.194546: unable to import ptvsd to enable debugging
2024-07-12 08:28:46.206510: wfastcgi.py 3.0.0 initialized
2024-07-12 08:35:34.040376: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 08:35:34.052376: Running on_exit tasks
2024-07-12 08:36:11.383925: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 08:36:11.424929: unable to import ptvsd to enable debugging
2024-07-12 08:36:11.437917: wfastcgi.py 3.0.0 initialized
2024-07-12 08:41:48.675779: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 08:41:48.691778: Running on_exit tasks
2024-07-12 09:02:28.653249: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 09:02:28.654295: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 09:02:28.654295: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 09:02:28.710254: unable to import ptvsd to enable debugging
2024-07-12 09:02:28.827253: unable to import ptvsd to enable debugging
2024-07-12 09:02:28.827253: wfastcgi.py 3.0.0 initialized
2024-07-12 09:02:28.852253: unable to import ptvsd to enable debugging
2024-07-12 09:02:28.852253: wfastcgi.py 3.0.0 initialized
2024-07-12 09:02:28.864254: wfastcgi.py 3.0.0 initialized
2024-07-12 09:05:31.461284: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 09:05:31.478288: Running on_exit tasks
2024-07-12 09:05:31.479288: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 09:05:31.508285: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 09:05:31.521288: Running on_exit tasks
2024-07-12 09:07:20.856156: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 09:07:20.856156: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 09:07:20.858156: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 09:07:20.896157: unable to import ptvsd to enable debugging
2024-07-12 09:07:20.916159: unable to import ptvsd to enable debugging
2024-07-12 09:07:20.928161: wfastcgi.py 3.0.0 initialized
2024-07-12 09:12:34.872323: Running on_exit tasks
2024-07-12 09:12:34.884335: Running on_exit tasks
2024-07-12 09:12:34.907329: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-12 09:12:34.907329: Running on_exit tasks
2024-07-12 10:40:54.278790: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 10:40:54.338782: unable to import ptvsd to enable debugging
2024-07-12 10:40:54.349788: wfastcgi.py 3.0.0 initialized
2024-07-12 10:45:06.943826: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 10:45:06.958823: Running on_exit tasks
2024-07-12 11:02:11.446981: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 11:02:11.459971: unable to import ptvsd to enable debugging
2024-07-12 11:02:11.469971: wfastcgi.py 3.0.0 initialized
2024-07-12 11:07:00.008188: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 11:07:00.024191: Running on_exit tasks
2024-07-12 11:15:15.782707: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 11:15:15.782707: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 11:15:15.783708: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 11:15:15.828708: unable to import ptvsd to enable debugging
2024-07-12 11:15:15.834708: unable to import ptvsd to enable debugging
2024-07-12 11:15:15.851708: wfastcgi.py 3.0.0 initialized
e debugging
2024-07-12 11:15:15.863710: wfastcgi.py 3.0.0 initialized
2024-07-12 11:19:09.108968: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 11:19:09.109968: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 11:19:09.137969: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 11:19:09.152972: Running on_exit tasks
2024-07-12 11:19:09.175970: Running on_exit tasks
2024-07-12 11:46:16.557038: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 11:46:16.588039: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 11:46:16.615038: unable to import ptvsd to enable debugging
2024-07-12 11:46:16.616037: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 11:46:16.631045: wfastcgi.py 3.0.0 initialized
2024-07-12 11:46:16.642038: unable to import ptvsd to enable debugging
2024-07-12 11:46:16.664048: unable to import ptvsd to enable debugging
2024-07-12 11:46:16.675045: wfastcgi.py 3.0.0 initialized
2024-07-12 11:50:38.408479: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 11:50:38.423478: Running on_exit tasks
2024-07-12 11:50:38.423478: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 11:50:38.454479: Running on_exit tasks
2024-07-12 11:50:38.456480: wfastcgi.py exiting because web.config has changed, matching .*((\.py)|(\.config))$
2024-07-12 11:50:38.496478: Running on_exit tasks
2024-07-12 12:29:21.275181: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 12:29:21.314180: unable to import ptvsd to enable debugging
2024-07-12 12:29:21.326189: wfastcgi.py 3.0.0 initialized
2024-07-12 12:34:35.315033: Running on_exit tasks
2024-07-12 12:57:09.116031: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 12:57:09.154038: unable to import ptvsd to enable debugging
2024-07-12 12:57:09.167032: wfastcgi.py 3.0.0 initialized
2024-07-12 13:02:02.602588: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 13:02:02.616591: Running on_exit tasks
2024-07-12 13:13:18.606793: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 13:13:18.644826: unable to import ptvsd to enable debugging
2024-07-12 13:13:18.655782: wfastcgi.py 3.0.0 initialized
2024-07-12 13:18:32.745710: Running on_exit tasks
2024-07-12 13:35:56.189618: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 13:35:56.229626: unable to import ptvsd to enable debugging
2024-07-12 13:35:56.242623: wfastcgi.py 3.0.0 initialized
2024-07-12 13:41:14.488426: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 13:41:14.500427: Running on_exit tasks
2024-07-12 13:45:51.894875: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 13:45:51.930868: unable to import ptvsd to enable debugging
2024-07-12 13:45:51.941884: wfastcgi.py 3.0.0 initialized
2024-07-12 13:46:30.782732: wfastcgi.py exiting because uploadservice\urls.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 13:46:30.912736: Running on_exit tasks
2024-07-12 13:46:35.087369: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-12 13:46:35.123372: unable to import ptvsd to enable debugging
2024-07-12 13:46:35.136373: wfastcgi.py 3.0.0 initialized
2024-07-12 13:49:40.074918: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-12 13:49:40.086917: Running on_exit tasks
2024-07-12 14:00:38.789842: Error occurred while reading WSGI handler:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 791, in main
    env, handler = read_wsgi_handler(response.physical_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 633, in read_wsgi_handler
    handler = get_wsgi_handler(os.getenv("WSGI_HANDLER"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 600, in get_wsgi_handler
    handler = __import__(module_name, fromlist=[name_list[0][0]])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\wsgi.py", line 16, in <module>
    application = get_wsgi_application()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\wsgi.py", line 12, in get_wsgi_application
    django.setup(set_prefix=False)
  File "C:\Python312\Lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Python312\Lib\site-packages\django\apps\registry.py", line 83, in populate
    raise RuntimeError("populate() isn't reentrant")
RuntimeError: populate() isn't reentrant


StdOut: 

StdErr: 
2024-07-12 14:00:38.800845: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 791, in main
    env, handler = read_wsgi_handler(response.physical_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 633, in read_wsgi_handler
    handler = get_wsgi_handler(os.getenv("WSGI_HANDLER"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 600, in get_wsgi_handler
    handler = __import__(module_name, fromlist=[name_list[0][0]])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\wsgi.py", line 16, in <module>
    application = get_wsgi_application()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\wsgi.py", line 12, in get_wsgi_application
    django.setup(set_prefix=False)
  File "C:\Python312\Lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Python312\Lib\site-packages\django\apps\registry.py", line 83, in populate
    raise RuntimeError("populate() isn't reentrant")
RuntimeError: populate() isn't reentrant
2024-07-12 14:00:38.811841: Running on_exit tasks
2024-07-12 14:00:38.822838: wfastcgi.py 3.0.0 closed
=======
>>>>>>> parent of 14da6ca (complete upload service troubleshoot)
2024-07-15 10:12:41.301212: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 10:12:41.336214: unable to import ptvsd to enable debugging
2024-07-15 10:12:41.348220: wfastcgi.py 3.0.0 initialized
2024-07-15 10:19:05.453015: Running on_exit tasks
2024-07-15 10:48:06.713608: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 10:48:06.755610: unable to import ptvsd to enable debugging
2024-07-15 10:48:06.767600: wfastcgi.py 3.0.0 initialized
2024-07-15 10:55:05.817060: Running on_exit tasks
2024-07-15 11:01:13.879457: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:01:13.921447: unable to import ptvsd to enable debugging
2024-07-15 11:01:13.938458: wfastcgi.py 3.0.0 initialized
2024-07-15 11:06:27.848768: Running on_exit tasks
2024-07-15 11:06:27.848768: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-15 11:15:19.873408: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:15:19.874406: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:15:19.875400: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:15:19.908408: unable to import ptvsd to enable debugging
2024-07-15 11:15:19.908408: unable to import ptvsd to enable debugging
2024-07-15 11:15:19.920475: wfastcgi.py 3.0.0 initialized
2024-07-15 11:20:32.584902: Running on_exit tasks
2024-07-15 11:20:32.585903: Running on_exit tasks
2024-07-15 11:20:32.585903: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-15 11:20:32.595900: Running on_exit tasks
2024-07-15 11:29:56.034686: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:29:56.034686: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:29:56.037761: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:29:56.079647: unable to import ptvsd to enable debugging
2024-07-15 11:29:56.079647: unable to import ptvsd to enable debugging
2024-07-15 11:29:56.103646: wfastcgi.py 3.0.0 initialized
2024-07-15 11:29:56.103646: wfastcgi.py 3.0.0 initialized
2024-07-15 11:29:56.103646: wfastcgi.py 3.0.0 initialized
2024-07-15 11:32:56.026868: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:32:56.066860: unable to import ptvsd to enable debugging
2024-07-15 11:32:56.083840: wfastcgi.py 3.0.0 initialized
2024-07-15 11:33:30.412913: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:33:30.451859: unable to import ptvsd to enable debugging
2024-07-15 11:33:30.465858: wfastcgi.py 3.0.0 initialized
2024-07-15 11:38:44.361787: Running on_exit tasks
2024-07-15 11:38:45.055057: Running on_exit tasks
2024-07-15 11:38:45.055057: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-15 11:47:56.164936: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:47:56.165935: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:47:56.202931: unable to import ptvsd to enable debugging
2024-07-15 11:47:56.215929: wfastcgi.py 3.0.0 initialized
2024-07-15 11:47:56.215929: unable to import ptvsd to enable debugging
2024-07-15 11:47:56.226932: wfastcgi.py 3.0.0 initialized
2024-07-15 11:47:56.257944: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 11:47:56.272930: unable to import ptvsd to enable debugging
2024-07-15 11:47:56.282936: wfastcgi.py 3.0.0 initialized
2024-07-15 11:57:50.172964: Running on_exit tasks
2024-07-15 11:57:50.172964: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-15 11:57:50.173964: Running on_exit tasks
2024-07-15 11:57:50.195978: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-15 11:57:50.195978: Running on_exit tasks
2024-07-15 12:10:16.506242: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 12:10:16.547287: unable to import ptvsd to enable debugging
2024-07-15 12:10:16.559247: wfastcgi.py 3.0.0 initialized
2024-07-15 12:15:30.599875: Running on_exit tasks
2024-07-15 12:38:07.627106: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 12:38:07.675107: unable to import ptvsd to enable debugging
2024-07-15 12:38:07.689106: wfastcgi.py 3.0.0 initialized
2024-07-15 12:38:07.723106: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 12:38:07.763109: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-15 12:38:07.766109: unable to import ptvsd to enable debugging
2024-07-15 12:38:07.790110: unable to import ptvsd to enable debugging
2024-07-15 12:38:07.803110: wfastcgi.py 3.0.0 initialized
2024-07-15 12:43:21.058596: Running on_exit tasks
2024-07-15 12:43:21.059599: Running on_exit tasks
2024-07-15 12:43:21.081596: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-15 12:43:21.081596: Running on_exit tasks
2024-07-16 08:40:18.358791: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-16 08:40:18.374798: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-16 08:40:18.376790: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-16 08:40:18.385790: unable to import ptvsd to enable debugging
2024-07-16 08:40:18.407791: unable to import ptvsd to enable debugging
2024-07-16 08:40:18.407791: wfastcgi.py 3.0.0 initialized
2024-07-16 08:40:18.430806: wfastcgi.py 3.0.0 initialized
2024-07-16 08:45:30.781335: Running on_exit tasks
2024-07-16 08:45:30.782335: Running on_exit tasks
2024-07-16 08:45:30.805334: Running on_exit tasks
2024-07-16 08:45:30.805334: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-16 10:06:02.174330: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-16 10:06:02.174330: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-16 10:06:02.300328: unable to import ptvsd to enable debugging
2024-07-16 10:06:02.300328: unable to import ptvsd to enable debugging
2024-07-16 10:06:02.301329: unable to import ptvsd to enable debugging
2024-07-16 10:06:02.324330: wfastcgi.py 3.0.0 initialized
2024-07-16 10:06:02.324330: wfastcgi.py 3.0.0 initialized
2024-07-16 10:11:10.230973: Running on_exit tasks
2024-07-16 10:11:10.230973: Running on_exit tasks
2024-07-16 10:11:10.231977: Running on_exit tasks
2024-07-16 11:01:25.137311: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-16 11:01:25.151313: unable to import ptvsd to enable debugging
2024-07-16 11:01:25.151313: unable to import ptvsd to enable debugging
2024-07-16 11:01:25.224310: wfastcgi.py 3.0.0 initialized
2024-07-16 11:01:25.241309: wfastcgi.py 3.0.0 initialized
2024-07-16 11:06:35.670523: Running on_exit tasks
2024-07-16 11:06:35.707522: Running on_exit tasks
2024-07-17 04:42:37.505832: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-17 04:42:37.517830: unable to import ptvsd to enable debugging
2024-07-17 04:42:37.530804: wfastcgi.py 3.0.0 initialized
2024-07-17 04:47:50.483477: Running on_exit tasks
2024-07-17 04:47:50.483477: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-17 09:17:46.263863: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-17 09:17:46.297858: unable to import ptvsd to enable debugging
2024-07-17 09:17:46.312878: wfastcgi.py 3.0.0 initialized
2024-07-17 09:22:58.942561: Running on_exit tasks
2024-07-17 09:22:58.942561: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-17 11:20:17.150621: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-17 11:20:17.151622: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-17 11:20:17.156619: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-17 11:20:17.188629: unable to import ptvsd to enable debugging
2024-07-17 11:20:17.200623: wfastcgi.py 3.0.0 initialized
2024-07-17 11:20:17.200623: wfastcgi.py 3.0.0 initialized
2024-07-17 11:25:29.442612: Running on_exit tasks
2024-07-17 11:25:29.457619: Running on_exit tasks
2024-07-17 11:25:29.482714: Running on_exit tasks
2024-07-17 11:25:29.482714: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-17 14:38:27.038662: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-17 14:38:27.051663: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-17 14:38:27.064670: unable to import ptvsd to enable debugging
2024-07-17 14:38:27.075673: wfastcgi.py 3.0.0 initialized
2024-07-17 14:38:27.075673: unable to import ptvsd to enable debugging
2024-07-17 14:38:27.097670: wfastcgi.py 3.0.0 initialized
2024-07-17 14:43:39.932633: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-17 14:43:39.954637: Running on_exit tasks
2024-07-17 14:43:39.954637: Running on_exit tasks
2024-07-17 14:43:39.971634: Running on_exit tasks
2024-07-17 14:43:39.972635: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-18 08:53:09.627308: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-18 08:53:09.640307: unable to import ptvsd to enable debugging
2024-07-18 08:53:09.652307: wfastcgi.py 3.0.0 initialized
2024-07-18 08:58:22.518240: Running on_exit tasks
2024-07-18 08:58:22.519255: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-18 09:36:46.480051: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-18 09:36:46.516052: unable to import ptvsd to enable debugging
2024-07-18 09:36:46.529066: wfastcgi.py 3.0.0 initialized
2024-07-18 09:42:00.563096: Running on_exit tasks
2024-07-18 09:42:00.563096: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-22 08:47:25.610892: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-22 08:47:25.620898: unable to import ptvsd to enable debugging
2024-07-22 08:47:25.631890: wfastcgi.py 3.0.0 initialized
2024-07-22 08:52:28.853555: Running on_exit tasks
2024-07-22 08:52:28.853555: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-22 08:52:46.027584: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-22 08:52:46.068591: unable to import ptvsd to enable debugging
2024-07-22 08:52:46.080585: wfastcgi.py 3.0.0 initialized
2024-07-22 08:58:00.193063: Running on_exit tasks
2024-07-22 08:58:00.193063: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-22 09:45:22.949786: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-22 09:45:22.985785: unable to import ptvsd to enable debugging
2024-07-22 09:45:22.997790: wfastcgi.py 3.0.0 initialized
2024-07-22 09:50:37.079328: Running on_exit tasks
2024-07-22 09:50:37.079328: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-22 10:09:40.593707: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-22 10:09:40.635712: unable to import ptvsd to enable debugging
2024-07-22 10:09:40.647714: wfastcgi.py 3.0.0 initialized
2024-07-22 10:14:54.695744: Running on_exit tasks
2024-07-23 04:55:38.024201: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 04:55:38.036194: unable to import ptvsd to enable debugging
2024-07-23 04:55:38.047194: wfastcgi.py 3.0.0 initialized
2024-07-23 05:01:26.075913: Running on_exit tasks
2024-07-23 05:01:26.075913: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 05:06:49.279145: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 05:06:49.318145: unable to import ptvsd to enable debugging
2024-07-23 05:06:49.330148: wfastcgi.py 3.0.0 initialized
2024-07-23 05:12:03.352878: Running on_exit tasks
2024-07-23 05:12:03.353879: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 08:52:35.520014: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 08:52:35.532003: unable to import ptvsd to enable debugging
2024-07-23 08:52:35.543003: wfastcgi.py 3.0.0 initialized
2024-07-23 08:57:48.563560: Running on_exit tasks
2024-07-23 08:57:48.563560: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 10:01:36.974071: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 10:01:37.014067: unable to import ptvsd to enable debugging
2024-07-23 10:01:37.027077: wfastcgi.py 3.0.0 initialized
2024-07-23 10:06:51.095600: Running on_exit tasks
2024-07-23 10:06:51.095600: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 11:47:47.559166: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 11:47:47.560167: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 11:47:47.563167: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 11:47:47.593167: unable to import ptvsd to enable debugging
2024-07-23 11:47:47.593167: unable to import ptvsd to enable debugging
2024-07-23 11:47:47.604177: wfastcgi.py 3.0.0 initialized
2024-07-23 11:47:47.604177: wfastcgi.py 3.0.0 initialized
2024-07-23 11:58:14.689160: Running on_exit tasks
2024-07-23 11:58:14.691159: Running on_exit tasks
2024-07-23 11:58:14.719184: Running on_exit tasks
2024-07-23 11:58:14.720160: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 13:27:26.609380: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 13:27:26.644380: unable to import ptvsd to enable debugging
2024-07-23 13:27:26.655400: wfastcgi.py 3.0.0 initialized
2024-07-23 13:27:27.833400: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 13:27:27.870397: unable to import ptvsd to enable debugging
2024-07-23 13:27:27.883396: wfastcgi.py 3.0.0 initialized
2024-07-23 13:27:27.942397: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 13:27:27.978407: unable to import ptvsd to enable debugging
2024-07-23 13:27:27.990418: wfastcgi.py 3.0.0 initialized
2024-07-23 13:29:17.879142: wfastcgi.py exiting because uploadservice\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-23 13:29:17.894143: Running on_exit tasks
2024-07-23 13:36:01.354820: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 13:36:01.390821: unable to import ptvsd to enable debugging
2024-07-23 13:36:01.403814: wfastcgi.py 3.0.0 initialized
2024-07-23 13:44:45.474267: Running on_exit tasks
2024-07-23 13:44:45.474267: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 13:51:48.419152: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 13:51:48.460157: unable to import ptvsd to enable debugging
2024-07-23 13:51:48.472161: wfastcgi.py 3.0.0 initialized
2024-07-23 13:57:02.738867: Running on_exit tasks
2024-07-23 14:24:18.961068: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:24:18.961068: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:24:19.177079: unable to import ptvsd to enable debugging
2024-07-23 14:24:19.178080: unable to import ptvsd to enable debugging
2024-07-23 14:24:19.200083: wfastcgi.py 3.0.0 initialized
e debugging
2024-07-23 14:24:19.200083: wfastcgi.py 3.0.0 initialized
2024-07-23 14:24:19.213079: wfastcgi.py 3.0.0 initialized
2024-07-23 14:34:07.029909: Running on_exit tasks
2024-07-23 14:34:07.029909: Running on_exit tasks
2024-07-23 14:34:07.083914: Running on_exit tasks
2024-07-23 14:34:07.083914: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 14:34:07.083914: Running on_exit tasks
2024-07-23 14:34:07.095910: Running on_exit tasks
2024-07-23 14:38:57.032759: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:38:57.032759: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:38:57.099767: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:38:57.099767: unable to import ptvsd to enable debugging
etpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:38:57.136760: wfastcgi.py 3.0.0 initialized
2024-07-23 14:38:57.136760: wfastcgi.py 3.0.0 initialized
e debugging
2024-07-23 14:38:57.164761: wfastcgi.py 3.0.0 initialized
2024-07-23 14:38:57.164761: wfastcgi.py 3.0.0 initialized
2024-07-23 14:44:09.541273: Running on_exit tasks
2024-07-23 14:44:09.541273: Running on_exit tasks
2024-07-23 14:44:09.585282: Running on_exit tasks
2024-07-23 14:44:09.614274: Running on_exit tasks
2024-07-23 14:44:09.614274: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 14:44:33.942039: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:44:33.944038: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:44:34.005038: unable to import ptvsd to enable debugging
2024-07-23 14:44:34.005038: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:44:34.006038: unable to import ptvsd to enable debugging
etpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:44:34.030043: wfastcgi.py 3.0.0 initialized
e debugging
2024-07-23 14:44:34.030043: unable to import ptvsd to enable debugging
2024-07-23 14:44:34.044043: wfastcgi.py 3.0.0 initialized
2024-07-23 14:44:34.045037: wfastcgi.py 3.0.0 initialized
2024-07-23 14:49:36.239454: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:49:36.277454: unable to import ptvsd to enable debugging
2024-07-23 14:49:36.291454: wfastcgi.py 3.0.0 initialized
2024-07-23 14:49:36.336458: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:49:36.371456: unable to import ptvsd to enable debugging
2024-07-23 14:49:36.389455: wfastcgi.py 3.0.0 initialized
2024-07-23 14:49:36.797470: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 14:49:36.832465: unable to import ptvsd to enable debugging
2024-07-23 14:49:36.844466: wfastcgi.py 3.0.0 initialized
2024-07-23 14:54:24.328304: Running on_exit tasks
2024-07-23 14:54:37.765806: Running on_exit tasks
2024-07-23 14:54:37.779804: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 14:54:37.780806: Running on_exit tasks
2024-07-23 14:54:37.803806: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 14:54:37.803806: Running on_exit tasks
2024-07-23 15:00:08.709854: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:00:08.770854: unable to import ptvsd to enable debugging
2024-07-23 15:00:08.795854: wfastcgi.py 3.0.0 initialized
2024-07-23 15:00:08.946858: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:00:08.998857: unable to import ptvsd to enable debugging
2024-07-23 15:00:09.021858: wfastcgi.py 3.0.0 initialized
2024-07-23 15:00:09.021858: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:00:09.036859: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:00:09.062859: unable to import ptvsd to enable debugging
2024-07-23 15:00:09.064859: unable to import ptvsd to enable debugging
2024-07-23 15:00:09.098859: wfastcgi.py 3.0.0 initialized
2024-07-23 15:00:09.099861: wfastcgi.py 3.0.0 initialized
2024-07-23 15:05:22.394281: Running on_exit tasks
2024-07-23 15:05:22.395281: Running on_exit tasks
2024-07-23 15:05:22.411295: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 15:05:22.439285: Running on_exit tasks
2024-07-23 15:05:22.439285: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 15:05:22.459282: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 15:05:22.460282: Running on_exit tasks
2024-07-23 15:29:35.829420: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:29:35.832418: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:29:35.831422: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:29:35.865426: unable to import ptvsd to enable debugging
2024-07-23 15:29:35.865426: unable to import ptvsd to enable debugging
2024-07-23 15:29:35.865426: unable to import ptvsd to enable debugging
2024-07-23 15:29:35.919421: wfastcgi.py 3.0.0 initialized
2024-07-23 15:29:35.922421: wfastcgi.py 3.0.0 initialized
2024-07-23 15:29:35.923421: wfastcgi.py 3.0.0 initialized
2024-07-23 15:29:35.946421: wfastcgi.py 3.0.0 initialized
2024-07-23 15:35:58.126270: Running on_exit tasks
2024-07-23 15:40:03.115288: Running on_exit tasks
2024-07-23 15:40:03.128288: Running on_exit tasks
2024-07-23 15:40:03.128288: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 15:40:03.132300: Running on_exit tasks
2024-07-23 15:59:13.157943: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:59:13.165943: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:59:13.166943: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:59:13.214945: unable to import ptvsd to enable debugging
2024-07-23 15:59:13.214945: unable to import ptvsd to enable debugging
2024-07-23 15:59:13.214945: unable to import ptvsd to enable debugging
2024-07-23 15:59:13.221945: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:59:13.228945: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 15:59:13.271944: wfastcgi.py 3.0.0 initialized
e debugging
2024-07-23 15:59:13.271944: unable to import ptvsd to enable debugging
2024-07-23 15:59:13.271944: wfastcgi.py 3.0.0 initialized
2024-07-23 15:59:13.323948: wfastcgi.py 3.0.0 initialized
2024-07-23 16:04:24.096392: Running on_exit tasks
2024-07-23 16:04:24.152393: Running on_exit tasks
2024-07-23 16:04:24.152393: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:04:27.493452: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:04:27.512451: Running on_exit tasks
2024-07-23 16:04:27.513453: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:04:28.488470: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:04:28.490471: Running on_exit tasks
2024-07-23 16:04:28.487471: Running on_exit tasks
2024-07-23 16:04:59.541698: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:04:59.556699: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:04:59.564699: unable to import ptvsd to enable debugging
2024-07-23 16:04:59.566700: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:04:59.591702: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:04:59.593700: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:04:59.667741: unable to import ptvsd to enable debugging
:04:59.667741: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:04:59.671702: unable to import ptvsd to enable debugging
2024-07-23 16:04:59.723702: unable to import ptvsd to enable debugging
2024-07-23 16:04:59.725702: wfastcgi.py 3.0.0 initialized
2024-07-23 16:04:59.766705: wfastcgi.py 3.0.0 initialized
e debugging
2024-07-23 16:04:59.781706: wfastcgi.py 3.0.0 initialized
2024-07-23 16:04:59.836708: wfastcgi.py 3.0.0 initialized
2024-07-23 16:04:59.837706: wfastcgi.py 3.0.0 initialized
2024-07-23 16:10:11.263845: Running on_exit tasks
2024-07-23 16:10:11.263845: Running on_exit tasks
2024-07-23 16:10:11.325850: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:10:11.325850: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:10:11.325850: Running on_exit tasks
2024-07-23 16:10:11.325850: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:10:11.326847: Running on_exit tasks
2024-07-23 16:10:11.380853: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:10:11.380853: Running on_exit tasks
2024-07-23 16:10:11.380853: Running on_exit tasks
2024-07-23 16:10:20.223226: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:10:20.223226: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:10:20.263249: unable to import ptvsd to enable debugging
2024-07-23 16:10:20.267228: unable to import ptvsd to enable debugging
2024-07-23 16:10:20.289228: wfastcgi.py 3.0.0 initialized
2024-07-23 16:10:20.307236: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-23 16:10:20.321236: unable to import ptvsd to enable debugging
2024-07-23 16:10:20.334233: wfastcgi.py 3.0.0 initialized
2024-07-23 16:15:31.749676: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-23 16:15:31.749676: Running on_exit tasks
2024-07-23 16:15:31.750677: Running on_exit tasks
2024-07-23 16:15:31.786676: Running on_exit tasks
2024-07-23 16:15:31.786676: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-24 02:53:37.553463: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 02:53:37.565458: unable to import ptvsd to enable debugging
2024-07-24 02:53:37.577460: wfastcgi.py 3.0.0 initialized
2024-07-24 02:58:50.605474: Running on_exit tasks
2024-07-24 02:58:50.605474: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-24 05:00:10.046010: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 05:00:10.059008: unable to import ptvsd to enable debugging
2024-07-24 05:00:10.072008: wfastcgi.py 3.0.0 initialized
2024-07-24 05:05:23.115591: Running on_exit tasks
2024-07-24 05:05:23.115591: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-24 06:52:27.440331: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 06:52:27.476333: unable to import ptvsd to enable debugging
2024-07-24 06:52:27.488324: wfastcgi.py 3.0.0 initialized
2024-07-24 06:57:41.606316: Running on_exit tasks
2024-07-24 06:57:41.606316: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-24 08:02:11.684403: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 08:02:11.719459: unable to import ptvsd to enable debugging
2024-07-24 08:02:11.732398: wfastcgi.py 3.0.0 initialized
2024-07-24 08:07:25.846041: Running on_exit tasks
2024-07-24 08:07:25.846041: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-24 09:45:53.224351: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 09:45:53.245368: unable to import ptvsd to enable debugging
2024-07-24 09:45:53.270365: wfastcgi.py 3.0.0 initialized
2024-07-24 09:55:25.272731: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-24 09:55:25.301733: Running on_exit tasks
2024-07-24 10:39:19.386169: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 10:39:19.422174: unable to import ptvsd to enable debugging
2024-07-24 10:39:19.436170: wfastcgi.py 3.0.0 initialized
2024-07-24 10:40:18.380012: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-24 10:40:18.403015: Running on_exit tasks
2024-07-24 10:40:26.083693: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 10:40:26.121704: unable to import ptvsd to enable debugging
2024-07-24 10:40:26.134700: wfastcgi.py 3.0.0 initialized
2024-07-24 10:47:05.109119: wfastcgi.py exiting because rduploadservice\settings.py has changed, matching .*((\.py)|(\.config))$
2024-07-24 10:47:05.122117: Running on_exit tasks
2024-07-24 10:47:34.590449: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 10:47:34.630451: unable to import ptvsd to enable debugging
2024-07-24 10:47:34.643456: wfastcgi.py 3.0.0 initialized
2024-07-24 10:48:10.700036: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-24 10:48:10.717036: Running on_exit tasks
2024-07-24 10:48:33.663597: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 10:48:33.700608: unable to import ptvsd to enable debugging
2024-07-24 10:48:33.712597: wfastcgi.py 3.0.0 initialized
2024-07-24 10:49:57.532612: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-24 10:49:57.548622: Running on_exit tasks
2024-07-24 10:50:12.749957: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 10:50:12.786955: unable to import ptvsd to enable debugging
2024-07-24 10:50:12.799954: wfastcgi.py 3.0.0 initialized
2024-07-24 10:55:26.845858: Running on_exit tasks
2024-07-24 11:16:25.648233: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 11:16:25.684234: unable to import ptvsd to enable debugging
2024-07-24 11:16:25.697237: wfastcgi.py 3.0.0 initialized
2024-07-24 11:16:57.237781: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-24 11:16:57.249782: Running on_exit tasks
2024-07-24 11:17:02.921112: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 11:17:02.960119: unable to import ptvsd to enable debugging
2024-07-24 11:17:02.973114: wfastcgi.py 3.0.0 initialized
2024-07-24 11:18:56.622439: wfastcgi.py exiting because ai_file_reader\event_handler.py has changed, matching .*((\.py)|(\.config))$
2024-07-24 11:18:56.720443: Running on_exit tasks
2024-07-24 11:20:34.244546: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 11:20:34.296859: unable to import ptvsd to enable debugging
2024-07-24 11:20:34.312561: wfastcgi.py 3.0.0 initialized
2024-07-24 11:25:48.327350: Running on_exit tasks
2024-07-24 12:11:13.778179: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 12:11:13.815181: unable to import ptvsd to enable debugging
2024-07-24 12:11:13.827174: wfastcgi.py 3.0.0 initialized
2024-07-24 12:22:52.893465: Running on_exit tasks
2024-07-24 12:22:52.894472: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-24 15:09:26.755287: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 15:09:26.768291: unable to import ptvsd to enable debugging
2024-07-24 15:09:26.780280: wfastcgi.py 3.0.0 initialized
2024-07-24 15:14:38.625366: Running on_exit tasks
2024-07-24 16:56:50.439764: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 16:56:50.493723: unable to import ptvsd to enable debugging
2024-07-24 16:56:50.505724: wfastcgi.py 3.0.0 initialized
2024-07-24 17:01:59.240849: Running on_exit tasks
2024-07-24 17:16:39.500250: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 17:16:39.557252: unable to import ptvsd to enable debugging
2024-07-24 17:16:39.570252: wfastcgi.py 3.0.0 initialized
2024-07-24 17:21:51.966196: Running on_exit tasks
2024-07-24 17:30:32.268602: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-24 17:30:32.342604: unable to import ptvsd to enable debugging
2024-07-24 17:30:32.355604: wfastcgi.py 3.0.0 initialized
2024-07-24 17:35:42.688409: Running on_exit tasks
2024-07-25 05:27:49.250295: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 05:27:49.265296: unable to import ptvsd to enable debugging
2024-07-25 05:27:49.280295: wfastcgi.py 3.0.0 initialized
2024-07-25 05:32:59.070705: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-25 05:32:59.071704: Running on_exit tasks
2024-07-25 15:02:44.315799: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 15:02:44.327796: unable to import ptvsd to enable debugging
2024-07-25 15:02:44.341792: wfastcgi.py 3.0.0 initialized
2024-07-25 15:05:06.372244: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-25 15:05:06.385246: Running on_exit tasks
2024-07-25 15:25:51.724393: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 15:25:51.765393: unable to import ptvsd to enable debugging
2024-07-25 15:25:51.778398: wfastcgi.py 3.0.0 initialized
2024-07-25 15:39:15.780940: Running on_exit tasks
2024-07-25 15:39:15.780940: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-25 15:44:38.703442: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 15:44:38.741446: unable to import ptvsd to enable debugging
2024-07-25 15:44:38.754453: wfastcgi.py 3.0.0 initialized
2024-07-25 15:58:37.769480: Running on_exit tasks
2024-07-25 16:06:50.190844: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 16:06:50.231828: unable to import ptvsd to enable debugging
2024-07-25 16:06:50.243836: wfastcgi.py 3.0.0 initialized
2024-07-25 16:12:04.248833: Running on_exit tasks
2024-07-25 16:15:39.640126: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 16:15:39.677126: unable to import ptvsd to enable debugging
2024-07-25 16:15:39.690135: wfastcgi.py 3.0.0 initialized
2024-07-25 16:20:52.449270: Running on_exit tasks
2024-07-25 16:23:00.164334: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 16:23:00.206317: unable to import ptvsd to enable debugging
2024-07-25 16:23:00.219315: wfastcgi.py 3.0.0 initialized
2024-07-25 16:30:34.213181: Running on_exit tasks
2024-07-25 16:42:57.729756: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 16:42:57.776746: unable to import ptvsd to enable debugging
2024-07-25 16:42:57.794742: wfastcgi.py 3.0.0 initialized
2024-07-25 16:50:42.486126: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-25 16:50:42.501126: Running on_exit tasks
2024-07-25 16:58:28.112766: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 16:58:28.133759: unable to import ptvsd to enable debugging
2024-07-25 16:58:28.152759: wfastcgi.py 3.0.0 initialized
2024-07-25 17:02:10.820271: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 17:02:10.858271: unable to import ptvsd to enable debugging
2024-07-25 17:02:10.871278: wfastcgi.py 3.0.0 initialized
2024-07-25 17:18:08.805087: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 17:18:08.847086: unable to import ptvsd to enable debugging
2024-07-25 17:18:08.860088: wfastcgi.py 3.0.0 initialized
2024-07-25 17:30:57.736403: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-25 17:30:57.758403: Running on_exit tasks
2024-07-25 17:30:57.759404: Running on_exit tasks
2024-07-25 17:37:43.190347: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 17:37:43.227345: unable to import ptvsd to enable debugging
2024-07-25 17:37:43.239355: wfastcgi.py 3.0.0 initialized
2024-07-25 17:44:42.287306: Running on_exit tasks
2024-07-25 23:02:11.243109: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:02:11.256110: unable to import ptvsd to enable debugging
2024-07-25 23:02:11.270111: wfastcgi.py 3.0.0 initialized
2024-07-25 23:02:20.653281: Error occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    callback, callback_args, callback_kwargs = self.resolve_request(request)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 313, in resolve_request
    resolver_match = resolver.resolve(request.path_info)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\corsheaders\middleware.py", line 56, in __call__
    result = self.get_response(request)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 849, in main
    for part in result:
  File "C:\Python312\Lib\site-packages\applicationinsights\requests\WSGIApplication.py", line 82, in __call__
    for part in self._wsgi_application(environ, status_interceptor):
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\wsgi.py", line 124, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 428, in get_traceback_html
    c = Context(self.get_traceback_data(), use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 411, in get_traceback_data
    c["raising_view_name"] = get_caller(self.request)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\views\debug.py", line 102, in get_caller
    resolver_match = resolve(request.path)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 686, in resolve
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\rduploadservice\urls.py", line 25, in <module>
    path('ai-file-reader/', include('ai_file_reader.urls')),
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\urls.py", line 2, in <module>
    from .views import process_file
ImportError: cannot import name 'process_file' from 'ai_file_reader.views' (C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ai_file_reader\views.py)


StdOut: 

StdErr: 
2024-07-25 23:04:49.218522: wfastcgi.py exiting because ai_file_reader\urls.py has changed, matching .*((\.py)|(\.config))$
2024-07-25 23:04:49.232527: Running on_exit tasks
2024-07-25 23:04:55.376645: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:04:55.415650: unable to import ptvsd to enable debugging
2024-07-25 23:04:55.431639: wfastcgi.py 3.0.0 initialized
2024-07-25 23:06:12.288654: wfastcgi.py exiting because ai_file_reader\urls.py has changed, matching .*((\.py)|(\.config))$
2024-07-25 23:06:12.304655: Running on_exit tasks
2024-07-25 23:06:19.655825: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:06:19.692832: unable to import ptvsd to enable debugging
2024-07-25 23:06:19.706840: wfastcgi.py 3.0.0 initialized
2024-07-25 23:13:53.622522: Running on_exit tasks
2024-07-25 23:13:53.622522: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-25 23:14:43.805336: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:14:43.840336: unable to import ptvsd to enable debugging
2024-07-25 23:14:43.854349: wfastcgi.py 3.0.0 initialized
2024-07-25 23:17:39.470182: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-25 23:17:39.486184: Running on_exit tasks
2024-07-25 23:18:14.912795: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:18:14.953797: unable to import ptvsd to enable debugging
2024-07-25 23:18:14.968793: wfastcgi.py 3.0.0 initialized
2024-07-25 23:30:28.976261: Running on_exit tasks
2024-07-25 23:33:17.847855: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:33:17.945835: unable to import ptvsd to enable debugging
2024-07-25 23:33:17.958867: wfastcgi.py 3.0.0 initialized
2024-07-25 23:48:24.143208: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-25 23:48:24.206207: Running on_exit tasks
2024-07-25 23:48:24.632215: Running on_exit tasks
2024-07-25 23:49:11.835094: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:49:11.850099: unable to import ptvsd to enable debugging
2024-07-25 23:49:11.863094: wfastcgi.py 3.0.0 initialized
2024-07-25 23:54:24.721054: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-25 23:54:24.751057: Running on_exit tasks
2024-07-25 23:54:24.751057: Running on_exit tasks
2024-07-25 23:54:51.596095: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-25 23:54:51.633100: unable to import ptvsd to enable debugging
2024-07-25 23:54:51.647100: wfastcgi.py 3.0.0 initialized
2024-07-25 23:57:07.338663: wfastcgi.py exiting because ai_file_reader\urls.py has changed, matching .*((\.py)|(\.config))$
2024-07-25 23:57:07.359664: Running on_exit tasks
2024-07-26 00:00:10.939121: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 00:00:10.961115: unable to import ptvsd to enable debugging
2024-07-26 00:00:10.995115: wfastcgi.py 3.0.0 initialized
2024-07-26 00:08:54.809987: Running on_exit tasks
2024-07-26 04:34:18.065101: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 04:34:18.108110: unable to import ptvsd to enable debugging
2024-07-26 04:34:18.124116: wfastcgi.py 3.0.0 initialized
2024-07-26 04:39:24.820798: Running on_exit tasks
2024-07-26 04:39:24.820798: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-26 07:25:14.170631: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 07:25:14.184645: unable to import ptvsd to enable debugging
2024-07-26 07:25:14.198637: wfastcgi.py 3.0.0 initialized
2024-07-26 07:30:06.739194: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-26 07:30:06.758194: Running on_exit tasks
2024-07-26 14:50:35.226128: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 14:50:35.242126: unable to import ptvsd to enable debugging
2024-07-26 14:50:35.256132: wfastcgi.py 3.0.0 initialized
2024-07-26 14:55:48.122452: Running on_exit tasks
2024-07-26 14:55:48.122452: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-26 14:58:00.499442: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 14:58:00.537426: unable to import ptvsd to enable debugging
2024-07-26 14:58:00.551415: wfastcgi.py 3.0.0 initialized
2024-07-26 14:59:31.136081: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-07-26 14:59:31.153081: Running on_exit tasks
2024-07-26 15:01:47.428458: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 15:01:47.465495: unable to import ptvsd to enable debugging
2024-07-26 15:01:47.480457: wfastcgi.py 3.0.0 initialized
2024-07-26 15:07:01.542459: Running on_exit tasks
2024-07-26 15:07:21.405045: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 15:07:21.443053: unable to import ptvsd to enable debugging
2024-07-26 15:07:21.458055: wfastcgi.py 3.0.0 initialized
2024-07-26 15:12:35.488046: Running on_exit tasks
2024-07-26 15:12:35.488046: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-07-26 15:14:59.259699: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 15:14:59.306696: unable to import ptvsd to enable debugging
2024-07-26 15:14:59.328819: wfastcgi.py 3.0.0 initialized
2024-07-26 15:20:13.368388: Running on_exit tasks
2024-07-26 15:25:25.288615: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 15:25:25.309617: unable to import ptvsd to enable debugging
2024-07-26 15:25:25.353616: wfastcgi.py 3.0.0 initialized
2024-07-26 15:30:39.371710: Running on_exit tasks
2024-07-26 15:34:56.785401: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-07-26 15:34:56.827402: unable to import ptvsd to enable debugging
2024-07-26 15:34:56.860402: wfastcgi.py 3.0.0 initialized
2024-09-06 05:26:09.472109: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-06 05:26:09.488109: unable to import ptvsd to enable debugging
2024-09-06 05:26:09.503117: wfastcgi.py 3.0.0 initialized
2024-09-06 05:31:20.508358: Running on_exit tasks
2024-09-06 05:31:20.508358: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-06 13:33:47.845101: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-06 13:33:47.860116: unable to import ptvsd to enable debugging
2024-09-06 13:33:47.873101: wfastcgi.py 3.0.0 initialized
2024-09-06 13:39:01.861744: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-06 13:39:01.879745: Running on_exit tasks
2024-09-06 14:49:50.290626: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-06 14:49:50.327475: unable to import ptvsd to enable debugging
2024-09-06 14:49:50.341474: wfastcgi.py 3.0.0 initialized
2024-09-06 14:49:53.548519: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-06 14:49:53.585518: unable to import ptvsd to enable debugging
2024-09-06 14:49:53.602520: wfastcgi.py 3.0.0 initialized
2024-09-06 14:55:07.621993: Running on_exit tasks
2024-09-06 15:08:09.698031: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-06 15:08:09.741031: unable to import ptvsd to enable debugging
2024-09-06 15:08:09.756034: wfastcgi.py 3.0.0 initialized
2024-09-06 15:13:23.767372: Running on_exit tasks
2024-09-09 08:15:17.108523: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-09 08:15:17.123587: unable to import ptvsd to enable debugging
2024-09-09 08:15:17.136540: wfastcgi.py 3.0.0 initialized
2024-09-09 08:20:26.685738: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-09 08:20:26.686732: Running on_exit tasks
2024-09-09 08:25:14.948046: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-09 08:25:14.985043: unable to import ptvsd to enable debugging
2024-09-09 08:25:15.002046: wfastcgi.py 3.0.0 initialized
2024-09-09 08:30:29.042363: Running on_exit tasks
2024-09-09 08:30:29.042363: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-10 09:49:35.293831: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-10 09:49:35.308830: unable to import ptvsd to enable debugging
2024-09-10 09:49:35.322830: wfastcgi.py 3.0.0 initialized
2024-09-10 09:50:25.693591: wfastcgi.py exiting because ai_file_reader\views.py has changed, matching .*((\.py)|(\.config))$
2024-09-10 09:50:25.713591: Running on_exit tasks
2024-09-10 11:39:50.268995: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-10 11:39:50.284995: unable to import ptvsd to enable debugging
2024-09-10 11:39:50.299012: wfastcgi.py 3.0.0 initialized
2024-09-10 11:45:02.857709: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-10 11:45:02.878709: Running on_exit tasks
2024-09-10 11:45:02.878709: Running on_exit tasks
2024-09-11 06:19:37.242138: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-11 06:19:37.264131: unable to import ptvsd to enable debugging
2024-09-11 06:19:37.278142: wfastcgi.py 3.0.0 initialized
2024-09-11 06:25:53.502542: Running on_exit tasks
2024-09-11 06:25:53.502542: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-11 06:55:10.721754: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-11 06:55:10.758775: unable to import ptvsd to enable debugging
2024-09-11 06:55:10.774753: wfastcgi.py 3.0.0 initialized
2024-09-11 07:00:24.855413: Running on_exit tasks
2024-09-11 07:00:24.855413: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-11 07:20:26.071671: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-11 07:20:26.106941: unable to import ptvsd to enable debugging
2024-09-11 07:20:26.122679: wfastcgi.py 3.0.0 initialized
2024-09-11 07:25:40.190805: Running on_exit tasks
2024-09-11 07:25:40.190805: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-11 14:26:09.714849: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-11 14:26:09.731850: unable to import ptvsd to enable debugging
2024-09-11 14:26:09.746842: wfastcgi.py 3.0.0 initialized
2024-09-11 14:31:22.522731: Running on_exit tasks
2024-09-11 14:31:22.522731: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-12 07:35:20.540404: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-12 07:35:20.558324: unable to import ptvsd to enable debugging
2024-09-12 07:35:20.572329: wfastcgi.py 3.0.0 initialized
2024-09-12 07:40:33.303523: Running on_exit tasks
2024-09-12 07:40:33.303523: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-12 14:13:11.973308: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-12 14:13:12.031305: unable to import ptvsd to enable debugging
2024-09-12 14:13:12.045312: wfastcgi.py 3.0.0 initialized
2024-09-12 14:13:12.045312: unable to import ptvsd to enable debugging
2024-09-12 14:13:12.060305: wfastcgi.py 3.0.0 initialized
2024-09-12 14:18:23.249982: Running on_exit tasks
2024-09-12 14:18:23.250979: Running on_exit tasks
2024-09-12 14:36:06.880926: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-12 14:36:06.923928: unable to import ptvsd to enable debugging
2024-09-12 14:36:06.941941: wfastcgi.py 3.0.0 initialized
2024-09-12 14:41:20.810000: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-12 14:41:20.810000: Running on_exit tasks
2024-09-13 04:54:56.831872: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-13 04:54:56.849872: unable to import ptvsd to enable debugging
2024-09-13 04:54:56.865874: wfastcgi.py 3.0.0 initialized
2024-09-13 05:00:07.390217: Running on_exit tasks
2024-09-13 05:00:07.390217: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-16 03:44:40.072175: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-16 03:44:40.087146: unable to import ptvsd to enable debugging
2024-09-16 03:44:40.100164: wfastcgi.py 3.0.0 initialized
2024-09-16 03:49:50.171120: Running on_exit tasks
2024-09-16 03:49:50.171120: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-16 04:14:28.878495: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-16 04:14:28.914651: unable to import ptvsd to enable debugging
2024-09-16 04:14:28.929492: wfastcgi.py 3.0.0 initialized
2024-09-16 04:19:43.031716: Running on_exit tasks
2024-09-16 04:19:43.031716: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-16 04:28:53.893440: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-16 04:28:53.929438: unable to import ptvsd to enable debugging
2024-09-16 04:28:53.944447: wfastcgi.py 3.0.0 initialized
2024-09-16 04:34:08.080980: Running on_exit tasks
2024-09-16 04:34:08.080980: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-16 05:01:15.513997: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-16 05:01:15.533997: unable to import ptvsd to enable debugging
2024-09-16 05:01:15.547996: wfastcgi.py 3.0.0 initialized
2024-09-16 05:06:28.342660: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-16 05:06:28.342660: Running on_exit tasks
2024-09-18 04:11:32.393529: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-18 04:11:32.409847: unable to import ptvsd to enable debugging
2024-09-18 04:11:32.423519: wfastcgi.py 3.0.0 initialized
2024-09-18 04:16:45.404020: Running on_exit tasks
2024-09-18 04:16:45.404020: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-18 04:19:31.258389: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-18 04:19:31.294400: unable to import ptvsd to enable debugging
2024-09-18 04:19:31.307395: wfastcgi.py 3.0.0 initialized
2024-09-18 04:24:45.434017: Running on_exit tasks
2024-09-18 04:24:45.434017: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-18 05:17:39.299411: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-18 05:17:39.314402: unable to import ptvsd to enable debugging
2024-09-18 05:17:39.329405: wfastcgi.py 3.0.0 initialized
2024-09-18 05:22:52.389191: Running on_exit tasks
2024-09-18 05:22:52.389191: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-19 04:29:09.779823: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-19 04:29:09.795813: unable to import ptvsd to enable debugging
2024-09-19 04:29:09.810818: wfastcgi.py 3.0.0 initialized
2024-09-19 04:34:44.726906: Running on_exit tasks
2024-09-19 04:34:44.727895: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-19 08:59:27.572106: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-19 08:59:27.587095: unable to import ptvsd to enable debugging
2024-09-19 08:59:27.601087: wfastcgi.py 3.0.0 initialized
2024-09-19 09:04:40.610668: Running on_exit tasks
2024-09-19 09:04:40.610668: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-19 09:45:20.082140: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-19 09:45:20.117141: unable to import ptvsd to enable debugging
2024-09-19 09:45:20.136154: wfastcgi.py 3.0.0 initialized
2024-09-19 09:50:34.177616: Running on_exit tasks
2024-09-19 09:50:34.177616: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-19 10:50:29.910829: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-19 10:50:29.925836: unable to import ptvsd to enable debugging
2024-09-19 10:50:29.938830: wfastcgi.py 3.0.0 initialized
2024-09-19 10:59:12.882701: Running on_exit tasks
2024-09-19 10:59:12.882701: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-20 06:10:18.051400: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-20 06:10:18.168405: unable to import ptvsd to enable debugging
2024-09-20 06:10:18.184396: wfastcgi.py 3.0.0 initialized
2024-09-20 06:19:29.779375: Running on_exit tasks
2024-09-20 06:19:29.779375: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-20 14:37:09.920176: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-20 14:37:09.939177: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-20 14:37:09.966184: unable to import ptvsd to enable debugging
2024-09-20 14:37:09.981185: wfastcgi.py 3.0.0 initialized
2024-09-20 14:37:09.981185: wfastcgi.py 3.0.0 initialized
2024-09-20 14:42:19.318066: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-20 14:42:19.318066: Running on_exit tasks
2024-09-20 14:42:19.319065: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-20 14:42:19.365106: Running on_exit tasks
2024-09-20 14:42:19.365106: Running on_exit tasks
2024-09-20 14:51:35.032726: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-20 14:51:35.073734: unable to import ptvsd to enable debugging
2024-09-20 14:51:35.074724: unable to import ptvsd to enable debugging
2024-09-20 14:51:35.106725: wfastcgi.py 3.0.0 initialized
2024-09-20 14:56:48.818673: Running on_exit tasks
2024-09-20 14:57:58.827106: Running on_exit tasks
2024-09-20 14:57:58.827106: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-21 20:47:36.670425: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-21 20:47:36.684419: unable to import ptvsd to enable debugging
2024-09-21 20:47:36.698418: wfastcgi.py 3.0.0 initialized
2024-09-21 20:52:47.903118: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-21 20:52:47.903118: Running on_exit tasks
2024-09-25 10:22:42.464874: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-25 10:22:42.479882: unable to import ptvsd to enable debugging
2024-09-25 10:22:42.492882: wfastcgi.py 3.0.0 initialized
2024-09-25 10:27:50.124847: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-25 10:27:50.460854: Running on_exit tasks
2024-09-25 10:27:50.689858: Running on_exit tasks
2024-09-25 10:52:57.336661: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-25 10:52:57.337656: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-09-25 10:52:57.377657: unable to import ptvsd to enable debugging
2024-09-25 10:52:57.377657: unable to import ptvsd to enable debugging
2024-09-25 10:52:57.391663: wfastcgi.py 3.0.0 initialized
2024-09-25 10:58:11.471986: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-25 10:58:11.472984: Running on_exit tasks
2024-09-25 10:58:11.507984: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-09-25 10:58:11.508985: Running on_exit tasks
2024-10-02 09:21:54.434922: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 09:21:54.434922: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 09:21:54.464923: unable to import ptvsd to enable debugging
2024-10-02 09:21:54.479936: wfastcgi.py 3.0.0 initialized
2024-10-02 09:21:54.479936: wfastcgi.py 3.0.0 initialized
2024-10-02 09:22:19.978770: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 09:22:20.016786: unable to import ptvsd to enable debugging
2024-10-02 09:22:20.034769: wfastcgi.py 3.0.0 initialized
2024-10-02 09:22:21.143785: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 09:22:21.186785: unable to import ptvsd to enable debugging
2024-10-02 09:22:21.205786: wfastcgi.py 3.0.0 initialized
2024-10-02 09:27:32.980032: Running on_exit tasks
2024-10-02 09:27:36.566117: Running on_exit tasks
2024-10-02 09:32:47.966878: Running on_exit tasks
2024-10-02 09:32:51.479381: Running on_exit tasks
2024-10-02 10:28:16.400566: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 10:28:16.400566: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 10:28:16.434560: unable to import ptvsd to enable debugging
2024-10-02 10:28:16.450568: wfastcgi.py 3.0.0 initialized
e debugging
2024-10-02 10:28:16.463558: wfastcgi.py 3.0.0 initialized
2024-10-02 10:38:10.387060: Running on_exit tasks
2024-10-02 10:39:55.383139: Running on_exit tasks
2024-10-02 10:39:55.383139: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-02 12:59:27.306948: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 12:59:27.363956: unable to import ptvsd to enable debugging
2024-10-02 12:59:27.364951: unable to import ptvsd to enable debugging
2024-10-02 12:59:27.391949: wfastcgi.py 3.0.0 initialized
2024-10-02 12:59:27.391949: wfastcgi.py 3.0.0 initialized
2024-10-02 13:04:38.083843: Running on_exit tasks
2024-10-02 13:04:38.083843: Running on_exit tasks
2024-10-02 13:39:26.826803: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 13:39:26.868798: unable to import ptvsd to enable debugging
2024-10-02 13:39:26.883806: wfastcgi.py 3.0.0 initialized
2024-10-02 13:39:26.925803: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 13:39:26.941799: unable to import ptvsd to enable debugging
2024-10-02 13:39:26.956802: wfastcgi.py 3.0.0 initialized
2024-10-02 13:44:40.688606: Running on_exit tasks
2024-10-02 13:44:40.690613: Running on_exit tasks
2024-10-02 13:57:58.321569: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 13:57:58.323570: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 13:57:58.378571: unable to import ptvsd to enable debugging
2024-10-02 13:57:58.401576: unable to import ptvsd to enable debugging
2024-10-02 13:57:58.422571: wfastcgi.py 3.0.0 initialized
2024-10-02 14:03:47.326529: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-02 14:03:47.326529: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-02 14:03:47.326529: Running on_exit tasks
2024-10-02 14:03:47.359529: Running on_exit tasks
2024-10-02 14:03:47.359529: Running on_exit tasks
2024-10-02 14:05:41.857762: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 14:05:41.893767: unable to import ptvsd to enable debugging
2024-10-02 14:05:41.910771: wfastcgi.py 3.0.0 initialized
2024-10-02 14:05:41.982764: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 14:05:42.020764: unable to import ptvsd to enable debugging
2024-10-02 14:05:42.057765: wfastcgi.py 3.0.0 initialized
2024-10-02 14:22:00.555906: Running on_exit tasks
2024-10-02 14:22:00.581912: Running on_exit tasks
2024-10-02 14:50:26.716037: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 14:50:26.732065: unable to import ptvsd to enable debugging
2024-10-02 14:50:26.748060: wfastcgi.py 3.0.0 initialized
2024-10-02 14:50:26.775045: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 14:50:26.789043: unable to import ptvsd to enable debugging
2024-10-02 14:50:26.804043: wfastcgi.py 3.0.0 initialized
2024-10-02 14:56:12.911323: Running on_exit tasks
2024-10-02 14:56:12.932328: Running on_exit tasks
2024-10-02 14:56:12.932328: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-02 15:22:28.312485: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 15:22:28.351480: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 15:22:28.358480: unable to import ptvsd to enable debugging
2024-10-02 15:22:28.385480: wfastcgi.py 3.0.0 initialized
2024-10-02 15:22:28.389481: unable to import ptvsd to enable debugging
2024-10-02 15:22:28.421486: wfastcgi.py 3.0.0 initialized
2024-10-02 15:27:42.165524: Running on_exit tasks
2024-10-02 15:27:42.182513: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-02 15:27:42.182513: Running on_exit tasks
2024-10-02 15:41:57.917646: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 15:41:57.918646: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-02 15:41:57.956648: unable to import ptvsd to enable debugging
2024-10-02 15:41:57.971647: wfastcgi.py 3.0.0 initialized
e debugging
2024-10-02 15:41:57.992655: wfastcgi.py 3.0.0 initialized
2024-10-02 15:47:11.994717: Running on_exit tasks
2024-10-02 15:47:11.996718: Running on_exit tasks
2024-10-03 08:35:31.411973: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-03 08:35:31.415980: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-03 08:35:31.440974: unable to import ptvsd to enable debugging
2024-10-03 08:35:31.453974: wfastcgi.py 3.0.0 initialized
2024-10-03 08:40:44.329901: Running on_exit tasks
2024-10-03 08:40:44.348904: Running on_exit tasks
2024-10-03 08:45:14.863387: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-03 08:45:14.901376: unable to import ptvsd to enable debugging
2024-10-03 08:45:14.919377: wfastcgi.py 3.0.0 initialized
2024-10-03 08:45:14.950376: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-03 08:45:14.966376: unable to import ptvsd to enable debugging
2024-10-03 08:45:14.981384: wfastcgi.py 3.0.0 initialized
2024-10-03 08:50:28.966967: Running on_exit tasks
2024-10-03 08:50:28.968954: Running on_exit tasks
2024-10-03 11:13:28.710244: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-03 11:13:28.728200: unable to import ptvsd to enable debugging
2024-10-03 11:13:28.742198: wfastcgi.py 3.0.0 initialized
2024-10-03 11:13:31.396236: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-03 11:13:31.440236: unable to import ptvsd to enable debugging
2024-10-03 11:13:31.456235: wfastcgi.py 3.0.0 initialized
2024-10-03 11:18:41.482371: Running on_exit tasks
2024-10-03 11:18:41.482371: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-03 11:18:45.353652: Running on_exit tasks
2024-10-03 11:18:45.353652: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-04 08:46:00.985888: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-04 08:46:00.985888: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-04 08:46:01.001896: unable to import ptvsd to enable debugging
2024-10-04 08:46:01.001896: unable to import ptvsd to enable debugging
2024-10-04 08:46:01.016885: wfastcgi.py 3.0.0 initialized
2024-10-04 08:46:01.016885: wfastcgi.py 3.0.0 initialized
2024-10-04 08:51:09.592957: Running on_exit tasks
2024-10-04 08:51:09.593959: Running on_exit tasks
2024-10-04 08:57:01.207916: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-04 08:57:01.245917: unable to import ptvsd to enable debugging
2024-10-04 08:57:01.260923: wfastcgi.py 3.0.0 initialized
2024-10-04 08:57:01.302930: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-04 08:57:01.319925: unable to import ptvsd to enable debugging
2024-10-04 08:57:01.334931: wfastcgi.py 3.0.0 initialized
2024-10-04 09:02:15.316594: Running on_exit tasks
2024-10-04 09:02:15.317589: Running on_exit tasks
2024-10-07 11:19:08.613341: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-07 11:19:08.616297: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-07 11:19:08.646298: unable to import ptvsd to enable debugging
2024-10-07 11:19:08.661307: wfastcgi.py 3.0.0 initialized
2024-10-07 11:19:08.661307: wfastcgi.py 3.0.0 initialized
2024-10-07 11:24:21.455869: Running on_exit tasks
2024-10-07 11:24:21.457861: Running on_exit tasks
2024-10-09 10:45:14.703898: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 10:45:14.719898: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 10:45:14.735898: unable to import ptvsd to enable debugging
2024-10-09 10:45:14.748898: wfastcgi.py 3.0.0 initialized
2024-10-09 10:52:12.510105: Running on_exit tasks
2024-10-09 10:52:12.528085: Running on_exit tasks
2024-10-09 10:52:12.528085: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 10:52:21.326922: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 10:52:21.367923: unable to import ptvsd to enable debugging
2024-10-09 10:52:21.386923: wfastcgi.py 3.0.0 initialized
2024-10-09 10:52:22.108932: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 10:52:22.150934: unable to import ptvsd to enable debugging
2024-10-09 10:52:22.167935: wfastcgi.py 3.0.0 initialized
2024-10-09 10:58:09.483371: Running on_exit tasks
2024-10-09 10:58:09.511365: Running on_exit tasks
2024-10-09 10:58:09.513365: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 13:26:29.836585: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 13:26:29.851614: unable to import ptvsd to enable debugging
2024-10-09 13:26:29.865587: wfastcgi.py 3.0.0 initialized
2024-10-09 13:26:33.119636: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 13:26:33.153640: unable to import ptvsd to enable debugging
2024-10-09 13:26:33.169641: wfastcgi.py 3.0.0 initialized
2024-10-09 13:31:42.816960: Running on_exit tasks
2024-10-09 13:31:42.816960: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 13:31:47.274091: Running on_exit tasks
2024-10-09 13:31:47.274091: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 13:39:17.808754: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 13:39:17.808754: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 13:39:17.831760: unable to import ptvsd to enable debugging
2024-10-09 13:39:17.847747: unable to import ptvsd to enable debugging
2024-10-09 13:39:17.868747: wfastcgi.py 3.0.0 initialized
2024-10-09 13:39:17.868747: wfastcgi.py 3.0.0 initialized
2024-10-09 13:47:26.869628: Running on_exit tasks
2024-10-09 13:47:26.899614: Running on_exit tasks
2024-10-09 13:56:10.889007: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 13:56:10.925021: unable to import ptvsd to enable debugging
2024-10-09 13:56:10.942007: wfastcgi.py 3.0.0 initialized
2024-10-09 13:56:10.966008: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 13:56:11.004154: unable to import ptvsd to enable debugging
2024-10-09 13:56:11.022015: wfastcgi.py 3.0.0 initialized
2024-10-09 14:01:24.718834: Running on_exit tasks
2024-10-09 14:01:24.737831: Running on_exit tasks
2024-10-09 14:01:24.737831: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 14:10:44.845270: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 14:10:44.887279: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 14:10:44.892269: unable to import ptvsd to enable debugging
2024-10-09 14:10:44.923277: wfastcgi.py 3.0.0 initialized
2024-10-09 14:10:44.937270: unable to import ptvsd to enable debugging
2024-10-09 14:10:44.964271: wfastcgi.py 3.0.0 initialized
2024-10-09 14:15:58.386102: Running on_exit tasks
2024-10-09 14:15:58.403093: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 14:15:58.403093: Running on_exit tasks
2024-10-09 14:24:57.613436: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 14:24:57.614436: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 14:24:57.750440: unable to import ptvsd to enable debugging
2024-10-09 14:24:57.766439: wfastcgi.py 3.0.0 initialized
2024-10-09 14:24:57.766439: wfastcgi.py 3.0.0 initialized
2024-10-09 14:30:09.912599: Running on_exit tasks
2024-10-09 14:30:09.912599: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 14:30:09.929591: Running on_exit tasks
2024-10-09 14:30:09.929591: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 15:07:14.606312: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 15:07:14.645312: unable to import ptvsd to enable debugging
2024-10-09 15:07:14.661324: wfastcgi.py 3.0.0 initialized
2024-10-09 15:12:28.328558: Running on_exit tasks
2024-10-09 15:23:48.128605: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 15:23:48.144615: unable to import ptvsd to enable debugging
2024-10-09 15:23:48.159623: wfastcgi.py 3.0.0 initialized
2024-10-09 15:23:49.770639: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 15:23:49.809648: unable to import ptvsd to enable debugging
2024-10-09 15:23:49.826640: wfastcgi.py 3.0.0 initialized
2024-10-09 15:31:21.054843: Running on_exit tasks
2024-10-09 15:31:21.054843: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 15:31:23.849709: Running on_exit tasks
2024-10-09 15:31:23.849709: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 15:50:03.388174: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-09 15:50:03.423206: unable to import ptvsd to enable debugging
2024-10-09 15:50:03.438186: wfastcgi.py 3.0.0 initialized
2024-10-09 15:55:17.484539: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-09 15:55:17.484539: Running on_exit tasks
2024-10-10 09:22:26.712043: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-10 09:22:26.726041: unable to import ptvsd to enable debugging
2024-10-10 09:22:26.742038: wfastcgi.py 3.0.0 initialized
2024-10-10 09:27:38.272691: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-10 09:27:38.272691: Running on_exit tasks
2024-10-10 11:29:57.321690: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-10 11:29:57.322684: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-10 11:29:57.352680: unable to import ptvsd to enable debugging
2024-10-10 11:29:57.367684: wfastcgi.py 3.0.0 initialized
2024-10-10 11:38:40.086920: Running on_exit tasks
2024-10-10 11:38:40.086920: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-10 11:38:40.103926: Running on_exit tasks
2024-10-10 15:11:27.802041: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-10 15:11:27.913038: unable to import ptvsd to enable debugging
2024-10-10 15:11:27.913038: unable to import ptvsd to enable debugging
2024-10-10 15:11:27.929048: wfastcgi.py 3.0.0 initialized
2024-10-10 15:16:40.044808: Running on_exit tasks
2024-10-10 15:16:40.069813: Running on_exit tasks
2024-10-10 15:34:29.067525: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-10 15:34:29.071526: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-10 15:34:29.104525: unable to import ptvsd to enable debugging
2024-10-10 15:34:29.120526: wfastcgi.py 3.0.0 initialized
2024-10-10 15:34:29.120526: wfastcgi.py 3.0.0 initialized
2024-10-10 15:39:40.050477: Running on_exit tasks
2024-10-10 15:39:40.050477: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-10 15:39:40.065472: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-10 15:39:40.065472: Running on_exit tasks
2024-10-11 08:50:26.526503: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-11 08:50:26.542483: unable to import ptvsd to enable debugging
2024-10-11 08:50:26.556488: wfastcgi.py 3.0.0 initialized
2024-10-11 08:50:26.568488: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-11 08:50:26.587481: unable to import ptvsd to enable debugging
2024-10-11 08:50:26.601488: wfastcgi.py 3.0.0 initialized
2024-10-11 08:55:39.342130: Running on_exit tasks
2024-10-11 08:55:39.342130: Running on_exit tasks
2024-10-11 08:55:39.342130: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-11 10:16:39.184693: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-11 10:16:39.184693: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-11 10:16:39.242688: unable to import ptvsd to enable debugging
2024-10-11 10:16:39.261686: unable to import ptvsd to enable debugging
2024-10-11 10:16:39.278686: wfastcgi.py 3.0.0 initialized
2024-10-11 10:21:53.281127: Running on_exit tasks
2024-10-11 10:21:53.281127: Running on_exit tasks
2024-10-14 09:12:28.442454: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-14 09:12:28.462455: unable to import ptvsd to enable debugging
2024-10-14 09:12:28.478456: wfastcgi.py 3.0.0 initialized
2024-10-14 09:22:52.439067: Running on_exit tasks
2024-10-14 09:22:52.439067: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-14 12:05:33.438660: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-14 12:05:33.457698: unable to import ptvsd to enable debugging
2024-10-14 12:05:33.474669: wfastcgi.py 3.0.0 initialized
2024-10-14 12:10:45.109433: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-14 12:10:45.111432: Running on_exit tasks
2024-10-14 13:04:42.959626: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-14 13:04:42.962638: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-14 13:04:43.194635: unable to import ptvsd to enable debugging
2024-10-14 13:04:43.211647: wfastcgi.py 3.0.0 initialized
2024-10-14 13:04:43.211647: wfastcgi.py 3.0.0 initialized
2024-10-14 13:09:52.575098: Running on_exit tasks
2024-10-14 13:15:07.557770: Running on_exit tasks
2024-10-14 13:15:07.557770: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-14 15:40:28.184980: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-14 15:40:28.203980: unable to import ptvsd to enable debugging
2024-10-14 15:40:28.220973: wfastcgi.py 3.0.0 initialized
2024-10-14 15:45:37.863642: Running on_exit tasks
2024-10-18 07:26:29.346582: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-18 07:26:29.362562: unable to import ptvsd to enable debugging
2024-10-18 07:26:29.377733: wfastcgi.py 3.0.0 initialized
2024-10-18 07:31:33.564428: Running on_exit tasks
2024-10-18 08:41:24.438566: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-18 08:41:24.438566: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-18 08:41:24.439565: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-18 08:41:24.460568: unable to import ptvsd to enable debugging
2024-10-18 08:41:24.492565: unable to import ptvsd to enabl2024-10-18 08:41:24.492565: unable to import ptvsd to enable debugging
2024-10-18 08:41:24.522574: wfastcgi.py 3.0.0 initialized
2024-10-18 08:41:24.522574: wfastcgi.py 3.0.0 initialized
2024-10-18 08:41:24.523566: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-18 08:41:24.554565: unable to import ptvsd to enable debugging
2024-10-18 08:41:24.570574: wfastcgi.py 3.0.0 initialized
2024-10-18 08:46:38.545348: Running on_exit tasks
2024-10-18 08:46:38.545348: Running on_exit tasks
2024-10-18 08:46:38.546341: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-18 08:49:33.524088: Running on_exit tasks
2024-10-18 08:49:33.524088: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-24 04:17:08.150239: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-24 04:17:08.165240: unable to import ptvsd to enable debugging
2024-10-24 04:17:08.180245: wfastcgi.py 3.0.0 initialized
2024-10-24 04:22:07.964812: Running on_exit tasks
2024-10-24 05:54:13.368787: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-24 05:54:13.384780: unable to import ptvsd to enable debugging
2024-10-24 05:54:13.399780: wfastcgi.py 3.0.0 initialized
2024-10-24 05:59:26.399693: Running on_exit tasks
2024-10-24 05:59:26.399693: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-24 06:52:16.016246: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-24 06:52:16.053252: unable to import ptvsd to enable debugging
2024-10-24 06:52:16.069237: wfastcgi.py 3.0.0 initialized
2024-10-24 06:57:30.164483: Running on_exit tasks
2024-10-24 06:57:30.165486: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-24 07:04:11.606175: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-24 07:04:11.644172: unable to import ptvsd to enable debugging
2024-10-24 07:04:11.661175: wfastcgi.py 3.0.0 initialized
2024-10-24 07:09:25.710935: Running on_exit tasks
2024-10-24 07:09:25.710935: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-28 09:13:30.338518: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-28 09:13:30.353517: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-28 09:13:30.371529: unable to import ptvsd to enable debugging
2024-10-28 09:13:30.386525: wfastcgi.py 3.0.0 initialized
2024-10-28 09:13:30.386525: wfastcgi.py 3.0.0 initialized
2024-10-28 09:18:42.778641: Running on_exit tasks
2024-10-28 09:18:42.866708: Running on_exit tasks
2024-10-28 09:18:42.866708: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-28 09:18:44.265165: Running on_exit tasks
2024-10-31 08:20:25.737666: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-31 08:20:25.759713: unable to import ptvsd to enable debugging
2024-10-31 08:20:25.775668: wfastcgi.py 3.0.0 initialized
2024-10-31 08:25:38.537508: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-10-31 08:25:38.537508: Running on_exit tasks
2024-10-31 10:01:02.981987: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-10-31 10:01:03.000981: unable to import ptvsd to enable debugging
2024-10-31 10:01:03.019318: wfastcgi.py 3.0.0 initialized
2024-10-31 10:06:15.613830: Running on_exit tasks
2024-10-31 10:06:15.613830: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-04 07:12:14.902760: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-04 07:12:14.919748: unable to import ptvsd to enable debugging
2024-11-04 07:12:14.935764: wfastcgi.py 3.0.0 initialized
2024-11-04 07:17:27.659775: Running on_exit tasks
2024-11-04 07:17:27.659775: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-04 07:43:31.639823: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-04 07:43:31.656831: unable to import ptvsd to enable debugging
2024-11-04 07:43:31.672826: wfastcgi.py 3.0.0 initialized
2024-11-04 07:48:44.490036: Running on_exit tasks
2024-11-04 07:48:44.490036: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-08 04:57:39.302587: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-08 04:57:39.491573: unable to import ptvsd to enable debugging
2024-11-08 04:57:39.508590: wfastcgi.py 3.0.0 initialized
2024-11-08 05:03:14.313338: Running on_exit tasks
2024-11-08 05:03:14.313338: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-11 06:11:28.242429: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-11 06:11:28.258430: unable to import ptvsd to enable debugging
2024-11-11 06:11:28.274433: wfastcgi.py 3.0.0 initialized
2024-11-11 06:16:40.879694: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-11 06:16:40.879694: Running on_exit tasks
2024-11-11 09:40:14.851611: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-11 09:40:14.871612: unable to import ptvsd to enable debugging
2024-11-11 09:40:14.891614: wfastcgi.py 3.0.0 initialized
2024-11-11 09:45:27.150314: Running on_exit tasks
2024-11-11 09:45:27.150314: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-12 02:21:54.355194: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-12 02:21:54.374196: unable to import ptvsd to enable debugging
2024-11-12 02:21:54.390193: wfastcgi.py 3.0.0 initialized
2024-11-12 02:27:06.974543: Running on_exit tasks
2024-11-12 02:27:06.974543: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-12 03:06:13.157152: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-12 03:06:13.199151: unable to import ptvsd to enable debugging
2024-11-12 03:06:13.216152: wfastcgi.py 3.0.0 initialized
2024-11-12 03:11:27.188741: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-12 03:11:27.189741: Running on_exit tasks
2024-11-12 03:49:15.993460: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-12 03:49:16.030421: unable to import ptvsd to enable debugging
2024-11-12 03:49:16.047428: wfastcgi.py 3.0.0 initialized
2024-11-12 03:54:30.043960: Running on_exit tasks
2024-11-12 05:08:48.210108: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-12 05:08:48.251110: unable to import ptvsd to enable debugging
2024-11-12 05:08:48.271109: wfastcgi.py 3.0.0 initialized
2024-11-12 05:14:02.218063: Running on_exit tasks
2024-11-12 05:14:02.218063: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-13 04:48:47.593111: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-13 04:48:47.611111: unable to import ptvsd to enable debugging
2024-11-13 04:48:47.628112: wfastcgi.py 3.0.0 initialized
2024-11-13 04:54:00.023969: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-13 04:54:00.023969: Running on_exit tasks
2024-11-13 05:29:12.319126: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-13 05:29:12.338113: unable to import ptvsd to enable debugging
2024-11-13 05:29:12.355115: wfastcgi.py 3.0.0 initialized
2024-11-13 05:34:24.843111: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-13 05:34:24.843111: Running on_exit tasks
2024-11-13 11:29:42.295675: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-13 11:29:42.313675: unable to import ptvsd to enable debugging
2024-11-13 11:29:42.331674: wfastcgi.py 3.0.0 initialized
2024-11-13 11:34:54.852407: Running on_exit tasks
2024-11-13 11:34:54.853397: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-13 14:23:22.841780: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-13 14:23:22.881781: unable to import ptvsd to enable debugging
2024-11-13 14:23:22.896779: wfastcgi.py 3.0.0 initialized
2024-11-13 14:28:36.830590: Running on_exit tasks
2024-11-13 14:28:36.830590: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-14 06:48:14.539528: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-14 06:48:14.555575: unable to import ptvsd to enable debugging
2024-11-14 06:48:14.571542: wfastcgi.py 3.0.0 initialized
2024-11-14 06:53:19.604220: Running on_exit tasks
2024-11-17 21:36:21.337031: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-17 21:36:21.355026: unable to import ptvsd to enable debugging
2024-11-17 21:36:21.371036: wfastcgi.py 3.0.0 initialized
2024-11-17 21:41:59.821255: Running on_exit tasks
2024-11-17 21:41:59.821255: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-20 11:33:22.623416: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-20 11:33:22.639443: unable to import ptvsd to enable debugging
2024-11-20 11:33:22.654431: wfastcgi.py 3.0.0 initialized
2024-11-20 11:38:29.783723: Running on_exit tasks
2024-11-20 11:38:29.783723: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-26 10:58:07.016658: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-26 10:58:07.033657: unable to import ptvsd to enable debugging
2024-11-26 10:58:07.048661: wfastcgi.py 3.0.0 initialized
2024-11-26 11:03:14.078971: Running on_exit tasks
2024-11-26 11:03:14.078971: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-11-27 08:56:06.463206: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-11-27 08:56:06.480196: unable to import ptvsd to enable debugging
2024-11-27 08:56:06.497204: wfastcgi.py 3.0.0 initialized
2024-11-27 09:01:19.377401: Running on_exit tasks
2024-12-06 10:41:18.456578: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-12-06 10:41:18.456578: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-12-06 10:41:18.472197: unable to import ptvsd to enable debugging
2024-12-06 10:41:18.487835: wfastcgi.py 3.0.0 initialized
2024-12-06 10:48:43.556562: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-12-06 10:48:43.556562: Running on_exit tasks
wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-12-06 10:48:43.556562: Running on_exit tasks
2024-12-17 10:39:50.450444: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-12-17 10:39:50.496449: unable to import ptvsd to enable debugging
2024-12-17 10:39:50.810450: wfastcgi.py 3.0.0 initialized
2024-12-17 10:45:55.162121: Running on_exit tasks
2024-12-17 10:45:55.162121: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2024-12-17 12:20:31.538235: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2024-12-17 12:20:31.561224: unable to import ptvsd to enable debugging
2024-12-17 12:20:31.581224: wfastcgi.py 3.0.0 initialized
2024-12-17 12:25:43.949433: Running on_exit tasks
2025-01-08 03:31:08.365494: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-08 03:31:08.381487: unable to import ptvsd to enable debugging
2025-01-08 03:31:08.397488: wfastcgi.py 3.0.0 initialized
2025-01-08 03:36:45.572086: Running on_exit tasks
2025-01-08 03:36:45.572086: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-08 03:57:29.853664: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-08 03:57:29.898659: unable to import ptvsd to enable debugging
2025-01-08 03:57:29.914663: wfastcgi.py 3.0.0 initialized
2025-01-08 04:02:43.871934: Running on_exit tasks
2025-01-08 04:02:43.871934: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-08 06:00:41.111396: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-08 06:00:41.149402: unable to import ptvsd to enable debugging
2025-01-08 06:00:41.167388: wfastcgi.py 3.0.0 initialized
2025-01-08 06:08:15.200781: Running on_exit tasks
2025-01-08 06:08:15.200781: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-08 06:15:17.013431: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-08 06:15:17.074428: unable to import ptvsd to enable debugging
2025-01-08 06:15:17.096425: wfastcgi.py 3.0.0 initialized
2025-01-08 06:20:30.840753: Running on_exit tasks
2025-01-08 06:20:30.840753: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 02:46:07.623089: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 02:46:07.641087: unable to import ptvsd to enable debugging
2025-01-09 02:46:07.657083: wfastcgi.py 3.0.0 initialized
2025-01-09 02:51:20.546059: Running on_exit tasks
2025-01-09 02:51:20.547050: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 03:39:16.579047: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 03:39:16.620036: unable to import ptvsd to enable debugging
2025-01-09 03:39:16.636039: wfastcgi.py 3.0.0 initialized
2025-01-09 03:44:30.665139: Running on_exit tasks
2025-01-09 03:44:30.665139: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 06:38:27.456263: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 06:38:27.472273: unable to import ptvsd to enable debugging
2025-01-09 06:38:27.486264: wfastcgi.py 3.0.0 initialized
2025-01-09 06:43:40.480755: Running on_exit tasks
2025-01-09 06:43:40.480755: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 09:01:16.244731: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 09:01:16.245727: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 09:01:16.282729: unable to import ptvsd to enable debugging
2025-01-09 09:01:16.298727: unable to import ptvsd to enable debugging
2025-01-09 09:01:16.299736: wfastcgi.py 3.0.0 initialized
2025-01-09 09:01:16.317728: wfastcgi.py 3.0.0 initialized
2025-01-09 09:12:20.301937: Running on_exit tasks
2025-01-09 09:12:20.301937: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 09:12:20.302930: Running on_exit tasks
2025-01-09 09:15:40.180099: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 09:15:40.223098: unable to import ptvsd to enable debugging
2025-01-09 09:15:40.240098: wfastcgi.py 3.0.0 initialized
2025-01-09 09:15:40.332107: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 09:15:40.374100: unable to import ptvsd to enable debugging
2025-01-09 09:15:40.393102: wfastcgi.py 3.0.0 initialized
2025-01-09 09:20:54.199847: Running on_exit tasks
2025-01-09 09:20:54.200840: Running on_exit tasks
2025-01-09 09:24:37.431335: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 09:24:37.470332: unable to import ptvsd to enable debugging
2025-01-09 09:24:37.489328: wfastcgi.py 3.0.0 initialized
2025-01-09 09:24:37.513327: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 09:24:37.531330: unable to import ptvsd to enable debugging
2025-01-09 09:24:37.547328: wfastcgi.py 3.0.0 initialized
2025-01-09 09:32:11.464262: Running on_exit tasks
2025-01-09 09:32:11.464262: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 09:32:11.464262: Running on_exit tasks
2025-01-09 09:32:11.480262: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 10:00:14.021782: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 10:00:14.034784: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 10:00:14.055783: unable to import ptvsd to enable debugging
2025-01-09 10:00:14.055783: unable to import ptvsd to enable debugging
2025-01-09 10:00:14.096783: wfastcgi.py 3.0.0 initialized
2025-01-09 10:05:26.355853: Running on_exit tasks
2025-01-09 10:06:01.355191: Running on_exit tasks
2025-01-09 10:06:01.355191: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 11:24:38.806458: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 11:24:38.843451: unable to import ptvsd to enable debugging
2025-01-09 11:24:38.861443: wfastcgi.py 3.0.0 initialized
2025-01-09 11:29:52.860091: Running on_exit tasks
2025-01-09 11:29:52.861090: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-09 13:01:19.460463: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-09 13:01:19.479485: unable to import ptvsd to enable debugging
2025-01-09 13:01:19.498465: wfastcgi.py 3.0.0 initialized
2025-01-09 13:06:32.221859: Running on_exit tasks
2025-01-09 13:06:32.221859: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-10 01:51:51.000940: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-10 01:51:51.016939: unable to import ptvsd to enable debugging
2025-01-10 01:51:51.030948: wfastcgi.py 3.0.0 initialized
2025-01-10 02:01:44.046169: Running on_exit tasks
2025-01-10 03:53:26.603225: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-10 03:53:26.642222: unable to import ptvsd to enable debugging
2025-01-10 03:53:26.666223: wfastcgi.py 3.0.0 initialized
2025-01-10 03:58:40.670430: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-10 03:58:40.670430: Running on_exit tasks
2025-01-10 08:31:41.770595: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-10 08:31:41.793594: unable to import ptvsd to enable debugging
2025-01-10 08:31:41.808596: wfastcgi.py 3.0.0 initialized
2025-01-10 08:36:54.896428: Running on_exit tasks
2025-01-10 08:36:54.896428: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-11 07:26:44.937542: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-11 07:26:44.954540: unable to import ptvsd to enable debugging
2025-01-11 07:26:44.971544: wfastcgi.py 3.0.0 initialized
2025-01-11 07:31:57.828001: Running on_exit tasks
2025-01-11 07:31:57.828001: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-13 04:45:24.749904: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-13 04:45:24.768926: unable to import ptvsd to enable debugging
2025-01-13 04:45:24.784902: wfastcgi.py 3.0.0 initialized
2025-01-13 04:50:37.569569: Running on_exit tasks
2025-01-13 04:50:37.569569: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-13 07:23:25.353317: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-13 07:23:25.372333: unable to import ptvsd to enable debugging
2025-01-13 07:23:25.389378: wfastcgi.py 3.0.0 initialized
2025-01-13 07:28:38.324648: Running on_exit tasks
2025-01-13 07:28:38.324648: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-13 09:39:13.874820: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-13 09:39:13.910821: unable to import ptvsd to enable debugging
2025-01-13 09:39:13.928815: wfastcgi.py 3.0.0 initialized
2025-01-13 09:45:02.955781: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-13 09:45:02.955781: Running on_exit tasks
2025-01-13 10:09:52.144272: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-13 10:09:52.162261: unable to import ptvsd to enable debugging
2025-01-13 10:09:52.178274: wfastcgi.py 3.0.0 initialized
2025-01-13 10:15:05.122379: Running on_exit tasks
2025-01-13 10:15:05.122379: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-14 02:08:58.407111: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-14 02:08:58.425097: unable to import ptvsd to enable debugging
2025-01-14 02:08:58.440117: wfastcgi.py 3.0.0 initialized
2025-01-14 02:14:11.254562: Running on_exit tasks
2025-01-14 02:14:11.254562: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-14 02:28:28.819590: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-14 02:28:28.859582: unable to import ptvsd to enable debugging
2025-01-14 02:28:28.875582: wfastcgi.py 3.0.0 initialized
2025-01-14 02:33:42.925133: Running on_exit tasks
2025-01-14 02:33:42.926138: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-14 03:29:48.311877: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-14 03:29:48.333876: unable to import ptvsd to enable debugging
2025-01-14 03:29:48.357877: wfastcgi.py 3.0.0 initialized
2025-01-14 03:35:02.396362: Running on_exit tasks
2025-01-14 03:35:02.396362: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-14 07:49:38.487140: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-14 07:49:38.504132: unable to import ptvsd to enable debugging
2025-01-14 07:49:38.521131: wfastcgi.py 3.0.0 initialized
2025-01-14 07:54:51.397104: Running on_exit tasks
2025-01-14 07:54:51.397104: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
2025-01-14 10:38:47.845130: wfastcgi.py will restart when files in C:\inetpub\rdportal-iisnode\python_server\rduploadservice\ are changed: .*((\.py)|(\.config))$
2025-01-14 10:38:47.881130: unable to import ptvsd to enable debugging
2025-01-14 10:38:47.897128: wfastcgi.py 3.0.0 initialized
2025-01-14 10:44:01.970758: Running on_exit tasks
2025-01-14 10:44:01.970758: Unhandled exception in wfastcgi.py: Traceback (most recent call last):
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 774, in main
    record = read_fastcgi_record(fcgi_stream)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\wfastcgi.py", line 158, in read_fastcgi_record
    data = stream.read(8)     # read record
           ^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument
