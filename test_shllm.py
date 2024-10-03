import subprocess

def test_shllm_ping_localhost():
    output = subprocess.check_output(["python3", "shllm.py", "command to ping 127.0.0.1"]).decode("utf-8").strip()
    print(output)
    assert "Command to be copied to clipboard: ping 127.0.0.1" in output
