Feature: The search menu on the website https://edu.ro/.

  Scenario: Check that the user can search keywords in the search menu
    Given I am on the home page
    When I enter the text 'Studii universitare de master' in the search menu
    And I press the 'ENTER' button on the keyboard
    Then It should be visible and the first result should be identical to text 'Studii universitare de master'
    When I replaces in the search bar 'Studii universitare de master' with the text 'Învățământ primar'
    And I press the 'Căutare' button
    Then It should be visible and the first result should be identical to text 'Învățământ primar'

  Scenario: Check that user can search using special characters from the valid class
    Given I am on the home page
    When  I enter the text '   '(3 blank spaces) in the search menu
    And I press the 'ENTER' button on the keyboard
    Then It should be visible the message 'Căutare'
    When I enter the text '   '(3 blank spaces) in the search bar
    And I press the 'Căutare' button
    Then It should be visible the error message 'Vă rugăm să introduceți câteva cuvinte cheie.'

  Scenario: Check that user can search using special characters from the invalid class
    Given I am on the home page
    When  I enter the text '///' in the search menu
    And I press the 'ENTER' button on the keyboard
    Then It should be visible the message 'Căutare'
    When I enter the text '///' in the search bar
    And I press the 'Căutare' button
    Then It should be visible the error message 'Vă rugăm să introduceți câteva cuvinte cheie.'