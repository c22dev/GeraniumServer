import os
import time

log_directory = 'log'

def cleanup_old_logs():
    current_time = time.time()
    deleted_count = 0
    for root, dirs, files in os.walk(log_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if current_time - os.path.getmtime(file_path) > 15 * 24 * 60 * 60:  # 15 days
                os.remove(file_path)
                deleted_count += 1
        if not os.listdir(root) and root != log_directory:
            os.rmdir(root)
    print(f'deleted {deleted_count} log files')

if __name__ == '__main__':
    cleanup_old_logs()
