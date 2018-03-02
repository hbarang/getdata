from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException

# relative path to gecko driver
browser = webdriver.Firefox(executable_path="geckodriver.exe")


# getting input
def get_url():
    url = input("Enter the url: ")
    return str(url)


# getting price defined as offering price
def get_price():
    browser.get(get_url())
    test = browser.find_element_by_id("offering-price")
    cont = test.text
    print(cont)


def main():

    while True:
        case = input("Enter 1 if you want to exit or anything else for another url entry.")
        if case == "1":
            browser.close()
            return
        else:
            # waiting for browser to open
            try:
                browser.implicitly_wait(2)
                get_price()
            except InvalidArgumentException:
                print("Probably something wrong with url, try again.")
                pass


if __name__ == "__main__":
    main()