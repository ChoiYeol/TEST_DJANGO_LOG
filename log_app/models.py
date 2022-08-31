from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    use_for_related_fields = True  # 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.

    def get_queryset(self):
        return super().get_queryset().filter(deletedat__isnull=True)


class SoftDeleteModel(models.Model):
    deletedat = models.DateTimeField(db_column='deleted_at', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True  # 상속 할수 있게

    objects = SoftDeleteManager()  # 커스텀 매니저
    objects_all = models.Manager()  # 매니저

    def delete(self, using = None, keep_parents=False):
        self.deletedat = timezone.now()
        self.save(update_fields=['deletedat'])

    def hard_delete(self):
        try:
            super(SoftDeleteModel, self).delete()
        except Exception as e:
            pass

    def restore(self):  # 삭제된 레코드를 복구한다.
        self.deletedat = None
        self.save(update_fields=['deletedat'])


class QuickSeqs(SoftDeleteModel):
    index = models.AutoField(primary_key=True)
    fk_quick_id = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='created_at', auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updated_at', auto_now=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'quick_seqs'


class Users(models.Model):
    index = models.IntegerField()
    uuid = models.CharField(primary_key=True, max_length=20)
    bot_user_key = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    type = models.IntegerField()
    createdat = models.DateTimeField(db_column='created_at')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updated_at')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'users'
