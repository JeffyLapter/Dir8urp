# -*- coding: UTF-8 -*-
def get_302_info(domain):
    try:
        page_302 = requests.get(domain,headers=header,allow_redirects = False,timeout=3)
        if page_302.status_code == 302:
            redirect_domain = page_302.headers['Location']
            print("[!] 302 redirect from {} to {}".format(domain, redirect_domain))
            return redirect_domain
        else:
            return False
    except requests.exceptions.ConnectTimeout:
        print("Connect time out")
        return False
    except requests.exceptions.ConnectionError:
        print("Unknown server")
        return False
