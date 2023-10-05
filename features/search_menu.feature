Feature: The search menu on the website https://edu.ro/.

  Background:
    Given I am on the home page

  Scenario: Check that the user can search keywords in the search menu
    When I enter the text 'Studii universitare de master' in the search menu
    And I press the 'ENTER' button on the keyboard
    Then It should be visible and the first result should be identical to text 'Studii universitare de master'
    When I replaces in the search bar 'Studii universitare de master' with the text 'Bacalaurea'
    And I press the 'Cautare' button
    Then It should be visible and the first result should be identical to text 'Bacalaureat'

  Scenario: Check that user can search using special characters from the valid class
    When  I enter the text '   '(3 blank spaces) in the search menu
    And I press the 'ENTER' button on the keyboard
    Then It should be visible the message 'Cautare'
    When I enter the text '   '(3 blank spaces) in the search bar
    And I press the 'Cautare' button
    Then It should be visible the error message 'Va rugam sa introduceti cateva cuvinte cheie.'

  Scenario Outline: Check that user can search using multiple combinations of special characters from the invalid class
    Given I am on the search page
    When I enter '<special_caracters>' in the search bar
    And I press the 'Cautare' button
    Then It should be visible the error message 'You must include at least one positive keyword with 3 characters or more.'
    Examples:
      | special_caracters |
      | ---               |
      | +++               |
      | ***               |
      | ___               |
      | ...               |