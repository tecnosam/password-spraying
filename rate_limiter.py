import time

class RateLimiter:
    def __init__(self, requests_per_minute):
        self.requests_per_minute = requests_per_minute
        self.allowance = requests_per_minute
        self.last_check = time.time()
        
    def limit_reached(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_check
        self.last_check = current_time
        self.allowance += elapsed_time * (self.requests_per_minute / 60)
        if self.allowance > self.requests_per_minute:
            self.allowance = self.requests_per_minute
        if self.allowance < 1:
            return True
        self.allowance -= 1
        return False

# Example usage
limiter = RateLimiter(30)  # Limit to 30 requests per minute

while True:
    if limiter.limit_reached():
        print("Rate limit reached. Waiting...")
        time.sleep(1)  # Wait 1 second before trying again
    else:
        print("Request allowed")

