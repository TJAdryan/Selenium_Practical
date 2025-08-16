## 1. Testing for Dynamic Content (AJAX) ⏳
What it does: This test verifies that content loaded asynchronously (without a page refresh) appears as expected. Many websites load data in the background after the initial page load. This test waits for a specific element to appear before checking its content, which is a crucial skill for testing modern apps.

Key Selenium Concepts:

Explicit Waits (WebDriverWait): This is the correct way to handle dynamic content. It tells Selenium to wait for a certain condition to be met before proceeding, preventing tests from failing because an element hasn't loaded yet.

Expected Conditions (EC): These are the conditions that WebDriverWait waits for, such as an element being visible, clickable, or present in the DOM.

Python Example:

Python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

try:
    # Find the "Start" button and click it
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # Create a wait object (wait up to 10 seconds)
    wait = WebDriverWait(driver, 10)

    # Wait until the element with id 'finish' is visible, then get its text
    finish_element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    # Assert that the correct text appeared on the page
    assert "Hello World!" in finish_element.text
    print("✅ Test Passed: Dynamic content loaded correctly.")

finally:
    driver.quit()
## 2. Handling Multiple Browser Tabs or Windows 📑
What it does: This test verifies that clicking a link that opens a new tab works correctly. It then switches focus to the new tab, performs an action (like checking the title), closes the new tab, and switches back to the original tab.

Key Selenium Concepts:

driver.window_handles: A list of unique identifiers for all open windows/tabs.

driver.switch_to.window(): Switches the driver's focus to the specified window/tab.

Python Example:

Python

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

try:
    # Get the handle of the original window
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1

    # Click the link that opens a new window
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    # Wait for the new window to open and get its handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Assert we are on the new window by checking its heading
    assert driver.find_element(By.TAG_NAME, "h3").text == "New Window"
    print("✅ Switched to new window successfully.")

    # Close the new window
    driver.close()

    # Switch back to the original window
    driver.switch_to.window(original_window)

    # Assert we are back on the original window
    assert driver.title == "The Internet"
    print("✅ Switched back to original window successfully.")

finally:
    driver.quit()
## 3. Performing a Drag and Drop Action 🖱️
What it does: This test simulates a user dragging an element and dropping it onto another element. This is useful for testing user interfaces with features like reordering lists, uploading files, or building dashboards.

Key Selenium Concepts:

ActionChains: A class for building a sequence of user actions like mouse movements, button clicks, and keyboard events.

drag_and_drop(): A convenience method within ActionChains to perform the entire drag-and-drop gesture.

Python Example:

Python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

try:
    # Identify the source and target elements
    source_element = driver.find_element(By.ID, "column-a")
    target_element = driver.find_element(By.ID, "column-b")

    # Get initial text to verify the change later
    initial_source_text = source_element.text
    initial_target_text = target_element.text

    # Create an ActionChains object and perform the drag and drop
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

    # Assert that the text of the columns has swapped
    assert source_element.text == initial_target_text
    assert target_element.text == initial_source_text
    print("✅ Test Passed: Drag and drop was successful.")

finally:
    driver.quit()
## 4. Taking a Screenshot on Test Failure 📸
What it does: This isn't a test of a website feature, but a test automation feature. It automatically saves a screenshot if a test fails (e.g., an assertion fails or an element isn't found). This is incredibly useful for debugging, especially when running tests in a headless environment or a CI/CD pipeline.

Key Selenium Concepts:

driver.save_screenshot(): Saves a PNG image of the current browser viewport.

Try/Except Blocks: Standard Python error handling used to catch exceptions during the test run.

Python Example:

Python

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium")
    search_box.submit()
    
    # This assertion will fail on purpose to trigger the screenshot
    assert "This text is not on the page" in driver.page_source
    print("Test passed... but it shouldn't have!")

except AssertionError as e:
    # Generate a unique filename with a timestamp
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_name = f"failure_screenshot_{now}.png"
    
    # Save the screenshot
    driver.save_screenshot(screenshot_name)
    print(f"❌ Test Failed! Screenshot saved as: {screenshot_name}")
    # Re-raise the exception so the test runner still reports a failure
    raise e

finally:
    driver.quit()











Tools

Gemini can make mistakes, so double-check it

