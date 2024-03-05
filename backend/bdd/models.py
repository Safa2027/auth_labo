from django.db import models


   
class chercheur (models.Model) :
    chercheur_id=models.CharField(max_length=100 , primary_key=True)
    nom_complet=models.CharField(max_length=100 )
    grade=models.CharField(max_length=100 )
    diplome =models.CharField(max_length=100 )
    hindex=models.IntegerField()
    type=models.CharField(max_length=100 )
    projet_id=models.ForeignKey('projet',on_delete =models.CASCADE)
    dblp=models.URLField()
    ggl_scholar=models.URLField()
    site_personel=models.URLField()

class publication (models.Model):
    publication_id=models.CharField(max_length=100 , primary_key=True)
    chercheur_id =models.ForeignKey(chercheur,on_delete =models.CASCADE)
    nom=models.CharField(max_length=100 )
    nb_page=models.IntegerField()
    nb_volumes=models.IntegerField()
    nb_citations=models.IntegerField()
    Lien=models.URLField()
    rang=models.IntegerField()
    class Meta:
     unique_together = (('publication_id', 'chercheur_id'),) 

class projet(models.Model):
   projet_id=models.IntegerField(primary_key=True)
   nom=models.CharField(max_length=100 )
   domain=models.CharField(max_length=100 )
   type=models.CharField(max_length=100 )
   date_debut=models.DateTimeField()
   date_fin=models.DateTimeField()


class chercheur_projet(models.Model):
   projet_id=models.ForeignKey(projet,on_delete =models.CASCADE)  
   chercheur_id=models.ForeignKey(chercheur,on_delete =models.CASCADE)
   role=models.CharField(max_length=100 )
   class meta :
      unique_together=(('projet_id','chercheur_id'),)

class venue(models.Model):
   venue_id=models.CharField(max_length=100,primary_key=True )
   type=models.CharField(max_length=100)
   nom=models.CharField(max_length=100)
   periodicite=models.CharField(max_length=100)

class pub_venue(models.Model):
   venue_id=models.ForeignKey(venue,on_delete =models.CASCADE)
   publication_id=models.ForeignKey(publication,on_delete =models.CASCADE)
   date=models.DateTimeField()
   class Meta :
      unique_together=(('venue_id','publication_id'),)


class encadrement(models.Model):
   encadrement_id = models.IntegerField(primary_key=True )
   type = models.CharField(max_length=100)
   date =models.DateTimeField()


class chercheur_encadrement():
    chercheur_id=models.ForeignKey(chercheur,on_delete =models.CASCADE)
    encadrement_id=models.ForeignKey(encadrement,on_delete =models.CASCADE) 
    type = models.CharField(max_length=100)
    class Meta:
       unique_together = (('chercheur_id','encadrement_id'),)


class classement(models.Model):
   classement_id = models.IntegerField(primary_key=True)
   nom= models.CharField(max_length = 100)



class venue_classement(models.Model) :
    classement_id=models.ForeignKey(classement,on_delete =models.CASCADE)
    venue_id=models.ForeignKey(venue,on_delete =models.CASCADE) 
    classement = models.CharField(max_length = 100)
    class Meta:
       unique_together = (('classement_id','venue_id'),)

class publucation_classement(models.Model):
    classement_id=models.ForeignKey(classement,on_delete =models.CASCADE)
    publication_id=models.ForeignKey(publication,on_delete =models.CASCADE)
    classement = models.CharField(max_length = 100)
    class Meta:
       unique_together = (('classement_id','publication_id'),)


class utilisateur (models.Model):
   utilisateur_id = models.IntegerField(primary_key=True)
   email = models.EmailField()
   mot_de_pass =models.CharField(max_length = 255)
   numero_tel =models.CharField(max_length = 15)
   role=models.CharField(max_length = 100)
   chercheur_id=models.ForeignKey(chercheur,on_delete =models.CASCADE)
          




    


