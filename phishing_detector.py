from urllib.parse import urlparse

url = input("Enter URL: ")

parsed = urlparse(url)
hostname = parsed.hostname

score = 0
reasons = []

if not hostname:
    print("Invalid URL")
    exit()

# Check HTTPS
if parsed.scheme != "https":
    score += 1
    reasons.append("URL is not using HTTPS")

# Check for IP address
if hostname.replace(".", "").isdigit():
    score += 2
    reasons.append("URL uses an IP address instead of a domain name")

# Check suspicious characters
if "@" in url:
    score += 2
    reasons.append("URL contains @ symbol")

# Check suspicious words
words = ["login", "verify", "update", "bank", "password", "account", "secure"]

for word in words:
    if word in hostname.lower():
        score += 1
        reasons.append(f"Suspicious word found: {word}")

print("\nURL Analysis")
print("-" * 30)

if score >= 3:
    print("Result: Potentially Suspicious ⚠️")
else:
    print("Result: No obvious phishing indicators found ✅")

print("\nReasons:")

if reasons:
    for reason in reasons:
        print("-", reason)
else:
    print("- No suspicious indicators detected")