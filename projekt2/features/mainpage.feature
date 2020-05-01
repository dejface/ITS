Feature: Overall page functionality

    Scenario: Currency change
        Given User is on any eshop page
        And User clicks on "Currency" option
        When new currency is selected
        Then currency on page was changed

    Scenario: Webpage loading
        Given User has opened internet browser
        And user has internet connection
        When user searches for eshop page
        Then page correctly loads

    Scenario: Newsletter subscription
        Given user is on any eshop page
        And user is logged in
        When user clicks on "Newsletter"
        And user clicks "Continue"
        Then user has newsletter subscription

    Scenario: Wish list
        Given user is on any eshop page
        And user is logged in
        When clicks on "Wish list"
        Then user wish list is shown