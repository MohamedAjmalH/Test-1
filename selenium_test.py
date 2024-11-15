from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the Flask app
url = "http://127.0.0.1:5000/"

# Initialize the WebDriver (this example uses Chrome; adjust for Firefox if needed)
driver = webdriver.Chrome()

try:
    # Open the Flask app URL
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    
    # Locate elements by their tag or class; assuming they are displayed as paragraphs (<p>) in HTML
    mae_element = driver.find_element(By.XPATH, "//p[strong[text()='Mean Absolute Error (MAE):']]")
    mse_element = driver.find_element(By.XPATH, "//p[strong[text()='Mean Squared Error (MSE):']]")
    r2_element = driver.find_element(By.XPATH, "//p[strong[text()='R² Score:']]")
    
    # Retrieve and print the metric values for verification
    mae_text = mae_element.text
    mse_text = mse_element.text
    r2_text = r2_element.text
    
    print("Automated Testing Output:")
    print(mae_text)
    print(mse_text)
    print(r2_text)

    # Verify that the metrics are displayed correctly
    assert "Mean Absolute Error (MAE):" in mae_text, "MAE value not displayed correctly!"
    assert "Mean Squared Error (MSE):" in mse_text, "MSE value not displayed correctly!"
    assert "R² Score:" in r2_text, "R² Score value not displayed correctly!"

    print("All metrics are displayed correctly.")
    
except AssertionError as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser
    driver.quit()
