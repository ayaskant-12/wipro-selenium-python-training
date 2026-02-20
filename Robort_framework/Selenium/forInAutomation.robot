*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify multiselect check Buttons
    Open Browser    ${url}  firefox
    Maximize Browser Window
    ${elements}=    Get WebElements    xpath://input[@type='checkbox']
    FOR    ${element}    IN    @{elements}
        Click Element    ${element}
        Sleep    2s
    END
    Close Browser