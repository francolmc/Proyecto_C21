from django.db import models

# Create your models here.
class Project():
    def __init__(self, title: str, description: str, draft: bool):
        self.title = title
        self.description = description
        self.draft = draft
    
    def is_draft(self):
        return self.draft

projects = [
    Project('Mapeo de pozos', 'Proyecto para identificar pozos para explotación.', False),
    Project('Somos agiles', 'Con esto se busca la posbilidad de llevar control de proyectos con Agile.', False)
]