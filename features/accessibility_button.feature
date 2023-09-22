Feature: Accessibility button functionality on the website https://edu.ro/.

  Scenario: Check that the user can increase or decrease the text size
    Given I am on the home page
    When I click on the 'Accessibility' button
    And I click on the '+' button 16 times
    Then It should be visible that the text in the page increases its size
    When I click on the '=' button
    Then It should be visible that the text from the page returns to its original state
    When I click on the '-' button 8 times
    Then It should be visible that the text in the page decreases its size

  Scenario: Check that the user can change the contrast of the text
    Given I am on the home page
    When I click on the 'Accessibility' button
    And I click on the 'Ridicat' button
    Then It should be visible that the contrast of the text on the page ensures easy and clear reading
    When I click on the 'Normal' button
    Then It should be visible that the text from the page returns to its original state

  Scenario: Check that the user can change the page style
    Given I am on the home page
    When I click on the 'Accessibility' button
    And I click on the 'Page Style' button
    And I click on the 'Black/White' button
    Then It should be visible that the text on the page changes color in black and the background of the text in white
    When  I click on the 'Page Style' button
    And I click on the 'White/Black' button
    Then It should be visible that the text on the page changes color in white and the background of the text in black
    When  I click on the 'Page Style' button
    And I click on the 'Yellow/Blue' button
    Then It should be visible that the text on the page changes color in yellow and the background of the text in blue
    When  I click on the 'Page Style' button
    And I click on the 'Standard' button
    Then It should be visible that the text from the page returns to its original state