Feature: The language selector on the website https://edu.ro/.

  Scenario: Check that the user can choose another language in the language selector
    Given I am on the home page
    When I click on the 'language selector' button
    And I click on the 'English' button
    Then It should be visible the 'Engleza' button in Google Translate bar