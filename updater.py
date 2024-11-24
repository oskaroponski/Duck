import subprocess
try:
    result = subprocess.run(
        ["git", "pull", "origin", "main"],
        check=True,
        text=True,
        capture_output=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    exit(f"[ERROR] {e.stderr}")
except Exception as e:
    exit(f"[ERROR] {str(e)}")
