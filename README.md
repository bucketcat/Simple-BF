This is for a site that returns 200 on a failed login, and that only has a raw HTML div as its only error message. It checks for redirect. It can be adjusted for return code, response header length and more.

All fields that you need to adjust should have a corresponding comment. Don't forget to install the wordlist. 

While we do reduce the total amount of requests by specifying a minimum password length, this script still has a large footprint and is probably not something you'd ideally use in a real penetration test due to potential DoS problems. For CTF/Labs it's fine. It's also really slow by nature. Seriously, use hashbased cracking if possible or Hydra. Raw bruteforce should only ever be a last resort. If you need to do a raw bruteforce, try to adjust the minimum length for whatever the target website has set it to. Adjusting it to the length of a browser or password managers standard generated length is also an option.

The line ending rules are LF. For Windows, you probably want to change to CRLF. This can easily be done by opening it in notepad++ and changing the LF > CRLF. Same goes for OSX and CR.

![image](https://github.com/bucketcat/Simple-BF/assets/91589201/9c714700-60c1-4f47-914a-9be4ab2c8396)




![image](https://github.com/bucketcat/Simple-BF/assets/91589201/af812b7b-dc9f-49e6-94c8-d8c893861995)



Use reponsibly.

