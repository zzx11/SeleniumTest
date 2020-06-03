from selenium import webdriver
import os


def screen_shot(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace("\\", "/")
    base = base_dir.split('/testcase')[0]
    print(base)
    file_path = base + "/Report/Image/" + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == "__main__":
    dr = webdriver.Chrome()
    dr.get("https://www.baidu.com")
    screen_shot(dr, "aa.png")
    dr.quit()
