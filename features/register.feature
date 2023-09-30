Feature: Register account functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to register page
    When I enter mandatory fields
    And I select privacy policy option
    And I click on continue button
    Then Account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to register page
    When I enter details into all fields
    And I select privacy policy option
    And I click on continue button
    Then Account should get created

  @register
  Scenario: Register with duplicate email address
    Given I navigate to register page
    When I enter existing account email into the email field
    And I select privacy policy option
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  @register
  Scenario: Register without providing any fields
    Given I navigate to register page
    When I dont enter anything into the fields
    And I click on continue button
    Then Proper warning message for every mandatory fields should be displayed