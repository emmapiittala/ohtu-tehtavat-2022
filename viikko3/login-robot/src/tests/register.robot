*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials   emmaa  pasS2word123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Create User  emmaa  pasS2word123
    Input Credentials  emmaa  namatestitviemunjarjen
    

Register With Too Short Username And Valid Password
    Input Credentials  ck  p4zzw0rz123
    Output Should Contain   Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  opiskelija  jee
    Output Should Contain   Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  obiskelija  abcdefghijklmnopqrs
    Output Should Contain    Password is invalid

***Keywords***
Input New Command And Create User
    Input New Command
