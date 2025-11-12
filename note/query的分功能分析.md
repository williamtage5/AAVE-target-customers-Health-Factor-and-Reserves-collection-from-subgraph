这份源码文件（`explorer_query的源码.md`）是 GraphQL 资源管理器（GraphiQL Explorer）界面的 HTML 片段。它展示了一个 Aave 子图（subgraph）的 GraphQL API 的所有**根查询字段 (Root Query Fields)**。

这意味着，您可以使用这些字段作为查询的起点，来获取 Aave 平台上的各种数据。这些字段几乎都提供了单数和复数两种形式：
* **单数形式**（例如 `pool`）：通常用于通过唯一 ID（如合约地址）精确查询单个实体。
* **复数形式**（例如 `pools`）：用于查询实体的列表，通常支持分页（`first`, `skip`）、排序（`orderBy`）和过滤（`where`）等参数。

以下是基于该源码的提纲式分析，说明了您可以查询的数据类别：

---

### Aave GraphQL API 可查询数据提纲

**1. 核心实体数据 (Protocol, Pool, Reserve)**
* **协议 (Protocol)**：查询整个 Aave 协议的顶层数据。
    * `protocol`, `protocols`
* **资金池 (Pool)**：查询特定的Aave市场（池）。
    * `pool`, `pools`
* **储备 (Reserve)**：查询池中特定资产（如 DAI, ETH）的储备状态、利率、配置等。
    * `reserve`, `reserves`

**2. 用户数据 (User Data)**
* **用户 (User)**：查询特定的用户账户。
    * `user`, `users`
* **用户储备仓位 (UserReserve)**：查询用户在特定资产上的详细仓位信息（如存款、借款、是否用作抵押品）。
    * `userReserve`, `userReserves`
* **用户交易 (UserTransaction)**：查询用户的交易历史。
    * `userTransaction`, `userTransactions`
* **用户奖励 (UserReward)**：查询用户的奖励信息。
    * `userReward`, `userRewards`
* **用户 E-Mode (UserEModeSet)**：查询用户设置 E-Mode（高效率模式）的事件。
    * `userEModeSet`, `userEModeSets`

**3. 交易与事件数据 (Transactions & Events)**
* **存款 (Supply)**：查询存款事件。
    * `supply`, `supplies`
* **取款 (RedeemUnderlying)**：查询取款事件。
    * `redeemUnderlying`, `redeemUnderlyings`
* **借款 (Borrow)**：查询借款事件。
    * `borrow`, `borrows`
* **还款 (Repay)**：查询还款事件。
    * `repay`, `repays`
* **清算 (LiquidationCall)**：查询清算事件。
    * `liquidationCall`, `liquidationCalls`
* **闪电贷 (FlashLoan)**：查询闪电贷事件。
    * `flashLoan`, `flashLoans`
* **利率交换 (SwapBorrowRate)**：查询用户切换借款利率模式（稳定/可变）的事件。
    * `swapBorrowRate`, `swapBorrowRates`
* **稳定利率调整 (RebalanceStableBorrowRate)**：查询稳定利率重新平衡的事件。
    * `rebalanceStableBorrowRate`, `rebalanceStableBorrowRates`
* **抵押品设置 (UsageAsCollateral)**：查询用户切换资产是否用作抵押品的事件。
    * `usageAsCollateral`, `usageAsCollaterals`

**4. 价格与预言机数据 (Price & Oracles)**
* **价格预言机 (PriceOracle)**：查询Aave使用的价格预言机。
    * `priceOracle`, `priceOracles`
* **预言机资产 (PriceOracleAsset)**：查询预言机跟踪的特定资产。
    * `priceOracleAsset`, `priceOracleAssets`
* **Chainlink 聚合器 (ChainlinkAggregator)**：查询 Chainlink 价格源。
    * `chainlinkAggregator`, `chainlinkAggregators`

**5. 历史数据 (Historical Data)**
* **价格历史 (PriceHistory)**：查询资产的价格历史记录。
    * `priceHistoryItem`, `priceHistoryItems`
    * `usdEthPriceHistoryItem`, `usdEthPriceHistoryItems`
* **储备参数历史 (ReserveParamsHistory)**：查询储备金配置参数（如LTV、清算门槛）的变更历史。
    * `reserveParamsHistoryItem`, `reserveParamsHistoryItems`
    * `reserveConfigurationHistoryItem`, `reserveConfigurationHistoryItems`
* **代币余额历史 (TokenBalanceHistory)**：查询 aToken, sToken, vToken 的余额历史。
    * `atokenBalanceHistoryItem`, `atokenBalanceHistoryItems`
    * `stokenBalanceHistoryItem`, `stokenBalanceHistoryItems`
    * `vtokenBalanceHistoryItem`, `vtokenBalanceHistoryItems`
* **交换历史 (SwapHistory)**：查询资产交换历史。
    * `swapHistory`, `swapHistories`

**6. 配置与映射 (Configuration & Mappings)**
* **E-Mode 类别 (EModeCategory)**：查询 E-Mode（高效率模式）的类别配置。
    * `emodeCategory`, `emodeCategories`
    * `emodeCategoryConfig`, `emodeCategoryConfigs`
* **隔离模式 (IsolationMode)**：查询隔离模式的债务更新。
    * `isolationModeTotalDebtUpdated`, `isolationModeTotalDebtUpdateds`
* **合约映射 (Mappings)**：查询合约地址到资金池的映射。
    * `contractToPoolMapping`, `contractToPoolMappings`
    * `mapAssetPool`, `mapAssetPools`

**7. 奖励与推荐人 (Rewards & Referrers)**
* **奖励 (Reward)**：查询奖励代币的信息。
    * `reward`, `rewards`
* **奖励控制器 (RewardsController)**：查询奖励分发合约。
    * `rewardsController`, `rewardsControllers`
* **奖励预言机 (RewardFeedOracle)**：查询奖励的价格源。
    * `rewardFeedOracle`, `rewardFeedOracles`
* **推荐人 (Referrer)**：查询推荐人数据。
    * `referrer`, `referrers`

**8. GHO & V3 特定功能 (GHO & V3 Specifics)**
* **GHO (MintUnbacked / BackUnbacked)**：查询 GHO（Aave 的稳定币）的铸造和销毁事件。
    * `mintUnbacked`, `mintUnbackeds`
    * `backUnbacked`, `backUnbackeds`
* **铸币到金库 (MintedToTreasury)**：查询铸造到金库的代币。
    * `mintedToTreasury`, `mintedToTreasuries`
* **授权 (DelegatedAllowance)**：查询稳定和可变债务代币的授权。
    * `stableTokenDelegatedAllowance`, `stableTokenDelegatedAllowances`
    * `variableTokenDelegatedAllowance`, `variableTokenDelegatedAllowances`

**9. 子图元数据 (Subgraph Metadata)**
* **元数据 (\_meta)**：查询子图本身的元数据，例如它同步到的最新区块号。
    * `_meta`

# 第一部分：核心实体数据 (Protocol, Pool, Reserve)

好的，我来为您详细分析 **“1. 核心实体数据 (Protocol, Pool, Reserve)”** 这一部分。

首先，需要明确一点：您提供的源码截图（`explorer_query的源码.md`）是 Aave V3 官方子图（Subgraph）的查询字段。这个子图采用了 Messari 的**标准化借贷协议schema（schema）**。

在这个标准 schema 中，您提到的 `Protocol`、`Pool` 和 `Reserve` 在 schema 中有对应的实体名称：

  * **`Protocol`** 对应的是 **`LendingProtocol`** 实体。
  * **`Pool`** 对应的是 **`Market`** 实体（一个资金池/市场）。
  * **`Reserve`** 的概念被**包含在 `Market` 实体**中。一个 `Market` 实体就是指**单一资产的储备池**（例如 "USDC 市场"），它包含了该储备池的所有财务参数和状态。

因此，您查询 `pools` 字段，实际是在查询 `Market` 实体的列表。查询 `reserves` 字段也是在查询 `Market` 实体。以下是这些实体可查询的详细属性及其具体意义。

-----

### 1\. `Protocol` (即 `LendingProtocol` 实体)

这是描述整个 Aave 协议的顶层实体。查询 `protocol` 或 `protocols` 会返回以下类型的全局数据：

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 协议的唯一标识符（通常是协议的主合约地址）。 |
| `name` | `String` | 协议的名称，例如 "Aave V3"。 |
| `slug` | `String` | 协议的 URL 友好名称，例如 "aave-v3"。 |
| `network` | `String` | 该协议部署所在的区块链网络（例如 `MAINNET`, `ARBITRUM`）。 |
| `schemaVersion` | `String` | 正在使用的 Messari schema 版本号。 |
| `subgraphVersion` | `String` | 这个子图（subgraph）的版本号。 |
| `totalValueLockedUSD` | `BigDecimal` | **协议总锁仓量 (TVL)**：协议中所有市场（Reserves）存款总价值的美元计价。 |
| `totalDepositBalanceUSD` | `BigDecimal` | **协议总存款余额**：所有用户存入协议的总资产的美元价值。 |
| `totalBorrowBalanceUSD` | `BigDecimal` | **协议总借款余额**：所有用户从协议借出的总资产的美元价值。 |
| `cumulativeDepositUSD` | `BigDecimal` | **累计存款总额**：自协议创建以来所有存款事件的累计美元价值。 |
| `cumulativeBorrowUSD` | `BigDecimal` | **累计借款总额**：自协议创建以来所有借款事件的累计美元价值。 |
| `cumulativeLiquidateUSD` | `BigDecimal` | **累计清算总额**：自协议创建以来所有清算事件的累计美元价值。 |
| `marketCount` | `Int` | 协议中的市场（Reserves）总数。 |
| `markets` | `[Market!]` | 一个数组，**关联到该协议下的所有 `Market`（资金池）实体**。这是进行嵌套查询的关键。 |
| `_baseCurrency` | `String` | 协议用于内部计算的基准货币（例如 `USD`）。 |
| `_baseCurrencyPriceInUSD` | `BigDecimal` | 基准货币相对于 USD 的价格（如果是USD，则为 1）。 |

-----

### 2\. `Pool` (即 `Market` 实体)

这是您分析的核心，代表一个**特定资产的借贷市场/资金池**（例如 Aave 的 "USDC 市场" 或 "WETH 市场"）。您查询 `pools` 或 `reserves` 字段时，返回的就是这个实体的列表。

#### 关键识别属性

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 市场的唯一标识符（通常是该资产的**底层代币合约地址**）。 |
| `name` | `String` | 市场的名称（例如 "Aave V3 Ethereum WETH"）。 |
| `protocol` | `LendingProtocol!` | **关联到顶层的 `LendingProtocol` 实体**。 |
| `inputToken` | `Token!` | **该市场的底层资产**（例如 USDC 代币）。这是一个**关联到 `Token` 实体的链接**，您可以进一步查询 `inputToken { id name symbol decimals }`。 |

#### 财务状态属性

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `totalValueLockedUSD` | `BigDecimal` | **市场 TVL (美元)**：当前市场中（存款）的总资产价值。 |
| `totalDepositBalanceUSD` | `BigDecimal` | **市场总存款 (美元)**：当前市场中所有用户存款的总价值。 |
| `totalBorrowBalanceUSD` | `BigDecimal` | **市场总借款 (美元)**：当前市场中所有用户借款的总价值。 |
| `availableLiquidity` | `BigInt` | **可用流动性（原生单位）**：当前可供借出的资产数量，以原生代币单位表示（例如 2000000000000000000000 WETH）。**这是一个快照值**。 |
| `availableLiquidityUSD` | `BigDecimal` | **可用流动性（美元）**：`availableLiquidity` 的美元价值。 |
| `cumulativeDepositUSD` | `BigDecimal` | **累计存款 (美元)**：此市场历史累计存款的美元价值。 |
| `cumulativeBorrowUSD` | `BigDecimal` | **累计借款 (美元)**：此市场历史累计借款的美元价值。 |
| `cumulativeLiquidateUSD` | `BigDecimal` | **累计清算 (美元)**：在此市场中作为抵押品被清算的累计美元价值。 |

#### 风险与配置参数

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `maximumLTV` | `BigDecimal` | **最大贷款价值比 (LTV)**：抵押该资产可借出的最大价值比例（例如 0.75 表示 75%）。 |
| `liquidationThreshold` | `BigDecimal` | **清算门槛**：抵押品价值与债务价值的比率，低于此值将触发清算（例如 0.80 表示 80%）。 |
| `liquidationPenalty` | `BigDecimal` | **清算罚金**：清算时，清算人购买抵押品所能享受的折扣（例如 0.05 表示 5%）。 |
| `isActive` | `Boolean` | 该市场当前是否活跃（可进行存款/借款）。 |
| `canBeBorrowed` | `Boolean` | 该资产是否可被借出。 |
| `canUseAsCollateral` | `Boolean` | 该资产是否可用作抵押品。 |
| `reserveFactor` | `BigDecimal` | **储备因子**：协议从存款利息中抽取并存入金库的比例（例如 0.1 表示 10%）。 |
| `eModeCategory` | `EModeCategory` | **关联的 E-Mode 类别**：如果该资产属于某个高效率模式 (E-Mode) 类别。 |

-----

### 3\. `Reserve` (利率及代币属性)

如前所述，`Reserve` 的核心数据**已包含在 `Market` 实体中**。此外，与该市场（Reserve）相关的**利率**和**代币**（aToken, debtToken）有专门的实体来存储。

#### A. 利率 (通过 `Market` 实体查询)

`Market` 实体通过 `rates` 字段关联到 `InterestRate` 实体。

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `rates` | `[InterestRate!]` | **一个利率数组**。通常包含两个元素：一个用于存款（LENDER），一个用于借款（BORROWER）。 |
| `rates { id rate side type }` | `[InterestRate!]` | 这是一个嵌套查询示例：<br>- `id`: 利率的唯一 ID。<br>- `side`: 利率的类型 (`LENDER` 或 `BORROWER`)。<br>- `type`: 利率模式 (`STABLE` 或 `VARIABLE`)。<br>- `rate`: **年利率 (APR)**。 |

**\!\! 重要提示：关于利率 (rate) 字段**
在 Aave 子图中，`rate` 字段存储的不是 0.05 (5%) 这样的百分比。它存储的是一个称为 **RAY** 的极大整数（$10^{27}$ 精度）。您需要通过特定公式将其转换为 APY。

#### B. 储备代币 (通过 `Market` 实体查询)

`Market` 实体还包含了与其关联的各种代币信息。

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `inputToken` | `Token!` | **底层资产代币**（例如 `USDC`）。 |
| `outputToken` | `Token!` | **aToken (存款凭证代币)**（例如 `aUSDC`）。这是一个关联实体，您可以查询其 `id`, `name`, `symbol`。 |
| `variableDebtToken` | `Token!` | **可变利率债务代币**（例如 `variableDebtUSDC`）。 |
| `stableDebtToken` | `Token!` | **稳定利率债务代币**（例如 `stableDebtUSDC`）。 |

# 第二部分：用户数据 (User Data)

好的，我们来详细分析 **“2. 用户数据 (User Data)”** 这一部分。

这组实体（Entities）是 Aave 子图的核心，允许您跟踪单个用户（钱包地址）的完整活动，包括他们的头寸、历史记录和配置。

---

### 1. `User` 实体

* **查询字段**: `user` (通过ID) / `users` (列表查询)
* **实体描述**: 代表一个与 Aave 协议交互过的唯一用户账户（即一个以太坊钱包地址）。这是所有特定用户数据的顶层入口。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **用户的钱包地址**（例如 `0x...`）。这是该实体的主键。 |
| `reserves` | `[UserReserve!]` | **关联的用户仓位列表**。这是 `User` 实体**最重要**的属性之一。它是一个数组，链接到该用户在所有市场中的所有 `UserReserve`（仓位）实体。您可以通过这个字段进行嵌套查询，以获取用户的所有存款和借款。 |
| `borrowedReservesCount` | `Int` | **借款储备数量**。一个整数，表示该用户当前在多少个*不同*的市场中持有借款头寸。 |
| `eModeCategoryId` | `String` | **E-Mode 类别 ID**。如果用户处于 E-Mode（高效率模式），这里会显示该模式类别的 ID。您可以将此 ID 与 `EModeCategory` 实体相关联，以获取该模式的详细信息（例如 LTV、清算门槛）。 |
| `transactions` | `[UserTransaction!]` | **关联的交易列表**。一个数组，链接到该用户的所有 `UserTransaction`（交易历史）实体。 |
| `unclaimedRewards` | `BigDecimal` | **未领取的奖励（USD）**。该用户已累积但尚未领取的*所有*奖励的总美元价值。 |
| `healthFactor` | `BigDecimal` | **健康因子**。*（注意：这个字段可能不直接在 `User` 实体上，因为它需要实时计算。子图通常提供计算健康因子所需的所有静态数据，如 `UserReserve` 中的抵押品余额、债务余额以及 `Reserve` 中的清算门槛。）* |

---

### 2. `UserReserve` 实体

* **查询字段**: `userReserve` (通过ID) / `userReserves` (列表查询)
* **实体描述**: **这是最重要的用户数据实体**。它代表一个 `User` 在一个特定 `Reserve`（市场）中的**仓位**。例如，用户 A 在 USDC 市场上的存款和借款信息。如果一个用户向 USDC 存款并借入 ETH，他们将拥有*两个* `UserReserve` 实体（一个用于 USDC 仓位，一个用于 ETH 仓位）。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。通常是 `user.id` 和 `reserve.id` 的组合（例如 `0x...user-0x...reserve`）。 |
| `user` | `User!` | **关联的用户**。链接回拥有此仓位的 `User` 实体。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。链接到该仓位所在的 `Reserve` 实体。通过这个，您可以获取该市场的所有参数（如 `liquidationThreshold`, `LTV`, `reserveFactor` 等）。 |
| `usageAsCollateralEnabled` | `Boolean` | **是否用作抵押品**。一个布尔值（`true`/`false`），表示用户是否已将此资产（他们的存款）设置为抵押品。 |
| `currentATokenBalance` | `BigDecimal` | **当前 aToken 余额（含利息）**。用户当前持有的 aToken 数量，这个值会**随时间增长**，因为它代表了本金加上**已累积的存款利息**。这是查询用户存款余额的**关键字段**。 |
| `currentVariableDebt` | `BigDecimal` | **当前可变债务（含利息）**。用户的可变利率借款余额，**包含已累积的利息**。 |
| `currentStableDebt` | `BigDecimal` | **当前稳定债务（含利息）**。用户的稳定利率借款余额，**包含已累积的利息**。 |
| `currentTotalDebt` | `BigDecimal` | **当前总债务**。`currentVariableDebt + currentStableDebt` 的总和。 |
| `scaledATokenBalance` | `BigDecimal` | **标准化的 aToken 余额**。这是用户持有的 aToken 的“基础”数量。`currentATokenBalance` 是通过 `scaledATokenBalance * reserve.liquidityIndex` 计算得出的。 |
| `scaledVariableDebt` | `BigDecimal` | **标准化的可变债务**。计算当前可变债务的基础值。 |
| `stableBorrowRate` | `BigDecimal` | **稳定借款利率**。如果用户有稳定借款，这里显示他们锁定的年利率（APR）。 |
| `lastUpdateTimestamp` | `Int` | **最后更新时间戳**。该仓位最后一次被交互（如存款、取款、借款、还款）的区块时间戳。 |

---

### 3. `UserTransaction` 实体

* **查询字段**: `userTransaction` (通过ID) / `userTransactions` (列表查询)
* **实体描述**: 这是一个**事件**实体，记录了用户执行的每笔交易。这对于构建用户活动历史至关重要。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **交易哈希 (Tx Hash)**。例如 `0x...`。 |
| `type` | `String` | **交易类型**。一个枚举值（字符串），描述了交易的类别，例如：`DEPOSIT`, `BORROW`, `REPAY`, `WITHDRAW` (即 `RedeemUnderlying`), `LIQUIDATION_CALL`, `SWAP_BORROW_RATE`。 |
| `user` | `User!` | **关联的用户**。发起此交易的 `User` 实体。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。此交易交互的资产市场。 |
| `amount` | `BigDecimal` | **交易金额**。所涉资产的原生单位数量。 |
| `timestamp` | `Int` | **交易时间戳**。交易发生的区块时间戳。 |
| `liquidator` | `User` | **清算人**。（*仅用于 `LIQUIDATION_CALL` 类型*）执行清算的用户的地址。 |
| `collateralReserve` | `Reserve` | **抵押品储备**。（*仅用于 `LIQUIDATION_CALL` 类型*）被清算的抵押品所在的市场。 |
| `collateralAmount` | `BigDecimal` | **抵押品金额**。（*仅用于 `LIQUIDATION_CALL` 类型*）被清算的抵押品数量。 |
| `principalReserve` | `Reserve` | **债务储备**。（*仅用于 `LIQUIDATION_CALL` 类型*）被偿还的债务资产的市场。 |
| `principalAmount` | `BigDecimal` | **债务金额**。（*仅用于 `LIQUIDATION_CALL` 类型*）被偿还的债务数量。 |

---

### 4. `UserReward` 实体

* **查询字段**: `userReward` (通过ID) / `userRewards` (列表查询)
* **实体描述**: 用于跟踪用户在不同市场（通过存款或借款）累积的激励**奖励**（例如 $AAVE 或其他代币）。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。 |
| `user` | `User!` | **关联的用户**。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。产生该奖励的市场。 |
| `rewardToken` | `Token!` | **关联的奖励代币**。链接到 `Token` 实体，显示奖励代币的地址、符号（symbol）等。 |
| `unclaimedBalance` | `BigDecimal` | **未领取的余额**。用户已累积但尚未领取的该特定 `rewardToken` 的数量。 |

---

### 5. `UserEModeSet` 实体

* **查询字段**: `userEModeSet` (通过ID) / `userEModeSets` (列表查询)
* **实体描述**: 这是一个**事件**实体，在用户**设置或更改**其 E-Mode（高效率模式）时被创建。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **交易哈希 (Tx Hash)**。 |
| `user` | `User!` | **关联的用户**。 |
| `category` | `EModeCategory!` | **关联的 E-Mode 类别**。链接到用户*进入*的 `EModeCategory` 实体。 |
| `timestamp` | `Int` | **交易时间戳**。 |

# 第三部分：交易与事件数据 (Transactions & Events)

好的，我们来详细分析 **“3. 交易与事件数据 (Transactions & Events)”** 这一部分。

这组实体（Entities）是 Aave 子图的核心，允许您跟踪单个用户（钱包地址）的完整活动，包括他们的头寸、历史记录和配置。

---

### 1. `User` 实体

* **查询字段**: `user` (通过ID) / `users` (列表查询)
* **实体描述**: 代表一个与 Aave 协议交互过的唯一用户账户（即一个以太坊钱包地址）。这是所有特定用户数据的顶层入口。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **用户的钱包地址**（例如 `0x...`）。这是该实体的主键。 |
| `reserves` | `[UserReserve!]` | **关联的用户仓位列表**。这是 `User` 实体**最重要**的属性之一。它是一个数组，链接到该用户在所有市场中的所有 `UserReserve`（仓位）实体。您可以通过这个字段进行嵌套查询，以获取用户的所有存款和借款。 |
| `borrowedReservesCount` | `Int` | **借款储备数量**。一个整数，表示该用户当前在多少个*不同*的市场中持有借款头寸。 |
| `eModeCategoryId` | `String` | **E-Mode 类别 ID**。如果用户处于 E-Mode（高效率模式），这里会显示该模式类别的 ID。您可以将此 ID 与 `EModeCategory` 实体相关联，以获取该模式的详细信息（例如 LTV、清算门槛）。 |
| `transactions` | `[UserTransaction!]` | **关联的交易列表**。一个数组，链接到该用户的所有 `UserTransaction`（交易历史）实体。 |
| `unclaimedRewards` | `BigDecimal` | **未领取的奖励（USD）**。该用户已累积但尚未领取的*所有*奖励的总美元价值。 |
| `healthFactor` | `BigDecimal` | **健康因子**。*（注意：这个字段可能不直接在 `User` 实体上，因为它需要实时计算。子图通常提供计算健康因子所需的所有静态数据，如 `UserReserve` 中的抵押品余额、债务余额以及 `Reserve` 中的清算门槛。）* |

---

### 2. `UserReserve` 实体

* **查询字段**: `userReserve` (通过ID) / `userReserves` (列表查询)
* **实体描述**: **这是最重要的用户数据实体**。它代表一个 `User` 在一个特定 `Reserve`（市场）中的**仓位**。例如，用户 A 在 USDC 市场上的存款和借款信息。如果一个用户向 USDC 存款并借入 ETH，他们将拥有*两个* `UserReserve` 实体（一个用于 USDC 仓位，一个用于 ETH 仓位）。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。通常是 `user.id` 和 `reserve.id` 的组合（例如 `0x...user-0x...reserve`）。 |
| `user` | `User!` | **关联的用户**。链接回拥有此仓位的 `User` 实体。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。链接到该仓位所在的 `Reserve` 实体。通过这个，您可以获取该市场的所有参数（如 `liquidationThreshold`, `LTV`, `reserveFactor` 等）。 |
| `usageAsCollateralEnabled` | `Boolean` | **是否用作抵押品**。一个布尔值（`true`/`false`），表示用户是否已将此资产（他们的存款）设置为抵押品。 |
| `currentATokenBalance` | `BigDecimal` | **当前 aToken 余额（含利息）**。用户当前持有的 aToken 数量，这个值会**随时间增长**，因为它代表了本金加上**已累积的存款利息**。这是查询用户存款余额的**关键字段**。 |
| `currentVariableDebt` | `BigDecimal` | **当前可变债务（含利息）**。用户的可变利率借款余额，**包含已累积的利息**。 |
| `currentStableDebt` | `BigDecimal` | **当前稳定债务（含利息）**。用户的稳定利率借款余额，**包含已累积的利息**。 |
| `currentTotalDebt` | `BigDecimal` | **当前总债务**。`currentVariableDebt + currentStableDebt` 的总和。 |
| `scaledATokenBalance` | `BigDecimal` | **标准化的 aToken 余额**。这是用户持有的 aToken 的“基础”数量。`currentATokenBalance` 是通过 `scaledATokenBalance * reserve.liquidityIndex` 计算得出的。 |
| `scaledVariableDebt` | `BigDecimal` | **标准化的可变债务**。计算当前可变债务的基础值。 |
| `stableBorrowRate` | `BigDecimal` | **稳定借款利率**。如果用户有稳定借款，这里显示他们锁定的年利率（APR）。 |
| `lastUpdateTimestamp` | `Int` | **最后更新时间戳**。该仓位最后一次被交互（如存款、取款、借款、还款）的区块时间戳。 |

---

### 3. `UserTransaction` 实体

* **查询字段**: `userTransaction` (通过ID) / `userTransactions` (列表查询)
* **实体描述**: 这是一个**事件**实体，记录了用户执行的每笔交易。这对于构建用户活动历史至关重要。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **交易哈希 (Tx Hash)**。例如 `0x...`。 |
| `type` | `String` | **交易类型**。一个枚举值（字符串），描述了交易的类别，例如：`DEPOSIT`, `BORROW`, `REPAY`, `WITHDRAW` (即 `RedeemUnderlying`), `LIQUIDATION_CALL`, `SWAP_BORROW_RATE`。 |
| `user` | `User!` | **关联的用户**。发起此交易的 `User` 实体。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。此交易交互的资产市场。 |
| `amount` | `BigDecimal` | **交易金额**。所涉资产的原生单位数量。 |
| `timestamp` | `Int` | **交易时间戳**。交易发生的区块时间戳。 |
| `liquidator` | `User` | **清算人**。（*仅用于 `LIQUIDATION_CALL` 类型*）执行清算的用户的地址。 |
| `collateralReserve` | `Reserve` | **抵押品储备**。（*仅用于 `LIQUIDATION_CALL` 类型*）被清算的抵押品所在的市场。 |
| `collateralAmount` | `BigDecimal` | **抵押品金额**。（*仅用于 `LIQUIDATION_CALL` 类型*）被清算的抵押品数量。 |
| `principalReserve` | `Reserve` | **债务储备**。（*仅用于 `LIQUIDATION_CALL` 类型*）被偿还的债务资产的市场。 |
| `principalAmount` | `BigDecimal` | **债务金额**。（*仅用于 `LIQUIDATION_CALL` 类型*）被偿还的债务数量。 |

---

### 4. `UserReward` 实体

* **查询字段**: `userReward` (通过ID) / `userRewards` (列表查询)
* **实体描述**: 用于跟踪用户在不同市场（通过存款或借款）累积的激励**奖励**（例如 $AAVE 或其他代币）。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。 |
| `user` | `User!` | **关联的用户**。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。产生该奖励的市场。 |
| `rewardToken` | `Token!` | **关联的奖励代币**。链接到 `Token` 实体，显示奖励代币的地址、符号（symbol）等。 |
| `unclaimedBalance` | `BigDecimal` | **未领取的余额**。用户已累积但尚未领取的该特定 `rewardToken` 的数量。 |

---

### 5. `UserEModeSet` 实体

* **查询字段**: `userEModeSet` (通过ID) / `userEModeSets` (列表查询)
* **实体描述**: 这是一个**事件**实体，在用户**设置或更改**其 E-Mode（高效率模式）时被创建。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **交易哈希 (Tx Hash)**。 |
| `user` | `User!` | **关联的用户**。 |
| `category` | `EModeCategory!` | **关联的 E-Mode 类别**。链接到用户*进入*的 `EModeCategory` 实体。 |
| `timestamp` | `Int` | **交易时间戳**。 |

# 第四部分：价格与预言机数据 (Price & Oracles)

好的，这是对 **“4. 价格与预言机数据 (Price & Oracles)”** 部分的详细分析。

这组实体（Entities）是 Aave 协议的基石之一，用于跟踪所有资产的价格，这是进行借贷、计算抵押率和执行清算的前提。

---

### 1. `PriceOracle` 实体

* **查询字段**: `priceOracle` (通过ID) / `priceOracles` (列表查询)
* **实体描述**: 代表 Aave 协议所使用的**主价格预言机合约**。在 Aave V3 中，这通常是一个 `AaveOracle` 合约，它本身不产生价格，而是从 Chainlink 或其他来源聚合价格。这更像是一个“预言机管理器”。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **预言机合约地址**。这是 Aave 部署的 `AaveOracle` 或 `PriceOracle` 合约的地址。 |
| `proxyPriceProvider` | `Bytes` | **代理价格提供者地址**。Aave 预言机通常指向一个 Chainlink `PriceFeed` 注册表或类似的代理合约。 |
| `assets` | `[PriceOracleAsset!]` | **关联的资产列表**。一个数组，链接到所有由该预言机跟踪价格的 `PriceOracleAsset` 实体。 |
| `usdPriceEth` | `BigInt` | **ETH 的美元价格**。预言机报告的 ETH-USD 价格。这是一个非常重要的值，因为许多非美元资产的价格最初是**以 ETH 计价**的，子图会使用这个值将它们转换为 USD。 |
| `fallbackOracle` | `Bytes` | **备用预言机地址**。当主价格源（如 Chainlink）失效时，协议会使用的备用预言机合约地址。 |

---

### 2. `PriceOracleAsset` 实体

* **查询字段**: `priceOracleAsset` (通过ID) / `priceOracleAssets` (列表查询)
* **实体描述**: 代表一个**特定资产的价格信息**。每个由 Aave 预言机跟踪的资产（如 USDC, WETH, AAVE）都会有一个对应的 `PriceOracleAsset` 实体。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **资产的合约地址**。例如 USDC 的地址 `0x...`。 |
| `oracle` | `PriceOracle!` | **关联的预言机**。链接回管理此资产价格的 `PriceOracle` 实体。 |
| `asset` | `Token!` | **关联的代币**。链接到 `Token` 实体（在其他 schema 中可能是 `Reserve` 实体），以获取代币的符号、名称、小数位数等信息。 |
| `priceInEth` | `BigInt` | **以 ETH 计价的价格**。该资产 1 个单位价值多少 ETH。**这是子图中的核心价格字段**。 |
| `priceInUsd` | `BigDecimal` | **以 USD 计价的价格**。该资产 1 个单位价值多少美元。*（这个值通常由子图通过 `priceInEth * priceOracle.usdPriceEth` 计算得出）*。 |
| `priceSource` | `Bytes` | **价格源地址**。*（可能存在）* 获取此价格的**直接来源合约地址**，这通常是一个 `ChainlinkAggregator` 合约地址。 |
| `isFallbackOracle` | `Boolean` | **是否使用备用预言机**。一个布尔值 (`true`/`false`)，指示当前价格是否来自备用预言机（`PriceOracle.fallbackOracle`）而不是主价格源。 |
| `lastUpdateTimestamp` | `Int` | **最后更新时间戳**。价格最后一次在链上更新的区块时间戳。 |

---

### 3. `ChainlinkAggregator` 实体

* **查询字段**: `chainlinkAggregator` (通过ID) / `chainlinkAggregators` (列表查询)
* **实体描述**: 这是一个辅助实体，用于直接跟踪 Aave 所依赖的 **Chainlink 价格源合约**（也称为 Aggregator）。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **Chainlink Aggregator 合约地址**。这个地址通常与 `PriceOracleAsset` 中的 `priceSource` 字段相对应。 |
| `oracle` | `PriceOracle!` | **关联的预言机**。链接回使用此 Chainlink 源的 Aave `PriceOracle` 实体。 |
| `asset` | `Token!` | **关联的代币**。此价格源所代表的资产。 |
| `price` | `BigInt` | **最新价格（原始数据）**。Chainlink 合约报告的**原始**价格。这是一个没有处理过的大整数（`BigInt`）。 |
| `decimals` | `Int` | **小数位数**。`price` 字段所使用的小数位数。例如，USD 价格源通常是 8 位小数；ETH 价格源通常是 18 位小数。 |
| `timestamp` | `Int` | **最新价格的时间戳**。Chainlink 聚合器报告 `price` 的时间。 |

# 第五部分：历史数据 (Historical Data)

好的，这是对 **“5. 历史数据 (Historical Data)”** 部分的详细分析。

这组实体（Entities）非常重要，因为它们**不是**存储当前状态（Current State），而是作为**日志**或**快照**，记录了协议、市场或用户数据随时间发生的**每一次变更**。通过查询这些实体，您可以重建一个资产或一个用户的完整历史。

---

### 1. 价格历史 (PriceHistory)

这组实体用于跟踪**资产价格随时间的变化**。

#### A. `PriceHistoryItem` 实体
* **查询字段**: `priceHistoryItem` (通过ID) / `priceHistoryItems` (列表查询)
* **实体描述**: 这是一个通用的价格快照实体。**每当** Aave 预言机更新**任何**受支持资产的价格时，就会**创建一个** `PriceHistoryItem` 实体。这允许您为特定资产（如 USDC, WBTC）绘制详细的价格图表或查询其在任意时间点的历史价格。

##### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。通常是 `asset.id` 和 `timestamp` 的组合（例如 `0x...asset-1678886400`）。 |
| `asset` | `PriceOracleAsset!` | **关联的资产**。链接到 `PriceOracleAsset` 实体，以识别这是哪个资产的价格。 |
| `priceInEth` | `BigInt` | **以 ETH 计价的价格**。在该时间点，1 单位该资产价值多少 ETH（以 $10^{18}$ 精度表示）。 |
| `priceInUsd` | `BigDecimal` | **以 USD 计价的价格**。在该时间点，1 单位该资产价值多少美元。 |
| `timestamp` | `Int` | **时间戳**。该价格快照被记录的区块时间戳。 |

#### B. `UsdEthPriceHistoryItem` 实体
* **查询字段**: `usdEthPriceHistoryItem` (通过ID) / `usdEthPriceHistoryItems` (列表查询)
* **实体描述**: 这是一个**专门**的价格历史实体，**仅用于跟踪 ETH 对 USD 的价格**。它之所以被单独记录，是因为在 Aave 中，许多资产首先被定价为 `priceInEth`。子图需要使用这个 `UsdEthPriceHistoryItem` 列表，才能将其余所有资产的 `priceInEth` 历史值换算为 `priceInUsd` 历史值。

##### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。通常就是 `timestamp`。 |
| `price` | `BigInt` | **ETH 的美元价格**。在该时间点，1 ETH 价值多少美元（通常以 $10^{8}$ 或 $10^{18}$ 精度表示，取决于预言机）。 |
| `timestamp` | `Int` | **时间戳**。该价格快照被记录的区块时间戳。 |

---

### 2. 储备参数历史 (ReserveParamsHistory)

这组实体用于跟踪**市场（储备）配置参数的变更**。当 Aave 治理（Governance）投票通过一项提案，例如“将 USDC 的 LTV 提高到 80%”时，这些实体就会被创建。

#### A. `ReserveParamsHistoryItem` 实体
* **查询字段**: `reserveParamsHistoryItem` (通过ID) / `reserveParamsHistoryItems` (列表查询)
* **实体描述**: 专门记录**利率模型参数**的变更历史。Aave 的利率是根据资金利用率动态计算的，其计算模型（例如斜率、最优利用率点）可以被治理调整。此实体记录了这些调整。

##### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符，通常是 `reserve.id` 和 `timestamp` 的组合。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。链接到被修改的 `Reserve` 实体。 |
| `variableBorrowRate` | `BigInt` | **新的可变借款基础利率**（RAY, $10^{27}$ 精度）。 |
| `variableBorrowSlope1` | `BigInt` | **新的利率曲线斜率1**（RAY）。 |
| `variableBorrowSlope2` | `BigInt` | **新的利率曲线斜率2**（RAY）。 |
| `stableBorrowRate` | `BigInt` | **新的稳定借款利率**（RAY）。 |
| `...` | `...` | 其他与利率模型相关的参数（如最优利用率 `optimalUtilisationRate` 等）。 |
| `timestamp` | `Int` | **时间戳**。该变更生效的区块时间戳。 |

#### B. `ReserveConfigurationHistoryItem` 实体
* **查询字段**: `reserveConfigurationHistoryItem` (通过ID) / `reserveConfigurationHistoryItems` (列表查询)
* **实体描述**: 专门记录**风险配置参数**的变更历史。这与上面的利率模型不同，它跟踪的是 LTV、清算门槛、罚金等。

##### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符，通常是 `reserve.id` 和 `timestamp` 的组合。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。链接到被修改的 `Reserve` 实体。 |
| `ltv` | `BigDecimal` | **新的 LTV**（贷款价值比）。 |
| `liquidationThreshold` | `BigDecimal` | **新的清算门槛**。 |
| `liquidationBonus` | `BigDecimal` | **新的清算罚金（奖金）**。 |
| `reserveFactor` | `BigDecimal` | **新的储备因子**（协议收入比例）。 |
| `borrowingEnabled` | `Boolean` | **新的借款状态**（是否允许借款）。 |
| `stableBorrowRateEnabled` | `Boolean` | **新的稳定利率状态**（是否允许稳定利率借款）。 |
| `isActive` | `Boolean` | **新的活跃状态**。 |
| `isFrozen` | `Boolean` | **新的冻结状态**。 |
| `timestamp` | `Int` | **时间戳**。该变更生效的区块时间戳。 |

---

### 3. 代币余额历史 (TokenBalanceHistory)

这组实体用于跟踪**特定用户**的 aToken (存款)、sToken (稳定债务) 和 vToken (可变债务) **余额的每一次变化**。

#### `ATokenBalanceHistoryItem` / `STokenBalanceHistoryItem` / `VTokenBalanceHistoryItem` 实体
* **查询字段**: `atoken...`, `stoken...`, `vtoken...` (及复数形式)
* **实体描述**: 这三类实体结构几乎相同。**每当**一个用户的 aToken, sToken 或 vToken 余额**发生变动**时（例如，`Supply` 导致 aToken 增加，`Borrow` 导致 vToken 增加，`Repay` 导致 vToken 减少），就会创建一个相应的条目。
    * **aToken**: 存款凭证（利息在此累积）。
    * **sToken**: 稳定债务凭证。
    * **vToken**: 可变债务凭证。
* **注意**: 即使用
    户不主动操作，aToken 和 vToken 的**实际**余额（`balance`）也会因利息累积而*实时变化*。`scaledBalance` 字段则用于存储**未计利息**的“标准份额”。

##### 详细属性分析 (通用)
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。 |
| `userReserve` | `UserReserve!` | **关联的用户仓位**。链接到该余额所属的 `UserReserve` 实体。 |
| `scaledBalance` | `BigInt` | **新的标准余额**。未计入利息指数的“份额”余额。 |
| `balance` | `BigInt` | **新的当前余额**。已计入利息指数的余额 (`scaledBalance * index`)。 |
| `index` | `BigInt` | **当时的利息指数**。记录此次余额变动时，该代币（存款或债务）的利息累积指数。 |
| `timestamp` | `Int` | **时间戳**。余额变更的区块时间戳。 |

---

### 4. `SwapHistory` 实体

* **查询字段**: `swapHistory` (通过ID) / `swapHistories` (列表查询)
* **实体描述**: 记录 Aave V3 的**“互换 (Swap)”** 功能事件。这*不是*指 DEX 交易（如 Uniswap）。这指的是 Aave 协议内原生的**抵押品互换**或**债务互换**功能。
    * **抵押品互换**: 用户将已存入的抵押品（如 USDC）一键式地换成另一种资产（如 WETH），而无需先取款、再交易、再存款。
    * **债务互换**: 用户将现有的债务（如 借了 DAI）一键式地换成另一种债务（如 借了 USDC）。

##### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符，通常是**交易哈希 (Tx Hash)**。 |
| `user` | `User!` | **关联的用户**。执行此次互换的用户。 |
| `fromAsset` | `Reserve!` | **源资产**。被换*出*的资产所在的 `Reserve`。 |
| `toAsset` | `Reserve!` | **目标资产**。被换*入*的资产所在的 `Reserve`。 |
| `fromAmount` | `BigInt` | **源资产数量**。被换出的数量。 |
| `toAmount` | `BigInt` | **目标资产数量**。换入的数量。 |
| `isCollateralSwap` | `Boolean` | *（推测属性）* 用于区分是抵押品互换（`true`）还是债务互换（`false`）的标志。 |
| `timestamp` | `Int` | **时间戳**。互换发生的区块时间戳。 |


# 第六部分：配置与映射 (Configuration & Mappings)

好的，这是对 **“6. 配置与映射 (Configuration & Mappings)”** 部分的详细分析。

这组实体（Entities）主要用于定义 Aave V3 中的高级借贷模式（如 E-Mode 和隔离模式）的参数，并提供了关键的辅助工具，以便在不同的合约地址之间进行导航。

---

### 1. E-Mode 类别 (EModeCategory)

* **查询字段**: `emodeCategory` (通过ID) / `emodeCategories` (列表查询)
* **实体描述**: 代表 Aave V3 的“高效率模式”（E-Mode）的一个特定类别。E-Mode 允许用户在抵押和借入**同类别**资产时（例如，都
  是稳定币），享受极高的贷款价值比（LTV）和清算门槛，从而大幅提高资本效率。`EModeCategory` 实体存储了这些特定类别的参数。
* **`emodeCategoryConfig`**: 这个字段在功能上与 `emodeCategory` 高度重叠或可能是一个别名/旧称。在实际查询中，`EModeCategory` 是您需要查找的核心实体，它存储着 E-Mode 的当前配置状态。

#### `EModeCategory` 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **类别 ID**。一个数字（例如 `1`），唯一标识这个 E-Mode 类别（例如，ID `1` 通常代表“稳定币类别”）。 |
| `label` | `String` | **类别标签**。一个人类可读的名称，用于描述这个类别（例如 "Stablecoin E-Mode"）。 |
| `ltv` | `BigDecimal` | **新的 LTV**。当用户激活此 E-Mode 时，此类别中资产的贷款价值比（例如 `0.98` 表示 98%）。 |
| `liquidationThreshold` | `BigDecimal` | **新的清算门槛**。激活此 E-Mode 时的清算门槛（例如 `0.99` 表示 99%）。 |
| `liquidationBonus` | `BigDecimal` | **新的清算奖金（罚金）**。激活此 E-Mode 时的清算折扣。 |
| `reserves` | `[Reserve!]` | **关联的储备列表**。一个数组，包含所有**属于**这个 E-Mode 类别的 `Reserve`（市场）实体。 |
| `priceOracle` | `PriceOracle` | **关联的价格预言机**。*（可能存在）* 此 E-Mode 类别可能使用的特定价格预言机。 |

---

### 2. 隔离模式 (IsolationMode)

* **查询字段**: `isolationModeTotalDebtUpdated` (通过ID) / `isolationModeTotalDebtUpdateds` (列表查询)
* **实体描述**: 这是一个**事件实体**。Aave V3 的“隔离模式”允许上架风险较高的新资产。当一个资产处于隔离模式时，用户只能将其作为抵押品，并且**只能借入**特定的稳定币，同时该资产的**总债务有上限**。`IsolationModeTotalDebtUpdated` 实体会在该隔离资产的**总债务余额发生变化**时被创建和记录。

#### `IsolationModeTotalDebtUpdated` 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符，通常是**交易哈希 (Tx Hash) + 日志索引**。 |
| `asset` | `Reserve!` | **关联的资产**。链接到处于隔离模式的 `Reserve`（市场）实体。 |
| `newTotalDebt` | `BigInt` | **新的总债务**。此次更新后，该隔离资产背后的总债务（以原生单位计）。 |
| `timestamp` | `Int` | **时间戳**。债务更新事件发生的区块时间戳。 |

---

### 3. 合约映射 (Mappings)

* **查询字段**: `contractToPoolMapping` / `mapAssetPool` (及复数形式)
* **实体描述**: 这两者都是**辅助工具 / 查找表**实体。在 Aave 协议中，一个资产（如 USDC）对应着多个合约地址：
    1.  **底层资产地址** (USDC)
    2.  **aToken 地址** (aUSDC)
    3.  **Variable Debt Token 地址** (vUSDC)
    4.  **Stable Debt Token 地址** (sUSDC)

    在子图中，`Pool`（或 `Reserve`/`Market`）实体的主 `id` 通常是**底层资产地址**。

    当您只有一个 aToken 或 vToken 地址时，很难直接找到它属于哪个 `Pool`。`ContractToPoolMapping` 和 `MapAssetPool` 实体就是为了解决这个问题而创建的。它们提供了从**任何**相关合约（aToken, vToken, sToken）地址**映射回**其所属的 `Pool` 实体的快捷方式。

#### `ContractToPoolMapping` / `MapAssetPool` 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **合约地址**。这是**被映射的**合约地址，例如 `aUSDC` 的地址 `0x...`。 |
| `pool` | `Pool!` | **关联的资金池**。链接到该合约所属的主 `Pool`（或 `Reserve`）实体。 |
| `type` | `String` | *（推测属性）* 可能包含一个字符串，用于标识 `id` 处的地址是什么类型（例如 "ATOKEN", "VTOKEN", "STOKEN"）。 |

# 第七部分：奖励与推荐人 (Rewards & Referrers)

好的，这是对 **“7. 奖励与推荐人 (Rewards & Referrers)”** 部分的详细分析。

这组实体（Entities）用于跟踪 Aave 协议的流动性挖矿激励（Rewards）和推荐计划（Referral Program）。

---

### 1. `Reward` 实体

* **查询字段**: `reward` (通过ID) / `rewards` (列表查询)
* **实体描述**: 代表一个特定的**奖励代币及其分发配置**。Aave 协议（或相关方）可能会为特定市场（如在 Optimism 上的 USDC 存款）提供额外的代币激励（如 $OP 代币）。`Reward` 实体就封装了这种激励的详细信息。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。通常是**奖励代币的合约地址**。 |
| `token` | `Token!` | **关联的代币**。链接到 `Token` 实体，以获取奖励代币的符号（symbol）、名称（name）和小数位数（decimals）。 |
| `controller` | `RewardsController!` | **关联的控制器**。链接到负责分发此奖励的 `RewardsController` 实体。 |
| `distributionEnd` | `Int` | **分发结束时间**。该奖励计划结束的区块时间戳。 |
| `rewardOracle` | `RewardFeedOracle!` | **关联的奖励预言机**。链接到用于获取此奖励代币价格的 `RewardFeedOracle` 实体。 |
| `reserves` | `[Reserve!]` | **关联的储备列表**。一个数组，包含所有正在分发此奖励的 `Reserve`（市场）实体。 |
| `emissionPerSecond` | `BigInt` | *（推测属性）* 每秒钟释放的奖励代币数量。 |

---

### 2. `RewardsController` 实体

* **查询字段**: `rewardsController` (通过ID) / `rewardsControllers` (列表查询)
* **实体描述**: 代表一个 Aave **奖励分发智能合约**的地址。这个合约负责处理计算和分发奖励的逻辑。一个 Aave 资金池（Pool）通常会有一个主 `RewardsController`。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **RewardsController 合约地址**。 |
| `rewards` | `[Reward!]` | **关联的奖励列表**。一个数组，链接到所有由此控制器管理的 `Reward` 实体。 |
| `rewardOracle` | `RewardFeedOracle` | **关联的预言机**。此控制器用于定价其管理的所有奖励代币的预言机合约地址。 |
| `pool` | `Pool!` | **关联的资金池**。此奖励控制器所属的 `Pool`（或 `Market`）实体。 |
| `emissionManager` | `Bytes` | **释放管理者地址**。有权调整奖励释放率的账户地址。 |

---

### 3. `RewardFeedOracle` 实体

* **查询字段**: `rewardFeedOracle` (通过ID) / `rewardFeedOracles` (列表查询)
* **实体描述**: 这是一个专门用于**奖励代币的价格预言机**实体。它与主 `PriceOracle`（用于抵押品和债务资产）分离，因为奖励代币（如 $stkAAVE, $OP, $ARB）可能使用不同的价格来源。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **奖励代币的预言机合约地址**。 |
| `reward` | `Reward!` | **关联的奖励**。链接到此预言机正在定价的 `Reward` 实体。 |
| `priceInEth` | `BigInt` | **以 ETH 计价的价格**。1 单位奖励代币价值多少 ETH。 |
| `priceInUsd` | `BigDecimal` | **以 USD 计价的价格**。1 单位奖励代币价值多少美元。 |
| `priceSource` | `Bytes` | **价格源地址**。此价格的直接来源（例如 Chainlink 聚合器地址）。 |
| `lastUpdateTimestamp` | `Int` | **最后更新时间戳**。价格最后一次在链上更新的区块时间戳。 |

---

### 4. `Referrer` 实体

* **查询字段**: `referrer` (通过ID) / `referrers` (列表查询)
* **实体描述**: 代表 Aave V3 **推荐计划**中的一个**推荐人**。当一个新用户通过推荐码或链接与 Aave 交互时，该推荐人可以从该用户的活动中赚取一部分佣金（通常来自协议收入）。

#### 详细属性分析

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | **推荐人的钱包地址**。 |
| `referrals` | `[User!]` | **被推荐的用户列表**。一个数组，链接到所有通过此推荐人加入的 `User` 实体。 |
| `totalCommissionEarned` | `BigDecimal` | **赚取的总佣金（USD）**。此推荐人历史赚取的总佣金的美元价值。 |
| `referredUsersCount` | `Int` | **被推荐用户总数**。此推荐人推荐的用户数量。 |

# 第八部分：GHO & V3 特定功能 (GHO & V3 Specifics)

好的，这是对 **“8. GHO & V3 特定功能 (GHO & V3 Specifics)”** 部分的详细分析。

这组实体（Entities）代表了 Aave V3 引入的特定新功能，尤其是与 Aave 的原生稳定币 GHO 相关的操作，以及 V3 的信用授权（Credit Delegation）功能。

---

### 1. GHO (MintUnbacked / BackUnbacked)

GHO 是 Aave 的原生、超额抵押稳定币。虽然 GHO 的常规借贷（针对用户抵押品）会被记录为标准的 `Borrow` 事件，但 GHO 还有一个特殊的“促进者 (Facilitator)”机制。促进者（例如其他协议或 Aave DAO 本身）被授予在*没有*超额抵押的情况下铸造 (Mint) GHO 的能力，通常有严格的限额。`MintUnbacked` 和 `BackUnbacked` 实体专门用于跟踪这种**非用户抵押**的 GHO 铸造和销毁事件。

#### A. `MintUnbacked` 实体
* **查询字段**: `mintUnbacked` (通过ID) / `mintUnbackeds` (列表查询)
* **实体描述**: 这是一个**事件实体**。当一个被授权的“促进者” (Facilitator) 铸造 GHO 时，会创建一个 `MintUnbacked` 条目。这**不是**普通用户的借款。

##### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符，通常是**交易哈希 (Tx Hash) + 日志索引**。 |
| `reserve` | `Reserve!` | **关联的 GHO 储备**。链接到 GHO 的 `Reserve` (市场) 实体。 |
| `user` | `User!` | **GHO 接收者**。GHO 被铸造到的目标地址。 |
| `onBehalfOf` | `User!` | **发起者**。发起此次铸造的“促进者” (Facilitator) 地址。 |
| `amount` | `BigInt` | **铸造数量**。被铸造的 GHO 的数量（原生单位）。 |
| `timestamp` | `Int` | **时间戳**。铸造事件发生的区块时间戳。 |

#### B. `BackUnbacked` 实体
* **查询字段**: `backUnbacked` (通过ID) / `backUnbackeds` (列表查询)
* **实体描述**: 这是一个**事件实体**。它是 `MintUnbacked` 的反向操作。当“促进者”销毁 (Burn) 或偿还 (Back) 之前“无抵押”铸造的 GHO 时，会创建一个 `BackUnbacked` 条目。

##### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符，通常是**交易哈希 (Tx Hash) + 日志索引**。 |
| `reserve` | `Reserve!` | **关联的 GHO 储备**。链接到 GHO 的 `Reserve` (市场) 实体。 |
| `user` | `User!` | **销毁者/偿还者**。执行此次销毁操作的“促进者” (Facilitator) 地址。 |
| `amount` | `BigInt` | **销毁数量**。被销毁或偿还的 GHO 的数量（原生单位）。 |
| `timestamp` | `Int` | **时间戳**。销毁事件发生的区块时间戳。 |

---

### 2. `MintedToTreasury` 实体

* **查询字段**: `mintedToTreasury` (通过ID) / `mintedToTreasuries` (列表查询)
* **实体描述**: 这是一个**事件实体**。Aave 协议通过“储备因子” (`reserveFactor`) 从存款人赚取的利息中抽取一部分作为协议收入。这部分收入会累积在 `Reserve` 合约中。当这些累积的费用被**提取**并发送到 Aave DAO 金库 (Treasury) 时，就会触发并创建一个 `MintedToTreasury` 事件实体。

#### 详细属性分析
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符，通常是**交易哈希 (Tx Hash) + 日志索引**。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。从中提取费用的 `Reserve` 实体。 |
| `treasury` | `User!` | **金库**。接收这些费用的 Aave DAO 金库地址（被建模为 `User` 实体）。 |
| `amount` | `BigInt` | **提取数量**。被提取并发送到金库的代币数量（通常是 aToken）。 |
| `timestamp` | `Int` | **时间戳**。提取事件发生的区块时间戳。 |

---

### 3. 授权 (DelegatedAllowance)

这组实体代表 Aave V3 的**信用授权 (Credit Delegation)** 功能。此功能允许一个用户（`delegator`，授权人）将其**借款额度**（而非其代币）授权给另一个用户（`delegatee`，被授权人）使用。例如，一个有 100 万美元抵押品的用户 A，可以将其借款额度授权给用户 B，允许用户 B 在*不提供任何抵押品*的情况下借款，但使用的是 A 的信用额度。

#### A. `StableTokenDelegatedAllowance` 实体
* **查询字段**: `stableTokenDelegatedAllowance` (通过ID) / `stableTokenDelegatedAllowances` (列表查询)
* **实体描述**: 这是一个**状态实体**（State Entity），*不是*事件。它存储了特定用户之间关于**稳定利率债务代币** (sToken) 的**当前**信用授权状态。

#### B. `VariableTokenDelegatedAllowance` 实体
* **查询字段**: `variableTokenDelegatedAllowance` (通过ID) / `variableTokenDelegatedAllowances` (列表查询)
* **实体描述**: 这是一个**状态实体**。它存储了特定用户之间关于**可变利率债务代币** (vToken) 的**当前**信用授权状态。

##### 详细属性分析 (Stable 和 Variable 实体结构相同)
| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `id` | `ID!` | 唯一标识符。通常是 `delegator-delegatee-reserve` 的组合。 |
| `delegator` | `User!` | **授权人**。出让其借款额度的 `User` 实体。 |
| `delegatee` | `User!` | **被授权人**。被允许使用借款额度的 `User` 实体。 |
| `reserve` | `Reserve!` | **关联的储备（市场）**。该授权所适用的资产市场（例如 USDC 市场）。 |
| `amountAllowed` | `BigInt` | **当前授权额度**。`delegatee` 被允许借入的*剩余*额度。当 `delegatee` 借款时，此值减少；当 `delegatee` 还款或 `delegator` 更新授权时，此值变化。 |
| `userReserve` | `UserReserve!` | **关联的用户仓位**。链接到**授权人**（`delegator`）在该 `Reserve` 中的 `UserReserve` 实体。 |

# 第九部分：子图元数据 (Subgraph Metadata)

好的，这是对 **“9. 子图元数据 (Subgraph Metadata)”** 部分的详细分析。

-----

### 1\. `_meta` 实体

  * **查询字段**: `_meta`
  * **实体描述**:
    `_meta` 并不是一个常规的数据实体（如 `Pool` 或 `User`），而是一个由 The Graph 协议（为所有子图）提供的**特殊查询字段**。

它的**唯一目的**是提供关于**子图本身状态**的元数据。这对于开发者来说至关重要，因为它能回答以下问题：

1.  **数据有多新？**（子图已经索引到哪个区块了？）
2.  **数据是否完整？**（子图在索引过程中是否遇到了错误？）
3.  **我正在查询的是哪个版本？**（我正在使用的是哪个部署实例？）

通过查询 `_meta`，您可以验证您所获取的 Aave 数据的**新鲜度**和**可靠性**。

#### 详细属性分析

`_meta` 字段返回一个包含以下属性的对象：

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `block` | `_Block_` | 一个嵌套对象，包含子图**已索引到的最新区块**的信息。这是判断数据新鲜度的关键。 |
| `deployment` | `String` | **部署 ID**。这是一个 IPFS 哈希值（CID，例如 `Qm...`），唯一标识当前正在运行的这个子图部署版本。这有助于您确认您正在查询的是否是您期望的子图版本。 |
| `hasIndexingErrors` | `Boolean` | **是否存在索引错误**。一个布尔值 (`true` / `false`)。如果为 `true`，则表示子图在处理历史数据时遇到了错误，**这可能导致数据不完整或不准确**。这是一个非常重要的健康检查字段。 |

#### `_meta { block }` 的嵌套属性

`block` 字段本身包含以下关键信息：

| 属性 (Attribute) | 类型 | 意义 |
| :--- | :--- | :--- |
| `hash` | `Bytes` | **最新区块的哈希值**。 |
| `number` | `BigInt` | **最新区块的高度（编号）**。这是最重要的字段。您可以将此区块号与链上的当前最新区块号进行比较，以确定子图的“延迟”（lag）或“同步进度”。 |
| `timestamp` | `BigInt` | **最新区块的时间戳**。这提供了该区块被挖出的Unix时间。 |

-----