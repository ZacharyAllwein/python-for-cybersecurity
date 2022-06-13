import dns
import dns.resolver
import socket


def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]] + result[1] + result[2]


def dns_request(domain):
    try:
        result = dns.resolver.resolve(domain, "A")

        if result:
            return {
                answer.to_text(): reverse_dns(answer.to_text()) for answer in result
            }

    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return {}


def subdomain_search(domain, dictionary, nums):

    results = {
        f"{word}.{domain}": dns_request(f"{word}.{domain}") for word in dictionary
    }

    if nums:
        results | {
            f"{word}{i}.{domain}": dns_request(f"{word}{i}.{domain}")
            for word in dictionary
            for i in range(0, 1)
        }

    return results


if __name__ == "__main__":
    dictionary = ["mail", "www"]
    print(subdomain_search("google.com", dictionary, True))
