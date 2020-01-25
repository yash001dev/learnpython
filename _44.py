#Working With File And Directories
from pathlib import Path
#It Provide 2 Path Acess 1.Absoulate Path 2.Relative Path
path=Path("ecommerce")
print(path.exists())

path2=Path("emails")
#print(path2.mkdir())


#Remove Directory
print(path2.rmdir())
