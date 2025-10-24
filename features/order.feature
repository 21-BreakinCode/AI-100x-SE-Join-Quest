@order_pricing
Feature: E-commerce Order Pricing Promotions
  As a shopper
  I want the system to calculate my order total with applicable promotions
  So that I can understand how much to pay and what items I will receive

  Scenario: Single product without promotions
    Given no promotions are applied
    When a customer places an order with:
      | productName | quantity | unitPrice |
      | T-shirt     | 1        | 500       |
    Then the order summary should be:
      | totalAmount |
      | 500         |
    And the customer should receive:
      | productName | quantity |
      | T-shirt     | 1        |

  Scenario: Threshold discount applies when subtotal reaches 1000
    Given the threshold discount promotion is configured:
      | threshold | discount |
      | 1000      | 100      |
    When a customer places an order with:
      | productName | quantity | unitPrice |
      | T-shirt     | 2        | 500       |
      | 褲子          | 1        | 600       |
    Then the order summary should be:
      | originalAmount | discount | totalAmount |
      | 1600           | 100      | 1500        |
    And the customer should receive:
      | productName | quantity |
      | T-shirt     | 2        |
      | 褲子          | 1        |

  Scenario: Buy-one-get-one for cosmetics - multiple products
    Given the buy one get one promotion for cosmetics is active
    When a customer places an order with:
      | productName | category  | quantity | unitPrice |
      | 口紅          | cosmetics | 1        | 300       |
      | 粉底液         | cosmetics | 1        | 400       |
    Then the order summary should be:
      | totalAmount |
      | 700         |
    And the customer should receive:
      | productName | quantity |
      | 口紅          | 2        |
      | 粉底液         | 2        |

  Scenario: Buy-one-get-one for cosmetics - same product twice
    Given the buy one get one promotion for cosmetics is active
    When a customer places an order with:
      | productName | category  | quantity | unitPrice |
      | 口紅          | cosmetics | 2        | 300       |
    Then the order summary should be:
      | totalAmount |
      | 600         |
    And the customer should receive:
      | productName | quantity |
      | 口紅          | 3        |

  Scenario: Buy-one-get-one for cosmetics - mixed categories
    Given the buy one get one promotion for cosmetics is active
    When a customer places an order with:
      | productName | category  | quantity | unitPrice |
      | 襪子          | apparel   | 1        | 100       |
      | 口紅          | cosmetics | 1        | 300       |
    Then the order summary should be:
      | totalAmount |
      | 400         |
    And the customer should receive:
      | productName | quantity |
      | 襪子          | 1        |
      | 口紅          | 2        |

  Scenario: Multiple promotions stacked
    Given the threshold discount promotion is configured:
      | threshold | discount |
      | 1000      | 100      |
    And the buy one get one promotion for cosmetics is active
    When a customer places an order with:
      | productName | category  | quantity | unitPrice |
      | T-shirt     | apparel   | 3        | 500       |
      | 口紅          | cosmetics | 1        | 300       |
    Then the order summary should be:
      | originalAmount | discount | totalAmount |
      | 1800           | 100      | 1700        |
    And the customer should receive:
      | productName | quantity |
      | T-shirt     | 3        |
      | 口紅          | 2        |

  Scenario: Double Eleven promotion - 12 items of same product gets bulk discount
    Given the Double Eleven promotion is active
    When a customer places an order with:
      | productName | quantity | unitPrice |
      | 襪子          | 12       | 100       |
    Then the order summary should be:
      | totalAmount |
      | 1000        |
    And the customer should receive:
      | productName | quantity |
      | 襪子          | 12       |

  Scenario: Double Eleven promotion - 27 items gets multiple bulk discounts
    Given the Double Eleven promotion is active
    When a customer places an order with:
      | productName | quantity | unitPrice |
      | 襪子          | 27       | 100       |
    Then the order summary should be:
      | totalAmount |
      | 2300        |
    And the customer should receive:
      | productName | quantity |
      | 襪子          | 27       |

  Scenario: Double Eleven promotion - 10 different products get no bulk discount
    Given the Double Eleven promotion is active
    When a customer places an order with:
      | productName | quantity | unitPrice |
      | Product-A   | 1        | 100       |
      | Product-B   | 1        | 100       |
      | Product-C   | 1        | 100       |
      | Product-D   | 1        | 100       |
      | Product-E   | 1        | 100       |
      | Product-F   | 1        | 100       |
      | Product-G   | 1        | 100       |
      | Product-H   | 1        | 100       |
      | Product-I   | 1        | 100       |
      | Product-J   | 1        | 100       |
    Then the order summary should be:
      | totalAmount |
      | 1000        |
    And the customer should receive:
      | productName | quantity |
      | Product-A   | 1        |
      | Product-B   | 1        |
      | Product-C   | 1        |
      | Product-D   | 1        |
      | Product-E   | 1        |
      | Product-F   | 1        |
      | Product-G   | 1        |
      | Product-H   | 1        |
      | Product-I   | 1        |
      | Product-J   | 1        |
