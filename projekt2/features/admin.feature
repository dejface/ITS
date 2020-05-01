Feature: Admin section

    Scenario: Log into admin
        Given user is on admin page
        And is not logged in
        When user enters correct login 
        And logs in
        Then user is logged as admin in admin section

    Scenario: Display products
        Given User is logged as admin
        When user clicks "Catalog"
        And user clicks "Products" 
        Then all products will show up

    Scenario: Display categories
        Given User is logged as admin
        When user clicks "Catalog"
        And user clicks "Categories" 
        Then all categories will show up

    Scenario: Log out
        Given User is logged as admin
        When user clicks "Logout"
        Then user is logged out