


**Apache Documention For Developement Team**

**Where Development Team Adds Their Files** <br>
-htdoc contains static files (index.html, styles, images, etc.) 

-outside of the htdocs folder put the components folder containing typescript files, until they are converted to js by tsc and manually put in the htdoc directory. Or we use a bundler to automate that same process.  

**View Website Locally** <br>
-Install Apache server for your operating system <br>
-Adjust SRVTOOT directory to your file path using forward slashes and no slash a the end of the path. See config file for more details (conf>httpd.conf).
Start server:<br>
-(windows) httpd -k start <br>
-(linux) sudo systemctl start apache2 <br>
-(mac) sudo launchctl load -w /System/Library/LaunchDaemons/org.apache.httpd.plist <br>
-Go to localhost port 80 **("Hello CareerRipple Team!")**<br>
-Note: you can't start with it with the shortcuts you might have to define the full path all th way to the httpd.exe and run that path.



**Original preloaded config settings (these are configurations and modules chosen from the modules folder). The commented explainations can be found in the conf>httpd.conf. This list just makes it easy to see them all together:**

        Define SRVROOT "c:/Apache24"

        ServerRoot "${SRVROOT}"

        Listen 80

        LoadModule actions_module modules/mod_actions.so
        LoadModule alias_module modules/mod_alias.so
        LoadModule allowmethods_module modules/mod_allowmethods.so
        LoadModule asis_module modules/mod_asis.so
        LoadModule auth_basic_module modules/mod_auth_basic.so
        LoadModule authn_core_module modules/mod_authn_core.so
        LoadModule authn_file_module modules/mod_authn_file.so
        LoadModule authz_core_module modules/mod_authz_core.so
        LoadModule authz_groupfile_module modules/mod_authz_groupfile.so
        LoadModule authz_host_module modules/mod_authz_host.so
        LoadModule authz_user_module modules/mod_authz_user.so
        LoadModule autoindex_module modules/mod_autoindex.so
        LoadModule cgi_module modules/mod_cgi.so
        LoadModule dir_module modules/mod_dir.so
        LoadModule env_module modules/mod_env.so
        LoadModule include_module modules/mod_include.so
        LoadModule isapi_module modules/mod_isapi.so
        LoadModule log_config_module modules/mod_log_config.so
        LoadModule mime_module modules/mod_mime.so
        LoadModule negotiation_module modules/mod_negotiation.so
        LoadModule setenvif_module modules/mod_setenvif.so


        <IfModule unixd_module>
          User daemon
          Group daemon
        </IfModule>
          
        ServerAdmin admin@example.com

        <Directory />
          AllowOverride none
          Require all denied
        </Directory>

        DocumentRoot "${SRVROOT}/htdocs"

        <Directory "${SRVROOT}/htdocs">
          Options Indexes FollowSymLinks
          AllowOverride None
          Require all granted
        </Directory>

        <IfModule dir_module>
          DirectoryIndex index.html
        </IfModule>

        <Files ".ht*">
          Require all denied
        </Files>

        ErrorLog "logs/error.log"

        LogLevel warn

        <IfModule log_config_module>
            LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \{User-Agent}i\"" combined
            LogFormat "%h %l %u %t \"%r\" %>s %b" common

          <IfModule logio_module>
            LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O" combinedio
          </IfModule>
            CustomLog "logs/access.log" common
        </IfModule>


        <IfModule alias_module>
          ScriptAlias /cgi-bin/ "${SRVROOT}/cgi-bin/"
        </IfModule>

        <IfModule cgid_module>
        </IfModule>

        <Directory "${SRVROOT}/cgi-bin">
            AllowOverride None
            Options None
            Require all granted
        </Directory>

        <IfModule headers_module>
            RequestHeader unset Proxy early
        </IfModule>

        <IfModule mime_module> 
          TypesConfig conf/mime.types 
          AddType application/x-compress .Z
          AddType application/x-gzip .gz .tgz 
        </IfModule>  

        <IfModule proxy_html_module>
        Include conf/extra/proxy-html.conf
        </IfModule>

        <IfModule ssl_module>
          SSLRandomSeed startup builtin
          SSLRandomSeed connect builtin
        </IfModule>
                                  
                          
 
                          
                          
                          
                          
  
  
  **Apache HTTP Server**              

  What is it?
  -----------

  The Apache HTTP Server is a powerful and flexible HTTP/1.1 compliant
  web server.  Originally designed as a replacement for the NCSA HTTP
  Server, it has grown to be the most popular web server on the
  Internet.  As a project of the Apache Software Foundation, the
  developers aim to collaboratively develop and maintain a robust,
  commercial-grade, standards-based server with freely available
  source code.

  The Latest Version
  ------------------

  Details of the latest version can be found on the Apache HTTP
  server project page under https://httpd.apache.org/.

  Documentation
  -------------

  The documentation available as of the date of this release is
  included in HTML format in the docs/manual/ directory.  The most
  up-to-date documentation can be found at
  https://httpd.apache.org/docs/2.4/.

  Installation
  ------------

  Please see the file called INSTALL.  Platform specific notes can be
  found in README.platforms.

  Licensing
  ---------

  Please see the file called LICENSE.

  Cryptographic Software Notice
  -----------------------------

  This distribution may include software that has been designed for use
  with cryptographic software.  The country in which you currently reside
  may have restrictions on the import, possession, use, and/or re-export
  to another country, of encryption software.  BEFORE using any encryption
  software, please check your country's laws, regulations and policies
  concerning the import, possession, or use, and re-export of encryption
  software, to see if this is permitted.  See <https://www.wassenaar.org/>
  for more information.

  The U.S. Government Department of Commerce, Bureau of Industry and
  Security (BIS), has classified this software as Export Commodity 
  Control Number (ECCN) 5D002.C.1, which includes information security
  software using or performing cryptographic functions with asymmetric
  algorithms.  The form and manner of this Apache Software Foundation
  distribution makes it eligible for export under the License Exception
  ENC Technology Software Unrestricted (TSU) exception (see the BIS 
  Export Administration Regulations, Section 740.13) for both object 
  code and source code.

  The following provides more details on the included files that
  may be subject to export controls on cryptographic software:

    Apache httpd 2.0 and later versions include the mod_ssl module under
       modules/ssl/
    for configuring and listening to connections over SSL encrypted
    network sockets by performing calls to a general-purpose encryption
    library, such as OpenSSL or the operating system's platform-specific
    SSL facilities.

    In addition, some versions of apr-util provide an abstract interface
    for symmetrical cryptographic functions that make use of a
    general-purpose encryption library, such as OpenSSL, NSS, or the
    operating system's platform-specific facilities. This interface is
    known as the apr_crypto interface, with implementation beneath the
    /crypto directory. The apr_crypto interface is used by the
    mod_session_crypto module available under
      modules/session
    for optional encryption of session information.

    Some object code distributions of Apache httpd, indicated with the
    word "crypto" in the package name, may include object code for the
    OpenSSL encryption library as distributed in open source form from
    <https://www.openssl.org/source/>.

  The above files are optional and may be removed if the cryptographic
  functionality is not desired or needs to be excluded from redistribution.
  Distribution packages of Apache httpd that include the word "nossl"
  in the package name have been created without the above files and are
  therefore not subject to this notice.

  Contacts
  --------

     o If you want to be informed about new code releases, bug fixes,
       security fixes, general news and information about the Apache server
       subscribe to the apache-announce mailing list as described under
       <https://httpd.apache.org/lists.html#http-announce>

     o If you want freely available support for running Apache please see the
       resources at <https://httpd.apache.org/support.html>

     o If you have a concrete bug report for Apache please see the instructions
       for bug reporting at <https://httpd.apache.org/bug_report.html>

     o If you want to participate in actively developing Apache please
       subscribe to the `dev@httpd.apache.org' mailing list as described at
       <https://httpd.apache.org/lists.html#http-dev>

