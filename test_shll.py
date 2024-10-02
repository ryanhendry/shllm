import subprocess

def test_shll_ping_localhost():
    output = subprocess.check_output(["python3", "shll.py", "command to ping my localhost"]).decode("utf-8").strip()
    print(output)
    assert "Command to be copied to clipboard: ping localhost" in output
