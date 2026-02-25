*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}      firefox
    Maximize Browser Window
#    Wait Until Element Is Visible    xpath://input[@id='c_bs_1']
    ${elements}=    Get WebElements    xpath://input[starts-with(@id,'c_bs_')]
    FOR    ${element}    IN    @{elements}
        Wait Until Element Is Visible    ${element}
        Scroll Element Into View    ${element}
        Sleep    2s
        Click Element    ${element}

    END
    Wait Until Element Is Visible       xpath://a[normalize-space()='Radio Button']
    Click Element       xpath://a[normalize-space()='Radio Button']
    Click Element       xpath://input[@value='igottwo']
    Close Browser
