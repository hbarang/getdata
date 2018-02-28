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
    browser.implicitly_wait(4)
    get_price()
    browser.close()


if __name__ == "__main__":
    main()