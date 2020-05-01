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
        And is on any page of eshop
        When user clicks "MyAccount"
        And clicks "Order history"
        Then history of order is shown

    Scenario: User logs out
        Given User is on any page of eshop
        And is logged in
        When User logs out
        Then user is logged out

    Scenario: Successful password change
        Given User is on MyAccount page
        And is logged in
        When user navigates to Change password page
        And fills new password
        And passwords are same
        And clicks "continue"
        Then password is changed

    Scenario: Unsuccessful password change
        Given User is on MyAccount page
        And is logged in
        When user navigates to Change password page
        And fills new password
        And passwords are not same
        And clicks "continue"
        Then password is not changed

    
