WebPyBootstrapStarter
=====================

HMVC inspired webpy starter with bootstrap ready

1. Create a virtual host or in your public html upload all the project files.
2. Configure your http.conf file then follow the setups here http://webpy.org/cookbook/mod_wsgi-apache
3. I think your done. Let me know if you have any questions.

My APACHE CONFIGURATION FOR WAMP SERVER
`````html
LoadModule wsgi_module modules/mod_wsgi.so

<Directory "${path}/data/localweb">
    Options Indexes FollowSymLinks ExecCGI
    AllowOverride All
    Require all granted
</Directory>

``````
