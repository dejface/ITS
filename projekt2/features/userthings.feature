Feature: User things

    Scenario: User makes registration
        Given User is on registration page
        And is not logged in
        When user fills all of needed information
        And accepts privacy policy
        And clicks "Continue"
        Then registration is successful

    Scenario: User fails to make registration because of empty field
        Given User is on registration page
        And is not logged in
        When user doesn't fill all of needed information
        And accepts privacy policy
        And clicks "Continue"
        Then registration is not successful

    Scenario: User fails to make registration because of policy accept
        Given User is on registration page
        And is not logged in
        When user fills all of needed information
        And doesn't accept privacy policy
        And clicks "Continue"
        Then registration is not successful

    Scenario: User logs into his account
        Given User is on login page
        And enters his e-mail address
        And enters correct password
        When user clicks "Login"
        Then user is logged in

    Scenario: View order history
        Given User is logged in 
        And user is on any eshop page
        When user clicks "MyAccount"
        And clicks "Order history"
        Then history of order is shown
