*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://automationexercise.com
${NAME}       Test User
${EMAIL}      testuser204@gmail.com
${SUBJECT}    Product Inquiry
${MESSAGE}    This is a test message
${FILE_PATH}  C:\\Users\\KIIT\\Downloads\\sampleFile.jpeg


*** Test Cases ***
Contact Us Form Test
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Wait Until Page Contains    Home    timeout=10s
    Click Element    xpath=//a[contains(text(),'Contact us')]
    Wait Until Page Contains    Get In Touch    timeout=10s
    Input Text    name=name    ${NAME}
    Input Text    name=email    ${EMAIL}
    Input Text    name=subject    ${SUBJECT}
    Input Text    id=message    ${MESSAGE}
    Choose File    name=upload_file    ${FILE_PATH}
    Click Button    name=submit
    Handle Alert    ACCEPT
    Wait Until Page Contains
    ...    Success! Your details have been submitted successfully.
    ...    timeout=10s
    Click Element    xpath=//a[contains(text(),'Home')]
    Wait Until Page Contains    Home    timeout=10s
    Close Browser
