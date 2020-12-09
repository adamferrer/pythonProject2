# Created by usuario at 08/12/2020
Feature: Orange Login
# Enter feature name here
  # Enter feature description here

  Scenario Outline: Login to Orange with valid parameters
  Given I launch Chrome browser
  When I open orange HRM Homepage
  And Enter username "<username>" and password "<password>"
  And Click on login button
 # Then User must successfully login to the Dashboard page
    Examples:
      | username |password|
      | admin    |admin123|
      | test     |adminxyz|
  # Enter scenario name here
    # Enter steps here