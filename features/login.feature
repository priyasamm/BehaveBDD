Feature: Login functionality
  @login @only
  Scenario Outline: Login with valid credentials
    Given I navigate to login page
    When I enter valid "<email>" and valid "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
    |email|password|
    |priyasam1111@gmail.com|12345|
  @login
  Scenario: Login with invalid email and valid password
    Given I navigate to login page
    When I enter invalid email and valid password into the fields
    And I click on Login button
    Then I should get proper warning message
  @login
  Scenario: Login with valid email and invalid password
    Given I navigate to login page
    When I enter valid email and invalid password into the fields
    And I click on Login button
    Then I should get proper warning message

  @login
  Scenario: Login with invalid credentials
    Given I navigate to login page
    When I enter invalid email and invalid password into the fields
    And I click on Login button
    Then I should get proper warning message

  @login
  Scenario: Login without email and password
    Given I navigate to login page
    When I enter without email and password into the fields
    And I click on Login button
    Then I should get proper warning message
