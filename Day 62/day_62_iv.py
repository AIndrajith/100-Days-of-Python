# Generating Logs for Backup Activities

def write_log(backup_dir, log_file, files):
    with open(log_file, "a") as log:
        log.write(f"Backup created: {backup_dir}")
        for file in files:
            log.write(f" - {file}\n")
        log.write("\n")