*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://automationexercise.com
${email}        testuser204@gmail.com
${password}     Test@123


*** Test Cases ***
Logout User Successfully
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Wait Until Page Contains    Home    timeout=10s
    Click Element    xpath=//a[contains(text(),'Signup / Login')]
    Wait Until Page Contains    Login to your account    timeout=10s
    Input Text    xpath=//input[@data-qa='login-email']    ${email}
    Input Text    xpath=//input[@data-qa='login-password']    ${password}
    Click Button    xpath=//button[@data-qa='login-button']
    Wait Until Page Contains    Logged in as    timeout=10s
    Click Element    xpath=//a[contains(text(),'Logout')]
    Close Browser
