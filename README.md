This is for a site that returns 200 on a failed login, and that only has a raw HTML div as its only error message. It checks for redirect. It can be adjusted for return code, response header length and more.

All fields that you need to adjust should have a corresponding comment. Don't forget to install the wordlist. 

While we do reduce the total amount of requests by specifying a minimum password length, this script still has a large footprint and is probably not something you'd ideally use in a real penetration test due to potential DoS problems. For CTF/Labs it's fine.

Use reponsibly.

