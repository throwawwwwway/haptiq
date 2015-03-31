ps aux | grep Python | grep -v "grep Python" | awk '{print $2}' | xargs kill -9
