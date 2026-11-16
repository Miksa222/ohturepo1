*** Settings ***
Resource  resource.robot


*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input  kalle
    Input  kalle123
    Run Application
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input  new
    Input  kalle
    Input  kalle123
    Input  new
    Input  kalle
    Input  kalle123
    Run Application
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input  new
    Input  ka
    Input  kalle123
    Run Application
    Output Should Contain  Username minimum length is 3

Register With Enough Long But Invalid Username And Valid Password
    Input  new
    Input  kallö
    Input  kalle123
    Run Application
    Output Should Contain  Username can only contain characters a-z

Register With Valid Username And Too Short Password
    Input  new
    Input  kalle
    Input  kalle12
    Run Application
    Output Should Contain  Password minimum length is 8

Register With Valid Username And Long Enough Password Containing Only Letters
    Input  new
    Input  kalle
    Input  kallekalle
    Run Application
    Output Should Contain  Password must not contain only letters







