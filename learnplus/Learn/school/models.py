from django.db import models
from django.utils.text import slugify


# Create your models here.
# class Filiere(models.Model):
#     nom = models.CharField(max_length=255)
#     date_add = models.DateTimeField(auto_now_add=True)
#     date_update = models.DateTimeField(auto_now=True)
#     status = models.BooleanField(default=True)


#     class Meta:
#         verbose_name = 'Filiere'
#         verbose_name_plural = 'Filieres'

#     def __str__(self):
#         return self.nom

class Matiere(models.Model):
    nom = models.CharField(max_length=255)
    # coefficient = models.IntegerField()
    # filiere = models.ForeignKey(Filiere,on_delete=models.CASCADE,related_name='matiere_filiere',null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True,  blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Matiere, self).save(*args, **kwargs)
    


    class Meta:
        verbose_name = 'Matiere'
        verbose_name_plural = 'Matieres'

    def __str__(self):
        return self.nom

class Niveau(models.Model):
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True,  blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Niveau, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Niveau'
        verbose_name_plural = 'Niveaux'

    def __str__(self):
        return self.nom

class Classe(models.Model):
    niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE,related_name='classe_niveau')
    numeroClasse = models.IntegerField()
    # filiere = models.ForeignKey(Filiere,on_delete=models.CASCADE,related_name='classe_filiere',null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    


    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.niveau.nom

class Chapitre(models.Model):
    
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE,related_name='classe_chapitre', null=True)
    matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE,related_name='matiere_chapitre')
    video = models.FileField(upload_to="ressources/cours", null=True)
    duree_en_heure = models.PositiveIntegerField(null=True)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True,  blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Chapitre, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Chapitre'
        verbose_name_plural = 'Chapitres'

    def __str__(self):
        return self.titre


class Cours(models.Model):
    titre = models.CharField(max_length=255)
    chapitre = models.ForeignKey(Chapitre,on_delete=models.CASCADE,related_name='cours_chapitre')
    duree = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True,  blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Cours, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Courss'

    def __str__(self):
        return self.titre



