from utils.logger import get_logger
import time

class BasePage:
    """
    Base page class that provides common web automation methods for all page objects.
    Includes exception handling and logging for enterprise-grade automation.
    """
    
    def __init__(self, page):
        """
        Initialize the BasePage with a Playwright page instance.
        
        Args:
            page: Playwright page object
            
        Effects:
            - Initializes logger
            - Sets page instance
            - Prints page null status for debugging
        """
        self.logger = get_logger()
        self.page = page
        print("is page null : "+ str(self.page is None))

    # ==================== Navigation Methods ====================
    
    def navigate(self, url):
        """
        Navigate to a specified URL.
        
        Args:
            url (str): The URL to navigate to
            
        Raises:
            Exception: If navigation fails
        """
        try:
            self.logger.info(f"Navigating to url: {url}")
            self.page.goto(url)
            self.logger.info(f"Successfully navigated to: {url}")
        except Exception as e:
            self.logger.error(f"Error navigating to {url}: {e}")
            print(f"Navigation error: {e}")
            raise

    # ==================== Click & Interaction Methods ====================
    
    def click(self, locator):
        """
        Click on an element located by the given locator.
        
        Args:
            locator (str): CSS selector or locator string
            
        Raises:
            Exception: If element not found or click fails
        """
        try:
            self.logger.info(f"Clicking on element: {locator}")
            self.page.locator(locator).click()
            self.logger.info(f"Successfully clicked element: {locator}")
        except Exception as e:
            self.logger.error(f"Error clicking on element {locator}: {e}")
            print(f"❌ Click error: {e}")
            raise

    def click_button(self, button_locator):
        """
        Click on a button element.
        
        Args:
            button_locator (str): CSS selector for the button
            
        Raises:
            Exception: If button not found or click fails
        """
        try:
            self.logger.info(f"Clicking button: {button_locator}")
            self.page.locator(button_locator).click()
            self.logger.info(f"Successfully clicked button: {button_locator}")
        except Exception as e:
            self.logger.error(f"Error clicking button {button_locator}: {e}")
            print(f"❌ Button click error: {e}")
            raise

    def click_link(self, link_locator):
        """
        Click on a link element.
        
        Args:
            link_locator (str): CSS selector for the link
            
        Raises:
            Exception: If link not found or click fails
        """
        try:
            self.logger.info(f"Clicking link: {link_locator}")
            self.page.locator(link_locator).click()
            self.logger.info(f"Successfully clicked link: {link_locator}")
        except Exception as e:
            self.logger.error(f"Error clicking link {link_locator}: {e}")
            print(f"❌ Link click error: {e}")
            raise

    # ==================== Text Input Methods ====================
    
    def fill(self, locator, text):
        """
        Fill a text input field with the given text.
        
        Args:
            locator (str): CSS selector for the input field
            text (str): Text to fill
            
        Raises:
            Exception: If element not found or fill fails
        """
        try:
            self.logger.info(f"Filling element: {locator}")
            self.page.locator(locator).fill(text)
            self.logger.info(f"Successfully filled element with: {text}")
        except Exception as e:
            self.logger.error(f"Error filling element {locator}: {e}")
            print(f"❌ Fill error: {e}")
            raise

    def fill_text_field(self, text_field_locator, text_value):
        """
        Fill a text field with the given text value.
        
        Args:
            text_field_locator (str): CSS selector for the text field
            text_value (str): Text value to enter
            
        Raises:
            Exception: If field not found or fill fails
        """
        try:
            self.logger.info(f"Filling text field: {text_field_locator} with value: {text_value}")
            self.page.locator(text_field_locator).clear()
            self.page.locator(text_field_locator).fill(text_value)
            self.logger.info(f"Successfully filled text field with: {text_value}")
        except Exception as e:
            self.logger.error(f"Error filling text field {text_field_locator}: {e}")
            print(f"❌ Text field error: {e}")
            raise

    def fill_textarea(self, textarea_locator, text_value):
        """
        Fill a textarea element with the given text.
        
        Args:
            textarea_locator (str): CSS selector for the textarea
            text_value (str): Text to fill
            
        Raises:
            Exception: If textarea not found or fill fails
        """
        try:
            self.logger.info(f"Filling textarea: {textarea_locator} with value: {text_value}")
            self.page.locator(textarea_locator).clear()
            self.page.locator(textarea_locator).fill(text_value)
            self.logger.info(f"Successfully filled textarea with: {text_value}")
        except Exception as e:
            self.logger.error(f"Error filling textarea {textarea_locator}: {e}")
            print(f"❌ Textarea error: {e}")
            raise

    def clear_text_field(self, locator):
        """
        Clear the text from a text field.
        
        Args:
            locator (str): CSS selector for the field
            
        Raises:
            Exception: If field not found or clear fails
        """
        try:
            self.logger.info(f"Clearing text field: {locator}")
            self.page.locator(locator).clear()
            self.logger.info(f"Successfully cleared text field")
        except Exception as e:
            self.logger.error(f"Error clearing text field {locator}: {e}")
            print(f"❌ Clear text error: {e}")
            raise

    # ==================== Selection Methods (Radio, Checkbox, Dropdown) ====================
    
    def select_radio_by_text(self, radio_locator, option):
        """
        Select a radio button.
        
        Args:
            radio_locator (str): CSS selector for the radio button
            
        Raises:
            Exception: If radio button not found or selection fails
        """
        option = str(option)
        try:
            radio_selected = False

            self.logger.info(f"Selecting radio button: {radio_locator} with value: {option}")
            all_options = self.page.locator(radio_locator)
            for each in all_options:
                if each.text == option:
                    self.page.locator(radio_locator).check()
                    self.logger.info(f"Successfully selected radio button: ", option)
                    radio_selected = True
                    break

            if not radio_selected:
                self.logger.error(f"Radio button not found or selection fails: {option}")
        except Exception as e:
            self.logger.error(f"Error selecting radio button {radio_locator}: with value: {option} {e}")
            print(f"❌ Radio button error: {e}")
            raise

    def select_checkbox(self, checkbox_locator):
        """
        Check a checkbox element.
        
        Args:
            checkbox_locator (str): CSS selector for the checkbox
            
        Raises:
            Exception: If checkbox not found or selection fails
        """
        try:
            self.logger.info(f"Selecting checkbox: {checkbox_locator}")
            self.page.locator(checkbox_locator).check()
            self.logger.info(f"Successfully selected checkbox")
        except Exception as e:
            self.logger.error(f"Error selecting checkbox {checkbox_locator}: {e}")
            print(f"❌ Checkbox error: {e}")
            raise

    def uncheck_checkbox(self, checkbox_locator):
        """
        Uncheck a checkbox element.
        
        Args:
            checkbox_locator (str): CSS selector for the checkbox
            
        Raises:
            Exception: If checkbox not found or uncheck fails
        """
        try:
            self.logger.info(f"Unchecking checkbox: {checkbox_locator}")
            self.page.locator(checkbox_locator).uncheck()
            self.logger.info(f"Successfully unchecked checkbox")
        except Exception as e:
            self.logger.error(f"Error unchecking checkbox {checkbox_locator}: {e}")
            print(f"❌ Uncheck error: {e}")
            raise

    def select_dropdown_option(self, dropdown_locator, option_value):
        """
        Select an option from a dropdown/select element.
        
        Args:
            dropdown_locator (str): CSS selector for the dropdown
            option_value (str): Value of the option to select
            
        Raises:
            Exception: If dropdown not found or selection fails
        """
        try:
            option_value = str(option_value)
            self.logger.info(f"Selecting option '{option_value}' from dropdown: {dropdown_locator}")
            self.page.locator(dropdown_locator).select_option(str(option_value))
            self.logger.info(f"Successfully selected option: {option_value}")
        except Exception as e:
            self.logger.error(f"Error selecting option {option_value} from {dropdown_locator}: {e}")
            print(f"❌ Dropdown selection error: {e}")
            raise

    # ==================== Text Retrieval Methods ====================
    
    def get_text(self, locator):
        """
        Get the text content from an element.
        
        Args:
            locator (str): CSS selector for the element
            
        Returns:
            str: The inner text of the element
            
        Raises:
            Exception: If element not found or retrieval fails
        """
        try:
            self.logger.info(f"Getting text from element: {locator}")
            text = self.page.locator(locator).inner_text()
            self.logger.info(f"Retrieved text: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Error getting text from element {locator}: {e}")
            print(f"❌ Get text error: {e}")
            raise

    def get_input_value(self, input_locator):
        """
        Get the value attribute from an input element.
        
        Args:
            input_locator (str): CSS selector for the input
            
        Returns:
            str: The value of the input
            
        Raises:
            Exception: If input not found or retrieval fails
        """
        try:
            self.logger.info(f"Getting input value from: {input_locator}")
            value = self.page.locator(input_locator).input_value()
            self.logger.info(f"Retrieved input value: {value}")
            return value
        except Exception as e:
            self.logger.error(f"Error getting input value from {input_locator}: {e}")
            print(f"❌ Get input value error: {e}")
            raise

    def get_attribute(self, locator, attribute_name):
        """
        Get an attribute value from an element.
        
        Args:
            locator (str): CSS selector for the element
            attribute_name (str): Name of the attribute
            
        Returns:
            str: The attribute value
            
        Raises:
            Exception: If element not found or retrieval fails
        """
        try:
            self.logger.info(f"Getting attribute '{attribute_name}' from element: {locator}")
            attribute_value = self.page.locator(locator).get_attribute(attribute_name)
            self.logger.info(f"Retrieved attribute value: {attribute_value}")
            return attribute_value
        except Exception as e:
            self.logger.error(f"Error getting attribute {attribute_name} from {locator}: {e}")
            print(f"❌ Get attribute error: {e}")
            raise

    # ==================== Mouse Actions ====================
    
    def mouse_hover(self, locator):
        """
        Hover the mouse over an element.
        
        Args:
            locator (str): CSS selector for the element
            
        Raises:
            Exception: If element not found or hover fails
        """
        try:
            self.logger.info(f"Hovering over element: {locator}")
            self.page.locator(locator).hover()
            self.logger.info(f"Successfully hovered over element")
        except Exception as e:
            self.logger.error(f"Error hovering over element {locator}: {e}")
            print(f"❌ Mouse hover error: {e}")
            raise

    def double_click(self, locator):
        """
        Double-click on an element.
        
        Args:
            locator (str): CSS selector for the element
            
        Raises:
            Exception: If element not found or double-click fails
        """
        try:
            self.logger.info(f"Double-clicking on element: {locator}")
            self.page.locator(locator).dblclick()
            self.logger.info(f"Successfully double-clicked element")
        except Exception as e:
            self.logger.error(f"Error double-clicking element {locator}: {e}")
            print(f"❌ Double-click error: {e}")
            raise

    def right_click(self, locator):
        """
        Right-click on an element.
        
        Args:
            locator (str): CSS selector for the element
            
        Raises:
            Exception: If element not found or right-click fails
        """
        try:
            self.logger.info(f"Right-clicking on element: {locator}")
            self.page.locator(locator).click(button="right")
            self.logger.info(f"Successfully right-clicked element")
        except Exception as e:
            self.logger.error(f"Error right-clicking element {locator}: {e}")
            print(f"❌ Right-click error: {e}")
            raise

    # ==================== Alert Handling ====================
    
    def accept_alert(self):
        """
        Accept (OK) an alert dialog.
        
        Raises:
            Exception: If alert handling fails
        """
        try:
            self.logger.info("Accepting alert dialog")
            self.page.once("dialog", lambda dialog: dialog.accept())
            self.logger.info("Successfully accepted alert")
        except Exception as e:
            self.logger.error(f"Error accepting alert: {e}")
            print(f"❌ Accept alert error: {e}")
            raise

    def dismiss_alert(self):
        """
        Dismiss (Cancel) an alert dialog.
        
        Raises:
            Exception: If alert handling fails
        """
        try:
            self.logger.info("Dismissing alert dialog")
            self.page.once("dialog", lambda dialog: dialog.dismiss())
            self.logger.info("Successfully dismissed alert")
        except Exception as e:
            self.logger.error(f"Error dismissing alert: {e}")
            print(f"❌ Dismiss alert error: {e}")
            raise

    def handle_alert(self, accept=True):
        """
        Handle an alert by accepting or dismissing it.
        
        Args:
            accept (bool): True to accept, False to dismiss
            
        Raises:
            Exception: If alert handling fails
        """
        try:
            action = "accepting" if accept else "dismissing"
            self.logger.info(f"Handling alert by {action}")
            
            if accept:
                self.page.once("dialog", lambda dialog: dialog.accept())
            else:
                self.page.once("dialog", lambda dialog: dialog.dismiss())
            
            self.logger.info(f"Successfully handled alert")
        except Exception as e:
            self.logger.error(f"Error handling alert: {e}")
            print(f"❌ Alert handling error: {e}")
            raise

    def get_alert_text(self):
        """
        Get the text from an alert dialog.
        
        Returns:
            str: The alert message text
            
        Raises:
            Exception: If alert text retrieval fails
        """
        try:
            self.logger.info("Getting alert text")
            alert_text = None
            
            def capture_alert(dialog):
                nonlocal alert_text
                alert_text = dialog.message
                dialog.accept()
            
            self.page.once("dialog", capture_alert)
            self.logger.info(f"Retrieved alert text: {alert_text}")
            return alert_text
        except Exception as e:
            self.logger.error(f"Error getting alert text: {e}")
            print(f"❌ Get alert text error: {e}")
            raise

    # ==================== Window & Tab Management ====================
    
    def switch_to_new_window(self):
        """
        Wait for and switch to a newly opened window/tab.
        
        Returns:
            Page: The new page/window object
            
        Raises:
            Exception: If new window not found or switch fails
        """
        try:
            self.logger.info("Waiting for new window to open")
            with self.page.context.expect_page() as new_page_info:
                # The new page should be captured by context.expect_page()
                pass
            new_page = new_page_info.value
            self.logger.info("Successfully switched to new window")
            return new_page
        except Exception as e:
            self.logger.error(f"Error switching to new window: {e}")
            print(f"❌ Switch window error: {e}")
            raise

    def close_current_window(self):
        """
        Close the current window/page.
        
        Raises:
            Exception: If window close fails
        """
        try:
            self.logger.info("Closing current window")
            self.page.close()
            self.logger.info("Successfully closed current window")
        except Exception as e:
            self.logger.error(f"Error closing window: {e}")
            print(f"❌ Close window error: {e}")
            raise

    # ==================== Frame Handling ====================
    
    def switch_to_frame(self, frame_locator):
        """
        Switch to an iframe and return the frame locator for interaction.
        
        Args:
            frame_locator (str): CSS selector for the iframe
            
        Returns:
            FrameLocator: The frame locator object
            
        Raises:
            Exception: If frame not found or switch fails
        """
        try:
            self.logger.info(f"Switching to frame: {frame_locator}")
            frame = self.page.frame_locator(frame_locator)
            self.logger.info("Successfully switched to frame")
            return frame
        except Exception as e:
            self.logger.error(f"Error switching to frame {frame_locator}: {e}")
            print(f"❌ Switch frame error: {e}")
            raise

    def switch_to_frame_by_name(self, frame_name):
        """
        Switch to an iframe by its name attribute.
        
        Args:
            frame_name (str): The name attribute of the iframe
            
        Returns:
            FrameLocator: The frame locator object
            
        Raises:
            Exception: If frame not found
        """
        try:
            self.logger.info(f"Switching to frame by name: {frame_name}")
            frame = self.page.frame_locator(f'iframe[name="{frame_name}"]')
            self.logger.info(f"Successfully switched to frame: {frame_name}")
            return frame
        except Exception as e:
            self.logger.error(f"Error switching to frame by name {frame_name}: {e}")
            print(f"❌ Switch frame by name error: {e}")
            raise

    # ==================== JavaScript Execution ====================
    
    def execute_javascript(self, script, *args):
        """
        Execute JavaScript code in the context of the page.
        
        Args:
            script (str): JavaScript code to execute
            *args: Arguments to pass to the script
            
        Returns:
            Any: The result of the JavaScript execution
            
        Raises:
            Exception: If script execution fails
        """
        try:
            self.logger.info(f"Executing JavaScript: {script[:50]}...")
            result = self.page.evaluate(script, args)
            self.logger.info(f"Successfully executed JavaScript, result: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error executing JavaScript: {e}")
            print(f"❌ JavaScript execution error: {e}")
            raise

    def scroll_to_element(self, locator):
        """
        Scroll to an element on the page.
        
        Args:
            locator (str): CSS selector for the element
            
        Raises:
            Exception: If scroll fails
        """
        try:
            self.logger.info(f"Scrolling to element: {locator}")
            self.page.locator(locator).scroll_into_view_if_needed()
            self.logger.info("Successfully scrolled to element")
        except Exception as e:
            self.logger.error(f"Error scrolling to element {locator}: {e}")
            print(f"❌ Scroll error: {e}")
            raise

    def scroll_page(self, pixels):
        """
        Scroll the page by a specified number of pixels.
        
        Args:
            pixels (int): Number of pixels to scroll (positive = down, negative = up)
            
        Raises:
            Exception: If scroll fails
        """
        try:
            self.logger.info(f"Scrolling page by {pixels} pixels")
            self.page.evaluate(f"window.scrollBy(0, {pixels})")
            self.logger.info("Successfully scrolled page")
        except Exception as e:
            self.logger.error(f"Error scrolling page: {e}")
            print(f"❌ Page scroll error: {e}")
            raise

    # ==================== Element Visibility & Validation ====================
    
    def is_element_visible(self, locator):
        """
        Check if an element is visible on the page.
        
        Args:
            locator (str): CSS selector for the element
            
        Returns:
            bool: True if element is visible, False otherwise
            
        Raises:
            Exception: If check fails
        """
        try:
            self.logger.info(f"Checking visibility of element: {locator}")
            is_visible = self.page.locator(locator).is_visible()
            self.logger.info(f"Element visibility: {is_visible}")
            return is_visible
        except Exception as e:
            self.logger.error(f"Error checking element visibility {locator}: {e}")
            print(f"❌ Visibility check error: {e}")
            raise

    def is_element_enabled(self, locator):
        """
        Check if an element is enabled.
        
        Args:
            locator (str): CSS selector for the element
            
        Returns:
            bool: True if element is enabled, False otherwise
            
        Raises:
            Exception: If check fails
        """
        try:
            self.logger.info(f"Checking if element is enabled: {locator}")
            is_enabled = self.page.locator(locator).is_enabled()
            self.logger.info(f"Element enabled status: {is_enabled}")
            return is_enabled
        except Exception as e:
            self.logger.error(f"Error checking element enabled status {locator}: {e}")
            print(f"❌ Enabled check error: {e}")
            raise

    def wait_for_element(self, locator, timeout=10000):
        """
        Wait for an element to be present on the page.
        
        Args:
            locator (str): CSS selector for the element
            timeout (int): Timeout in milliseconds
            
        Raises:
            Exception: If element not found within timeout
        """
        try:
            self.logger.info(f"Waiting for element: {locator} (timeout: {timeout}ms)")
            self.page.locator(locator).wait_for(timeout=timeout)
            self.logger.info("Element found successfully")
        except Exception as e:
            self.logger.error(f"Error waiting for element {locator}: {e}")
            print(f"❌ Wait for element error: {e}")
            raise

    # ==================== Utility Methods ====================
    
    def take_screenshot(self, filename):
        """
        Take a screenshot of the current page and save it.
        
        Args:
            filename (str): Path and filename for the screenshot
            
        Raises:
            Exception: If screenshot fails
        """
        try:
            self.logger.info(f"Taking screenshot: {filename}")
            self.page.screenshot(path=filename)
            self.logger.info(f"Successfully saved screenshot: {filename}")
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")
            print(f"��� Screenshot error: {e}")
            raise

    def wait(self, milliseconds):
        """
        Wait/pause for a specified duration.
        
        Args:
            milliseconds (int): Duration to wait in milliseconds
        """
        try:
            self.logger.info(f"Waiting for {milliseconds}ms")
            time.sleep(milliseconds / 1000)
            self.logger.info("Wait completed")
        except Exception as e:
            self.logger.error(f"Error during wait: {e}")
            print(f"❌ Wait error: {e}")
            raise
