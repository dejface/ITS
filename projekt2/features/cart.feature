Feature: cart
    Scenario: Product is added to empty cart
        Given User is on exact product page
        And Cart is empty
        When User adds item to cart
        Then Cart contains one more item

    Scenario: Continue shopping from empty cart
        Given User is on cart page
        And Cart is empty
        When User clicks "Continue"
        Then Main page is loaded