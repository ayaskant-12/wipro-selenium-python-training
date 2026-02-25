*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://automationexercise.com
${BROWSER}    firefox

*** Test Cases ***
Verify All Products And Product Detail Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Home    15s
    Run Keyword And Ignore Error    Execute Javascript    document.body.classList.remove('modal-open')
    Run Keyword And Ignore Error    Execute Javascript    document.querySelectorAll('[class*="close"],[id*="close"]').forEach(el=>el.click())
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    Wait Until Element Is Visible    xpath=(//a[contains(text(),'View Product')])[1]    15s
    Execute Javascript    document.evaluate("(//a[contains(text(),'View Product')])[1]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
    Wait Until Location Contains    /product_details/    15s
    Page Should Contain Element    xpath=//h2
    Page Should Contain Element    xpath=//p[contains(text(),'Category')]
    Page Should Contain Element    xpath=//span[contains(text(),'Rs.')]
    Page Should Contain Element    xpath=//b[contains(text(),'Availability')]
    Page Should Contain Element    xpath=//b[contains(text(),'Condition')]
    Page Should Contain Element    xpath=//b[contains(text(),'Brand')]
    Close Browser
