Feature: cart

    Scenario: Product is added to non-empty cart
        Given User is on exact page
        And Cart has at least one item
        When User adds item to cart
        Then Cart contains one more item

    Scenario: Product is added to empty cart
        Given User is on exact page
        And Cart is empty
        When User adds item to cart
        Then Cart contains one more item

    Scenario: Show items in cart
        Given User is on exact page
        When User clicks on "Shopping cart"
        Then Items in cart are displayed

    Scenario: Continue shopping from cart
        Given User is in cart
        When User clicks "Continue shopping"
        Then Main page is loaded