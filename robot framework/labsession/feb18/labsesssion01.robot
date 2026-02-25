#Create a scalar variable ${NAME} and print it.
#Assign two numbers to variables and print their sum.
#Create a variable ${CITY} and use it inside a sentence.
#Reassign a variable value inside a test case and log the updated value.
#Create a list variable @{FRUITS} and print the first item.
#Loop through a list variable and print each element.
#Find the length of a list variable.
#Create a dictionary variable &{USER} and print one key value.
#Add a new key-value pair to a dictionary variable.
#Access dictionary values inside a loop and print key and value.


*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${NAME}        Ayaskant
${CITY}        Bangalore
@{FRUITS}      Apple    Mango    Banana
&{USER}        name=Ayaskant    age=25    role=Tester
${a}        10
${b}        20
${var}      Hello

*** Test Cases ***

1. Print Scalar Variable
    Log    ${NAME}

2. Sum Of Two Numbers
    ${sum}=    Evaluate    ${a} + ${b}
    Log    Sum is ${sum}

3. Use Variable Inside Sentence
    Log    I live in ${CITY}

4. Reassign Variable Value
    Log    Before: ${var}
    ${var}=    Set Variable    Updated Hello
    Log    After: ${var}

5. Print First Item Of List
    Log    ${FRUITS}[0]

6. Loop Through List
    FOR    ${fruit}    IN    @{FRUITS}
        Log    ${fruit}
    END

7. Find Length Of List
    ${length}=    Get Length    ${FRUITS}
    Log    Length is ${length}

8. Print Dictionary Key Value
    Log    Name is ${USER}[name]

9. Add New Key Value To Dictionary
    ${USER}=    Evaluate    dict($USER, city="Delhi")
    Log    City is ${USER}[city]

10. Loop Through Dictionary
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} : ${value}
    END
