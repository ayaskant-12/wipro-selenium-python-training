*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
Verify the login testcase
    Open Browser    ${url}      firefox
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@placeholder='Username']
    Input Text    xpath://input[@placeholder='Username']    Admin
    Input Text    xpath://input[@placeholder='Password']    admin123
    Click Element    xpath://button[normalize-space()='Login']
    Wait Until Element Is Visible    xpath://h6[@class=oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module]
    Element Should Be Visible    xpath://h6[@class=oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module]
    Close Browser
