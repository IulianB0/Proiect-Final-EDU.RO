Feature: Header functionality on the website https://edu.ro/.

  Scenario: Check if user is redirected to home page by 'logo'
    Given I am on the contact page
    When I click on the 'Logo' image
    Then It should be redirected to the home page

  Scenario: Check that the user can click on the header buttons and functioning correctly
    Given I am on the home page
    When I hold the mouse over the 'Minister' button
    Then It should be visible the text 'Date de contact'
    When I hold the mouse over the 'Învăţământ preuniversitar' button
    Then It should be visible the text 'Învățământ primar'
    When I hold the mouse over the 'Învățământ superior' button
    Then It should be visible the text 'Studii universitare de licență'
    When I hold the mouse over the 'România educată' button
    Then It should be visible the text 'Memorandum implementare'
    When I hold the mouse over the 'Cooperare internațională' button
    Then It should be visible the text 'Studiază în România'