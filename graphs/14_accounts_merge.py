from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adjacent = {}

        def dfs(merged_account, email: str):
            visited.add(email)
            merged_account.append(email)

            if email not in adjacent:
                return

            for neighbor in adjacent[email]:
                if neighbor not in visited:
                    dfs(merged_account, neighbor)

        # build adjacency list
        for account in accounts:
            n_neighbors = len(account)
            first_email = account[1]
            for i in range(2, n_neighbors):
                second_email = account[i]

                if first_email in adjacent:
                    adjacent[first_email].append(second_email)
                else:
                    adjacent[first_email] = [second_email]

                if second_email in adjacent:
                    adjacent[second_email].append(first_email)
                else:
                    adjacent[second_email] = [first_email]

        # traverse over all accounts to store components
        merged_accounts = []
        for account in accounts:
            account_name, account_first_email = account[0], account[1]

            if account_first_email not in visited:
                merged_account = []
                dfs(merged_account, account_first_email)
                merged_account = [account_name] + sorted(merged_account)

                merged_accounts.append(merged_account)

        return merged_accounts


if __name__ == "__main__":
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(accounts)
    solution = Solution()
    print(solution.accountsMerge(accounts))
