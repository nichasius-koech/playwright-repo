Feature: Tests User login
      Tests for User Login, Valid and Invalid Cases.

  Background: User Login Pre condition
    Given User navigates to Login Url
    And Login widgets are displayed

  Scenario: Login with correct credentials
    Given User enters correct user name and Password
    When User clicks on Login button
    Then User is successfully logged in

  Scenario: Login with wrong password
    Given User enters valid user name and wrong Password
    When User clicks on Login button
    Then User is not logged in