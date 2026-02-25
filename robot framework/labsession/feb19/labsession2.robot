*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php
*** Test Cases ***
Verify drop down
    Open Browser    ${url}      firefox
    Maximize Browser Window
    Wait Until Element Is Visible    id=state
    Select From List By Index    id=state       2
    Sleep    2s
    Select From List By Index    id=city        2
    Sleep    2s
    Close Browser