from django.db import models

class TaskStatus(models.TextChoices):

    TODO = "TODO", "To Do"

    IN_PROGRESS = "IN_PROGRESS", "In Progress"

    TESTING = "TESTING", "Testing"

    DONE = "DONE", "Done"
    
    
class Priority(models.TextChoices):

    LOW = "LOW", "Low"

    MEDIUM = "MEDIUM", "Medium"

    HIGH = "HIGH", "High"

    CRITICAL = "CRITICAL", "Critical"