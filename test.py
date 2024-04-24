import subprocess

def test_shll_ping_localhost():
    output = subprocess.check_output(["./shll", "command to ping my localhost"]).decode("utf-8").strip()
    print(output)
    assert "Command to be copied to clipboard: ping localhost" in output
