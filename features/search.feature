Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to the home page
    When I enter valid product in search box field
    And I click on search button
    Then Valid product gets displayed in the search results
  @search
  Scenario: Search for a invalid product
    Given I got navigated to the home page
    When I enter invalid product in search box field
    And I click on search button
    Then Proper error message displayed in the search results

  @search
  Scenario: Search without entering any product
    Given I got navigated to the home page
    When I dont enter anything in search box field
    And I click on search button
    Then Proper error message displayed in the search results