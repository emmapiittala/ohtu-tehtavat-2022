*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Invalid username or password

Login With Incorrect password
    Input Credentials     kalle    salasana
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials     /   jeejee
    Output Should Contain  Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kallejee   kalle1234
    Input Login Command  
