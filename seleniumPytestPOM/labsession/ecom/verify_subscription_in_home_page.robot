*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://automationexercise.com
${BROWSER}    chrome

*** Test Cases ***
Verify Subscription In Home Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Home    15s
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    Wait Until Page Contains    Subscription   15s
    Page Should Contain    Subscription
    Input Text    xpath=//input[@id='susbscribe_email']    testuser204@gmail.com
    Click Element    xpath=//button[@id='subscribe']
    Wait Until Page Contains    You have been successfully subscribed!    15s
    Page Should Contain    You have been successfully subscribed!
    Close Browser
