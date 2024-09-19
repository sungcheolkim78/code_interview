from typing import List
import re

class Solution:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    pattern_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')

    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    pattern_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:
        if self.pattern_IPv4.match(IP):
            return "IPv4"
        elif self.pattern_IPv6.match(IP):
            return "IPv6"
        else:
            return "Neither"

    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')
        for x in nums:
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"

    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            if len(x) == 0 or len(x) > 4:
                return "Neither"
            if not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"

    def validIPAddress2(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"


if __name__ == '__main__':
    sol = Solution()
    print(sol.validIPAddress2("255.255.255.255"))
    print(sol.validIPAddress2("123.123.123"))
    print(sol.validIPAddress2("172.16.255.1"))
    print(sol.validIPAddress2("2001:0db8:85a3:0:0:8A2E:0370:7334"))
