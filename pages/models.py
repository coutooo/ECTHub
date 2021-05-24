from django.db import models
# instalei pip3 install django-multiselectfield
from multiselectfield import MultiSelectField

# Create your models here.
class Ficheiros(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    
    resources = models.FileField(upload_to='resources/files')


    def __str__(self):
        return self.title

class User(models.Model):
    subjects_choices = (
            ('p1','Programação 1'),
            ('isd','Introdução aos Sistemas Digitais'),
            ('c1' ,'Cálculo 1'),
            ('alga','Álgebra Linear e Geometria Analítica'),
            ('labi','Laboratórios de Informática'),
            ('p2' ,'Programação 2'),
            ('lsd','Laboratórios de Sistemas Digitais'),
            ('md' ,'Matemática Discreta'),
            ('c2' ,'Cálculo 2'),
            ('p3' ,'Programação 3'),
            ('ac1','Arquitetura de Computadores 1'),
            ('mce','Mecânica e Campo Eletromagnético'),
            ('mpei','Métodos Probabilísticos para Engenharia Informática'),
            ('ac2','Arquitetura de Computadores 2'),
            ('se' ,'Sistemas Eletrónicos'),
            ('lfa','Linguagens Formais e Autómatos'),
            ('algc','Algoritmos e Complexidade'),
            ('iia','Introdução à Inteligência Artificial'),
            ('fr' ,'Fundamentos de Redes'),
            ('ams','Análise e Modelação de Sistemas'),
            ('so' ,'Sistemas de Operação'),
            ('ihc','Interação Humano-Computador'),
            ('pei','Projecto em Engenharia Informática'),
            ('ar' ,'Arquitectura de Redes'),
            ('bd' ,'Base de Dados'),
            ('ara','Arquitetura de Redes Avançada'),
            ('aca','Arquitetura de Computadores Avançada'),
            ('edc','Engenharia de Dados e Conhecimento'),
            ('cv' ,'Computação Visual'),
            ('s'  ,'Segurança'),
            ('sd' ,'Sistemas Distribuídos'),
            ('es' ,'Engenharia de Software'),
            ('cr' ,'Computação Reconfigurável'),
            ('ddr','Desempenho e Dimensionamento de Redes'),
            ('gpe' ,'Gestão de Projectos e Empreendorismo'),
            ('tese' ,'Dissertação'),
    )

    nmec = models.IntegerField()
    subjects = MultiSelectField(choices=subjects_choices)
