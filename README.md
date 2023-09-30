# DirFuzzer

This tool is multithreaded and checks for sensitive **directory** on the target, such as FFUF

	1. Multi Thread  , Fast
	2. Monitoring
	

## Installation

```
git clone https://github.com/rjsoheil/dirfuzzer.git
cd dirfuzzer
chmod +x dirfuzzer.py
python3 -m pip install -r requirements.txt
python3 dirfuzzer.py
```

## Usage
```
python3 dirfuzzer.py -h
```
This will display help for the tool. Here are all the switches it supports.
```
usage: dirfuzzer.py [-h] [--domain DOMAIN] [--threads {15,20}] [--code CODE] [--length] [--user_agent USER_AGENT] [--cookie COOKIE]

Directory Fuzzer _ Creator: rjsoheil _

options:
  -h, --help            show this help message and exit
  --domain DOMAIN,   -d DOMAIN
                        Target URL in the format http(s)://example.com
  [optional]--threads {15,20}, -t {15,20}
                        Number of threads (default: 15 or 20)
  [optional]--code CODE,       -mc CODE
                        Match HTTP status code : -mc 200 (RECOMMENDED: default: 200,403,500)
  [optional]--length,          -l          Display Content-Length Header value's
  [optional]--user_agent USER_AGENT, -ua USER_AGENT
                        Enter your User-Agent, defualt: Mozilla...
  [optional]--cookie COOKIE,   -c COOKIE
                        Enter value of your Cookie
```
## Recommended Usage

```
python3 dirfuzzer.py -d target.com -l -t 20
```
