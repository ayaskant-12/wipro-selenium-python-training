*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://automationexercise.com
${email}        testuser204@gmail.com
${password}     Test@123


*** Test Cases ***
Login User
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Wait Until Page Contains    Home    10s
    Click Element    xpath=//a[contains(text(),'Signup / Login')]
    Wait Until Page Contains    Login to your account    10s
    Input Text    xpath=//input[@data-qa='login-email']    ${EMAIL}
    Input Text    xpath=//input[@data-qa='login-password']    ${PASSWORD}
    Click Button    xpath=//button[@data-qa='login-button']
    Close Browser