Feature: Header functionality on the website https://edu.ro/.

  Background:
    Given I am on the home page

  Scenario: Check if user is redirected to home page by 'logo'
    When I click on the 'Logo' image
    Then It should be redirected to the home page

  Scenario: Check that the user can click on the header buttons and functioning correctly
    When I hold the mouse over the 'Minister' button
    Then It should be visible the text 'Date de contact'
    When I hold the mouse over the 'Invatamant preuniversitar' button
    Then It should be visible the text 'Invatamant primar'
    When I hold the mouse over the 'Invatamant superior' button
    Then It should be visible the text 'Studii universitare de licenta'
    When I hold the mouse over the 'Romania educata' button
    Then It should be visible the text 'Memorandum implementare'
    When I hold the mouse over the 'Cooperare internationala' button
    Then It should be visible the text 'Studiaza in Romania'