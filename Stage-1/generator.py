# 1. Yields log lines one by one, skips empty lines and lines starting with "#"
def read_log_stream(logs: list[str]):
    for log in logs:
        if not log or log.startswith("#"):
            continue
        yield log

# 2. Receives a stream, yields ONLY lines containing "ERROR" or "CRITICAL"
def filter_errors(log_stream):
    for log in log_stream:
        if "ERROR" in log or "CRITICAL" in log:
            yield log

# 3. Receives filtered stream, yields tuple (timestamp, level, message)
# Input line format: "2026-08-04 10:00:00 [ERROR] Database connection failed"
def parse_log_entry(error_stream):
    for log in error_stream:
        if "ERROR" not in log and "CRITICAL" not in log:
            continue
        parts = log.split(" ")
        timestamp = " ".join(parts[:2])
        level = parts[2][1:-1]
        message = " ".join(parts[3:])
        yield timestamp, level, message

if __name__ == "__main__":
    raw_logs = [
        "# Server Logs",
        "2026-08-04 10:00:00 [INFO] Server started",
        "",
        "2026-08-04 10:01:15 [ERROR] Database connection failed",
        "2026-08-04 10:02:00 [WARNING] High memory usage",
        "2026-08-04 10:03:22 [CRITICAL] Out of memory crash",
    ]
    # Chain the 3 generators and print each parsed error tuple
    stream = read_log_stream(raw_logs)
    errors = filter_errors(stream)
    parsed = parse_log_entry(errors)

    for entry in parsed:
        print(entry)
