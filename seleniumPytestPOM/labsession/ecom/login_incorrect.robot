*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}              https://automationexercise.com
${email}    wronguser@gmail.com
${password}     wrongpass123


*** Test Cases ***
Login User With Incorrect Email And Password
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Wait Until Page Contains    Home    timeout=10s
    Click Element    xpath=//a[contains(text(),'Signup / Login')]
    Wait Until Page Contains    Login to your account    timeout=10s
    Input Text    xpath=//input[@data-qa='login-email']    ${email}
    Input Text    xpath=//input[@data-qa='login-password']    ${password}
    Click Button    xpath=//button[@data-qa='login-button']
    Wait Until Page Contains    Your email or password is incorrect!
    Close Browser
