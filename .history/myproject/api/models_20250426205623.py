from django.db import models
from django.contrib.auth.models import User


class Tree(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    planted_date = models.DateField()
    height = models.FloatField()
    health_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WebsiteTask(models.Model):
    STATUS_CHOICES = [
        ("pending", "待处理"),
        ("in_progress", "进行中"),
        ("completed", "已完成"),
    ]

    PRIORITY_CHOICES = [
        ("low", "低"),
        ("medium", "中"),
        ("high", "高"),
    ]

    title = models.CharField(max_length=200, verbose_name="任务标题")
    description = models.TextField(blank=True, verbose_name="任务描述")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="状态"
    )
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium", verbose_name="优先级"
    )
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="截止时间")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "网站任务"
        verbose_name_plural = "网站任务列表"

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, verbose_name="电话")
    address = models.CharField(max_length=200, blank=True, verbose_name="地址")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


class ServicePlan(models.Model):
    name = models.CharField(max_length=100, verbose_name="服务名称")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    description = models.TextField(verbose_name="服务描述")
    duration = models.IntegerField(verbose_name="服务时长(天)")
    features = models.TextField(verbose_name="服务特性")

    class Meta:
        verbose_name = "服务计划"
        verbose_name_plural = "服务计划"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(ServicePlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")
    end_date = models.DateTimeField(verbose_name="结束时间")
    is_active = models.BooleanField(default=True, verbose_name="是否有效")
    payment_status = models.CharField(
        max_length=20, default="pending", verbose_name="支付状态"
    )

    class Meta:
        verbose_name = "订阅记录"
        verbose_name_plural = "订阅记录"
