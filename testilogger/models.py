from django.db import models

class TestCase(models.Model):
    STATUS_CHOICES = [
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('error', 'Error'),
        ('skip', 'Skip'),
    ]

    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pass')
    executed_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-executed_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['executed_at']),
        ]

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
