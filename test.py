from selenium import webdriver

browser = webdriver.Firefox(executable_path="geckodriver.exe")


def get_url():
    url = input("Enter url")
    return url


def get_price():
    browser.get(get_url())
    test = browser.find_element_by_id("offering-price")
    cont = test.text
    print(cont)


def main():
    browser.implicitly_wait(4)
    get_price()
    browser.close()


if __name__ == "__main__":
    main()