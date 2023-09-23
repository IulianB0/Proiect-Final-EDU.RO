Feature: Footer functionality on the website https://edu.ro/.

  Scenario: Check that the user can click on the footer buttons and functioning correctly
    Given I am on the home page
    When I click on the 'Organigramă' button
    Then It should redirect in the same browser with the link address 'https://www.edu.ro/organigrama'
    Given I am on the home page
    When I click on the 'Ordine de ministru' button
    Then It should redirect in the same browser with the link address 'https://www.edu.ro/legislațe-ordine-de-ministru'
    Given I am on the home page
    When I click on the 'Instagram' button
    Then It should redirect to a new browser with the link address 'https://www.instagram.com/edu.gov.ro/'
    Given I am on the home page
    When I click on the 'Facebook' button
    Then It should redirect to a new browser with the link address 'https://www.facebook.com/www.edu.ro/'