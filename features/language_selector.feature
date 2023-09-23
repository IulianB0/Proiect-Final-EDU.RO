Feature: The language selector on the website https://edu.ro/.

  Scenario: Check that the user can choose another language in the language selector
    Given I am on the home page
    When I click on the 'language selector' button
    And I click on the 'English' button
    Then It should be visible the 'Engleză' button in Google Translate bar
    When I click on the 'Engleză' button from the Google Translate bar
    And I click on the 'Bulgară' button from the Google Translate bar
    Then It should be visible the 'Bulgară' button in Google Translate bar
    When I click on the 'close' button from the Google Translate bar
    Then It should be visible that the text returns to the Romanian language

