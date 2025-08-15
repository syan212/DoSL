# DoSL (Denial of Service Language)

DoSL is a DSL for carrying out simple DoS attacks

## Commands
- `DEF-ATTACK name {attack_def}`: Signals to interpreter that `attack_def` are the definition of attack `name`.
- `END-DEF;`: Signals to interpreter that the attack commands for the definition of `name` have ended.
- `THREADS num;`: Number of threads for the attack.
- `REQUESTS num;`: Number of requests for each thread.
- `ATTACK-SEQ {attack_commands};`: Signals to the interpreter that the `attack_commands` are to be performed for the set amount of requests for the set amount of threads.
- `START-ATTACK name;`: Starts attack `name`.
- `STOP-ATTACK name;`: Terminates attack `name`.

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
DEF-ATTACK Num1;
THREADS 10;
REQUESTS 100;
ATTACK-SEQ {
GET -url "example.com" -referer "google.com,bing.com";
POST -url "example.com/api" -json {"DoS": "True"} -referer "google.comm";
};
END-DEF;
START-ATTACK Num1;
```
## License
This is licensed under the GNU Lesser General Public License v3.