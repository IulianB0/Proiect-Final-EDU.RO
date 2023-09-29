Feature: Footer functionality on the website https://edu.ro/.

  Scenario: Check that the user can click on the footer buttons and functioning correctly
    Given I am on the home page
    When I click on the 'Organigrama' button
    Then It should redirect in the same browser with the link address 'https://edu.ro/organigrama'
    Given I am on the home page
    When I click on the 'Harta site-ului' button
    Then It should redirect in the same browser with the link address 'https://edu.ro/sitemap'
    Given I am on the home page
    When I click on the 'Proiecte acte normative' button
    Then It should redirect in the same browser with the link address 'https://edu.ro/proiecte-acte-normative'
    Given I am on the home page
    When I click on the 'Ordine de ministru' button
    Then It should redirect to a new browser with the link address 'https://edu.ro/legislate-ordine-de-ministru'
