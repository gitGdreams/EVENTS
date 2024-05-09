import requests
import argparse

def test_command_injection(url, wordlist):
    try:
        with open(wordlist, "r") as f:
            payloads = f.readlines()

        for payload in payloads:
            # Craft the payload with the user-supplied command
            payload = {"parameter": payload.strip()}
            
            # Send a GET request with the payload
            response = requests.get(url, params=payload)
            
            # Check if the response indicates command execution
            if "Command executed successfully" in response.text:
                print("[+] Potential command injection vulnerability found with payload:", payload)
            else:
                print("[-] No command injection vulnerability found with payload:", payload)
    except Exception as e:
        print("[-] Error occurred:", e)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Test for command injection vulnerability")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("wordlist", help="Path to the wordlist file containing payloads")
    args = parser.parse_args()

    # Test for command injection
    test_command_injection(args.url, args.wordlist)
