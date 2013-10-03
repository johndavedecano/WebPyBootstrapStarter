WebPyBootstrapStarter
=====================

HMVC inspired webpy starter with bootstrap ready

1. Create a virtual host or in your public html upload all the project files.
2. Configure your http.conf file then follow the setups here http://webpy.org/cookbook/mod_wsgi-apache
3. I think your done. Let me know if you have any questions.

In your apps folder youll see theres a base module/apps(thats what they call it in django) you can just copy 
the base folder and rename it to something else..

My APACHE CONFIGURATION FOR WAMP SERVER

`````html
LoadModule wsgi_module modules/mod_wsgi.so

<Directory "${path}/public_html">
    Options Indexes FollowSymLinks ExecCGI
    AllowOverride All
    Require all granted
    AddType text/html .py
    AddHandler cgi-script .cgi .py
</Directory>

``````
MY HTACCESS FILE IN THE DOCUMENT ROOT DIRECTORY/PUBLIC_HTML

`````html
<Files index.py>
    SetHandler wsgi-script
    Options ExecCGI FollowSymLinks
</Files>
<IfModule mod_rewrite.c>
  RewriteEngine on
  RewriteBase /
  RewriteCond %{REQUEST_URI} !^/icons
  RewriteCond %{REQUEST_URI} !^/favicon.ico$
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_URI} !^(/.*)+index.py/
  RewriteRule ^(.*)$ index.py/$1 [PT]
</IfModule>

`````
