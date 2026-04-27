const { Builder, By, until } = require('selenium-webdriver');
const assert = require('assert');

async function loginTest() {
    let driver = await new Builder().forBrowser('chrome').build();

    try {
        // --------------------------------
        // 1. Open Login Page (Test Case)
        // --------------------------------
        await driver.get('https://the-internet.herokuapp.com/login');

        // --------------------------------
        // 2. Enter Credentials
        // --------------------------------
        await driver.findElement(By.id('username')).sendKeys('tomsmith');
        await driver.findElement(By.id('password')).sendKeys('SuperSecretPassword!');

        // --------------------------------
        // 3. Click Login Button
        // --------------------------------
        await driver.findElement(By.css('button[type="submit"]')).click();

        // --------------------------------
        // 4. Wait for Result
        // --------------------------------
        let message = await driver.wait(
            until.elementLocated(By.id('flash')),
            5000
        );

        let text = await message.getText();
        console.log("Message:", text);

        // --------------------------------
        // 5. Validate Expected Output
        // --------------------------------
        assert(text.includes('You logged into a secure area!'));
        console.log("✅ Login test passed");

    } catch (error) {
        console.log("❌ Test failed:", error.message);
    } finally {
        await driver.quit();
    }
}

loginTest();
