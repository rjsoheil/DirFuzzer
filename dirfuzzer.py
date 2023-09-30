import requests
from colorama import Back, Fore, Style
import threading
import sys
import queue as queue
import re
import argparse
from time import sleep
import pyfiglet
from pyfiglet import Figlet
import validators
import urllib3
urllib3.disable_warnings()

mylist = ['cgi-bin',
 'images',
 'admin',
 'includes',
 'modules',
 'templates',
 'cache',
 'media',
 'js',
 'language',
 'tmp',
 'search',
 'wp-content',
 'scripts',
 'css',
 'plugins',
 'administrator',
 'components',
 'installation',
 'wp-admin',
 'bin',
 'user',
 'libraries',
 'themes',
 'wp-includes',
 'xmlrpc',
 'forum',
 'stats',
 'contact',
 'misc',
 'test',
 'comment',
 'profiles',
 'node',
 'reply',
 'logout',
 'add',
 'register',
 'login',
 'password',
 'include',
 'download',
 'objects',
 'dyn',
 'img',
 'tag',
 'sites',
 'feed',
 'category',
 'blog',
 'install',
 'trackback',
 'temp',
 'logs',
 'files',
 'aspnet_client',
 'inc',
 'lib',
 'data',
 'comments',
 '_private',
 'help',
 'catalog',
 'page',
 'editor',
 'backup',
 'news',
 'flash',
 'uploads',
 'en',
 'downloads',
 'go',
 'forums',
 'members',
 'mambots',
 'docs',
 'api',
 'config',
 'checkout',
 'content',
 'newsletter',
 'assets',
 'shop',
 'pub',
 'styles',
 'upload',
 '_notes',
 'error',
 'database',
 'ads',
 'private',
 'engine',
 'template',
 'customer',
 'archives',
 'app',
 'rss',
 'author',
 'tools',
 'pdf',
 'ajax',
 'classes',
 'report',
 'vb',
 'store',
 'var',
 'skin',
 'db',
 '_vti_cnf',
 'banners',
 '_vti_log',
 'de',
 'common',
 'secure',
 '_vti_pvt',
 'updates',
 'gallery',
 'email',
 'tags',
 'cgi',
 'pages',
 'fr',
 'about',
 'dev',
 'links',
 'mail',
 'home',
 'cart',
 'users',
 'app_code',
 'archive',
 'video',
 'app_data',
 'downloader',
 'xml',
 'javascript',
 'plus',
 'php',
 'pkginfo',
 'review',
 'account',
 'html',
 'graphics',
 'cms',
 '_vti_bin',
 '_vti_txt',
 'support',
 'catalogsearch',
 '_mm',
 'display']

try:
    if __name__ == "__main__":
        def banner(target=False):
            f = Figlet(font='larry3d')
            v = Figlet(font='big')
            
            print("\n"+Fore.RED + f.renderText('DirFuzzer')+ Fore.CYAN + "Github: https://github.com/rjsoheil")
            sleep(2)
            print(Fore.GREEN + v.renderText('Soheil  is here')+Fore.WHITE+"")
    
            if target:
                sleep(1);print(Fore.RED+f"  [+][+] Start Attack to  {Back.WHITE+Fore.MAGENTA+target+Back.BLACK}{Fore.RED} [+][+]\n"+Fore.WHITE)
            else:    
                sys.exit()
    
        def url(url):
            x = re.search("^http(s)?:\/\/.*\..*", url)
            if x:
                return url
            elif validators.domain(url):
                schema = "https://"+url
                return schema
            else:
                print(Fore.GREEN+"Please enter the correct domain"+Fore.WHITE)
                sys.exit()
    
        def print_status(response, target, path):
            color = ""
            content_length = ""
            if args.length:
                content_length = f"{Fore.CYAN}[Word:{Fore.LIGHTMAGENTA_EX + str(response.headers.get('Content-Length'))}{Fore.CYAN}]{Fore.WHITE}"
            status_code = response.status_code
            default_status = [200,403,500]
    
            if args.code is None and (status_code in default_status):
                if status_code == 200:
                    color = Fore.GREEN+ "Done: "
                elif status_code == 403:
                    color = Fore.YELLOW+ "Check: "
                elif status_code == 500:
                    color = Fore.RED+ "Check: "
                print(f"{color}[!]{status_code}   {color}{target}/{path}    {content_length}\n"+Fore.WHITE+"")
            elif args.code is not None and (status_code == args.code):
                print(f"{Fore.CYAN}[!]{status_code}   {Fore.WHITE}{target}/{path}    {content_length}\n"+Fore.WHITE+"")
    
        def requester(num):
            global headers
            headers = {
                'User-Agent':f'{args.user_agent}'
                      }
            
            Cookie = {}
            if args.cookie is not None:
                string_data = args.cookie
                key, value = string_data.split(":")
                Cookie[key] = value
    
            error_occurred = False
            while True:
                path = q.get()
                try:
                    response = requests.get(f"{target}/{path}",verify=False, headers=headers, cookies=Cookie, timeout=3)
                    print_status(response, target, path)
    
                except KeyboardInterrupt:
                    print("Byee")
    
                except requests.exceptions.ConnectionError:
                    if not error_occurred:
                        print(Fore.RED + "Connection error"+ Fore.WHITE)
                        error_occurred = True
                    elif error_occurred:
                        break
                        sys.exit()
    
                q.task_done()
                if q.empty():
                    break
        if len(sys.argv) < 2:
        	print(Fore.RED+ "[+] Dfuzzer")
        	print(Fore.GREEN+ f"  [-] Use: python3 {sys.argv[0]} -h")
        	sleep(1);banner();sys.exit()
        else:
            # Arguments
            parser = argparse.ArgumentParser(description="Directory Fuzzer _ Creator: rjsoheil _")
            parser.add_argument("--domain" , "-d", help="Target URL in the format http(s)://example.com")
            parser.add_argument("--threads", "-t", type=int, default=15, choices=[15, 20] , help="Number of threads (default: 15 or 20)")   
            parser.add_argument("--code", "-mc", type=int, default=None, help="Match HTTP status code : -mc 200 (RECOMMENDED: default: 200,403,500)")
            parser.add_argument("--length", "-l", action="store_true", default=False, help="Display Content-Length Header value's")
            parser.add_argument("--user_agent", "-ua", type=str, help='Enter your User-Agent, defualt: Mozilla...', default="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0")
            parser.add_argument("--cookie", "-c", default=None, type=str, help='Enter value of your Cookie')
            args = parser.parse_args()

            # target stracture validation
            target = url(args.domain)

            # Welcome
            banner(target); sleep(2)

            # threading
            q = queue.Queue()
            threads = []
            for b in mylist:
                q.put(b)
            for n in range(int(args.threads)):
                t = threading.Thread(target=requester ,args=(n,))             
                threads.append(t)      
                t.start()
            for tr in threads:
                tr.join()
            q.join()
            print(Fore.GREEN+"Happy Hack!"+Fore.WHITE+"")
            
except (KeyboardInterrupt,ConnectionError,requests.exceptions.ConnectionError):
    print(Fore.RED+"Bye"+Fore.WHITE+"")
except (ConnectionError,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
    print(Fore.RED+"Connection Error"+Fore.WHITE+"")