## Alfred
A Mycroft integration for Jeedom

## Description 
Trigger Jeedom scenarios and actions using plain old English. If you are able to send a request to:
    http://#IP_JEEDOM#/core/api/jeeApi.php?apikey=#APIKEY#&type=scenario&id=#ID#&action=#ACTION# then it should work

## Examples 
* "Hey Mycroft, lights" => launches the scenario that turns all your lights on

## Prerequisites
You must install Mycroft on a Repseaker Core V2 and do: 

- sudo apt install python3-mraa libmraa1
- /home/respeaker/mycroft-core/bin/mycroft-msm update https://github.com/BugHunterPhilosopher/Alfred.git

## Credits 
BugHunterPhilosopher
