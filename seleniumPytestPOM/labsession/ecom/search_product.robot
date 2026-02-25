*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://automationexercise.com
${BROWSER}    chrome
${PRODUCT}    tshirt

*** Test Cases ***
Search Product
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Home    15s
    Click Element    xpath=//a[@href='/products']
    Wait Until Location Contains    /products    15s
    Page Should Contain Element    xpath=//h2[contains(text(),'All Products')]
    Input Text    xpath=//input[@id='search_product']    ${PRODUCT}
    Click Element    xpath=//button[@id='submit_search']
    Wait Until Page Contains    Searched Products    15s
    Page Should Contain Element    xpath=//h2[contains(text(),'Searched Products')]
    Page Should Contain Element    xpath=//div[@class='productinfo text-center']
    Close Browser
