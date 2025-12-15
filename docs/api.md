# Cursor API (generated)

Source: https://cursor.com/docs/api

This file is generated from the public Cursor docs and is intended to capture **all API endpoints, parameters, and response formats** present in those docs at generation time.

## Endpoint index

| Method | Path | Documented in |
| --- | --- | --- |
| GET | /analytics/ai-code/changes | [link](https://cursor.com/docs/account/teams/ai-code-tracking-api) |
| GET | /analytics/ai-code/changes.csv | [link](https://cursor.com/docs/account/teams/ai-code-tracking-api) |
| GET | /analytics/ai-code/commits | [link](https://cursor.com/docs/account/teams/ai-code-tracking-api) |
| GET | /analytics/ai-code/commits.csv | [link](https://cursor.com/docs/account/teams/ai-code-tracking-api) |
| GET | /analytics/by-user/agent-edits | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/ask-mode | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/client-versions | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/commands | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/mcp | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/models | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/plans | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/tabs | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/by-user/top-file-extensions | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/agent-edits | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/ask-mode | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/client-versions | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/commands | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/dau | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/leaderboard | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/mcp | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/models | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/plans | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/tabs | [link](https://cursor.com/docs/account/teams/analytics-api) |
| GET | /analytics/team/top-file-extensions | [link](https://cursor.com/docs/account/teams/analytics-api) |
| POST | /bugbot/repo/update | [link](https://cursor.com/docs/bugbot) |
| GET | /settings/repo-blocklists/repos | [link](https://cursor.com/docs/account/teams/admin-api) |
| DELETE | /settings/repo-blocklists/repos/:repoId | [link](https://cursor.com/docs/account/teams/admin-api) |
| POST | /settings/repo-blocklists/repos/upsert | [link](https://cursor.com/docs/account/teams/admin-api) |
| GET | /teams/audit-logs | [link](https://cursor.com/docs/account/teams/admin-api) |
| POST | /teams/daily-usage-data | [link](https://cursor.com/docs/account/teams/admin-api) |
| POST | /teams/filtered-usage-events | [link](https://cursor.com/docs/account/teams/admin-api) |
| GET | /teams/groups | [link](https://cursor.com/docs/account/teams/admin-api) |
| POST | /teams/groups | [link](https://cursor.com/docs/account/teams/admin-api) |
| DELETE | /teams/groups/:groupId | [link](https://cursor.com/docs/account/teams/admin-api) |
| GET | /teams/groups/:groupId | [link](https://cursor.com/docs/account/teams/admin-api) |
| PATCH | /teams/groups/:groupId | [link](https://cursor.com/docs/account/teams/admin-api) |
| DELETE | /teams/groups/:groupId/members | [link](https://cursor.com/docs/account/teams/admin-api) |
| POST | /teams/groups/:groupId/members | [link](https://cursor.com/docs/account/teams/admin-api) |
| GET | /teams/members | [link](https://cursor.com/docs/account/teams/admin-api) |
| POST | /teams/spend | [link](https://cursor.com/docs/account/teams/admin-api) |
| POST | /teams/user-spend-limit | [link](https://cursor.com/docs/account/teams/admin-api) |
| GET | /v0/agents | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| POST | /v0/agents | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| DELETE | /v0/agents/{id} | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| GET | /v0/agents/{id} | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| GET | /v0/agents/{id}/conversation | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| POST | /v0/agents/{id}/followup | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| POST | /v0/agents/{id}/stop | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| GET | /v0/me | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| GET | /v0/models | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |
| GET | /v0/repositories | [link](https://cursor.com/docs/cloud-agent/api/endpoints) |

## Full documentation by page

### Admin API

Source: https://cursor.com/docs/account/teams/admin-api

Endpoints found on this page:

- `GET /teams/members`
- `GET /teams/audit-logs`
- `GET /settings/repo-blocklists/repos`
- `GET /teams/groups`
- `GET /teams/groups/:groupId`
- `POST /teams/daily-usage-data`
- `POST /teams/spend`
- `POST /teams/filtered-usage-events`
- `POST /teams/user-spend-limit`
- `POST /settings/repo-blocklists/repos/upsert`
- `POST /teams/groups`
- `POST /teams/groups/:groupId/members`
- `DELETE /settings/repo-blocklists/repos/:repoId`
- `DELETE /teams/groups/:groupId`
- `DELETE /teams/groups/:groupId/members`
- `PATCH /teams/groups/:groupId`

# Admin API

The Admin API lets you programmatically access your team's data, including member information, usage metrics, and spending details.

-   The Admin API uses [Basic Authentication](/docs/api#basic-authentication) with your API key as the username.
-   For details on creating API keys, authentication methods, rate limits, and best practices, see the [API Overview](/docs/api).

## [Endpoints](#endpoints)

### [Get Team Members](#get-team-members)

GET `/teams/members`

Retrieve all team members and their details.

```
curl -X GET https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner"
    }
  ]
}
```

### [Get Audit Logs](#get-audit-logs)

GET `/teams/audit-logs`

Retrieve audit log events for your team with filtering. Track team activity, security events, and configuration changes. Rate limited to 20 requests per minute per team. See [rate limits and best practices](/docs/api#rate-limits).

#### [Parameters](#parameters)

`startTime` string | number

Start time (defaults to 7 days ago). See [Date Formats](#date-formats)

`endTime` string | number

End time (defaults to now). See [Date Formats](#date-formats)

`eventTypes` string

Comma-separated event types to filter by

`search` string

Search term to filter events

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Results per page (1-500). Default: `100`

`users` string

Filter by users. See [User Filtering](#user-filtering) below

Date range cannot exceed 30 days. Make multiple requests for longer periods.

#### [Date Formats](#date-formats)

The `startTime` and `endTime` parameters support multiple formats:

-   **Relative shortcuts**: `now`, `today`, `yesterday`, `7d` (7 days ago), `5h` (5 hours ago), `300s` (300 seconds ago)
-   **ISO 8601 strings**: `2024-01-15T12:00:00Z` or `2024-01-15T10:00:00-05:00`
-   **YYYY-MM-DD format**: `2024-01-15` (time defaults to 00:00:00 UTC)
-   **Unix timestamps**: `1705315200` (seconds) or `1705315200000` (milliseconds)

**Examples:**

-   `?startTime=7d&endTime=now` - Last 7 days
-   `?startTime=5h&endTime=now` - Last 5 hours
-   `?startTime=2024-01-15&endTime=2024-01-20` - Specific date range
-   `?startTime=1705315200000&endTime=1705401600000` - Unix timestamps

#### [User Filtering](#user-filtering)

The `users` parameter accepts multiple formats, comma-separated:

-   **Email addresses**: `developer@company.com,admin@company.com`
-   **Encoded user IDs**: `user_PDSPmvukpYgZEDXsoNirw3CFhy,user_kljUvI0ASZORvSEXf9hV0ydcso`

You can mix formats: `developer@company.com,12345,user_PDSPmvukpYgZEDXsoNirw3CFhy`

Maximum number of users per request equals `pageSize`.

```
curl -X GET "https://api.cursor.com/teams/audit-logs?users=admin@company.com,developer@company.com&eventTypes=login,settings_changed" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "events": [
    {
      "event_id": "evt_abc123",
      "timestamp": "2024-01-15T12:30:00.000Z",
      "user_email": "admin@company.com",
      "event_type": "settings_changed",
      "event_data": {
        "setting_name": "team_spend_limit",
        "old_value": 1000,
        "new_value": 2000
      }
    },
    {
      "event_id": "evt_def456",
      "timestamp": "2024-01-15T10:15:00.000Z",
      "user_email": "developer@company.com",
      "event_type": "login",
      "event_data": {
        "ip_address": "192.168.1.1",
        "user_agent": "Cursor/0.42.0"
      }
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 100,
    "totalCount": 2,
    "totalPages": 1,
    "hasNextPage": false,
    "hasPreviousPage": false
  },
  "params": {
    "teamId": 12345,
    "startDate": 1704729600000,
    "endDate": 1705334400000
  }
}
```

### [Get Daily Usage Data](#get-daily-usage-data)

POST `/teams/daily-usage-data`

Retrieve daily usage metrics for your team. Data is aggregated at the hourly level - we recommend polling this endpoint at most once per hour. Rate limited to 20 requests per minute per team. See [best practices](/docs/api#best-practices).

#### [Parameters](#parameters-1)

`startDate` number Required

Start date in epoch milliseconds

`endDate` number Required

End date in epoch milliseconds

Date range cannot exceed 30 days. Make multiple requests for longer periods.

```
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

**Response:**

```
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-5",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

### [Get Spending Data](#get-spending-data)

POST `/teams/spend`

Retrieve spending information for the current calendar month with search, sorting, and pagination.

#### [Parameters](#parameters-2)

`searchTerm` string

Search in user names and emails

`sortBy` string

Sort by: `amount`, `date`, `user`. Default: `date`

`sortDirection` string

Sort direction: `asc`, `desc`. Default: `desc`

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Results per page

```
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

**Response:**

```
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner",
      "hardLimitOverrideDollars": 0
    }
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

### [Get Usage Events Data](#get-usage-events-data)

POST `/teams/filtered-usage-events`

Retrieve detailed usage events for your team with comprehensive filtering, search, and pagination options. This endpoint provides granular insights into individual API calls, model usage, token consumption, and costs. Data is aggregated at the hourly level - we recommend polling this endpoint at most once per hour. Rate limited to 20 requests per minute per team. See [best practices](/docs/api#best-practices).

**Cost Calculation**: The API returns `cursorTokenFee` as a separate field on each event. The Cursor Dashboard UI sums the Cursor Token Fee (for teams with Cursor Token Fee enabled) and model costs together for display. To match dashboard totals, add `cursorTokenFee` to the model costs (`tokenUsage.totalCents`).

#### [Parameters](#parameters-3)

`startDate` number

Start date in epoch milliseconds

`endDate` number

End date in epoch milliseconds

`userId` number

Filter by specific user ID

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Number of results per page. Default: `10`

`email` string

Filter by user email address

```
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Response:**

```
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "cursorTokenFee": 1.18,
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "cursorTokenFee": 1.18,
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Included in Business",
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "cursorTokenFee": 0,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

### [Set User Spend Limit](#set-user-spend-limit)

POST `/teams/user-spend-limit`

Set spending limits for individual team members. This allows you to control how much each user can spend on AI usage within your team. Rate limited to 60 requests per minute per team. See [rate limits](/docs/api#rate-limits).

#### [Parameters](#parameters-4)

`userEmail` string Required

Email address of the team member

`spendLimitDollars` number | null Required

Spending limit in dollars (integer only, no decimals). Set to `null` to remove the limit.

-   The user must already be a member of your team
-   Only integer values are accepted (no decimal amounts)
-   Setting `spendLimitDollars` to 0 will set the limit to $0
-   Setting `spendLimitDollars` to `null` will clear/remove the limit entirely

```
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

**Successful response:**

```
{
  "outcome": "success",
  "message": "Spend limit set to $100 for user developer@company.com"
}
```

**Error response:**

```
{
  "outcome": "error",
  "message": "Invalid email format"
}
```

### [Get Team Repo Blocklists](#get-team-repo-blocklists)

GET `/settings/repo-blocklists/repos`

Retrieve all repository blocklists configured for your team. Add repositories and use patterns to prevent files or directories from being indexed or used as context.

#### [Pattern Examples](#pattern-examples)

Common blocklist patterns:

-   `*` - Block entire repository
-   `*.env` - Block all .env files
-   `config/*` - Block all files in config directory
-   `**/*.secret` - Block all .secret files in any subdirectory
-   `src/api/keys.ts` - Block specific file

```
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

### [Upsert Repo Blocklists](#upsert-repo-blocklists)

POST `/settings/repo-blocklists/repos/upsert`

Replace existing repository blocklists for the provided repos. This endpoint will only overwrite the patterns for the repositories provided. All other repos will be unaffected.

#### [Parameters](#parameters-5)

`repos` array Required

Array of repository blocklist objects. Each repository object must contain:

-   `url` string - Repository URL to blocklist
-   `patterns` string\[\] - Array of file patterns to block (glob patterns supported)

```
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools",
        "patterns": ["*"]
      }
    ]
  }'
```

**Response:**

```
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

### [Delete Repo Blocklist](#delete-repo-blocklist)

DELETE `/settings/repo-blocklists/repos/:repoId`

Remove a specific repository from the blocklist. Returns 204 No Content on successful deletion.

#### [Parameters](#parameters-6)

`repoId` string Required

ID of the repository blocklist to delete

```
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u YOUR_API_KEY:
```

**Response:**

```
204 No Content
```

## [Billing Groups](#billing-groups)

[Billing groups](/docs/account/enterprise/billing-groups) allow Enterprise admins to understand and manage spend across groups of users. This functionality is useful for reporting, internal chargebacks, and budgeting.

Billing groups are only available to beta customers on the Enterprise plan. To get access, please ask your account manager.

Members can only be in one billing group at a time. Members not assigned to any group are placed in a reserved `Unassigned` group.

### [List Groups](#list-groups)

GET `/teams/groups`

Retrieve all billing groups for your team with spend data for the current billing cycle.

#### [Parameters](#parameters-7)

`billingCycle` string

ISO date string (e.g., `2025-01-15`) to specify which billing cycle to query. Defaults to current cycle.

```
curl -X GET "https://api.cursor.com/teams/groups?billingCycle=2025-01-15" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "groups": [
    {
      "id": "group_PDSPmvukpYgZEDXsoNirw3CFhy",
      "name": "Engineering",
      "type": "BILLING",
      "directoryGroupId": null,
      "memberCount": 12,
      "createdAt": "2024-01-15T10:30:00.000Z",
      "updatedAt": "2024-01-20T14:22:00.000Z",
      "spendCents": 245000,
      "currentMembers": [
        {
          "userId": "user_abc123",
          "name": "Alex Developer",
          "email": "alex@company.com",
          "joinedAt": "2024-01-15T10:30:00.000Z",
          "leftAt": null,
          "spendCents": 12500
        }
      ],
      "formerMembers": [],
      "dailySpend": [
        { "date": "2025-01-15", "spendCents": 8500 },
        { "date": "2025-01-16", "spendCents": 9200 }
      ]
    },
    {
      "id": "group_kljUvI0ASZORvSEXf9hV0ydcso",
      "name": "Design",
      "type": "BILLING",
      "directoryGroupId": "dir_group_abc123xyz",
      "memberCount": 5,
      "createdAt": "2024-01-16T09:00:00.000Z",
      "updatedAt": "2024-01-16T09:00:00.000Z",
      "spendCents": 87500,
      "currentMembers": [],
      "formerMembers": [],
      "dailySpend": []
    }
  ],
  "unassignedGroup": {
    "id": "group_unassigned",
    "name": "Unassigned",
    "type": "BILLING",
    "directoryGroupId": null,
    "memberCount": 3,
    "createdAt": "2024-01-01T00:00:00.000Z",
    "updatedAt": "2024-01-01T00:00:00.000Z",
    "spendCents": 15000,
    "currentMembers": [],
    "formerMembers": [],
    "dailySpend": []
  },
  "billingCycle": {
    "cycleStart": "2025-01-01T00:00:00.000Z",
    "cycleEnd": "2025-02-01T00:00:00.000Z"
  }
}
```

### [Get Group](#get-group)

GET `/teams/groups/:groupId`

Retrieve a single billing group with its members and spend data for the current billing cycle.

#### [Parameters](#parameters-8)

`groupId` string Required

The encoded group ID (e.g., `group_PDSPmvukpYgZEDXsoNirw3CFhy`)

`billingCycle` string

ISO date string (e.g., `2025-01-15`) to specify which billing cycle to query. Defaults to current cycle.

```
curl -X GET "https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy?billingCycle=2025-01-15" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "group": {
    "id": "group_PDSPmvukpYgZEDXsoNirw3CFhy",
    "name": "Engineering",
    "type": "BILLING",
    "directoryGroupId": null,
    "memberCount": 3,
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-20T14:22:00.000Z",
    "spendCents": 125000,
    "currentMembers": [
      {
        "userId": "user_abc123",
        "name": "Alex Developer",
        "email": "alex@company.com",
        "joinedAt": "2024-01-15T10:30:00.000Z",
        "leftAt": null,
        "spendCents": 75000,
        "dailySpend": [
          { "date": "2025-01-15", "spendCents": 5000 },
          { "date": "2025-01-16", "spendCents": 7500 }
        ]
      },
      {
        "userId": "user_def456",
        "name": "Sam Engineer",
        "email": "sam@company.com",
        "joinedAt": "2024-01-16T09:15:00.000Z",
        "leftAt": null,
        "spendCents": 50000,
        "dailySpend": [
          { "date": "2025-01-15", "spendCents": 3500 },
          { "date": "2025-01-16", "spendCents": 4200 }
        ]
      }
    ],
    "formerMembers": [
      {
        "userId": "user_xyz789",
        "name": "Former Member",
        "email": "former@company.com",
        "joinedAt": "2024-01-10T08:00:00.000Z",
        "leftAt": "2024-01-14T17:00:00.000Z",
        "spendCents": 0
      }
    ],
    "dailySpend": [
      { "date": "2025-01-15", "spendCents": 8500 },
      { "date": "2025-01-16", "spendCents": 11700 }
    ]
  },
  "billingCycle": {
    "cycleStart": "2025-01-01T00:00:00.000Z",
    "cycleEnd": "2025-02-01T00:00:00.000Z"
  }
}
```

### [Create Group](#create-group)

POST `/teams/groups`

Create a new billing group. Rate limited to 20 requests per minute per team.

#### [Parameters](#parameters-9)

`name` string Required

Name of the group

`type` string

Group type. Currently only `BILLING` is supported. Default: `BILLING`

```
curl -X POST https://api.cursor.com/teams/groups \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Engineering"
  }'
```

**Response:**

```
{
  "group": {
    "id": "group_PDSPmvukpYgZEDXsoNirw3CFhy",
    "name": "Engineering",
    "type": "BILLING",
    "directoryGroupId": null,
    "memberCount": 0,
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-15T10:30:00.000Z",
    "members": []
  }
}
```

### [Update Group](#update-group)

PATCH `/teams/groups/:groupId`

Update a billing group's name or directory group attachment. Rate limited to 20 requests per minute per team.

Only one field can be updated per request. To update both name and directory attachment, make separate requests.

#### [Parameters](#parameters-10)

`groupId` string Required

The encoded group ID

`name` string

New name for the group

`directoryGroupId` string | null

Directory group ID to sync with, or `null` to detach from directory sync

```
curl -X PATCH https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Platform Engineering"
  }'
```

**Response:**

```
{
  "group": {
    "id": "group_PDSPmvukpYgZEDXsoNirw3CFhy",
    "name": "Platform Engineering",
    "type": "BILLING",
    "directoryGroupId": null,
    "memberCount": 3,
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-25T16:45:00.000Z",
    "members": [
      {
        "userId": "user_abc123",
        "name": "Alex Developer",
        "email": "alex@company.com",
        "joinedAt": "2024-01-15T10:30:00.000Z"
      }
    ]
  }
}
```

### [Delete Group](#delete-group)

DELETE `/teams/groups/:groupId`

Delete a billing group. Returns 204 No Content on success. Rate limited to 20 requests per minute per team.

Deleting a billing group is a destructive operation; data cannot be recovered. All historical usage for deleted groups is reassigned retroactively to the `Unassigned` group.

#### [Parameters](#parameters-11)

`groupId` string Required

The encoded group ID to delete

```
curl -X DELETE https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy \
  -u YOUR_API_KEY:
```

**Response:**

```
204 No Content
```

### [Add Members to Group](#add-members-to-group)

POST `/teams/groups/:groupId/members`

Add team members to a billing group. Users must already be members of your team and not currently assigned to another group. Rate limited to 20 requests per minute per team.

Billing groups synced with SCIM cannot be modified via the API. All member assignment for SCIM-synced groups must be handled via [SCIM](/docs/account/teams/scim).

#### [Parameters](#parameters-12)

`groupId` string Required

The encoded group ID

`userIds` string\[\] Required

Array of encoded user IDs to add (e.g., `["user_abc123", "user_def456"]`)

```
curl -X POST https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy/members \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userIds": ["user_abc123", "user_def456"]
  }'
```

**Response:**

```
{
  "group": {
    "id": "group_PDSPmvukpYgZEDXsoNirw3CFhy",
    "name": "Engineering",
    "type": "BILLING",
    "directoryGroupId": null,
    "memberCount": 2,
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-25T16:50:00.000Z",
    "members": [
      {
        "userId": "user_abc123",
        "name": "Alex Developer",
        "email": "alex@company.com",
        "joinedAt": "2024-01-25T16:50:00.000Z"
      },
      {
        "userId": "user_def456",
        "name": "Sam Engineer",
        "email": "sam@company.com",
        "joinedAt": "2024-01-25T16:50:00.000Z"
      }
    ]
  }
}
```

### [Remove Members from Group](#remove-members-from-group)

DELETE `/teams/groups/:groupId/members`

Remove team members from a billing group. Removed members are moved to the `Unassigned` group. Rate limited to 20 requests per minute per team.

Billing groups synced with SCIM cannot be modified via the API. All member changes for SCIM-synced groups must be handled via [SCIM](/docs/account/teams/scim).

#### [Parameters](#parameters-13)

`groupId` string Required

The encoded group ID

`userIds` string\[\] Required

Array of encoded user IDs to remove

```
curl -X DELETE https://api.cursor.com/teams/groups/group_PDSPmvukpYgZEDXsoNirw3CFhy/members \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userIds": ["user_def456"]
  }'
```

**Response:**

```
{
  "group": {
    "id": "group_PDSPmvukpYgZEDXsoNirw3CFhy",
    "name": "Engineering",
    "type": "BILLING",
    "directoryGroupId": null,
    "memberCount": 1,
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-25T17:00:00.000Z",
    "members": [
      {
        "userId": "user_abc123",
        "name": "Alex Developer",
        "email": "alex@company.com",
        "joinedAt": "2024-01-25T16:50:00.000Z"
      }
    ]
  }
}
```

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---

### AI Code Tracking API

Source: https://cursor.com/docs/account/teams/ai-code-tracking-api

Endpoints found on this page:

- `GET /analytics/ai-code/commits`
- `GET /analytics/ai-code/commits.csv`
- `GET /analytics/ai-code/changes`
- `GET /analytics/ai-code/changes.csv`

# AI Code Tracking API

The AI Code Tracking API lets you track AI-generated code contributions across your team's repositories, including per-commit AI usage and granular accepted AI changes.

-   The AI Code Tracking API uses [Basic Authentication](/docs/api#basic-authentication) with your API key as the username, the same method as the Admin API.
-   For details on creating API keys, authentication methods, rate limits, and best practices, see the [API Overview](/docs/api).
-   **Availability**: Enterprise only, [contact sales](https://cursor.com/contact-sales?source=docs-ai-code-tracking) to get access
-   **Status**: Alpha (response shapes and fields may change)
-   **Workspace limitation**: Metrics are only calculated for the git repository at the top level of the workspace root. Multi-root workspaces are not currently supported.

## [Endpoints](#endpoints)

### [Get AI Commit Metrics (JSON, paginated)](#get-ai-commit-metrics-json-paginated)

GET `/analytics/ai-code/commits`

Retrieve aggregated per-commit metrics that attribute lines to TAB, COMPOSER, and non-AI.

#### [Parameters](#parameters)

`startDate` string | date

ISO date string, the literal "now", or relative days like "7d" (means now - 7 days). Default: now - 7 days

`endDate` string | date

ISO date string, the literal "now", or relative days like "0d". Default: now

`page` number

Page number (1-based). Default: 1

`pageSize` number

Results per page. Default: 100, Max: 1000

`user` string

Optional filter by a single user. Accepts email (e.g., [developer@company.com](mailto:developer@company.com)), encoded ID (e.g., user\_abc123...), or numeric ID (e.g., 42)

  

#### [Response Fields](#response-fields)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Field</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">commitHash</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Git commit hash</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">userId</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Encoded user ID (e.g., user_abc123)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">userEmail</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">User's email address</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">repoName</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Repository name</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">branchName</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Branch name</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">isPrimaryBranch</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">boolean | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Whether this is the primary branch</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">totalLinesAdded</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines added in commit</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">totalLinesDeleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines deleted in commit</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">tabLinesAdded</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines added via TAB completions</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">tabLinesDeleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines deleted via TAB completions</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">composerLinesAdded</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines added via Composer</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">composerLinesDeleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines deleted via Composer</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">nonAiLinesAdded</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Non-AI lines added</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">nonAiLinesDeleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Non-AI lines deleted</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">message</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Commit message</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">commitTs</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Commit timestamp (ISO format)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">createdAt</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Ingestion timestamp (ISO format)</td></tr></tbody></table>

```
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: extract analytics client",
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

### [Download AI Commit Metrics (CSV, streaming)](#download-ai-commit-metrics-csv-streaming)

GET `/analytics/ai-code/commits.csv`

Download commit metrics data in CSV format for large data extractions.

#### [Parameters](#parameters-1)

`startDate` string | date

ISO date string, the literal "now", or relative days like "7d" (means now - 7 days). Default: now - 7 days

`endDate` string | date

ISO date string, the literal "now", or relative days like "0d". Default: now

`user` string

Optional filter by a single user. Accepts email (e.g., [developer@company.com](mailto:developer@company.com)), encoded ID (e.g., user\_abc123...), or numeric ID (e.g., 42)

#### [Response Headers](#response-headers)

-   Content-Type: text/csv; charset=utf-8

#### [CSV Columns](#csv-columns)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Column</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">commit_hash</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Git commit hash</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">user_id</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Encoded user ID</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">user_email</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">User's email address</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">repo_name</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Repository name</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">branch_name</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Branch name</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">is_primary_branch</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">boolean</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Whether this is the primary branch</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">total_lines_added</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines added in commit</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">total_lines_deleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines deleted in commit</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">tab_lines_added</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines added via TAB completions</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">tab_lines_deleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines deleted via TAB completions</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">composer_lines_added</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines added via Composer</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">composer_lines_deleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Lines deleted via Composer</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">non_ai_lines_added</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Non-AI lines added</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">non_ai_lines_deleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Non-AI lines deleted</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">message</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Commit message</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">commit_ts</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Commit timestamp (ISO format)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">created_at</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Ingestion timestamp (ISO format)</td></tr></tbody></table>

```
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u YOUR_API_KEY: \
  -o commits.csv
```

**Sample CSV Output:**

```
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: extract analytics client",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Add error handling",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

### [Get AI Code Change Metrics (JSON, paginated)](#get-ai-code-change-metrics-json-paginated)

GET `/analytics/ai-code/changes`

Retrieve granular accepted AI changes, grouped by deterministic changeId. Useful to analyze accepted AI events independent of commits.

#### [Parameters](#parameters-2)

`startDate` string | date

ISO date string, the literal "now", or relative days like "7d" (means now - 7 days). Default: now - 7 days

`endDate` string | date

ISO date string, the literal "now", or relative days like "0d". Default: now

`page` number

Page number (1-based). Default: 1

`pageSize` number

Results per page. Default: 100, Max: 1000

`user` string

Optional filter by a single user. Accepts email (e.g., [developer@company.com](mailto:developer@company.com)), encoded ID (e.g., user\_abc123...), or numeric ID (e.g., 42)

  

#### [Response Fields](#response-fields-1)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Field</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">changeId</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Deterministic ID for the change</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">userId</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Encoded user ID (e.g., user_abc123)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">userEmail</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">User's email address</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">source</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">"TAB" | "COMPOSER"</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Source of the AI change</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">model</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string | null</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">AI model used</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">totalLinesAdded</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines added</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">totalLinesDeleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines deleted</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">createdAt</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Ingestion timestamp (ISO format)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">metadata</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Array</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">File metadata (fileName may be omitted in privacy mode)</td></tr></tbody></table>

```
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        {
          "fileName": "src/analytics/report.ts",
          "fileExtension": "ts",
          "linesAdded": 12,
          "linesDeleted": 3
        },
        {
          "fileName": "src/analytics/ui.tsx",
          "fileExtension": "tsx",
          "linesAdded": 6,
          "linesDeleted": 1
        }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

### [Download AI Code Change Metrics (CSV, streaming)](#download-ai-code-change-metrics-csv-streaming)

GET `/analytics/ai-code/changes.csv`

Download change metrics data in CSV format for large data extractions.

#### [Parameters](#parameters-3)

`startDate` string | date

ISO date string, the literal "now", or relative days like "7d" (means now - 7 days). Default: now - 7 days

`endDate` string | date

ISO date string, the literal "now", or relative days like "0d". Default: now

`user` string

Optional filter by a single user. Accepts email (e.g., [developer@company.com](mailto:developer@company.com)), encoded ID (e.g., user\_abc123...), or numeric ID (e.g., 42)

#### [Response Headers](#response-headers-1)

-   Content-Type: text/csv; charset=utf-8

#### [CSV Columns](#csv-columns-1)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Column</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">change_id</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Deterministic ID for the change</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">user_id</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Encoded user ID</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">user_email</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">User's email address</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">source</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Source of the AI change (TAB or COMPOSER)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">model</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">AI model used</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">total_lines_added</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines added</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">total_lines_deleted</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Total lines deleted</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">created_at</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Ingestion timestamp (ISO format)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">metadata_json</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">JSON stringified array of metadata entries</td></tr></tbody></table>

```
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

**Sample CSV Output:**

```
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

---

## [Common Query Parameters](#common-query-parameters)

All endpoints accept the same query parameters via query string:

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Parameter</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Required</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">startDate</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string | date</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">ISO date string, the literal "now", or relative days like "7d" (means now - 7 days). Default: now - 7 days</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">endDate</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string | date</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">ISO date string, the literal "now", or relative days like "0d". Default: now</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">page</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Page number (1-based). Default: 1</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">pageSize</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Results per page. Default: 100, Max: 1000</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">user</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Optional filter by a single user. Accepts email (e.g., <a class="text-foreground underline decoration-neutral-600 underline-offset-2 transition-colors hover:decoration-neutral-700" href="mailto:developer@company.com" rel="noopener noreferrer" target="_blank">developer@company.com</a>), encoded ID (e.g., user_abc123...), or numeric ID (e.g., 42)</td></tr></tbody></table>

Responses return userId as an encoded external ID with the prefix user\_. This is stable for API consumption.

## [Semantics and How Metrics Are Computed](#semantics-and-how-metrics-are-computed)

-   **Sources**: "TAB" represents inline completions that were accepted; "COMPOSER" represents accepted diffs from Composer
-   **Lines metrics**: tabLinesAdded/Deleted and composerLinesAdded/Deleted are separately counted; nonAiLinesAdded/Deleted are derived as max(0, totalLines - AI lines)
-   **Privacy mode**: If enabled in the client, some metadata (like fileName) may be omitted
-   **Branch info**: isPrimaryBranch is true when the current branch equals the repo's default branch; may be undefined if repo info is unavailable

You can scan that file to understand how commits and changes are detected and reported.

## [Tips](#tips)

-   Use `user` parameter to quickly filter a single user across all endpoints
-   For large data extractions, prefer CSV endpoints—they stream in pages of 10,000 records server-side
-   `isPrimaryBranch` may be undefined if the client couldn't resolve the default branch
-   `commitTs` is the commit timestamp; `createdAt` is the ingestion time on our servers
-   Some fields may be absent when privacy mode is enabled on the client
-   Commit hashes are not unique or unchangeable. For example, you may see the same commit twice if you amend commits with extra information.
-   Commit timestamps will remain unchanged even if the commit is amended.

## [Changelog](#changelog)

-   **Alpha release**: Initial endpoints for commits and changes. Response shapes may evolve based on feedback

AI Code Tracking is available on the Enterprise plan

Contact our team to get access to detailed AI usage metrics.

[Contact Sales](https://cursor.com/contact-sales?source=docs-ai-code-tracking)

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---

### Analytics API

Source: https://cursor.com/docs/account/teams/analytics-api

Endpoints found on this page:

- `GET /analytics/team/agent-edits`
- `GET /analytics/team/tabs`
- `GET /analytics/team/dau`
- `GET /analytics/team/client-versions`
- `GET /analytics/team/models`
- `GET /analytics/team/top-file-extensions`
- `GET /analytics/team/mcp`
- `GET /analytics/team/commands`
- `GET /analytics/team/plans`
- `GET /analytics/team/ask-mode`
- `GET /analytics/team/leaderboard`
- `GET /analytics/by-user/agent-edits`
- `GET /analytics/by-user/tabs`
- `GET /analytics/by-user/models`
- `GET /analytics/by-user/top-file-extensions`
- `GET /analytics/by-user/client-versions`
- `GET /analytics/by-user/mcp`
- `GET /analytics/by-user/commands`
- `GET /analytics/by-user/plans`
- `GET /analytics/by-user/ask-mode`

# Analytics API

The Analytics API provides comprehensive insights into your team's Cursor usage, including AI-assisted coding metrics, active users, model usage, and more.

-   The Analytics API uses [Basic Authentication](/docs/api#basic-authentication). You can generate an API key from your [team settings page](https://cursor.com/settings).
-   For details on authentication, rate limits, and best practices, see the [API Overview](/docs/api).
-   **Availability**: Only for enterprise teams

### [Available Endpoints](#available-endpoints)

### [Agent Edits](#agent-edits)

GET `/analytics/team/agent-edits`

Get metrics on AI-suggested code edits accepted by your team in the Cursor IDE.

#### [Parameters](#parameters)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/agent-edits" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-15",
      "total_suggested_diffs": 145,
      "total_accepted_diffs": 98,
      "total_rejected_diffs": 47,
      "total_green_lines_accepted": 820,
      "total_red_lines_accepted": 160,
      "total_green_lines_rejected": 210,
      "total_red_lines_rejected": 60,
      "total_green_lines_suggested": 1030,
      "total_red_lines_suggested": 220,
      "total_lines_suggested": 1250,
      "total_lines_accepted": 980
    },
    {
      "event_date": "2025-01-16",
      "total_suggested_diffs": 132,
      "total_accepted_diffs": 89,
      "total_rejected_diffs": 43,
      "total_green_lines_accepted": 740,
      "total_red_lines_accepted": 150,
      "total_green_lines_rejected": 185,
      "total_red_lines_rejected": 55,
      "total_green_lines_suggested": 925,
      "total_red_lines_suggested": 175,
      "total_lines_suggested": 1100,
      "total_lines_accepted": 890
    }
  ],
  "params": {
    "metric": "agent-edits",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Tab Usage](#tab-usage)

GET `/analytics/team/tabs`

Get metrics on Tab autocomplete usage across your team.

#### [Parameters](#parameters-1)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/tabs" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-15",
      "total_suggestions": 5420,
      "total_accepts": 3210,
      "total_rejects": 2210,
      "total_green_lines_accepted": 4120,
      "total_red_lines_accepted": 2000,
      "total_green_lines_rejected": 1480,
      "total_red_lines_rejected": 730,
      "total_green_lines_suggested": 5600,
      "total_red_lines_suggested": 2740,
      "total_lines_suggested": 8340,
      "total_lines_accepted": 6120
    },
    {
      "event_date": "2025-01-16",
      "total_suggestions": 4980,
      "total_accepts": 3050,
      "total_rejects": 1930,
      "total_green_lines_accepted": 3890,
      "total_red_lines_accepted": 1890,
      "total_green_lines_rejected": 1350,
      "total_red_lines_rejected": 580,
      "total_green_lines_suggested": 5240,
      "total_red_lines_suggested": 2650,
      "total_lines_suggested": 7890,
      "total_lines_accepted": 5780
    }
  ],
  "params": {
    "metric": "tabs",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Daily Active Users (DAU)](#daily-active-users-dau)

GET `/analytics/team/dau`

Get daily active user counts for your team. DAU is the number of unique users who have used Cursor in a given day. An active user is a user who has used at least one AI feature in the Cursor IDE.

Response includes DAU breakdown metrics for the Cursor CLI, Cloud Agents, and BugBot.

#### [Parameters](#parameters-2)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/dau?startDate=14d&endDate=today" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "date": "2025-01-15",
      "dau": 42,
      "cli_dau": 5,
      "cloud_agent_dau": 37,
      "bugbot_dau": 10
    },
    {
      "date": "2025-01-16",
      "dau": 38,
      "cli_dau": 4,
      "cloud_agent_dau": 34,
      "bugbot_dau": 12
    }
  ],
  "params": {
    "metric": "dau",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Client Versions](#client-versions)

GET `/analytics/team/client-versions`

Get distribution of Cursor IDE client versions used by your team (defaults to last 7 days). We report the latest version for each user per day (if a user has installed multiple versions, we report the latest).

#### [Parameters](#parameters-3)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/client-versions" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-01",
      "client_version": "0.42.3",
      "user_count": 35,
      "percentage": 0.833
    },
    {
      "event_date": "2025-01-01",
      "client_version": "0.42.2",
      "user_count": 7,
      "percentage": 0.167
    }
  ],
  "params": {
    "metric": "client-versions",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Model Usage](#model-usage)

GET `/analytics/team/models`

Get metrics on AI model usage across your team.

#### [Parameters](#parameters-4)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/models" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "date": "2025-01-15",
      "model_breakdown": {
        "claude-sonnet-4.5": {
          "messages": 1250,
          "users": 28
        },
        "gpt-4o": {
          "messages": 450,
          "users": 15
        },
        "claude-opus-4": {
          "messages": 320,
          "users": 12
        }
      }
    },
    {
      "date": "2025-01-16",
      "model_breakdown": {
        "claude-sonnet-4.5": {
          "messages": 1180,
          "users": 26
        },
        "gpt-4o": {
          "messages": 420,
          "users": 14
        }
      }
    }
  ],
  "params": {
    "metric": "models",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Top File Extensions](#top-file-extensions)

GET `/analytics/team/top-file-extensions`

Get the most frequently edited files across your team in the Cursor IDE. Returns the top 5 file extensions per day by suggestion volume.

#### [Parameters](#parameters-5)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/top-file-extensions?startDate=30d&endDate=today" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-15",
      "file_extension": "tsx",
      "total_files": 156,
      "total_accepts": 98,
      "total_rejects": 45,
      "total_lines_suggested": 3230,
      "total_lines_accepted": 2340,
      "total_lines_rejected": 890
    },
    {
      "event_date": "2025-01-15",
      "file_extension": "ts",
      "total_files": 142,
      "total_accepts": 89,
      "total_rejects": 38,
      "total_lines_suggested": 2850,
      "total_lines_accepted": 2100,
      "total_lines_rejected": 750
    }
  ],
  "params": {
    "metric": "top-file-extensions",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [MCP Adoption](#mcp-adoption)

GET `/analytics/team/mcp`

Get metrics on MCP (Model Context Protocol) tool adoption across your team. Returns daily adoption counts broken down by tool name and MCP server name.

#### [Parameters](#parameters-6)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/mcp" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-15",
      "tool_name": "read_file",
      "mcp_server_name": "filesystem",
      "usage": 245
    },
    {
      "event_date": "2025-01-15",
      "tool_name": "search_web",
      "mcp_server_name": "brave-search",
      "usage": 128
    },
    {
      "event_date": "2025-01-16",
      "tool_name": "read_file",
      "mcp_server_name": "filesystem",
      "usage": 231
    }
  ],
  "params": {
    "metric": "mcp",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Commands Adoption](#commands-adoption)

GET `/analytics/team/commands`

Get metrics on Cursor command adoption across your team. Returns daily adoption counts broken down by command name.

#### [Parameters](#parameters-7)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/commands" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-15",
      "command_name": "explain",
      "usage": 89
    },
    {
      "event_date": "2025-01-15",
      "command_name": "refactor",
      "usage": 45
    },
    {
      "event_date": "2025-01-16",
      "command_name": "explain",
      "usage": 92
    }
  ],
  "params": {
    "metric": "commands",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Plans Adoption](#plans-adoption)

GET `/analytics/team/plans`

Get metrics on Plan mode adoption across your team. Returns daily adoption counts broken down by AI model used for plan generation.

#### [Parameters](#parameters-8)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/plans" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-15",
      "model": "claude-sonnet-4.5",
      "usage": 156
    },
    {
      "event_date": "2025-01-15",
      "model": "gpt-4o",
      "usage": 42
    },
    {
      "event_date": "2025-01-16",
      "model": "claude-sonnet-4.5",
      "usage": 148
    }
  ],
  "params": {
    "metric": "plans",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Ask Mode Adoption](#ask-mode-adoption)

GET `/analytics/team/ask-mode`

Get metrics on Ask mode adoption across your team. Returns daily adoption counts broken down by AI model used for Ask mode queries.

#### [Parameters](#parameters-9)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`users` string

Filter data to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/team/ask-mode" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": [
    {
      "event_date": "2025-01-15",
      "model": "claude-sonnet-4.5",
      "usage": 203
    },
    {
      "event_date": "2025-01-15",
      "model": "gpt-4o",
      "usage": 67
    },
    {
      "event_date": "2025-01-16",
      "model": "claude-sonnet-4.5",
      "usage": 198
    }
  ],
  "params": {
    "metric": "ask-mode",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31"
  }
}
```

### [Leaderboard](#leaderboard)

GET `/analytics/team/leaderboard`

Get a leaderboard of team members ranked by AI usage metrics.

**Behavior:**

-   **Without user filtering**: Returns users ranked by the specified metric (default: combined lines accepted)
-   **With user filtering**: Returns users that match the filter (with their actual team-wide rankings)
-   Supports pagination for teams with many members

#### [Parameters](#parameters-10)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`page` number

Page number for pagination (1-indexed). Default: `1`

`pageSize` number

Number of users per page (default: 10, max: 500)

`users` string

Filter to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

Returns separate leaderboards for Tab autocomplete and Agent edits. When filtering by users, those users appear with their **actual team-wide rank**, not a filtered rank. For example, if you request a user who ranks #45 overall, they'll appear with `rank: 45`.

```
# Get first page of leaderboard (top 10 users)
curl -X GET "https://api.cursor.com/analytics/team/leaderboard" \
  -u YOUR_API_KEY:
```

```
# Get second page with custom page size
curl -X GET "https://api.cursor.com/analytics/team/leaderboard?page=2&pageSize=20" \
  -u YOUR_API_KEY:
```

```
# Filter by specific users
curl -X GET "https://api.cursor.com/analytics/team/leaderboard?users=alice@example.com,bob@example.com" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": {
    "tab_leaderboard": {
      "data": [
        {
          "email": "alice@example.com",
          "user_id": "user_abc123",
          "total_accepts": 1334,
          "total_lines_accepted": 3455,
          "total_lines_suggested": 15307,
          "line_acceptance_ratio": 0.226,
          "accept_ratio": 0.233,
          "rank": 1
        },
        {
          "email": "bob@example.com",
          "user_id": "user_def789",
          "total_accepts": 796,
          "total_lines_accepted": 2090,
          "total_lines_suggested": 7689,
          "line_acceptance_ratio": 0.272,
          "accept_ratio": 0.273,
          "rank": 2
        }
      ],
      "total_users": 142
    },
    "agent_leaderboard": {
      "data": [
        {
          "email": "alice@example.com",
          "user_id": "user_abc123",
          "total_accepts": 914,
          "total_lines_accepted": 65947,
          "total_lines_suggested": 201467,
          "line_acceptance_ratio": 0.327,
          "favorite_model": "claude-sonnet-4.5",
          "rank": 1
        },
        {
          "email": "bob@example.com",
          "user_id": "user_def789",
          "total_accepts": 843,
          "total_lines_accepted": 61709,
          "total_lines_suggested": 51092,
          "line_acceptance_ratio": 1.208,
          "favorite_model": "claude-sonnet-4.5",
          "rank": 2
        }
      ],
      "total_users": 142
    }
  },
  "pagination": {
    "page": 1,
    "pageSize": 10,
    "totalUsers": 142,
    "totalPages": 15,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "leaderboard",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 10
  }
}
```

---

## [By-User Endpoints](#by-user-endpoints)

By-user endpoints provide the same metrics as team-level endpoints, but organized by individual users with pagination support. These are ideal for generating per-user reports or processing large teams in batches.

### [Common Query Parameters](#common-query-parameters)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Parameter</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Required</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">startDate</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Date string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Start date for the analytics period (default: 7 days ago)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">endDate</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Date string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">End date for the analytics period (default: today)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">page</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Page number (default: 1)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">pageSize</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">number</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Number of users per page (default: 100, max: 500)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">users</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Limit pagination to specific users (comma-separated emails or IDs, e.g., <code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">alice@example.com,user_abc123</code>)</td></tr></tbody></table>

**User Filtering:** When you provide the `users` parameter to by-user endpoints:

-   **Pagination is filtered**: Only the specified users are included in the result set and pagination counts
-   **Useful for**: Getting detailed data for specific team members without paginating through all users
-   Example: If you have 500 users but only want data for 3 specific users, filter by their emails to get all 3 in a single page

**Note:** By-user endpoints support the same date formats and shortcuts as team-level endpoints. See the [Date Formats](#date-formats) section above.

### [Response Format](#response-format)

All by-user endpoints return data in this format:

```
{
  "data": {
    "user1@example.com": [ /* user's data */ ],
    "user2@example.com": [ /* user's data */ ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 100,
    "totalUsers": 250,
    "totalPages": 3,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "agent-edits",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 100,
    "userMappings": [
      { "id": "user_abc123", "email": "user1@example.com" },
      { "id": "user_def456", "email": "user2@example.com" }
    ]
  }
}
```

**Response Structure:**

-   `data` - Object keyed by user email addresses, each containing an array of that user's metrics
-   `pagination` - Pagination information
-   `params` - Request parameters echoed back
    -   `userMappings` - Array mapping email addresses to public user IDs for this page. Useful for cross-referencing with other APIs or creating links to user profiles.

### [Available Endpoints](#available-endpoints-1)

All by-user endpoints follow the pattern: `/analytics/by-user/{metric}`

-   `GET /analytics/by-user/agent-edits` - Agent edits by user
-   `GET /analytics/by-user/tabs` - Tab usage by user
-   `GET /analytics/by-user/models` - Model usage by user
-   `GET /analytics/by-user/top-file-extensions` - Top files by user
-   `GET /analytics/by-user/client-versions` - Client versions by user
-   `GET /analytics/by-user/mcp` - MCP adoption by user
-   `GET /analytics/by-user/commands` - Commands adoption by user
-   `GET /analytics/by-user/plans` - Plans adoption by user
-   `GET /analytics/by-user/ask-mode` - Ask mode adoption by user

### [Agent Edits By User](#agent-edits-by-user)

GET `/analytics/by-user/agent-edits`

Get agent edits metrics organized by individual users with pagination support.

#### [Parameters](#parameters-11)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Number of users per page (default: 100, max: 500)

`users` string

Limit pagination to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/by-user/agent-edits?page=1&pageSize=50" \
  -u YOUR_API_KEY:
```

```
curl -X GET "https://api.cursor.com/analytics/by-user/agent-edits?users=alice@example.com,bob@example.com,carol@example.com" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": {
    "alice@example.com": [
      {
        "event_date": "2025-01-15",
        "suggested_lines": 125,
        "accepted_lines": 98
      },
      {
        "event_date": "2025-01-16",
        "suggested_lines": 110,
        "accepted_lines": 89
      }
    ],
    "bob@example.com": [
      {
        "event_date": "2025-01-15",
        "suggested_lines": 95,
        "accepted_lines": 72
      },
      {
        "event_date": "2025-01-16",
        "suggested_lines": 88,
        "accepted_lines": 65
      }
    ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 50,
    "totalUsers": 120,
    "totalPages": 3,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "agent-edits",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 50,
    "userMappings": [
      { "id": "user_abc123", "email": "alice@example.com" },
      { "id": "user_def456", "email": "bob@example.com" }
    ]
  }
}
```

### [MCP Adoption By User](#mcp-adoption-by-user)

GET `/analytics/by-user/mcp`

Get MCP tool adoption metrics organized by individual users with pagination support.

#### [Parameters](#parameters-12)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Number of users per page (default: 100, max: 500)

`users` string

Limit pagination to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/by-user/mcp?page=1&pageSize=50" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": {
    "alice@example.com": [
      {
        "event_date": "2025-01-15",
        "tool_name": "read_file",
        "mcp_server_name": "filesystem",
        "usage": 45
      },
      {
        "event_date": "2025-01-16",
        "tool_name": "read_file",
        "mcp_server_name": "filesystem",
        "usage": 38
      }
    ],
    "bob@example.com": [
      {
        "event_date": "2025-01-15",
        "tool_name": "search_web",
        "mcp_server_name": "brave-search",
        "usage": 23
      }
    ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 50,
    "totalUsers": 120,
    "totalPages": 3,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "mcp",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 50,
    "userMappings": [
      { "id": "user_abc123", "email": "alice@example.com" },
      { "id": "user_def456", "email": "bob@example.com" }
    ]
  }
}
```

### [Commands Adoption By User](#commands-adoption-by-user)

GET `/analytics/by-user/commands`

Get command adoption metrics organized by individual users with pagination support.

#### [Parameters](#parameters-13)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Number of users per page (default: 100, max: 500)

`users` string

Limit pagination to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/by-user/commands?page=1&pageSize=50" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": {
    "alice@example.com": [
      {
        "event_date": "2025-01-15",
        "command_name": "explain",
        "usage": 12
      },
      {
        "event_date": "2025-01-16",
        "command_name": "explain",
        "usage": 15
      }
    ],
    "bob@example.com": [
      {
        "event_date": "2025-01-15",
        "command_name": "refactor",
        "usage": 8
      }
    ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 50,
    "totalUsers": 120,
    "totalPages": 3,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "commands",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 50,
    "userMappings": [
      { "id": "user_abc123", "email": "alice@example.com" },
      { "id": "user_def456", "email": "bob@example.com" }
    ]
  }
}
```

### [Plans Adoption By User](#plans-adoption-by-user)

GET `/analytics/by-user/plans`

Get Plan mode adoption metrics organized by individual users with pagination support.

#### [Parameters](#parameters-14)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Number of users per page (default: 100, max: 500)

`users` string

Limit pagination to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/by-user/plans?page=1&pageSize=50" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": {
    "alice@example.com": [
      {
        "event_date": "2025-01-15",
        "model": "claude-sonnet-4.5",
        "usage": 23
      },
      {
        "event_date": "2025-01-16",
        "model": "claude-sonnet-4.5",
        "usage": 19
      }
    ],
    "bob@example.com": [
      {
        "event_date": "2025-01-15",
        "model": "gpt-4o",
        "usage": 12
      }
    ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 50,
    "totalUsers": 120,
    "totalPages": 3,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "plans",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 50,
    "userMappings": [
      { "id": "user_abc123", "email": "alice@example.com" },
      { "id": "user_def456", "email": "bob@example.com" }
    ]
  }
}
```

### [Ask Mode Adoption By User](#ask-mode-adoption-by-user)

GET `/analytics/by-user/ask-mode`

Get Ask mode adoption metrics organized by individual users with pagination support.

#### [Parameters](#parameters-15)

`startDate` string

Start date for analytics period (default: 7 days ago). See [Date Formats](#date-formats)

`endDate` string

End date for analytics period (default: today). See [Date Formats](#date-formats)

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Number of users per page (default: 100, max: 500)

`users` string

Limit pagination to specific users (comma-separated emails or user IDs, e.g., `alice@example.com,user_abc123`)

```
curl -X GET "https://api.cursor.com/analytics/by-user/ask-mode?page=1&pageSize=50" \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "data": {
    "alice@example.com": [
      {
        "event_date": "2025-01-15",
        "model": "claude-sonnet-4.5",
        "usage": 34
      },
      {
        "event_date": "2025-01-16",
        "model": "claude-sonnet-4.5",
        "usage": 28
      }
    ],
    "bob@example.com": [
      {
        "event_date": "2025-01-15",
        "model": "gpt-4o",
        "usage": 15
      }
    ]
  },
  "pagination": {
    "page": 1,
    "pageSize": 50,
    "totalUsers": 120,
    "totalPages": 3,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "ask-mode",
    "teamId": 12345,
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "page": 1,
    "pageSize": 50,
    "userMappings": [
      { "id": "user_abc123", "email": "alice@example.com" },
      { "id": "user_def456", "email": "bob@example.com" }
    ]
  }
}
```

---

## [Team-Level Endpoints](#team-level-endpoints)

Team-level endpoints provide aggregated metrics for your entire team or filtered subsets of users. All endpoints support date range filtering and optional user filtering.

### [Common Query Parameters](#common-query-parameters-1)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Parameter</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Required</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">startDate</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Date string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Start date for the analytics period (default: 7 days ago)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">endDate</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Date string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">End date for the analytics period (default: today)</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">users</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">string</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">No</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Filter data to specific users (comma-separated). Each value can be an email (e.g., <code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">alice@example.com</code>) or public user ID (e.g., <code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">user_abc123</code>). You can mix both formats.</td></tr></tbody></table>

**User Filtering:** The `users` parameter accepts a comma-separated list of identifiers. Each identifier can be:

-   **Email address** (e.g., `alice@example.com`) - Auto-detected by the presence of `@`
-   **Public user ID** (e.g., `user_abc123`) - Auto-detected by the `user_` prefix
-   **Mixed format** - You can combine emails and IDs in the same request

**Examples:**

```
# Filter by emails only
?users=alice@example.com,bob@example.com,carol@example.com

# Filter by public user IDs only
?users=user_abc123,user_def456,user_ghi789

# Mix emails and IDs
?users=alice@example.com,user_def456,bob@example.com
```

When you filter by users, the API returns data **only for those specific users**. This is useful for:

-   Analyzing specific team members or groups (e.g., engineering leads, specific project teams)
-   Generating reports for a subset of users
-   Comparing metrics across selected individuals

### [Date Formats](#date-formats)

**Default Behavior:** If you omit both `startDate` and `endDate`, the API defaults to the **last 7 days** (from 7 days ago until today). This is perfect for quick queries without specifying dates.

**Standard Formats:**

-   `YYYY-MM-DD` - Simple date format (e.g., `2025-01-15`) **← Recommended**
-   ISO 8601 timestamps (e.g., `2025-01-15T00:00:00Z`)

**Shortcuts:**

-   `now` or `today` - Current date (at 00:00:00)
-   `yesterday` - Yesterday's date (at 00:00:00)
-   `<number>d` - Days ago (e.g., `7d` = 7 days ago, `30d` = 30 days ago)

**Important Notes:**

-   **Time is ignored**: All dates are resolved to the day level (00:00:00 UTC). Sending `2025-01-15T14:30:00Z` is the same as `2025-01-15`.
-   **Use recommended formats**: Use `YYYY-MM-DD` or shortcuts for better HTTP caching support. Different time values (like `T14:30:00Z` vs `T08:00:00Z`) prevent cache hits even though they resolve to the same day.
-   **Date ranges**: Limited to a maximum of 30 days.

**Examples:**

```
# Omit dates for last 7 days (simplest and best for caching)
curl "https://api.cursor.com/analytics/team/agent-edits"

# Using YYYY-MM-DD format for specific date range (recommended)
?startDate=2025-01-01&endDate=2025-01-31

# Using shortcuts for last 30 days
?startDate=30d&endDate=today

# Using shortcuts for last 14 days
?startDate=14d&endDate=now

# ❌ Don't use timestamps - prevents caching and time is ignored anyway
?startDate=2025-01-15T14:30:00Z&endDate=2025-01-31T23:59:59Z
```

## [Rate Limits](#rate-limits)

Rate limits are enforced per team and reset every minute:

-   **Team-level endpoints**: 100 requests per minute per team
-   **By-user endpoints**: 50 requests per minute per team

**What happens when you exceed the rate limit?**

When you exceed the rate limit, you'll receive a `429 Too Many Requests` response:

```
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

## [Best Practices](#best-practices)

For general API best practices including exponential backoff, caching strategies, and error handling, see the [API Overview Best Practices](/docs/api#best-practices).

1.  **Use pagination for large teams**: If your team has more than 100 users, use the by-user endpoints with pagination to avoid timeouts.
2.  **Leverage caching**: Both Team and User level endpoints support ETags. Store the ETag and use `If-None-Match` headers to reduce unnecessary data transfer.
3.  **Filter by users when possible**: If you only need data for specific users, use the `users` parameter to reduce query time.
4.  **Date ranges**: Keep date ranges reasonable (e.g., 1-3 months) for optimal performance.

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---

### Bugbot

Source: https://cursor.com/docs/bugbot

Endpoints found on this page:

- `POST /bugbot/repo/update`

Core

# Bugbot

Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.

On Teams and Individual Plans, Bugbot includes a free tier: every user gets a limited number of free PR reviews each month. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to a 14‑day free Pro trial for unlimited reviews (subject to standard abuse guardrails).

## [How it works](#how-it-works)

Bugbot analyzes PR diffs and leaves comments with explanations and fix suggestions. It runs automatically on each PR update or manually when triggered.

-   Runs **automatic reviews** on every PR update
-   **Manual trigger** by commenting `cursor review` or `bugbot run` on any PR
-   **Uses existing PR comments as context**: reads GitHub PR comments (top‑level and inline) to avoid duplicate suggestions and build on prior feedback
-   **Fix in Cursor** links open issues directly in Cursor
-   **Fix in Web** links open issues directly in [cursor.com/agents](https://cursor.com/agents)

## [Setup](#setup)

GitHub.comGitLab.comGitHub Enterprise ServerGitLab Self-Hosted

Requires Cursor admin access and GitHub org admin access.

1.  Go to [cursor.com/dashboard](https://cursor.com/dashboard?tab=integrations)
2.  Navigate to the Integrations tab
3.  Click `Connect GitHub` (or `Manage Connections` if already connected)
4.  Follow the GitHub installation flow
5.  Return to the dashboard to enable Bugbot on specific repositories

## [Configuration](#configuration)

IndividualTeam

### [Repository settings](#repository-settings-1)

Team admins can enable Bugbot per repository, configure allow/deny lists for reviewers, and set:

-   Run **only once** per PR per installation, skipping subsequent commits
-   **Disable inline reviews** to prevent Bugbot from leaving comments directly on code lines

Bugbot runs for all contributors to enabled repositories, regardless of team membership.

### [Personal settings](#personal-settings-1)

Team members can override settings for their own PRs:

-   Run **only when mentioned** by commenting `cursor review` or `bugbot run`
-   Run **only once** per PR, skipping subsequent commits
-   **Enable reviews on draft PRs** to include draft pull requests in automatic reviews

### [Analytics](#analytics)

![Bugbot dashboard](/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fbugbot%2Fbugbot-dashboard.png&w=1920&q=75)

## [Rules](#rules)

Create `.cursor/BUGBOT.md` files to provide project-specific context for reviews. Bugbot always includes the root `.cursor/BUGBOT.md` file and any additional files found while traversing upward from changed files.

```
project/
  .cursor/BUGBOT.md          # Always included (project-wide rules)
  backend/
    .cursor/BUGBOT.md        # Included when reviewing backend files
    api/
      .cursor/BUGBOT.md      # Included when reviewing API files
  frontend/
    .cursor/BUGBOT.md        # Included when reviewing frontend files
```

### [Team rules](#team-rules)

Team admins can create rules from the [Bugbot dashboard](https://cursor.com/dashboard?tab=bugbot) that apply to all repositories in the team. These rules are available to every enabled repository, making it easy to enforce organization-wide standards.

When both Team Rules and project rule files (`.cursor/BUGBOT.md`) exist, Bugbot uses both. They are applied in this order: **Team Rules → project BUGBOT.md (including nested files) → User Rules**.

### [Examples](#examples)

### 

Security: Flag any use of eval() or exec()

### 

OSS licenses: Prevent importing disallowed licenses

### 

Language standards: Flag React componentWillMount usage

### 

Standards: Require tests for backend changes

### 

Style: Disallow TODO comments

## [Admin Configuration API](#admin-configuration-api)

Team admins can use the Bugbot Admin API to programmatically enable or disable Bugbot on repositories. This is useful for automating repository management or enabling Bugbot on large numbers of repositories at once.

### [Creating an API Key](#creating-an-api-key)

1.  Visit the [Settings tab in the Cursor dashboard](https://cursor.com/dashboard?tab=settings)
2.  Under **Advanced**, click **New Admin API Key**
3.  Save the API key

### [Enabling or Disabling Repositories](#enabling-or-disabling-repositories)

Use the `/bugbot/repo/update` endpoint to toggle Bugbot on or off for a repository:

```
curl -X POST https://api.cursor.com/bugbot/repo/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "repoUrl": "https://github.com/your-org/your-repo",
    "enabled": true
  }'
```

**Parameters:**

-   `repoUrl` (string, required): The full URL of the repository
-   `enabled` (boolean, required): `true` to enable Bugbot, `false` to disable it

The dashboard UI may take a moment to reflect changes made through the API due to caching. The API response shows the current state in the database.

## [Pricing](#pricing)

Bugbot offers two tiers: **Free** and **Pro**.

### [Free tier](#free-tier)

On Teams and Individual Cursor plans, every user gets a limited number of free PR reviews each month. For teams, each team member gets their own free reviews. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to a paid Bugbot plan for unlimited reviews.

### [Pro tier](#pro-tier)

IndividualsTeams

### [Per-user billing](#per-user-billing)

Teams pay $40 per user per month for unlimited reviews.

We count a user as someone who authored PRs reviewed by Bugbot in a month.

All licenses are relinquished at the start of each billing cycle, and will be assigned out on a first-come, first-served basis. If a user doesn't author any PRs reviewed by Bugbot in a month, the seat can be used by another user.

### [Seat limits](#seat-limits)

Team admins can set maximum Bugbot seats per month to control costs.

### [Getting started](#getting-started-1)

Subscribe through your team dashboard to enable billing.

### [Abuse guardrails](#abuse-guardrails)

In order to prevent abuse, we have a pooled cap of 200 pull requests per month for every Bugbot license. If you need more than 200 pull requests per month, please contact us at [hi@cursor.com](mailto:hi@cursor.com) and we'll be happy to help you out.

For example, if your team has 100 users, your organization will initially be able to review 20,000 pull requests per month. If you reach that limit naturally, please reach out to us and we'll be happy to increase the limit.

## [Troubleshooting](#troubleshooting)

If Bugbot isn't working:

1.  **Enable verbose mode** by commenting `cursor review verbose=true` or `bugbot run verbose=true` for detailed logs and request ID
2.  **Check permissions** to verify Bugbot has repository access
3.  **Verify installation** to confirm the GitHub app is installed and enabled

Include the request ID from verbose mode when reporting issues.

## [FAQ](#faq)

### 

Does Bugbot read GitHub PR comments?

### 

Is Bugbot privacy-mode compliant?

### 

What happens when I hit the free tier limit?

### 

How do I give Bugbot access to my GitLab or GitHub Enterprise Server instance?

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---

### Cloud Agents API

Source: https://cursor.com/docs/cloud-agent/api/endpoints

Endpoints found on this page:

- `GET /v0/agents`
- `GET /v0/agents/{id}`
- `GET /v0/agents/{id}/conversation`
- `GET /v0/me`
- `GET /v0/models`
- `GET /v0/repositories`
- `POST /v0/agents`
- `POST /v0/agents/{id}/followup`
- `POST /v0/agents/{id}/stop`
- `DELETE /v0/agents/{id}`

# Cloud Agents API

The Cloud Agents API lets you programmatically launch and manage cloud agents that work on your repositories.

-   The Cloud Agents API uses [Basic Authentication](/docs/api#basic-authentication). You can obtain an API key from your [Cursor Dashboard](https://cursor.com/settings).
-   For details on authentication methods, rate limits, and best practices, see the [API Overview](/docs/api).
-   View the full [OpenAPI specification](/docs-static/cloud-agents-openapi.yaml) for detailed schemas and examples.
-   MCP (Model Context Protocol) is not yet supported by the Cloud Agents API.

## [Endpoints](#endpoints)

### [List Agents](#list-agents)

GET `/v0/agents`

List all cloud agents for the authenticated user.

#### [Query Parameters](#query-parameters)

`limit` number (optional)

Number of cloud agents to return. Default: 20, Max: 100

`cursor` string (optional)

Pagination cursor from the previous response

```
curl --request GET \
  --url https://api.cursor.com/v0/agents \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "agents": [
    {
      "id": "bc_abc123",
      "name": "Add README Documentation",
      "status": "FINISHED",
      "source": {
        "repository": "https://github.com/your-org/your-repo",
        "ref": "main"
      },
      "target": {
        "branchName": "cursor/add-readme-1234",
        "url": "https://cursor.com/agents?id=bc_abc123",
        "prUrl": "https://github.com/your-org/your-repo/pull/1234",
        "autoCreatePr": false,
        "openAsCursorGithubApp": false,
        "skipReviewerRequest": false
      },
      "summary": "Added README.md with installation instructions and usage examples",
      "createdAt": "2024-01-15T10:30:00Z"
    },
    {
      "id": "bc_def456",
      "name": "Fix authentication bug",
      "status": "RUNNING",
      "source": {
        "repository": "https://github.com/your-org/your-repo",
        "ref": "main"
      },
      "target": {
        "branchName": "cursor/fix-auth-5678",
        "url": "https://cursor.com/agents?id=bc_def456",
        "autoCreatePr": true,
        "openAsCursorGithubApp": true,
        "skipReviewerRequest": false
      },
      "createdAt": "2024-01-15T11:45:00Z"
    }
  ],
  "nextCursor": "bc_ghi789"
}
```

### [Agent Status](#agent-status)

GET `/v0/agents/{id}`

Retrieve the current status and results of a cloud agent.

#### [Path Parameters](#path-parameters)

`id` string

Unique identifier for the cloud agent (e.g., bc\_abc123)

```
curl --request GET \
  --url https://api.cursor.com/v0/agents/bc_abc123 \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "id": "bc_abc123",
  "name": "Add README Documentation",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "branchName": "cursor/add-readme-1234",
    "url": "https://cursor.com/agents?id=bc_abc123",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234",
    "autoCreatePr": false,
    "openAsCursorGithubApp": false,
    "skipReviewerRequest": false
  },
  "summary": "Added README.md with installation instructions and usage examples",
  "createdAt": "2024-01-15T10:30:00Z"
}
```

### [Agent Conversation](#agent-conversation)

GET `/v0/agents/{id}/conversation`

Retrieve the conversation history of a cloud agent, including all user prompts and assistant responses.

If the cloud agent has been deleted, you cannot access the conversation.

#### [Path Parameters](#path-parameters-1)

`id` string

Unique identifier for the cloud agent (e.g., `bc_abc123`)

```
curl --request GET \
  --url https://api.cursor.com/v0/agents/bc_abc123/conversation \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "id": "bc_abc123",
  "messages": [
    {
      "id": "msg_001",
      "type": "user_message",
      "text": "Add a README.md file with installation instructions"
    },
    {
      "id": "msg_002",
      "type": "assistant_message",
      "text": "I'll help you create a comprehensive README.md file with installation instructions. Let me start by analyzing your project structure..."
    },
    {
      "id": "msg_003",
      "type": "assistant_message",
      "text": "I've created a README.md file with the following sections:\n- Project overview\n- Installation instructions\n- Usage examples\n- Configuration options"
    },
    {
      "id": "msg_004",
      "type": "user_message",
      "text": "Also add a section about troubleshooting"
    },
    {
      "id": "msg_005",
      "type": "assistant_message",
      "text": "I've added a troubleshooting section to the README with common issues and solutions."
    }
  ]
}
```

### [Launch an Agent](#launch-an-agent)

POST `/v0/agents`

Start a new cloud agent to work on your repository.

#### [Request Body](#request-body)

`prompt` object (required)

The task prompt for the agent, including optional images

`prompt.text` string (required)

The instruction text for the agent

`prompt.images` array (optional)

Array of image objects with base64 data and dimensions (max 5)

`model` string (optional)

The LLM to use (e.g., claude-4-sonnet). If not provided, we'll pick the most appropriate model.

`source` object (required)

Repository source information

`source.repository` string (required)

GitHub repository URL (e.g., [https://github.com/your-org/your-repo](https://github.com/your-org/your-repo))

`source.ref` string (optional)

Git ref (branch name, tag, or commit hash) to use as the base branch

`target` object (optional)

Target configuration for the agent

`target.autoCreatePr` boolean (optional)

Whether to automatically create a pull request when the agent completes. Default: false

`target.openAsCursorGithubApp` boolean (optional)

Whether to open the pull request as the Cursor GitHub App instead of as the user. Only applies if autoCreatePr is true. Default: false

`target.skipReviewerRequest` boolean (optional)

Whether to skip adding the user as a reviewer to the pull request. Only applies if autoCreatePr is true and the PR is opened as the Cursor GitHub App. Default: false

`target.branchName` string (optional)

Custom branch name for the agent to create

`webhook` object (optional)

[Webhook](/docs/cloud-agent/api/webhooks) configuration for status change notifications

`webhook.url` string (required if webhook provided)

URL to receive [webhook](/docs/cloud-agent/api/webhooks) notifications about agent status changes

`webhook.secret` string (optional)

Secret key for [webhook](/docs/cloud-agent/api/webhooks) payload verification (minimum 32 characters)

```
curl --request POST \
  --url https://api.cursor.com/v0/agents \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
  "prompt": {
    "text": "Add a README.md file with installation instructions",
    "images": [
      {
        "data": "iVBORw0KGgoAAAANSUhEUgAA...",
        "dimension": {
          "width": 1024,
          "height": 768
        }
      }
    ]
  },
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "autoCreatePr": true,
    "branchName": "feature/add-readme"
  }
}'
```

**Response:**

```
{
  "id": "bc_abc123",
  "name": "Add README Documentation",
  "status": "CREATING",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "branchName": "feature/add-readme",
    "url": "https://cursor.com/agents?id=bc_abc123",
    "autoCreatePr": true,
    "openAsCursorGithubApp": false,
    "skipReviewerRequest": false
  },
  "createdAt": "2024-01-15T10:30:00Z"
}
```

### [Add Follow-up](#add-follow-up)

POST `/v0/agents/{id}/followup`

Add a follow-up instruction to an existing cloud agent.

#### [Path Parameters](#path-parameters-2)

`id` string

Unique identifier for the cloud agent (e.g., bc\_abc123)

#### [Request Body](#request-body-1)

`prompt` object (required)

The follow-up prompt for the agent, including optional images

`prompt.text` string (required)

The follow-up instruction text for the agent

`prompt.images` array (optional)

Array of image objects with base64 data and dimensions (max 5)

```
curl --request POST \
  --url https://api.cursor.com/v0/agents/bc_abc123/followup \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
  "prompt": {
    "text": "Also add a section about troubleshooting",
    "images": [
      {
        "data": "iVBORw0KGgoAAAANSUhEUgAA...",
        "dimension": {
          "width": 1024,
          "height": 768
        }
      }
    ]
  }
}'
```

**Response:**

```
{
  "id": "bc_abc123"
}
```

### [Stop an Agent](#stop-an-agent)

POST `/v0/agents/{id}/stop`

Stop a running cloud agent. This pauses the agent's execution without deleting it.

You can only stop agents that are currently running. If you send a follow-up prompt to a stopped agent, it will start running again.

#### [Path Parameters](#path-parameters-3)

`id` string

Unique identifier for the cloud agent (e.g., `bc_abc123`)

```
curl --request POST \
  --url https://api.cursor.com/v0/agents/bc_abc123/stop \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "id": "bc_abc123"
}
```

### [Delete an Agent](#delete-an-agent)

DELETE `/v0/agents/{id}`

Delete a cloud agent. This action is permanent and cannot be undone.

#### [Path Parameters](#path-parameters-4)

`id` string

Unique identifier for the cloud agent (e.g., `bc_abc123`)

```
curl --request DELETE \
  --url https://api.cursor.com/v0/agents/bc_abc123 \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "id": "bc_abc123"
}
```

### [API Key Info](#api-key-info)

GET `/v0/me`

Retrieve information about the API key being used for authentication.

```
curl --request GET \
  --url https://api.cursor.com/v0/me \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "apiKeyName": "Production API Key",
  "createdAt": "2024-01-15T10:30:00Z",
  "userEmail": "developer@example.com"
}
```

### [List Models](#list-models)

GET `/v0/models`

Retrieve a list of recommended models for cloud agents.

We recommend having an "Auto" option where you don't provide a model name to the creation endpoint, and we will pick the most appropriate model.

```
curl --request GET \
  --url https://api.cursor.com/v0/models \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "models": [
    "claude-4-sonnet-thinking",
    "o3",
    "claude-4-opus-thinking"
  ]
}
```

### [List GitHub Repositories](#list-github-repositories)

GET `/v0/repositories`

Retrieve a list of GitHub repositories accessible to the authenticated user.

**This endpoint has very strict rate limits.**

Limit requests to **1 / user / minute**, and **30 / user / hour.**

This request can take tens of seconds to respond for users with access to many repositories.

Make sure to handle this information not being available gracefully.

```
curl --request GET \
  --url https://api.cursor.com/v0/repositories \
  -u YOUR_API_KEY:
```

**Response:**

```
{
  "repositories": [
    {
      "owner": "your-org",
      "name": "your-repo",
      "repository": "https://github.com/your-org/your-repo"
    },
    {
      "owner": "your-org",
      "name": "another-repo",
      "repository": "https://github.com/your-org/another-repo"
    },
    {
      "owner": "your-username",
      "name": "personal-project",
      "repository": "https://github.com/your-username/personal-project"
    }
  ]
}
```

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---

### Cursor APIs Overview

Source: https://cursor.com/docs/api

# Cursor APIs Overview

Cursor provides multiple APIs for programmatic access to your team's data, AI-powered coding agents, and analytics.

## [Available APIs](#available-apis)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">API</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Description</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Availability</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><a class="text-foreground underline decoration-neutral-600 underline-offset-2 transition-colors hover:decoration-neutral-700" href="/docs/account/teams/admin-api">Admin API</a></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Manage team members, settings, usage data, and spending. Build custom dashboards and monitoring tools.</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Enterprise teams</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><a class="text-foreground underline decoration-neutral-600 underline-offset-2 transition-colors hover:decoration-neutral-700" href="/docs/account/teams/analytics-api">Analytics API</a></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Comprehensive insights into team's Cursor usage, AI metrics, active users, and model usage.</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Enterprise teams</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><a class="text-foreground underline decoration-neutral-600 underline-offset-2 transition-colors hover:decoration-neutral-700" href="/docs/account/teams/ai-code-tracking-api">AI Code Tracking API</a></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Track AI-generated code contributions at commit and change levels for attribution and analytics.</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Enterprise teams</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><a class="text-foreground underline decoration-neutral-600 underline-offset-2 transition-colors hover:decoration-neutral-700" href="/docs/cloud-agent/api/endpoints">Cloud Agents API</a></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Programmatically create and manage AI-powered coding agents for automated workflows and code generation.</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Beta (All Plans)</td></tr></tbody></table>

## [Authentication](#authentication)

All Cursor APIs use Basic Authentication.

### [Basic Authentication](#basic-authentication)

Use your API key as the username in basic authentication (leave password empty):

```
curl https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

Or set the Authorization header directly:

```
Authorization: Basic {base64_encode('YOUR_API_KEY:')}
```

### [Creating API Keys](#creating-api-keys)

API keys are created from your team settings. Only team administrators can create and manage API keys.

#### [Admin API & AI Code Tracking API](#admin-api-ai-code-tracking-api)

1.  Navigate to **cursor.com/dashboard** → **Settings** tab → **Advanced** → **Admin API Keys**
2.  Click **Create New API Key**
3.  Give your key a descriptive name (e.g., "Usage Dashboard Integration")
4.  Copy the generated key immediately - you won't see it again

Key format: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

#### [Analytics API](#analytics-api)

Generate an API key from your [team settings page](https://cursor.com/settings).

#### [Cloud Agents API](#cloud-agents-api)

Create an API key from [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations).

API keys are tied to your organization and viewable by all admins. Keys are unaffected by the original creator's account status.

## [Rate Limits](#rate-limits)

All APIs implement rate limiting to ensure fair usage and system stability. Rate limits are enforced per team and reset every minute.

### [Rate Limits by API](#rate-limits-by-api)

<table class="min-w-full divide-y divide-neutral-200 bg-card dark:divide-muted dark:bg-card"><thead class="dark:text-neutral-300"><tr><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">API</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Endpoint Type</th><th class="whitespace-nowrap px-4 py-3 text-left font-medium text-xs" scope="col">Rate Limit</th></tr></thead><tbody class="divide-y divide-neutral-200 bg-background dark:divide-muted"><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><strong>Admin API</strong></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Most endpoints</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">20 requests/minute</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><strong>Admin API</strong></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><code class="rounded-sm border border-border bg-card/80 p-1 font-mono text-xs">/teams/user-spend-limit</code></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">60 requests/minute</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><strong>Analytics API</strong></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Team-level endpoints</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">100 requests/minute</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><strong>Analytics API</strong></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">By-user endpoints</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">50 requests/minute</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><strong>AI Code Tracking API</strong></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">All endpoints</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">20 requests/minute per endpoint</td></tr><tr><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100"><strong>Cloud Agents API</strong></td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">All endpoints</td><td class="px-4 py-3 text-neutral-900 text-base dark:text-neutral-100">Standard rate limiting</td></tr></tbody></table>

### [Rate Limit Response](#rate-limit-response)

When you exceed the rate limit, you'll receive a `429 Too Many Requests` response:

```
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

## [Caching](#caching)

Several APIs support HTTP caching with ETags to reduce bandwidth usage and improve performance.

### [Supported APIs](#supported-apis)

-   **Analytics API**: All endpoints (both team-level and by-user) support HTTP caching
-   **AI Code Tracking API**: Endpoints support HTTP caching

### [How Caching Works](#how-caching-works)

1.  **Initial Request**: Make a request to any supported endpoint
2.  **Response Includes ETag**: The API returns an `ETag` header in the response
3.  **Subsequent Requests**: Include the `ETag` value in an `If-None-Match` header
4.  **304 Not Modified**: If data hasn't changed, you'll receive a `304 Not Modified` response with no body

### [Example](#example)

```
# Initial request
curl -X GET "https://api.cursor.com/analytics/team/dau" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -D headers.txt

# Response includes: ETag: "abc123xyz"

# Subsequent request with ETag
curl -X GET "https://api.cursor.com/analytics/team/dau" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "If-None-Match: \"abc123xyz\""

# Returns 304 Not Modified if data hasn't changed
```

### [Cache Duration](#cache-duration)

-   Cache duration: 15 minutes (`Cache-Control: public, max-age=900`)
-   Responses include an `ETag` header
-   Include `If-None-Match` header in subsequent requests to receive `304 Not Modified` when data hasn't changed

### [Benefits](#benefits)

-   **Reduces bandwidth usage**: 304 responses contain no body
-   **Faster responses**: Avoids processing unchanged data
-   **Rate limit friendly**: 304 responses don't count against rate limits
-   **Better performance**: Especially useful for frequently polled endpoints

## [Best Practices](#best-practices)

### [1\. Implement Exponential Backoff](#1-implement-exponential-backoff)

When you receive a 429 response, wait before retrying with increasing delays:

```
import time
import requests

def make_request_with_backoff(url, headers, max_retries=5):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 429:
            # Exponential backoff: 1s, 2s, 4s, 8s, 16s
            wait_time = 2 ** attempt
            print(f"Rate limited. Waiting {wait_time}s before retry...")
            time.sleep(wait_time)
            continue
            
        return response
    
    raise Exception("Max retries exceeded")
```

### [2\. Distribute Requests Over Time](#2-distribute-requests-over-time)

Spread your API calls over time rather than making burst requests:

-   Schedule batch jobs to run at different intervals
-   Add delays between requests when processing large datasets
-   Use queuing systems to smooth out traffic spikes

### [3\. Leverage Caching](#3-leverage-caching)

**For Analytics API and AI Code Tracking API:**

These APIs support HTTP caching with ETags. See the [Caching](#caching) section above for details on how to use ETags to reduce bandwidth usage and avoid unnecessary requests.

**Key benefits:**

-   Reduces bandwidth usage
-   Faster responses when data hasn't changed
-   Doesn't count against rate limits (for 304 responses)

Use date shortcuts (`7d`, `30d`) instead of timestamps for better caching support in Analytics API.

### [4\. Monitor Your Usage](#4-monitor-your-usage)

Track your request patterns to stay within limits:

-   Log API call timestamps and response codes
-   Set up alerts for 429 responses
-   Monitor daily/weekly usage trends
-   Adjust polling intervals based on actual needs

### [5\. Batch Wisely](#5-batch-wisely)

For endpoints with pagination:

-   Use appropriate page sizes to get more data per request
-   For Analytics API by-user endpoints: Use `users` parameter to filter specific users
-   For large data extractions: Use CSV endpoints when available (they stream data efficiently)

### [6\. Poll at Appropriate Intervals](#6-poll-at-appropriate-intervals)

Don't over-poll endpoints that update infrequently:

-   **Admin API** `/teams/daily-usage-data`: Poll at most once per hour (data aggregated hourly)
-   **Admin API** `/teams/filtered-usage-events`: Poll at most once per hour (data aggregated hourly)
-   **Analytics API**: Use date shortcuts (`7d`, `30d`) for better caching support
-   **AI Code Tracking API**: Data is ingested in near real-time but polling every few minutes is sufficient

### [7\. Handle Errors Gracefully](#7-handle-errors-gracefully)

Implement proper error handling for all API calls:

```
async function fetchAnalytics(endpoint) {
  try {
    const response = await fetch(`https://api.cursor.com${endpoint}`, {
      headers: {
        'Authorization': `Basic ${btoa(API_KEY + ':')}`
      }
    });
    
    if (response.status === 429) {
      // Rate limited - implement backoff
      throw new Error('Rate limit exceeded');
    }
    
    if (response.status === 401) {
      // Invalid API key
      throw new Error('Authentication failed');
    }
    
    if (response.status === 403) {
      // Insufficient permissions
      throw new Error('Enterprise access required');
    }
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
}
```

## [Common Error Responses](#common-error-responses)

All APIs use standard HTTP status codes:

### [400 Bad Request](#400-bad-request)

Request parameters are invalid or missing required fields.

```
{
  "error": "Bad Request",
  "message": "Some users are not in the team"
}
```

### [401 Unauthorized](#401-unauthorized)

Invalid or missing API key.

```
{
  "error": "Unauthorized",
  "message": "Invalid API key"
}
```

### [403 Forbidden](#403-forbidden)

Valid API key but insufficient permissions (e.g., Enterprise features on non-Enterprise plan).

```
{
  "error": "Forbidden",
  "message": "Enterprise access required"
}
```

### [404 Not Found](#404-not-found)

Requested resource doesn't exist.

```
{
  "error": "Not Found",
  "message": "Resource not found"
}
```

### [429 Too Many Requests](#429-too-many-requests)

Rate limit exceeded. Implement exponential backoff.

```
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

### [500 Internal Server Error](#500-internal-server-error)

Server-side error. Contact support if persistent.

```
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred"
}
```

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---

### MCP Extension API Reference

Source: https://cursor.com/docs/context/mcp-extension-api

Context

# MCP Extension API Reference

The Cursor Extension API provides programmatic access to register and manage MCP servers without modifying `mcp.json` files directly. This is particularly useful for enterprise environments, onboarding tools, or MDM systems that need to dynamically configure MCP servers.

## [Overview](#overview)

The MCP Extension API allows you to:

-   Register MCP servers programmatically
-   Support both HTTP/SSE and stdio transport methods
-   Use the same configuration schema as `mcp.json`
-   Manage server registration dynamically

This API is useful for organizations that need to:

-   Deploy MCP configurations programmatically
-   Integrate MCP setup into onboarding workflows
-   Manage MCP servers through enterprise tools
-   Avoid manual `mcp.json` modifications

## [API Reference](#api-reference)

### [`vscode.cursor.mcp.registerServer`](#vscodecursormcpregisterserver)

Registers an MCP server that Cursor can communicate with.

**Signature:**

```
vscode.cursor.mcp.registerServer(config: ExtMCPServerConfig): void
```

**Parameters:**

-   `config: ExtMCPServerConfig` - The server configuration object

### [`vscode.cursor.mcp.unregisterServer`](#vscodecursormcpunregisterserver)

Unregisters a previously registered MCP server.

**Signature:**

```
vscode.cursor.mcp.unregisterServer(serverName: string): void
```

**Parameters:**

-   `serverName: string` - The name of the server to unregister

## [Type Definitions](#type-definitions)

Use these TypeScript definitions for type checking:

```
declare module "vscode" {
  export namespace cursor {
    export namespace mcp {
      export interface StdioServerConfig {
        name: string;
        server: {
          command: string;
          args: string[];
          env: Record<string, string>;
        };
      }

      export interface RemoteServerConfig {
        name: string;
        server: {
          url: string;
          /**
           * Optional HTTP headers to include with every request to this server (e.g. for authentication).
           * The keys are header names and the values are header values.
           */
          headers?: Record<string, string>;
        };
      }

      export type ExtMCPServerConfig = StdioServerConfig | RemoteServerConfig;

      /**
       * Register an MCP server that the Cursor extension can communicate with.
       *
       * The server can be exposed either over HTTP(S) (SSE/streamable HTTP) **or** as a local
       * stdio process.
       */
      export const registerServer: (config: ExtMCPServerConfig) => void;
      export const unregisterServer: (serverName: string) => void;
    }
  }
}
```

## [Configuration Types](#configuration-types)

### [HTTP/SSE Server Configuration](#httpsse-server-configuration)

For servers running on HTTP or Server-Sent Events:

```
interface RemoteServerConfig {
  name: string;
  server: {
    url: string;
    headers?: Record<string, string>;
  };
}
```

**Properties:**

-   `name`: Unique identifier for the server
-   `server.url`: The HTTP endpoint URL
-   `server.headers` (optional): HTTP headers for authentication or other purposes

### [Stdio Server Configuration](#stdio-server-configuration)

For local servers that communicate via standard input/output:

```
interface StdioServerConfig {
  name: string;
  server: {
    command: string;
    args: string[];
    env: Record<string, string>;
  };
}
```

**Properties:**

-   `name`: Unique identifier for the server
-   `server.command`: The executable command
-   `server.args`: Command line arguments
-   `server.env`: Environment variables

## [Examples](#examples)

### [HTTP/SSE Server](#httpsse-server)

Register a remote MCP server with authentication:

```
vscode.cursor.mcp.registerServer({
  name: "my-remote-server",
  server: {
    url: "https://api.example.com/mcp",
    headers: {
      Authorization: "Bearer your-token-here",
      "X-API-Key": "your-api-key",
    },
  },
});
```

### [Stdio Server](#stdio-server)

Register a local MCP server:

```
vscode.cursor.mcp.registerServer({
  name: "my-local-server",
  server: {
    command: "python",
    args: ["-m", "my_mcp_server"],
    env: {
      API_KEY: "your-api-key",
      DEBUG: "true",
    },
  },
});
```

### [Node.js Server](#nodejs-server)

Register a Node.js-based MCP server:

```
vscode.cursor.mcp.registerServer({
  name: "nodejs-server",
  server: {
    command: "npx",
    args: ["-y", "@company/mcp-server"],
    env: {
      NODE_ENV: "production",
      CONFIG_PATH: "/path/to/config",
    },
  },
});
```

## [Managing Servers](#managing-servers)

### [Unregister a Server](#unregister-a-server)

```
// Unregister a previously registered server
vscode.cursor.mcp.unregisterServer("my-remote-server");
```

### [Conditional Registration](#conditional-registration)

```
// Only register if not already registered
if (!isServerRegistered("my-server")) {
  vscode.cursor.mcp.registerServer({
    name: "my-server",
    server: {
      url: "https://api.example.com/mcp",
    },
  });
}
```

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---

### Webhooks

Source: https://cursor.com/docs/cloud-agent/api/webhooks

# Webhooks

When you create an agent with a webhook URL, Cursor will send HTTP POST requests to notify you about status changes. Currently, only `statusChange` events are supported, specifically when an agent encounters an `ERROR` or `FINISHED` state.

## [Webhook verification](#webhook-verification)

To ensure the webhook requests are authentically from Cursor, verify the signature included with each request:

### [Headers](#headers)

Each webhook request includes the following headers:

-   **`X-Webhook-Signature`** – Contains the HMAC-SHA256 signature in the format `sha256=<hex_digest>`
-   **`X-Webhook-ID`** – A unique identifier for this delivery (useful for logging)
-   **`X-Webhook-Event`** – The event type (currently only `statusChange`)
-   **`User-Agent`** – Always set to `Cursor-Agent-Webhook/1.0`

### [Signature verification](#signature-verification)

To verify the webhook signature, compute the expected signature and compare it with the received signature:

```
const crypto = require("crypto");

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature =
    "sha256=" +
    crypto.createHmac("sha256", secret).update(rawBody).digest("hex");

  return signature === expectedSignature;
}
```

```
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()

    return signature == expected_signature
```

Always use the raw request body (before any parsing) when computing the signature.

## [Payload format](#payload-format)

The webhook payload is sent as JSON with the following structure:

```
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Added README.md with installation instructions"
}
```

Note that some fields are optional and will only be included when available.

## [Best practices](#best-practices)

-   **Verify signatures** – Always verify the webhook signature to ensure the request is from Cursor
-   **Handle retries** – Webhooks may be retried if your endpoint returns an error status code
-   **Return quickly** – Return a 2xx status code as soon as possible
-   **Use HTTPS** – Always use HTTPS URLs for webhook endpoints in production
-   **Store raw payloads** – Store the raw webhook payload for debugging and future verification

English

-   English
-   简体中文
-   日本語
-   繁體中文
-   Español
-   Français
-   Português
-   한국어
-   Русский
-   Türkçe
-   Bahasa Indonesia
-   Deutsch

---
