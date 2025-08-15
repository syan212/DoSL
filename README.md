# DoSL (Denial of Service Language)

DoSL is a DSL (Domain Specific Language) for carrying out simple DoS attacks. This is for educational purposes only.

## Commands
All commands are case-insensitive.
- `DEF-ATTACK name {attack_def}`: Signals to interpreter that `attack_def` are the definition of attack `name`.
- `THREADS num;`: Number of threads for the attack. Use inside the braces after `DEF-ATTACK`.
- `REQUESTS num;`: Number of requests for each thread. Use inside the braces after `DEF-ATTACK`.
- `ATTACK-SEQ {attack_commands};`: Signals to the interpreter that the `attack_commands` are to be performed for the set amount of requests for the set amount of threads. Use inside the braces after `DEF-ATTACK`.
- `START-ATTACK name;`: Starts attack `name`.
- `STOP-ATTACK name;`: Terminates attack `name`.
- `SLEEP delay`: Sleeps for `delay` seconds. `delay` can be a float or an integer.

### Attack Commands
These commands are to be used inside curly brackets (`{}`).
#### `POST` 
Sends POST requests with the specified parameters as below
- `-url`: Specifies URL to send POST requests to. 
  - **Omittable?**: No. 
  - **Format**: Surround the URL with double quotes (`""`). Can start with `https://` or `http://` but if neither is specified, `https://` is added.
- `-data`: Non-JSON POST Data to send to URL. 
  - **Omittable?**: Yes.
  - **Default Value**: None.
  - **Format**: Suround the data with double quotes (`""`) and seperate the keys and values with colons (`:`).
  - Other Notes: Mutually exclusive with `-json`.
- `-json`: JSON POST Data to send to URL. 
  - **Omittable?**: Yes.
  - **Default Value**: None.
  - **Format**: Input as a JSON object.
  - Other Notes: Mutually exclusive with `-data`.
- `-proxies`: Proxies for the request.
  - **Omittable?**: Yes.  
  - **Default Value**: Configured in proxies.txt.
  - **Format**: Simply input the proxy/proxies protocol followed by `://` and the proxy IP and port surrounded by double quotes (`""`). If there are multiple proxies, seperate them with commas (`,`).
- `-referer`: Referer for the request headers. 
  - **Omittable?**: Yes.
  - **Default Value**: Configured in referers.txt 
  - **Format**: Can be list (chosen randomly from the entered list seperated by commas) or a single string, both surrounded by double quotes (`""`).
#### `GET` 
Sends GET requests with the specified parameters as below
- `-url`: Specifies URL to send GET requests to. 
  - **Omittable?**: No. 
  - **Format**: Surround the URL with double quotes (`""`). Can start with `https://` or `http://` but if neither is specified, `https://` is added.
- `-proxies`: Proxies for the request.
  - **Omittable?**: Yes.  
  - **Default Value**: Configured in proxies.txt.
  - **Format**: Simply input the proxy/proxies protocol followed by `://` and the proxy IP and port, all surrounded by double quotes (`""`). If there are multiple proxies, seperate them with commas (`,`).
- `-referer`: Referer for the request headers. 
  - **Omittable?**: Yes.
  - **Default Value**: Configured in referers.txt 
  - **Format**: Can be list (chosen randomly from the entered list seperated by commas) or a single string, both surrounded by double quotes (`""`).

## Other syntax
Semicolon (`;`) indicates EOL (End of line).
## Example
```
def-attack Num1{
    threads 10;
    requests 100;
    attack-seq {
        GET -url "example.com" -referer "google.com,bing.com";
        POST -url "example.com/api" -json {"DoS": "True"} -referer "google.com";
    };
};
start-attack Num1;
```
## License
This is licensed under the GNU Lesser General Public License v3.