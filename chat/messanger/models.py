from django.db import models

class Message(models.Model):
  author_id = models.IntegerField(null=True)
  recipient_id = models.IntegerField(null=True)  
  text = models.CharField(max_length=40,null=True)
  message_id = models.IntegerField()

  def __str__(self):
    return self.text

  def to_json(self):
    return {
      'author_id': self.author_id,
      'recipient_id': self.recipient_id,
      'text': self.text,
      'message_id': self.message_id
    }

class User(models.Model):
  user_id = models.IntegerField()
  name = models.CharField(max_length=40)
  surname = models.CharField(max_length=40)
  user_type = models.IntegerField()

  def to_json(self):
    return {
        "user_id": self.user_id,
        "name": self.name,
        "surname": self.surname,
        "user_type": str(self.user_type),

    }

  def __str__(self):
    return self.name


