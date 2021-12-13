from django.db import models
from django.db.models.lookups import StartsWith
from jalali_date import datetime2jalali, date2jalali
from accounts.models import PorfileModel
from django.core.validators import RegexValidator



class concertModel (models.Model):
    class Meta:
        verbose_name="کنسرت"
        verbose_name_plural = "کنسرت"
    Name=models.CharField(max_length=99, verbose_name="نام کنسرت")
    SingerName= models.CharField (max_length=99, verbose_name="خواننده")
    length = models.IntegerField( verbose_name="زمان")
    Poster =models.ImageField(upload_to=('concertimages/') , null=True, verbose_name="پوستر")

    def __str__(self):
        return self.Name


class locationModel (models.Model ):
    class Meta:
        verbose_name="محل برگزاری کنسرت"
        verbose_name_plural = "محل برگزاری کنسرت"
    
    id = models.IntegerField(primary_key=True, verbose_name="شماره")
    Name=models.CharField(max_length=99, verbose_name="مکان")
    Address=models.CharField(max_length=99,default="تهران -برج میلاد ", verbose_name="آدرس")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="شماره تماس")
    Phone=models.CharField(validators=[phone_regex], max_length=17, blank=True ,verbose_name="شماره تلفن")
    Capacity = models.IntegerField( verbose_name="ظرفیت")

    def __str__(self):
        return self.Name


class  timefieldModel (models.Model):
    class Meta:
        verbose_name="زمان برگزاری "
        verbose_name_plural = "زمان برگزاری "
    
    concertModel= models.ForeignKey (to = concertModel, on_delete=models.PROTECT, verbose_name="کنسرت")
    locationModel = models.ForeignKey (to = locationModel, on_delete=models.PROTECT, verbose_name="محل برگزاری")
    StarartDateTime =models.DateTimeField( verbose_name="زمان شروع")
    Seat = models.IntegerField( verbose_name="ظرفیت صندلی ")

    start=1
    end=2
    sales=3
    cancle=4
    status_choices =((start,"کنسرت در حال شروع شدن است "),
                    (end,"کنسرت پایان یافته"),
                    (sales,"بلیط ها فروخته شده"),
                    (cancle,"کنسرت کنسل شده"))

    status = models.IntegerField(choices=status_choices, verbose_name="وضعیت")

    def __str__(self) -> str:
        return "Your Consert : {} Time: {} location: {}".format(concertModel.Name,self.StarartDateTime,self.locationModel ) 
    def jalali_date (self):
        return datetime2jalali(self.StarartDateTime)


class TicketModel (models.Model):
    class Meta:
        verbose_name="بلیط"
        verbose_name_plural = "بلیط"

    PorfileModel=models.ForeignKey(PorfileModel,on_delete=models.PROTECT, verbose_name="پروفایل")
    timefieldModel = models.ForeignKey(to=timefieldModel, on_delete=models.PROTECT, verbose_name="زمان برگزاری")
    Name=models.CharField(max_length=99, verbose_name="نام بلیط")
    price = models.IntegerField( verbose_name="قیمت")
    imageticket = models.ImageField(upload_to=('ticketmodel/'), verbose_name="تصویر بلیط")

    def __str__(self) :
        return  "Porfile: {} Concertinfo: {}".format(PorfileModel.__str__(),timefieldModel.__str__())

