*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.saucedemo.com/
*** Test Cases ***
labsession
    Open Browser    ${url}      firefox
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@id='user-name']
    Input Text    xpath://input[@id='user-name']    standard_user
    Input Text    xpath://input[@id='password']    secret_sauce
    Click Element    xpath://input[@id='login-button']
    Wait Until Element Is Visible    xpath://div[@class='app_logo']
    Sleep    2s
    Click Element    xpath://button[@id='add-to-cart-sauce-labs-backpack']
    Sleep    2s
    Click Element    xpath://button[@id='add-to-cart-sauce-labs-bike-light']
    Sleep    2s
    Click Element    xpath://a[@class='shopping_cart_link']
    Sleep    2s
    Page Should Contain Element    xpath://div[normalize-space()='Sauce Labs Backpack']
    Page Should Contain Element    xpath://div[normalize-space()='Sauce Labs Bike Light']
    Click Element    xpath://button[@id='checkout']
    Sleep    2s
    Input Text    xpath://input[@id='first-name']    Ayaskant
    Sleep    2s
    Input Text    xpath://input[@id='last-name']    Dash
    Sleep    2s
    Input Text    xpath://input[@id='postal-code']    751024
    Sleep    2s
    Click Element    xpath://input[@id='continue']
    Sleep    2s
    Click Element    xpath://button[@id='finish']
    Sleep    2s
    Page Should Contain Element    xpath://h2[normalize-space()='Thank you for your order!']
    Close Browser