*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${name}     John
${city}     Hyderabad
${address}      St Peters Road
@{list1}    green   red     blue
@{list2}    apple   banana  grapes
&{creds}    username=admin      password=admin123

*** Test Cases ***
Verify the variables
    Log    ${name}
    Log    ${city}
    Log    ${address}
    FOR    ${l1}    IN    @{list1}
        Log    ${l1}
    END
    FOR    ${l2}    IN    @{list2}
        Log    ${l2}
    END
    Log    ${list1}[0]
    Log    ${list1}[1]
    Log    ${creds}[username]
    Log    ${creds}[password]