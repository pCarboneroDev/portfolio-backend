class Project:
    def __init__(self, name, description, imageUrl):
        self.name: str = name
        self.description: str = description
        self.imageUrl: str = imageUrl,
        self.projectUrl: str
        
    def __init__(self, name, description, imageUrl, projectUrl):
        self.name: str = name
        self.description: str = description
        self.imageUrl: str = imageUrl,
        self.projectUrl: str = projectUrl