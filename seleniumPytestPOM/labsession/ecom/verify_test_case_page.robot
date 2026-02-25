*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://automationexercise.com
${BROWSER}    firefox


*** Test Cases ***
Verify Test Cases Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Home    timeout=10s
    Click Element    xpath=//a[contains(text(),'Test Cases')]
    Wait Until Page Contains    Test Cases    timeout=10s
    Location Should Contain    /test_cases
    Close Browser
