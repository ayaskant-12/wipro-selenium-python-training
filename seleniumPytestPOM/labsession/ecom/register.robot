*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://automationexercise.com
${name}     TestUser
${email}        testuser204@gmail.com
${password}     Test@123

*** Test Cases ***
Register User
    Open Browser    ${url}      firefox
    Maximize Browser Window
    Page Should Contain    Home
    Click Element    xpath://a[normalize-space()='Signup / Login']
    Page Should Contain    New User Signup!
    Input Text    xpath://input[@placeholder='Name']    ${name}
    Input Text    xpath://input[@data-qa='signup-email']    ${email}
    Click Button    xpath://button[normalize-space()='Signup']
    Page Should Contain    Enter Account Information
    Click Element   xpath://input[@id='id_gender1']
    Input Text    xpath://input[@id='password']    ${password}
    Scroll Element Into View    id=days
    Select From List By Value    id=days    16
    Execute Javascript    document.getElementById('months').scrollIntoView(true)
    Select From List By Value    id=months      3
    Execute Javascript    document.getElementById('years').scrollIntoView(true)
    Select From List By Value    id=years       2003
    Click Element    id=newsletter
    Click Element    id=optin
    Input Text    id=first_name    Test
    Input Text    id=last_name    User
    Input Text    id=company    ABC Company
    Input Text    id=address1    Bangalore
    Input Text    id=address2    Kormangla
    Select From List By Label    id=country     India
    Input Text    id=state    Karnataka
    Input Text    id=city    Bangalore
    Input Text    id=zipcode    560001
    Input Text    id=mobile_number    7008412057
    Click Button    xpath://button[@data-qa='create-account']
    Page Should Contain    Account Created!
    Click Element    xpath://a[@data-qa='continue-button']
    Close Browser
