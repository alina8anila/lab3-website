from django.db import models

# Create your models here.


class ExchangeProgram(models.Model):
    university = models.CharField("університет", max_length=200)
    language = models.CharField("мови навчання", max_length=200)
    places = models.CharField("кількість місць", max_length=200)
    deadline = models.DateField("дедлайн подачі")
    description = models.TextField("опис")

    class Meta:
        ordering = ["deadline"]
        verbose_name = "програма обміну"
        verbose_name_plural = "програми обміну"

    def __str__(self):
        return self.university


class Department(models.Model):
    name = models.CharField("назва кафедри", max_length=200)
    head = models.CharField("завідувач кафедри", max_length=200)

    class Meta:
        ordering = ["name"]
        verbose_name = "кафедра"
        verbose_name_plural = "кафедри"

    def __str__(self):
        return self.name


class Program(models.Model):
    class Level(models.TextChoices):
        BACHELOR = "bachelor", "бакалаврський"
        MASTER = "master", "магістерський"
        PHD = "phd", "PhD"

    name = models.CharField("назва освітньої програми", max_length=200)
    level = models.CharField(
        "рівень освіти",
        max_length=20,
        choices=Level.choices,
        default=Level.BACHELOR,
    )
    code = models.CharField("код освітньої програми", max_length=200)
    description = models.TextField("короткий опис")
    coordinator_name = models.CharField("координатор набору", max_length=200)
    coordinator_email = models.EmailField("контакт координатора", max_length=200)
    department = models.ForeignKey(
        "Department",
        on_delete=models.PROTECT,
        related_name="programs",
        verbose_name="випускова кафедра",
    )
    disciplines = models.TextField(
        "дисципліни", blank=True, help_text="Кожна дисципліна — з нового рядка"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "освітня програма"
        verbose_name_plural = "освітні програми"

    def __str__(self):
        return self.name

    @property
    def disciplines_list(self):
        result = []
        for line in self.disciplines.splitlines():
            clean_line = line.strip()
            if clean_line:
                result.append(clean_line)
        return result


class Teacher(models.Model):
    name = models.CharField("ім'я викладача", max_length=200)
    position = models.CharField("посада", max_length=200)
    degree = models.CharField("науковий ступінь", max_length=200)
    department = models.ForeignKey(
        "Department",
        on_delete=models.PROTECT,
        related_name="teachers",
        verbose_name="Кафедра",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "викладач"
        verbose_name_plural = "викладачі"

    def __str__(self):
        return self.name


class HomePageContent(models.Model):
    title = models.CharField("назва факультету", max_length=200)
    about = models.TextField("опис факультету")
    contacts = models.TextField("контакти")
    updated_at = models.DateTimeField("оновлено", auto_now=True)

    class Meta:
        verbose_name = "текст головної сторінки"
        verbose_name_plural = "текст головної сторінки"

    def __str__(self):
        return self.title
