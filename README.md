#Cippy-RE

Reverse Engineering [Cippy App].

##How to get your Cippy ID

1. Open ```CippyProxy.jar``` on your Computer.
2. Use HTTP-Proxy to route all traffic to your Computer and open Cippy App on your phone.
3. Note your Cippy-ID


##How to use (rate.html)

1. Open your browser without protections. (Tested on Safari and Chrome)
  - Chrome users need start from console:
    ```
      chrome.exe --disable-web-security
    ```
2. Open rate.html and enter your Cippy-ID
3. Press start!
4. Enjoy


##How to use (cippy.py)
```cippy.py``` is a Cippy bot written in Python. You can start it directly from a bash shell.

1. Open ```cippy.py``` in a Texteditor and insert your Cippy ID. You can also insert your Pushover information to get updates via push directly on your Smartphone.
2. ```cippy.py``` depends on the python requests library. To install simply run the following commands in your shell.
  ```bash
  $ pip install requests
  $ pip install requests
  ```
3. Run with ```./cippy.py```
4. Enjoy

[Cippy App]: http://http://www.cippy.it
