def replace_function(name, *args):
    func_name = name.__name__.replace("_", " ")
    print(func_name, *args)


def open_browser(browser_name):
    replace_function(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    replace_function(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    replace_function(find_registration_button_on_login_page, page_url, button_text)

open_browser("Chrome")
go_to_companyname_homepage("https:/google.com")
find_registration_button_on_login_page("URL", "Login")