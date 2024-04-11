- User

  - Email
  - Username
  - FirstName
  - LastName
  - Phone
  - Address
    - Street
    - City
    - Zip
    - Country

- Bank

  - UserId
  - Institution
  - RoutingNumber
  - AccountNumber

- Account

  - UserId
  - FundId
  - Value
  - Total Return
  - Transactions

- Transactions

  - UserId
  - FundId
  - AccountId
  - Value
  - Type(debit/credit)
  - Status(processing,rejected,cancelled,completed)

- Fund

  - Description
  - Team
  - Manager
  - Value
  - Trades
  - NAV
  - Total Return
  - Yield
  - NumIssuedShares
  - Assets

    - Meta, 1,000
    - GOOG, 1,000
    - HOOD, 1,000
    - TSLA, 1,000

  - Historic Returns
  - Historic Yields

- Trades

  - FundId
  - Sym
  - Price
  - Data

- NAV

  - FundId
  - Date
  - Open
  - Close
  - High
  - Low
  - Assets
    - [
      {
      sym: 0,
      shares: 0,
      shares: 0,
      },
      ]
