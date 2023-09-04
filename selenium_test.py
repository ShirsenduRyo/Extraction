from selenium import webdriver

try:
    # Specify the path to ChromeDriver
    chrome_driver_path = "D:\\chrome-win64\\chrome-win64"  # Replace with your actual path
    
    # Initialize the WebDriver with the specified path
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Open a website
    driver.get("https://www.google.com")

    # Check if the page title matches what you expect
    print(actual_title)
    expected_title = "Google"
    actual_title = driver.title

    if expected_title in actual_title:
        print("Selenium setup is correct. The page title is as expected:", actual_title)
    else:
        print("Selenium setup is correct, but the page title does not match:", actual_title)

except Exception as e:
    print("Selenium setup is not correct. Error:", str(e))

finally:
    # Close the browser
    driver.quit()
