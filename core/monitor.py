import time
import random
import requests

class ContainerMonitor:
    def __init__(self, threshold=80):
        self.threshold = threshold
        self.containers = {}

    def get_stats(self, container_id):
        # Mocking docker stats for demonstration
        cpu_usage = random.uniform(10, 95)
        mem_usage = random.uniform(20, 90)
        return {"cpu": cpu_usage, "mem": mem_usage}

    def check_and_scale(self, container_id):
        stats = self.get_stats(container_id)
        print(f"Monitoring {container_id}: CPU {stats['cpu']:.2f}% | MEM {stats['mem']:.2f}%")
        
        if stats['cpu'] > self.threshold:
            self.scale_up(container_id)
        elif stats['cpu'] < 20:
            self.scale_down(container_id)

    def scale_up(self, container_id):
        print(f"[!] ALERT: High load on {container_id}. Scaling up...")
        # Integration with Webhooks or Cloud APIs would go here
        self.notify_webhook(f"Container {container_id} scaled UP due to high load.")

    def scale_down(self, container_id):
        print(f"[*] INFO: Low load on {container_id}. Scaling down...")
        self.notify_webhook(f"Container {container_id} scaled DOWN to save resources.")

    def notify_webhook(self, message):
        # Mock webhook notification
        print(f"[Webhook] Sending: {message}")

if __name__ == "__main__":
    monitor = ContainerMonitor()
    while True:
        monitor.check_and_scale("web-app-01")
        time.sleep(5)
