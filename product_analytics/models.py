# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    addressid = models.AutoField(db_column='addressID', primary_key=True)  # Field name made lowercase.
    profileid = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='profileID')  # Field name made lowercase.
    cityid = models.ForeignKey('Cities', models.DO_NOTHING, db_column='cityID', blank=True, null=True)  # Field name made lowercase.
    timezoneid = models.PositiveIntegerField(db_column='timezoneID', blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    stationid = models.ForeignKey('CitiesMetroStations', models.DO_NOTHING, db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    districtid = models.ForeignKey('CitiesDistricts', models.DO_NOTHING, db_column='districtID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    namecrm = models.CharField(db_column='nameCrm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    about = models.TextField(blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house = models.CharField(max_length=255, blank=True, null=True)
    coords = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    workingempty = models.PositiveIntegerField(db_column='workingEmpty')  # Field name made lowercase.
    workexperience = models.CharField(db_column='workExperience', max_length=50, blank=True, null=True)  # Field name made lowercase.
    allprice = models.PositiveIntegerField(db_column='allPrice')  # Field name made lowercase.
    education = models.TextField(blank=True, null=True)
    reviews = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField()
    catalog = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    crop = models.JSONField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class AddressesOnlineSettings(models.Model):
    onlinesettingid = models.AutoField(db_column='onlineSettingID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID')  # Field name made lowercase.
    recordnotlater = models.IntegerField(db_column='recordNotLater', blank=True, null=True)  # Field name made lowercase.
    recordnotprev = models.IntegerField(db_column='recordNotPrev', blank=True, null=True)  # Field name made lowercase.
    editableuntil = models.PositiveIntegerField(db_column='editableUntil')  # Field name made lowercase.
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses_online_settings'


class Albums(models.Model):
    albumid = models.AutoField(db_column='albumID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID')  # Field name made lowercase.
    serviceid = models.PositiveIntegerField(db_column='serviceID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'albums'


class AlbumsIcons(models.Model):
    albumiconsid = models.AutoField(db_column='albumIconsID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    sort = models.PositiveIntegerField(blank=True, null=True)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albums_icons'


class Amocrm(models.Model):
    amocrmid = models.AutoField(db_column='amocrmID', primary_key=True)  # Field name made lowercase.
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    leadid = models.PositiveIntegerField(db_column='leadID')  # Field name made lowercase.
    contactid = models.PositiveIntegerField(db_column='contactID')  # Field name made lowercase.
    use = models.PositiveIntegerField()
    pay = models.PositiveIntegerField()
    date_pay = models.BigIntegerField(blank=True, null=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)
    utm = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amocrm'


class Backgrounds(models.Model):
    backgroundid = models.AutoField(db_column='backgroundID', primary_key=True)  # Field name made lowercase.
    gradient = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backgrounds'


class BaseIdeasCategories(models.Model):
    baseideascategoryid = models.AutoField(db_column='baseIdeasCategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=255)
    sort = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_ideas_categories'


class BaseIdeasPostTag(models.Model):
    baseideaspostid = models.ForeignKey('BaseIdeasPosts', models.DO_NOTHING, db_column='baseIdeasPostID')  # Field name made lowercase.
    baseideastagid = models.ForeignKey('BaseIdeasTags', models.DO_NOTHING, db_column='baseIdeasTagID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'base_ideas_post_tag'


class BaseIdeasPosts(models.Model):
    baseideaspostid = models.AutoField(db_column='baseIdeasPostID', primary_key=True)  # Field name made lowercase.
    baseideascategoryid = models.ForeignKey(BaseIdeasCategories, models.DO_NOTHING, db_column='baseIdeasCategoryID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    video = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    textmini = models.TextField(db_column='textMini')  # Field name made lowercase.
    duration = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=255)
    active = models.PositiveIntegerField()
    sort = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_ideas_posts'


class BaseIdeasReviews(models.Model):
    baseideasreviewid = models.AutoField(db_column='baseIdeasReviewID', primary_key=True)  # Field name made lowercase.
    baseideaspostid = models.ForeignKey(BaseIdeasPosts, models.DO_NOTHING, db_column='baseIdeasPostID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    stars = models.PositiveIntegerField()
    message = models.CharField(max_length=500)
    parentid = models.IntegerField(db_column='parentID', blank=True, null=True)  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_ideas_reviews'


class BaseIdeasTags(models.Model):
    baseideastagid = models.AutoField(db_column='baseIdeasTagID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_ideas_tags'


class Bids(models.Model):
    bidid = models.AutoField(db_column='bidID', primary_key=True)  # Field name made lowercase.
    masterid = models.PositiveIntegerField(db_column='masterID')  # Field name made lowercase.
    clientid = models.ForeignKey('Clients', models.DO_NOTHING, db_column='clientID')  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID')  # Field name made lowercase.
    serviceid = models.ForeignKey('CrmServices', models.DO_NOTHING, db_column='serviceID')  # Field name made lowercase.
    adminid = models.PositiveIntegerField(db_column='adminID', blank=True, null=True)  # Field name made lowercase.
    profileid = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='profileID')  # Field name made lowercase.
    comment = models.CharField(max_length=255, blank=True, null=True)
    timefrom = models.TimeField(db_column='timeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='timeTo', blank=True, null=True)  # Field name made lowercase.
    timeduration = models.CharField(db_column='timeDuration', max_length=50)  # Field name made lowercase.
    price = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField()
    active = models.PositiveIntegerField()
    filled = models.PositiveIntegerField()
    isonline = models.PositiveIntegerField(db_column='isOnline')  # Field name made lowercase.
    ischecked = models.PositiveIntegerField(db_column='isChecked')  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cancelreason = models.TextField(db_column='cancelReason', blank=True, null=True)  # Field name made lowercase.
    cancelid = models.IntegerField(db_column='cancelID', blank=True, null=True)  # Field name made lowercase.
    reminder = models.IntegerField(blank=True, null=True)
    sms = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bids'


class BlockingTimes(models.Model):
    blocktimeid = models.AutoField(db_column='blockTimeID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    timefrom = models.TimeField(db_column='timeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='timeTo', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blocking_times'


class BlogsCategories(models.Model):
    catid = models.AutoField(db_column='catID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text = models.CharField(max_length=3000)
    alias = models.CharField(unique=True, max_length=255)
    parentid = models.CharField(db_column='parentID', max_length=255)  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs_categories'


class BlogsPosts(models.Model):
    postid = models.AutoField(db_column='postID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text = models.TextField()
    alias = models.CharField(unique=True, max_length=255)
    catid = models.ForeignKey(BlogsCategories, models.DO_NOTHING, db_column='catID')  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs_posts'


class BlogsSettings(models.Model):
    settingid = models.AutoField(db_column='settingID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=200)
    name = models.CharField(unique=True, max_length=200)
    value = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs_settings'


class BookingHours(models.Model):
    bookinghourid = models.AutoField(db_column='bookingHourID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    timeformatid = models.ForeignKey('TimesFormat', models.DO_NOTHING, db_column='timeFormatID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_hours'


class Cities(models.Model):
    cityid = models.AutoField(db_column='cityID', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey('Countries', models.DO_NOTHING, db_column='countryID')  # Field name made lowercase.
    regionid = models.ForeignKey('Regions', models.DO_NOTHING, db_column='regionID')  # Field name made lowercase.
    timezoneid = models.ForeignKey('Timezones', models.DO_NOTHING, db_column='timezoneID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    prepositionalname = models.CharField(db_column='prepositionalName', max_length=255)  # Field name made lowercase.
    alias = models.CharField(max_length=255)
    coordx = models.FloatField(db_column='coordX')  # Field name made lowercase.
    coordy = models.FloatField(db_column='coordY')  # Field name made lowercase.
    delivery_threshold = models.DecimalField(max_digits=8, decimal_places=2)
    ismetro = models.PositiveIntegerField(db_column='isMetro')  # Field name made lowercase.
    isdistrict = models.PositiveIntegerField(db_column='isDistrict')  # Field name made lowercase.
    seotitle = models.CharField(db_column='seoTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seodescription = models.CharField(db_column='seoDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seoh1 = models.CharField(db_column='seoH1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seotext = models.TextField(db_column='seoText', blank=True, null=True)  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class CitiesDeliveries(models.Model):
    citydeliveryid = models.BigAutoField(db_column='cityDeliveryID', primary_key=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='cityID')  # Field name made lowercase.
    delivery = models.CharField(max_length=255)
    price = models.IntegerField()
    info = models.CharField(max_length=255)
    sort = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_deliveries'


class CitiesDistricts(models.Model):
    districtid = models.AutoField(db_column='districtID', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='cityID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    prepositionalname = models.CharField(db_column='prepositionalName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(max_length=255, blank=True, null=True)
    seotitle = models.CharField(db_column='seoTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seodescription = models.CharField(db_column='seoDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seotext = models.TextField(db_column='seoText', blank=True, null=True)  # Field name made lowercase.
    sort = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_districts'


class CitiesMetroLines(models.Model):
    lineid = models.AutoField(db_column='lineID', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='cityID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_metro_lines'


class CitiesMetroStations(models.Model):
    stationid = models.AutoField(db_column='stationID', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='cityID')  # Field name made lowercase.
    lineid = models.ForeignKey(CitiesMetroLines, models.DO_NOTHING, db_column='lineID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    coordx = models.FloatField(db_column='coordX')  # Field name made lowercase.
    coordy = models.FloatField(db_column='coordY')  # Field name made lowercase.
    code = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_metro_stations'


class CitiesPayments(models.Model):
    citypaymentid = models.BigAutoField(db_column='cityPaymentID', primary_key=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='cityID')  # Field name made lowercase.
    payment = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_payments'


class Clients(models.Model):
    clientid = models.AutoField(db_column='clientID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    profileid = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='profileID')  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    gender = models.PositiveIntegerField()
    birthday = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    blockingonline = models.PositiveIntegerField(db_column='blockingOnline')  # Field name made lowercase.
    sale = models.PositiveIntegerField(blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    crop = models.JSONField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class ClientsBids(models.Model):
    bidclientid = models.AutoField(db_column='bidClientID', primary_key=True)  # Field name made lowercase.
    bidid = models.ForeignKey(Bids, models.DO_NOTHING, db_column='bidID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients_bids'


class ClientsType(models.Model):
    clienttypeid = models.AutoField(db_column='clientTypeID', primary_key=True)  # Field name made lowercase.
    profileid = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='profileID')  # Field name made lowercase.
    colorid = models.ForeignKey('Colors', models.DO_NOTHING, db_column='colorID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients_type'


class ClientsUsers(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.ForeignKey(Clients, models.DO_NOTHING, db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients_users'


class Colors(models.Model):
    colorid = models.AutoField(db_column='colorID', primary_key=True)  # Field name made lowercase.
    color = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colors'


class Consultants(models.Model):
    consultantid = models.AutoField(db_column='consultantID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    crop = models.JSONField(blank=True, null=True)
    count = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultants'


class Contacts(models.Model):
    contactid = models.AutoField(db_column='contactID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text_first = models.CharField(max_length=1000)
    mail = models.CharField(max_length=255, blank=True, null=True)
    phones = models.CharField(max_length=255, blank=True, null=True)
    coord = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(unique=True, max_length=255)
    text_second = models.CharField(max_length=1000)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class Countries(models.Model):
    countryid = models.AutoField(db_column='countryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    sort = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Courses(models.Model):
    courseid = models.AutoField(db_column='courseID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    status = models.PositiveIntegerField()
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'


class CrmCategories(models.Model):
    categoryid = models.AutoField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='templateID')  # Field name made lowercase.
    colorid = models.IntegerField(db_column='colorID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    sort = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    hidden = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    moderation = models.PositiveIntegerField()
    moderationcomment = models.CharField(db_column='moderationComment', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_categories'


class CrmMastersCategories(models.Model):
    mastercategoryid = models.BigAutoField(db_column='masterCategoryID', primary_key=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_masters_categories'


class CrmMastersServices(models.Model):
    masterservicesid = models.BigAutoField(db_column='masterServicesID', primary_key=True)  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='serviceID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_masters_services'


class CrmRecommendedCategories(models.Model):
    recommendedcategoryid = models.BigAutoField(db_column='recommendedCategoryID', primary_key=True)  # Field name made lowercase.
    colorid = models.IntegerField(db_column='colorID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    ismenu = models.IntegerField(db_column='isMenu', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_recommended_categories'


class CrmRecommendedServices(models.Model):
    recommendedserviceid = models.BigAutoField(db_column='recommendedServiceID', primary_key=True)  # Field name made lowercase.
    recommendedcategoryid = models.IntegerField(db_column='recommendedCategoryID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    ismenu = models.IntegerField(db_column='isMenu', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_recommended_services'


class CrmServices(models.Model):
    serviceid = models.AutoField(db_column='serviceID', primary_key=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.
    templateid = models.IntegerField(db_column='templateID')  # Field name made lowercase.
    title = models.CharField(max_length=255)
    customertitle = models.CharField(db_column='customerTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    time = models.IntegerField()
    sort = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    isonline = models.IntegerField(db_column='isOnline')  # Field name made lowercase.
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    blocktime = models.IntegerField(db_column='blockTime', blank=True, null=True)  # Field name made lowercase.
    isblocktime = models.IntegerField(db_column='isBlockTime', blank=True, null=True)  # Field name made lowercase.
    moderation = models.PositiveIntegerField()
    moderationcomment = models.CharField(db_column='moderationComment', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_services'


class DisplayBlocks(models.Model):
    displayblockid = models.AutoField(db_column='displayBlockID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    instagram = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'display_blocks'


class EmployeePosition(models.Model):
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    positionid = models.PositiveIntegerField(db_column='positionID', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_position'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Favorites(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    addressid = models.PositiveIntegerField(db_column='addressID', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorites'


class FcmTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    fcm_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fcm_tokens'


class Galleries(models.Model):
    galleryid = models.BigAutoField(db_column='galleryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    sort = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galleries'


class HoursWork(models.Model):
    workid = models.AutoField(db_column='workID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID', blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(max_length=255)
    timeoff = models.CharField(db_column='timeOff', max_length=255)  # Field name made lowercase.
    timeto = models.CharField(db_column='timeTo', max_length=255)  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hours_work'


class Instagram(models.Model):
    instagramid = models.AutoField(db_column='instagramID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID', blank=True, null=True)  # Field name made lowercase.
    profileid = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    backgroundid = models.ForeignKey(Backgrounds, models.DO_NOTHING, db_column='backgroundID', blank=True, null=True)  # Field name made lowercase.
    backgroundyour = models.PositiveIntegerField(db_column='backgroundYour', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    whatsappstatus = models.PositiveIntegerField(db_column='whatsappStatus')  # Field name made lowercase.
    viberstatus = models.PositiveIntegerField(db_column='viberStatus')  # Field name made lowercase.
    vkstatus = models.PositiveIntegerField(db_column='vkStatus')  # Field name made lowercase.
    whatsappphone = models.CharField(db_column='whatsappPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    viberphone = models.CharField(db_column='viberPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vk = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    isonlinestatus = models.PositiveIntegerField(db_column='isOnlineStatus')  # Field name made lowercase.
    phonestatus = models.PositiveIntegerField(db_column='phoneStatus')  # Field name made lowercase.
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instagram'


class Invites(models.Model):
    inviteid = models.AutoField(db_column='inviteID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    access_token = models.CharField(max_length=100, blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invites'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Log(models.Model):
    logid = models.AutoField(db_column='logID', primary_key=True)  # Field name made lowercase.
    profileid = models.IntegerField(db_column='profileID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    message = models.TextField()
    useragent = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='isRead', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class LogsBids(models.Model):
    logbidid = models.AutoField(db_column='logBidID', primary_key=True)  # Field name made lowercase.
    bidid = models.IntegerField(db_column='bidID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    message = models.TextField(blank=True, null=True)
    useragent = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs_bids'


class LogsSchedule(models.Model):
    logscheduleid = models.AutoField(db_column='logScheduleID', primary_key=True)  # Field name made lowercase.
    scheduleid = models.IntegerField(db_column='scheduleID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    message = models.TextField(blank=True, null=True)
    useragent = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs_schedule'


class MarketBonusSettings(models.Model):
    bonussettingid = models.AutoField(db_column='bonusSettingID', primary_key=True)  # Field name made lowercase.
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_bonus_settings'


class MarketCategories(models.Model):
    categoryid = models.AutoField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    parentid = models.PositiveIntegerField(db_column='parentID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    seoh1 = models.CharField(db_column='seoH1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seoh2 = models.CharField(db_column='seoH2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seotext = models.TextField(db_column='seoText', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_categories'


class MarketCategoryFilters(models.Model):
    marketcategoryfiltersid = models.AutoField(db_column='marketCategoryFiltersID', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(MarketCategories, models.DO_NOTHING, db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    sort = models.PositiveIntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_category_filters'


class MarketFavorites(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    productid = models.ForeignKey('MarketProducts', models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_favorites'


class MarketFilterItems(models.Model):
    marketfilteritemsid = models.AutoField(db_column='marketFilterItemsID', primary_key=True)  # Field name made lowercase.
    marketcategoryfiltersid = models.ForeignKey(MarketCategoryFilters, models.DO_NOTHING, db_column='marketCategoryFiltersID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_filter_items'


class MarketOrders(models.Model):
    orderid = models.AutoField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house = models.CharField(max_length=255, blank=True, null=True)
    flat = models.CharField(max_length=255, blank=True, null=True)
    delivery_type = models.CharField(max_length=45, blank=True, null=True)
    full_address = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    type = models.PositiveIntegerField()
    delivery_price = models.IntegerField(blank=True, null=True)
    paymentstatus = models.IntegerField(db_column='paymentStatus')  # Field name made lowercase.
    payment = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    adminid = models.IntegerField(db_column='adminID', blank=True, null=True)  # Field name made lowercase.
    profileid = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    processingstatus = models.IntegerField(db_column='processingStatus')  # Field name made lowercase.
    departuredate = models.DateTimeField(db_column='departureDate', blank=True, null=True)  # Field name made lowercase.
    tracknumber = models.CharField(db_column='trackNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customerorder_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    customerorder_agent_id = models.CharField(max_length=255, blank=True, null=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    addbonuses = models.CharField(db_column='addBonuses', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deductbonuses = models.CharField(db_column='deductBonuses', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datebonuses = models.DateTimeField(db_column='dateBonuses', blank=True, null=True)  # Field name made lowercase.
    deleted_at = models.DateTimeField(blank=True, null=True)
    stock = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_orders'


class MarketOrdersProducts(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(MarketOrders, models.DO_NOTHING, db_column='orderID', blank=True, null=True, related_name="rn_product_in_orders")  # Field name made lowercase.
    productid = models.ForeignKey('MarketProducts', models.DO_NOTHING, db_column='productID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField()
    saleprice = models.FloatField(db_column='salePrice', blank=True, null=True)  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_orders_products'


class MarketProductGroups(models.Model):
    marketgroupid = models.AutoField(db_column='marketGroupID', primary_key=True)  # Field name made lowercase.
    categoryid = models.PositiveIntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=555, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    profileid = models.IntegerField(db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    sale = models.IntegerField()
    new = models.IntegerField()
    popular = models.IntegerField()
    sort = models.IntegerField()
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    article = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    length = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_product_groups'


class MarketProductItems(models.Model):
    productitemid = models.AutoField(db_column='productItemID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('MarketProducts', models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    marketfilteritemsid = models.ForeignKey(MarketFilterItems, models.DO_NOTHING, db_column='marketFilterItemsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'market_product_items'


class MarketProductParameters(models.Model):
    parameterid = models.AutoField(db_column='parameterID', primary_key=True)  # Field name made lowercase.
    marketgroupid = models.ForeignKey(MarketProductGroups, models.DO_NOTHING, db_column='marketGroupID')  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_product_parameters'


class MarketProducts(models.Model):
    productid = models.AutoField(db_column='productID', primary_key=True)  # Field name made lowercase.
    marketgroupid = models.ForeignKey(MarketProductGroups, models.DO_NOTHING, db_column='marketGroupID', blank=True, null=True, related_name='rn_group_id')  # Field name made lowercase.
    code = models.PositiveIntegerField(blank=True, null=True)
    article = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    externalcode = models.CharField(db_column='externalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profileid = models.PositiveIntegerField(db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    active = models.PositiveIntegerField(blank=True, null=True)
    stock = models.IntegerField()
    new = models.PositiveIntegerField()
    sale = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    saleprice = models.FloatField(db_column='salePrice', blank=True, null=True)  # Field name made lowercase.
    purchaseprice = models.FloatField(db_column='purchasePrice', blank=True, null=True)  # Field name made lowercase.
    minprice = models.FloatField(db_column='minPrice', blank=True, null=True)  # Field name made lowercase.
    masterprice = models.FloatField(db_column='masterPrice', blank=True, null=True)  # Field name made lowercase.
    studioprice = models.FloatField(db_column='studioPrice', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_products'


class MarketStepsPercent(models.Model):
    steppercentid = models.AutoField(db_column='stepPercentID', primary_key=True)  # Field name made lowercase.
    amount = models.IntegerField(blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_steps_percent'


class MarketTags(models.Model):
    tagid = models.AutoField(db_column='tagID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_tags'


class Menus(models.Model):
    menuid = models.AutoField(db_column='menuID', primary_key=True)  # Field name made lowercase.
    parentid = models.PositiveIntegerField(db_column='parentID')  # Field name made lowercase.
    typeid = models.ForeignKey('MenusTypes', models.DO_NOTHING, db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    route = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    sitemap = models.PositiveIntegerField(db_column='siteMap')  # Field name made lowercase.
    sort = models.PositiveIntegerField()
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus'


class MenusTypes(models.Model):
    menutypeid = models.AutoField(db_column='menuTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    route = models.CharField(max_length=255, blank=True, null=True)
    sitemap = models.PositiveIntegerField(db_column='siteMap')  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus_types'


class MessageRoleTypes(models.Model):
    messageroletypeid = models.BigAutoField(db_column='messageRoleTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_role_types'


class Messages(models.Model):
    messageid = models.AutoField(db_column='messageID', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField()
    profileid = models.IntegerField(db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    bidid = models.ForeignKey(Bids, models.DO_NOTHING, db_column='bidID', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class MessagesRoles(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    messageid = models.ForeignKey(Messages, models.DO_NOTHING, db_column='messageID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    messageroletypeid = models.ForeignKey(MessageRoleTypes, models.DO_NOTHING, db_column='messageRoleTypeID', blank=True, null=True)  # Field name made lowercase.
    read = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages_roles'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class Pages(models.Model):
    pageid = models.AutoField(db_column='pageID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text_first = models.CharField(max_length=1000)
    text_second = models.TextField()
    alias = models.CharField(unique=True, max_length=255)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class PasswordResets(models.Model):
    passwordresetid = models.AutoField(db_column='passwordResetID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    smscount = models.PositiveIntegerField(db_column='smsCount')  # Field name made lowercase.
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PayrollRuleCategory(models.Model):
    payrollruleid = models.ForeignKey('PayrollRules', models.DO_NOTHING, db_column='payrollRuleID')  # Field name made lowercase.
    categoryid = models.ForeignKey(CrmCategories, models.DO_NOTHING, db_column='categoryID')  # Field name made lowercase.
    serviceid = models.ForeignKey(CrmServices, models.DO_NOTHING, db_column='serviceID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=8, decimal_places=2)
    value_type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'payroll_rule_category'


class PayrollRules(models.Model):
    payrollruleid = models.BigAutoField(db_column='payrollRuleID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID')  # Field name made lowercase.
    name = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    basesalary = models.DecimalField(db_column='baseSalary', max_digits=8, decimal_places=2)  # Field name made lowercase.
    value_type = models.PositiveIntegerField()
    periodicity_type = models.PositiveIntegerField()
    base_periodicity_type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payroll_rules'


class Payrolls(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    bidid = models.OneToOneField(Bids, models.DO_NOTHING, db_column='bidID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payrolls'


class PermissionSections(models.Model):
    permission_section_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission_sections'


class Permissions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    permission_section_id = models.CharField(max_length=255, blank=True, null=True)
    guard_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Places(models.Model):
    placeid = models.AutoField(db_column='placeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'


class Positions(models.Model):
    positionid = models.AutoField(db_column='positionID', primary_key=True)  # Field name made lowercase.
    profileid = models.IntegerField(db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    colorid = models.PositiveIntegerField(db_column='colorID')  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sort = models.IntegerField()
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'positions'


class PriceTemplates(models.Model):
    templateid = models.AutoField(db_column='templateID', primary_key=True)  # Field name made lowercase.
    profileid = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_templates'


class Profiles(models.Model):
    profileid = models.AutoField(db_column='profileID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    consultantid = models.PositiveIntegerField(db_column='consultantID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    steps = models.PositiveIntegerField()
    allprice = models.PositiveIntegerField(db_column='allPrice')  # Field name made lowercase.
    allinstagram = models.PositiveIntegerField(db_column='allInstagram')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class ProfilesSteps(models.Model):
    profilestepid = models.AutoField(db_column='profileStepID', primary_key=True)  # Field name made lowercase.
    stepid = models.PositiveIntegerField(db_column='stepID')  # Field name made lowercase.
    profileid = models.PositiveIntegerField(db_column='profileID')  # Field name made lowercase.
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles_steps'


class PushSubscriptions(models.Model):
    subscribable_type = models.CharField(max_length=255)
    subscribable_id = models.PositiveBigIntegerField()
    endpoint = models.CharField(unique=True, max_length=500)
    public_key = models.CharField(max_length=255, blank=True, null=True)
    auth_token = models.CharField(max_length=255, blank=True, null=True)
    content_encoding = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_subscriptions'


class Regions(models.Model):
    regionid = models.AutoField(db_column='regionID', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Countries, models.DO_NOTHING, db_column='countryID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    sort = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class Reviews(models.Model):
    reviewid = models.AutoField(db_column='reviewID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID', related_name='only_for_fix_errors_addressid')  # Field name made lowercase.
    clientid = models.ForeignKey('Users', models.DO_NOTHING, db_column='clientID', related_name='only_for_fix_errors_clientid')  # Field name made lowercase.
    bidid = models.ForeignKey(Bids, models.DO_NOTHING, db_column='bidID', blank=True, null=True)  # Field name made lowercase.
    stars = models.PositiveIntegerField()
    message = models.CharField(max_length=500)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    masterid = models.ForeignKey('Users', models.DO_NOTHING, db_column='masterID', blank=True, null=True, related_name='only_for_fix_errors_masterid')  # Field name made lowercase.
    read = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'reviews'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ru_name = models.CharField(max_length=255, blank=True, null=True)
    profileid = models.IntegerField(db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    guard_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Schedule(models.Model):
    scheduleid = models.AutoField(db_column='scheduleID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    type = models.PositiveIntegerField()
    date = models.DateField()
    timefrom = models.TimeField(db_column='timeFrom')  # Field name made lowercase.
    timebreakfrom = models.TimeField(db_column='timeBreakFrom', blank=True, null=True)  # Field name made lowercase.
    timebreakto = models.TimeField(db_column='timeBreakTo', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='timeTo')  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class ScheduleAddressUser(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sort = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule_address_user'


class Seofilters(models.Model):
    filterseoid = models.AutoField(db_column='filterSeoID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='cityID')  # Field name made lowercase.
    catservicesid = models.PositiveIntegerField(db_column='catServicesID')  # Field name made lowercase.
    seotitle = models.CharField(db_column='seoTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seodescription = models.CharField(db_column='seoDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seoh1 = models.CharField(db_column='seoH1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seotext = models.TextField(db_column='seoText', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoFilters'


class SeoCitiesCategories(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='cityID')  # Field name made lowercase.
    catservicesid = models.PositiveIntegerField(db_column='catServicesID')  # Field name made lowercase.
    seotitle = models.CharField(db_column='seoTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seodescription = models.CharField(db_column='seoDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seoh1 = models.CharField(db_column='seoH1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seotext = models.TextField(db_column='seoText', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seo_cities_categories'


class Sessions(models.Model):
    id = models.CharField(unique=True, max_length=50, blank=True, primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    last_activity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Settings(models.Model):
    settingid = models.AutoField(db_column='settingID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID')  # Field name made lowercase.
    tag = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    addfield = models.CharField(db_column='addField', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class SettingsAddField(models.Model):
    addfieldid = models.AutoField(db_column='addFieldID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    src = models.CharField(max_length=255, blank=True, null=True)
    srcxs = models.CharField(db_column='srcXs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    srcmd = models.CharField(db_column='srcMd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings_add_field'


class SettingsGroups(models.Model):
    groupid = models.AutoField(db_column='groupID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings_groups'


class ShortUrls(models.Model):
    shorturlid = models.AutoField(db_column='shortUrlID', primary_key=True)  # Field name made lowercase.
    longurl = models.CharField(db_column='longUrl', max_length=255)  # Field name made lowercase.
    shorturl = models.CharField(db_column='shortUrl', max_length=255)  # Field name made lowercase.
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'short_urls'


class SocialProviders(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_providers'


class SocialTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    social_provider = models.ForeignKey(SocialProviders, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    social_user_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    expires_in = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_tokens'


class Steps(models.Model):
    stepid = models.AutoField(db_column='stepID', primary_key=True)  # Field name made lowercase.
    triumphid = models.PositiveIntegerField(db_column='triumphID')  # Field name made lowercase.
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'steps'


class Surveys(models.Model):
    surveyid = models.AutoField(db_column='surveyID', primary_key=True)  # Field name made lowercase.
    profileid = models.ForeignKey(Profiles, models.DO_NOTHING, db_column='profileID')  # Field name made lowercase.
    numberemployees = models.IntegerField(db_column='numberEmployees', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surveys'


class TimesFormat(models.Model):
    timeformatid = models.AutoField(db_column='timeFormatID', primary_key=True)  # Field name made lowercase.
    minuts = models.IntegerField(blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'times_format'


class Timezones(models.Model):
    timezoneid = models.AutoField(db_column='timezoneID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    regular = models.CharField(max_length=50, blank=True, null=True)
    summer = models.CharField(max_length=50, blank=True, null=True)
    winter = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    regularformat = models.CharField(db_column='regularFormat', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timezones'


class TopMasters(models.Model):
    topmasterid = models.AutoField(db_column='topMasterID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    typeprice = models.IntegerField(db_column='typePrice', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'top_masters'


class Triumphs(models.Model):
    triumphid = models.AutoField(db_column='triumphID', primary_key=True)  # Field name made lowercase.
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    keys = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'triumphs'


class UploadFiles(models.Model):
    uploadfilesid = models.AutoField(db_column='uploadFilesID', primary_key=True)  # Field name made lowercase.
    modelid = models.IntegerField(db_column='modelID', blank=True, null=True)  # Field name made lowercase.
    addmodelid = models.PositiveIntegerField(db_column='addModelID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    mimetype = models.CharField(db_column='mimeType', max_length=100)  # Field name made lowercase.
    extension = models.CharField(max_length=100, blank=True, null=True)
    size = models.PositiveIntegerField()
    modelname = models.CharField(db_column='modelName', max_length=255)  # Field name made lowercase.
    crop = models.JSONField(blank=True, null=True)
    sort = models.PositiveIntegerField(blank=True, null=True)
    uniquevalue = models.CharField(db_column='uniqueValue', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    main = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_files'


class UploadFilesProduct(models.Model):
    uploadfilesproductid = models.AutoField(db_column='uploadFilesProductID', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='productID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    mimetype = models.CharField(db_column='mimeType', max_length=100)  # Field name made lowercase.
    extension = models.CharField(max_length=100, blank=True, null=True)
    size = models.PositiveIntegerField()
    sort = models.PositiveIntegerField(blank=True, null=True)
    uniquevalue = models.CharField(db_column='uniqueValue', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_files_product'


class UserOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    orderid = models.ForeignKey(MarketOrders, models.DO_NOTHING, db_column='orderID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_order'


class UserStudio(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    profileid = models.ForeignKey(Profiles, models.DO_NOTHING, db_column='profileID', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_studio'


class Users(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    whence = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=255, blank=True, null=True)
    phoneactive = models.PositiveIntegerField(db_column='phoneActive')  # Field name made lowercase.
    access_token = models.CharField(max_length=10000, blank=True, null=True)
    gender = models.PositiveIntegerField()
    triumph = models.PositiveIntegerField()
    topmaster = models.PositiveIntegerField(db_column='topMaster')  # Field name made lowercase.
    birthday = models.CharField(max_length=50, blank=True, null=True)
    associatephone = models.CharField(db_column='associatePhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.IntegerField()
    messagesetting = models.PositiveIntegerField(db_column='messageSetting', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    providerid = models.CharField(db_column='providerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    providertoken = models.CharField(db_column='providerToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    crop = models.JSONField(blank=True, null=True)
    payrollruleid = models.ForeignKey(PayrollRules, models.DO_NOTHING, db_column='payrollRuleID', blank=True, null=True)  # Field name made lowercase.
    view_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    pushes_at = models.DateTimeField(blank=True, null=True)
    pushtoken = models.CharField(db_column='pushToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isonline = models.IntegerField(db_column='isOnline')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class UsersDelivery(models.Model):
    deliveryid = models.AutoField(db_column='deliveryID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    cityid = models.PositiveIntegerField(db_column='cityID')  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    patronymic = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house = models.CharField(max_length=255, blank=True, null=True)
    flat = models.CharField(max_length=255, blank=True, null=True)
    payment = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_delivery'


class UsersSms(models.Model):
    userssmsid = models.AutoField(db_column='usersSmsID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    date = models.DateTimeField()
    secret = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    attempt = models.IntegerField()
    active = models.IntegerField()
    restore = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'users_sms'


class UsersStatus(models.Model):
    statusid = models.AutoField(db_column='statusID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField()
    profileid = models.IntegerField(db_column='profileID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_status'


class UsersTriumphs(models.Model):
    usertriumphid = models.AutoField(db_column='userTriumphID', primary_key=True)  # Field name made lowercase.
    triumphid = models.PositiveIntegerField(db_column='triumphID', blank=True, null=True)  # Field name made lowercase.
    userid = models.PositiveIntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_triumphs'


class WhitelistCategories(models.Model):
    whitelistcategoriesid = models.BigAutoField(db_column='whitelistCategoriesID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'whitelist_categories'


class WhitelistServices(models.Model):
    whitelistservicesid = models.BigAutoField(db_column='whitelistServicesID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'whitelist_services'


class WorkPlaces(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='addressID', blank=True, null=True)  # Field name made lowercase.
    placeid = models.PositiveIntegerField(db_column='placeID', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_places'
