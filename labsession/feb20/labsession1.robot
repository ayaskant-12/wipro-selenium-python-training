*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem


*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/upload-download.php

${upload_file}      C:\\Users\\KIIT\\Downloads\\code.png
${download_dir}     C:\\Users\\KIIT\\Downloads

*** Test Cases ***
Download File Test
    Open Browser    ${url}      firefox
    Maximize Browser Window
    Click Element    xpath://a[@id='downloadButton']
    Sleep    5s
    File Should Exist       ${download_dir}\\sampleFile.jpeg
    Close Browser
Upload File Test
    Open Browser    ${url}      firefox
    Maximize Browser Window 
    Choose File    xpath://input[@id='uploadFile']    ${upload_file}
    Sleep    3
    Close Browser