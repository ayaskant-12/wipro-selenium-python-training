*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://automationexercise.com
${name}       TestUser
${email}        testuser204@gmail.com
*** Test Cases ***
Register User With Existing Email
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Wait Until Page Contains    Home    timeout=10s
    Click Element    xpath=//a[contains(text(),'Signup / Login')]
    Wait Until Page Contains    New User Signup!    timeout=10s
    Input Text    name=name    ${NAME}
    Input Text    xpath=//input[@data-qa='signup-email']    ${EMAIL}
    Click Button    xpath=//button[@data-qa='signup-button']
    Wait Until Page Contains    Email Address already exist!    timeout=10s
    Close Browser
